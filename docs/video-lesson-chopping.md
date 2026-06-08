# Chopping workshop recordings into lesson videos

This documents the process used to turn the LLM Zoomcamp **live-workshop
recordings** into per-lesson video clips for the course, and logs the manual
trim fixes made during review.

Working files live in the repo's gitignored `.tmp/` directory:

```
.tmp/
  videos/                       # source masters + chopped clips
    module1-rag-720p.mkv        # best-quality source (downloaded from YouTube)
    ...
    clips/                      # output: one mp4 per lesson
  transcripts/                  # timestamped transcripts (per module)
  chop.sh                       # generic chopper (spec -> clips)
  chop-all.sh                   # driver: chop every module from its spec
  <module>.spec                 # machine-readable cut list per module
  <module>-chop-plan.md         # human-readable plan per module
```

## Module ↔ video map

Playlist: `https://www.youtube.com/playlist?list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv`

| Module | Video | YouTube ID |
|--------|-------|-----------|
| 1 — Part 1 (RAG) | Build Your First RAG Application | `KSItlTAsMsk` |
| 1 — Part 2 (Agents) | From RAG to AI Agents | `RAqLWJsLZb4` |
| 2 — Vector Search | Vector Databases | `BC3NsRUNEIg` |
| 3 — Orchestration | *(no video)* | — |
| 4 — Evaluation | RAG and Agents Evaluation | `WUGtDveIe7A` |
| 5 — Monitoring | Monitoring LLM Applications | `ImY5-Q97sRw` |

## The pipeline

### 1. Fetch the transcript
Pulled from YouTube (free, accurate) rather than transcribing the local files:

```bash
python ~/.claude/skills/fetch-youtube/youtube.py <video-id> > .tmp/transcripts/<module>.txt
```

Transcripts are timestamped (`M:SS text` / `H:MM:SS text`), which is what the
chop plan is built from.

### 2. Get the best-quality source
**YouTube tops out at 720p for these uploads — there is no 1080p.** A casual
download often grabs the *lowest*-bitrate 720p (avc1 ~194 kb/s). Grab the best
stream instead (vp9 720p ~336 kb/s + best audio):

```bash
uvx yt-dlp -f "bv*[height<=720]+ba/b[height<=720]" -S "res:720,br" \
  --merge-output-format mkv -o "<module>-720p.%(ext)s" \
  "https://www.youtube.com/watch?v=<id>"
```

(The true high-res master is the original screen recording, not on YouTube.)

### 3. Build the chop plan
Read the module's lessons (`<NN>-*.md`) and the transcript, then map each
lesson to transcript timestamp ranges at **clean verbal boundaries** (start of
a sentence, not mid-word). Two outputs per module:

- `<module>-chop-plan.md` — human-readable table + trim/discard notes.
- `<module>.spec` — machine-readable, one line per clip:
  ```
  clipname|start1-end1[,start2-end2,...]      # integer seconds
  ```
  Multiple comma-separated ranges are **concatenated** into one clip (used to
  drop interruptions inside a lesson). Lines starting with `#` are comments.

What gets trimmed: opening course promo ("star the repo / like the video"),
course-logistics Q&A, "I'll answer that later" filler, dead air, and failed/
irrelevant tangents. Q&A that is genuinely lesson content is kept. Clips do not
have to be contiguous, and a lesson's clip may come from a different position in
the video than its course order (e.g. Module 1 Part 2 films the RAG revision
before the agents concept).

### 4. Chop + normalize
`chop.sh` re-encodes each clip (frame-accurate) and applies **YouTube loudness
normalization** in the same pass:

```bash
bash .tmp/chop.sh <source.mkv> .tmp/videos/clips <module>.spec <filename-prefix>
```

Encoder settings: `libx264 -preset faster -crf 23 -pix_fmt yuv420p`,
audio `aac -b:a 192k`, loudness `loudnorm=I=-14:TP=-1.5:LRA=11` (YouTube target).
`chop-all.sh` runs this for every module.

### 5. Reproduce / iterate
To re-cut a lesson, edit its line in the `.spec` and re-run `chop.sh` for that
module (or regenerate the single clip with a direct `ffmpeg` command). The spec
+ plan are the source of truth.

## Conventions

- **Resolution:** 720p (source ceiling). Clips keep source resolution.
- **Loudness:** −14 LUFS, true peak −1.5 dBTP (YouTube normalization target).
- **Naming:** `<module-prefix>-l<NN>-<slug>.mp4`, e.g.
  `module1-rag-l05-search.mp4`, derived from the lesson filename.
- **Output:** `.tmp/videos/clips/` (gitignored).

## Gotchas

- **Never edit the chop script while its batch is running.** Bash re-reads the
  script file by byte offset as it executes; an edit shifts the offsets and
  corrupts the run, which can clobber already-finished clips. Either let the
  batch finish, or regenerate individual clips with standalone `ffmpeg` calls.
- **720p is the max on YouTube** for these videos; re-encoding can't recover
  detail the source never had. For higher quality, use the original recording.
- Editing a spec is safe any time (the running chopper already parsed it); just
  re-run afterwards.

## Manual fixes made during review

Module 1 Part 1, after watching the first cut:

- **Source quality** — replaced the low-bitrate 720p (avc1 ~194 kb/s) with the
  best 720p (vp9 ~336 kb/s) and re-chopped.
- **L02 (Environment)** — dropped the "I'll answer those later / everything's
  ready" filler and the trailing RAG segue; now two segments
  (08:15–20:31 + 21:03–21:50) ending on the provider-alternatives Q&A.
- **L07 (RAG Pipeline)** — moved the end from 1:14:11 to 1:14:09 so it lands on
  "...all the three functions." instead of a clipped "and uh".
- **L08 / L09 boundary** — moved the "I just want to show you one last thing"
  teaser off the end of L08 (now ends "...rag client." at 1:30:51) and onto the
  start of L09.
- **L09 (Data Ingestion)** — first ended at 1:44:02 (felt abrupt), then changed
  to **include the full failed live demo**, ending at 1:46:46 on "...you can
  check the notes."

Repo:

- **`01-agentic-rag/README.md`** — it only linked the Part 1 (RAG) video; added
  the missing Part 2 (Agents) video link.
