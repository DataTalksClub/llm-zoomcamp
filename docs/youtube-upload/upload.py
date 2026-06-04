#!/usr/bin/env python3
"""Upload lesson clips to YouTube from a manifest, add them to a playlist.

Run with uv (no project deps added):

  uv run --with google-api-python-client --with google-auth-oauthlib \
    python upload.py \
      --client-secret client_secret.json \
      --manifest part1-manifest.json \
      --videos-dir ../videos/clips

State is written to upload-state.json so re-running skips already-uploaded
clips (useful if the daily upload quota is hit — just run again the next day).
"""
import argparse
import json
import sys
import time
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube"]  # upload + playlist edit


def get_service(client_secret: Path, token: Path):
    creds = None
    if token.exists():
        creds = Credentials.from_authorized_user_file(str(token), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(client_secret), SCOPES)
            # Opens a browser for one-time consent, catches the redirect locally.
            creds = flow.run_local_server(port=0)
        token.write_text(creds.to_json(), encoding="utf-8")
    return build("youtube", "v3", credentials=creds)


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def upload_one(youtube, path: Path, snippet: dict, status: dict) -> str:
    body = {"snippet": snippet, "status": status}
    media = MediaFileUpload(str(path), chunksize=-1, resumable=True)
    request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
    response = None
    while response is None:
        _, response = request.next_chunk()
    return response["id"]


def add_to_playlist(youtube, playlist_id: str, video_id: str):
    youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {"kind": "youtube#video", "videoId": video_id},
            }
        },
    ).execute()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--client-secret", type=Path, default=Path("client_secret.json"))
    ap.add_argument("--token", type=Path, default=Path("token.json"))
    ap.add_argument("--manifest", type=Path, default=Path("part1-manifest.json"))
    ap.add_argument("--videos-dir", type=Path, default=Path("../videos/clips"))
    ap.add_argument("--state", type=Path, default=Path("upload-state.json"))
    args = ap.parse_args()

    cfg = load_json(args.manifest)
    state = load_json(args.state)  # {filename: {"videoId":..., "inPlaylist":bool}}
    youtube = get_service(args.client_secret, args.token)

    tags = cfg.get("tags", [])
    playlist_id = cfg.get("playlistId")

    for v in cfg["videos"]:
        fname = v["file"]
        path = (args.videos_dir / fname).resolve()
        rec = state.get(fname, {})

        if not path.exists():
            print(f"SKIP (missing file): {fname}", file=sys.stderr)
            continue

        try:
            if not rec.get("videoId"):
                snippet = {
                    "title": v["title"],
                    "description": v["description"],
                    "tags": tags,
                    "categoryId": cfg.get("categoryId", "27"),
                    "defaultLanguage": cfg.get("defaultLanguage", "en"),
                }
                status = {"privacyStatus": cfg.get("privacyStatus", "unlisted"),
                          "selfDeclaredMadeForKids": False}
                print(f"Uploading: {v['title']} ...", flush=True)
                vid = upload_one(youtube, path, snippet, status)
                rec["videoId"] = vid
                rec["inPlaylist"] = False
                state[fname] = rec
                args.state.write_text(json.dumps(state, indent=2), encoding="utf-8")
                print(f"  uploaded -> https://youtu.be/{vid}", flush=True)
            else:
                print(f"already uploaded: {v['title']} -> https://youtu.be/{rec['videoId']}")

            if playlist_id and not rec.get("inPlaylist"):
                add_to_playlist(youtube, playlist_id, rec["videoId"])
                rec["inPlaylist"] = True
                state[fname] = rec
                args.state.write_text(json.dumps(state, indent=2), encoding="utf-8")
                print("  added to playlist", flush=True)

        except HttpError as e:
            msg = str(e)
            if "quotaExceeded" in msg or "uploadLimitExceeded" in msg:
                print("\nQuota/upload limit reached. Progress saved to "
                      f"{args.state}. Re-run tomorrow to continue.", file=sys.stderr)
                return 2
            print(f"ERROR on {fname}: {msg}", file=sys.stderr)
            # keep going with the next video
            time.sleep(2)

    done = sum(1 for r in state.values() if r.get("videoId"))
    print(f"\nDone. {done}/{len(cfg['videos'])} uploaded.")
    print("Video URLs:")
    for v in cfg["videos"]:
        r = state.get(v["file"], {})
        if r.get("videoId"):
            print(f"  {v['title']}: https://youtu.be/{r['videoId']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
