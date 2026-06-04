# Publishing lesson clips to YouTube

Scripts and process for getting the chopped lesson clips
(see [../video-lesson-chopping.md](../video-lesson-chopping.md)) onto YouTube
with correct titles, descriptions, visibility, and playlist.

## Recommended flow: manual upload + API rename

YouTube **locks videos uploaded *via the API* to private** until the API
project passes a one-time compliance audit. Editing metadata on videos you
uploaded yourself (`videos.update`) has **no such restriction** and is cheap.
So the simplest reliable path is:

1. **Bulk-upload** the clips by drag-and-drop in YouTube Studio. YouTube titles
   each draft after the file name, turning dashes into spaces
   (`module1-rag-l05-search.mp4` → title `module1 rag l05 search`).
2. **Run `rename.py`** — it finds each uploaded video by that filename-title
   (matching is dash/space/case-insensitive), then sets the real title,
   description, tags and category, flips it to **unlisted**, and adds it to the
   playlist. Re-running is safe (state file + idempotent playlist add).

## One-time: create an OAuth credential

`videos.update` is a write call, so it needs your authorization (it's your
channel — there's no way around a one-time Google sign-in).

1. [Google Cloud Console](https://console.cloud.google.com) → create/select a project.
2. **APIs & Services → Library →** enable **"YouTube Data API v3"**.
3. **OAuth consent screen →** External; add your channel's Google account under
   **Test users**.
4. **Credentials → Create credentials → OAuth client ID → Application type:
   Desktop app →** Create → **Download JSON**.
5. Save it next to these scripts as **`client_secret.json`**
   (gitignored — never commit it).

## Configure the manifest

[`part1-manifest.json`](part1-manifest.json) holds, per video, the `file`
(clip filename), `title`, and `description`, plus global `privacyStatus`,
`playlistId`, `tags`, `categoryId`, `defaultLanguage`. Copy it per module and
edit. `file` is only used to derive the match title (filename without
extension) — the script does not read the local file for renaming.

## Run

From the folder containing the scripts + `client_secret.json`:

```bash
# dry run: print which uploaded video matched which new title; change nothing
uv run --with google-api-python-client --with google-auth-oauthlib \
  python rename.py --dry-run

# apply: set metadata, flip to unlisted, add to playlist
uv run --with google-api-python-client --with google-auth-oauthlib \
  python rename.py
```

The first run opens a browser once for consent. You'll see "Google hasn't
verified this app" → **Advanced → Go to … (unsafe) → Allow**; that's expected
for your own Desktop-app credential and fine for `videos.update` (no audit).
A `token.json` is cached so later runs need no browser.

Tip on Windows: prefix with `PYTHONUTF8=1` so em dashes in titles print
without a console encoding error.

## Files

- **`rename.py`** — match manually-uploaded videos by filename and set metadata
  (title/description/tags), visibility, and playlist via `videos.update`.
  **The main script.**
- **`add_chapters.py`** — append chapter timecodes to each video's description
  (`videos.update`).
- **`clip_transcript.py`** — slice the original recording's transcript into
  per-clip, clip-relative transcripts (using the chop spec) so chapters can be
  prepared before YouTube's ASR is ready; handles multi-segment clips.
- **`upload.py`** — full API upload via `videos.insert`. Works, but on an
  unaudited project the uploaded videos are locked to **private** until the
  project is audited. Only useful if your project is already audited.
- **`part1-manifest.json`, `part2-manifest.json`** — per-video titles &
  descriptions (Module 1 Parts 1 & 2); templates for the other modules.

## Quota & cost

Default YouTube Data API quota is 10,000 units/day.
`videos.update` ≈ 50 units, `playlistItems.insert` ≈ 50 — renaming 10 videos is
~1,000 units. (`videos.insert` uploads cost ~1,600 each → ~6/day.)

## Subtitles & chapter timecodes

Once a video is uploaded and processed, YouTube auto-generates captions (ASR).
These can be fetched and turned into chapter timecodes for the description.

1. **Fetch the transcript** (timestamped) with the fetch-youtube skill:
   ```bash
   uv run --with youtube-transcript-api --with python-dotenv \
     python ~/.claude/skills/fetch-youtube/youtube.py <video-id> > captions/<clip>.txt
   ```
   Output is one `M:SS text` line per caption cue.
   - Captions lag a few minutes after upload. If you get *"Subtitles are
     disabled for this video"*, the ASR track isn't ready yet — retry later.
   - The auto-captions are lowercased and unpunctuated, and mis-hear jargon
     (e.g. "rack" = RAG, "chipt" = ChatGPT, "min search" = minsearch).

2. **Generate chapters** from the transcript, aligned to the lesson's `##`
   sections. YouTube renders chapters from the description when:
   - the first timestamp is `0:00`,
   - there are **at least 3** timestamps in ascending order,
   - each chapter is **at least 10 seconds** long.
   Format: `M:SS Title` (use `H:MM:SS` past one hour), concise titles. Example:
   ```
   0:00 Intro
   0:35 What is a language model
   1:33 Training large language models
   ```
   Saved under `chapters/<clip>.txt`.

3. **(Optional) Add chapters to the video** by appending the block to the
   description via `videos.update` (same auth as `rename.py`). This is a normal
   update — not subject to the upload audit lock.

### Preparing timecodes in advance (no waiting for ASR)

You don't have to wait for YouTube to generate captions after upload. The
original recording's transcript (the one used to build the chop plan) is
already accurate, and the spec records each clip's exact segment ranges. Use
`clip_transcript.py` to slice that transcript into per-clip, **clip-relative**
transcripts right after chopping:

```bash
uv run python clip_transcript.py \
  --transcript ../transcripts/<module>.txt \
  --spec ../<module>.spec \
  --out-dir captions
```

It handles clips that drop bits from the middle (**multi-segment** clips): each
kept segment is shifted by the cumulative duration of the segments before it,
so the timecodes line up with the concatenated clip — a single-segment clip is
just `t − start`, a multi-segment clip is the piecewise version of the same.
Generate chapters from these files exactly as you would from YouTube-fetched
captions, and they're ready to inject the moment the uploads register.
(Fetching YouTube's own ASR still works as a fallback once it's ready.)

## Linking the videos in the lessons

Add each video to the top of its lesson markdown, right after the `# ` heading,
using the **playlist-embedded** URL so clicking opens it inside the playlist:

```
Video: [Watch this lesson](https://www.youtube.com/watch?v=<id>&list=<playlistId>)
```

Match the video to the lesson by lesson number. Insert as its own paragraph
between the H1 and the first body paragraph.

## Publishing "Draft" videos

A bulk drag-and-drop leaves videos as **Drafts** if the Studio upload wizard
wasn't completed. Notes:

- The video can read `uploadStatus=processed` / `privacyStatus=unlisted` via the
  API and even be reachable by link, yet still show **"Draft"** in Studio.
- **The Data API cannot publish a draft** — there is no draft field. A published
  video and a draft return identical `videos.list` status, so `videos.update`
  can't flip it.
- **Publish in Studio.** Batch: Studio → **Content** → tick the draft rows →
  **Edit ▾ → Visibility → Unlisted → Update videos**. Per-video fallback: open
  the draft → **Edit draft → Visibility → Unlisted → Save**.
- Best prevention: finish the upload wizard (set visibility on the last step)
  so videos never become drafts.

### Automating the publish step

The draft step only exists because we upload by hand. To remove it:

- **Get the API project audited** (a one-time compliance form). Once audited,
  `upload.py` (`videos.insert`) uploads *and* publishes at the requested
  visibility with no draft state — the whole flow becomes scriptable end to end.
  This is the real fix.
- **Browser automation** (e.g. a Playwright MCP server driving Studio) can click
  the bulk visibility edit, but it's more fragile than the audited-API route.

## Security

Never commit `client_secret.json`, `token.json`, or `*-state.json` — they're in
`.gitignore` here. Treat them like passwords.
