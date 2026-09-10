# Imagegen repair provenance

## Agentic retry flow diagram

- **Published asset:** `11-agents-intro-04-agentic-flow-diagram-imagegen.png`
- **Lesson:** `11-agents-intro.md`
- **Reason for repair:** the previous redraw changed the failed search from `Olama` to `Ollama`, making the retry story self-contradictory.
- **Original source:** `11-agents-intro-04-agentic-flow-diagram.jpg` (`640x360`, SHA-256 `cb72766cb27b8dddc1220456f21748cac25b020694ebb51bae02e1c4a801b9e1`)
- **Retained bounded crop:** `11-agents-intro-04-agentic-flow-diagram-source-crop-tight.png` (`260x270`, crop coordinates `(x=190, y=85, w=260, h=270)`, SHA-256 `90ed43583aeb4655a62c1e64ac77849ed7592d69ae3b16294e83dae332b3b2e7`)
- **Generation:** built-in imagegen edit using the original JPG and the bounded crop; run `exec-abf6b1f8-fa80-4b25-974e-e64782e61016`.
- **Published output:** `1037x1517`, SHA-256 `9b2c8c2ffef239cd000472007f09ef97eab01f335b7fdbe86109de1e542f5ff1`.
- **C2PA:** metadata present with URN `urn:c2pa:3234ffbe-19a2-4ddd-b446-1bbc1ccaf5f4`.

The redraw preserves exactly these four states, in order:

1. `search - Olama - no useful results`
2. `LLM: Hmm, no results. Maybe a typo for "Ollama"?`
3. `search - Ollama - found results!`
4. `LLM: Here's how to run Ollama locally...`

The original browser/Zoom chrome, camera tile, cursor, and selection highlight were removed. The output was inspected at native resolution and as a 608px-wide render (`608x889`); all four states and arrows remained readable. C2PA metadata was checked for presence; standalone cryptographic verification was not run because `c2patool` is unavailable.
