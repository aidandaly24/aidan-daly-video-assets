# Voice casting

Everything public about how the sitcom cast sounds: the clone registry, the
generated test lines, and the sample library from the Voice Casting Board era.

| Path | What it is |
|---|---|
| `CLONES.md` | The ElevenLabs clone registry — who is cloned, from what, and Aidan's verdict on each attempt. Canon Aidan voice: **"Aidan Daly"**, the clone Aidan made himself in the ElevenLabs web UI reading their provided passage (it beat both of Muse's memo-based clones, which were deleted at his direction). |
| `clones/` | Generated test lines only — the three script lines (normal / hype / annoyed) rendered by each clone attempt, kept so the A/B history in CLONES.md stays audible. |
| `preview-*.mp3` | Tuned stock-catalog previews from the board era (Aidan's and Kearns' measured picks) — the pre-cloning approach, kept for the record. |
| `samples/` | The board's voice-sample library: raw samples, `norm/` (normalized), `intros/` + `intros2/` (intro reads), and the American audition reels. |

## Deliberately NOT here

- **Raw personal voice recordings stay out of this public repo.** Aidan's source
  memo and the WAVs derived from it live only in the private workspace. What
  gets published is the registry and the *generated* outputs — never the
  unscripted personal audio a clone was trained on. Future members' clones
  follow the same rule.
- The Voice Casting Board itself is a Muse Space, not a repo file. Its
  decisions land here as `CLONES.md` (clones) and, once scene casting is final,
  as `VOICES.md` alongside the Blender design package in
  [`../cameo-library/designs/blender/`](../cameo-library/designs/blender/).
