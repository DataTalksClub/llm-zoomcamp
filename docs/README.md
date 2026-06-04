# Course video production pipeline

How a live workshop recording becomes per-lesson YouTube videos that are linked
from the course. Intermediate working files (sources, clips, transcripts,
specs, credentials) live in the repo's gitignored `.tmp/` directory.

## The steps, end to end

1. **Identify & transcribe** — find the module's recording in the YouTube
   playlist and fetch its transcript.
2. **Download the best source** — `yt-dlp`, best available 720p.
3. **Build a chop plan** — map each lesson to timestamp ranges at clean verbal
   boundaries (per-module `<module>.spec` + `<module>-chop-plan.md`).
4. **Chop + normalize** — `chop.sh` re-encodes each lesson clip and applies
   YouTube loudness normalization.
   → Steps 1–4 are detailed in **[video-lesson-chopping.md](video-lesson-chopping.md)**;
   the final per-module cut lists are in **[chop-specs/](chop-specs/)**.
5. **Upload** — bulk drag-and-drop the clips into YouTube Studio.
6. **Set metadata** — `rename.py`: titles, descriptions, tags; set unlisted;
   add to the course playlist.
7. **Add chapters** — get chapter timecodes (fetch YouTube's auto-captions, or
   prepare them in advance from the original transcript with
   `clip_transcript.py`) and append them to each description with
   `add_chapters.py`.
8. **Link in the lessons** — add `Video: [Watch this lesson](…&list=<playlist>)`
   at the top of each lesson markdown (playlist-embedded URL).
9. **Publish** — clear the Studio "Draft" state (bulk visibility edit in
   Studio; the Data API can't do this).
   → Steps 5–9 and all scripts are detailed in
   **[youtube-upload/README.md](youtube-upload/README.md)**.

## Fully automating it

The only non-scriptable step is publishing drafts. To remove it, either get the
API project **audited** (then `upload.py`/`videos.insert` uploads *and*
publishes directly — no drafts) or drive Studio with **browser automation**.
See the "Publishing Draft videos" section in the upload guide.
