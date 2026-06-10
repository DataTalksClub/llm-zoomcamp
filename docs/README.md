# Course video production pipeline → moved

The tooling and docs for turning live-workshop recordings into per-lesson YouTube
videos (download, chop, upload/rename, playlist organization, chapters) now live
in a standalone, reusable project:

**[`youtube-manager-agent`](https://github.com/alexeygrigorev/youtube-manager-agent)**
(local sibling checkout: `../../youtube-manager-agent`)

That repo contains the chopping pipeline (`download.sh`, `chop.sh`,
`clip_transcript.py`, `docs/chopping.md`), the YouTube Data API scripts
(`rename.py`, `upload.py`, `add_chapters.py`, `add_to_playlist.py`,
`list_playlist.py`), the per-module manifests, and this course's cut-list specs
under `examples/`.
