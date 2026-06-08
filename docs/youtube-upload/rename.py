#!/usr/bin/env python3
"""Fix metadata on videos you uploaded manually to YouTube Studio.

You upload the 10 .mp4 files via Studio (their titles default to the file
names, e.g. "module1-rag-l05-search"). This script matches each manifest
entry to the uploaded video by that default title, then:

  - sets the proper title / description / tags / category,
  - sets privacy to the manifest's privacyStatus (e.g. unlisted),
  - adds the video to the playlist.

This uses videos.update (NOT videos.insert), so it is NOT subject to the
unaudited-project private-lock, and it's cheap (~50 units per update).

Run with uv (no project deps added):

  uv run --with google-api-python-client --with google-auth-oauthlib \
    python rename.py --client-secret client_secret.json --manifest part1-manifest.json
"""
import argparse
import json
import re
import sys
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/youtube"]


def get_service(client_secret: Path, token: Path):
    creds = None
    if token.exists():
        creds = Credentials.from_authorized_user_file(str(token), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(client_secret), SCOPES)
            creds = flow.run_local_server(port=0)
        token.write_text(creds.to_json(), encoding="utf-8")
    return build("youtube", "v3", credentials=creds)


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def norm(s: str) -> str:
    """Normalize a title for matching: YouTube turns filename dashes/underscores
    into spaces, so compare on lowercased alphanumerics separated by spaces."""
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def uploads_playlist_id(youtube) -> str:
    r = youtube.channels().list(part="contentDetails", mine=True).execute()
    return r["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]


def list_uploaded_titles(youtube, uploads_pl: str) -> dict:
    """Return {normalized_title: videoId}, keeping the newest on collision."""
    out, page = {}, None
    while True:
        r = youtube.playlistItems().list(
            part="snippet", playlistId=uploads_pl, maxResults=50, pageToken=page
        ).execute()
        for it in r.get("items", []):
            sn = it["snippet"]
            key = norm(sn["title"])
            if key not in out:  # iterating newest-first, so keep the newest
                out[key] = sn["resourceId"]["videoId"]
        page = r.get("nextPageToken")
        if not page:
            return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--client-secret", type=Path, default=Path("client_secret.json"))
    ap.add_argument("--token", type=Path, default=Path("token.json"))
    ap.add_argument("--manifest", type=Path, default=Path("part1-manifest.json"))
    ap.add_argument("--state", type=Path, default=Path("rename-state.json"))
    ap.add_argument("--dry-run", action="store_true", help="match only, change nothing")
    args = ap.parse_args()

    cfg = load_json(args.manifest)
    state = load_json(args.state)
    youtube = get_service(args.client_secret, args.token)

    uploads_pl = uploads_playlist_id(youtube)
    titles = list_uploaded_titles(youtube, uploads_pl)
    playlist_id = cfg.get("playlistId")
    tags = cfg.get("tags", [])

    for v in cfg["videos"]:
        stem = Path(v["file"]).stem  # default title YouTube assigns on upload
        vid = state.get(v["file"], {}).get("videoId") or titles.get(norm(stem))
        if not vid:
            print(f"NO MATCH for '{stem}' — upload {v['file']} first, or rename its "
                  f"default title to '{stem}'.", file=sys.stderr)
            continue

        print(f"{v['title']}  <-  {stem}  ({vid})")
        if args.dry_run:
            continue

        rec = state.get(v["file"], {"videoId": vid})
        try:
            youtube.videos().update(part="snippet,status", body={
                "id": vid,
                "snippet": {
                    "title": v["title"],
                    "description": v["description"],
                    "tags": tags,
                    "categoryId": cfg.get("categoryId", "27"),
                    "defaultLanguage": cfg.get("defaultLanguage", "en"),
                },
                "status": {"privacyStatus": cfg.get("privacyStatus", "unlisted")},
            }).execute()
            rec["updated"] = True

            if playlist_id and not rec.get("inPlaylist"):
                youtube.playlistItems().insert(part="snippet", body={"snippet": {
                    "playlistId": playlist_id,
                    "resourceId": {"kind": "youtube#video", "videoId": vid},
                }}).execute()
                rec["inPlaylist"] = True

            state[v["file"]] = rec
            args.state.write_text(json.dumps(state, indent=2), encoding="utf-8")
            print(f"  updated + playlisted -> https://youtu.be/{vid}")
        except HttpError as e:
            print(f"  ERROR: {e}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
