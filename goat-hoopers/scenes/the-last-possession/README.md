# "The Last Possession" — pilot sitcom scene (audio production)

The first GOAT Hoopers animated-sitcom scene, produced audio-first on 2026-11-10
as the template the Blender build will animate to. Clubhouse set, full ensemble,
2:29.5 finished mix. Aidan's verdict: likes it, continue — his notes are in
`FEEDBACK.md` and are deliberately deferred to one Final Cut revision pass once
the animated cut exists (do not re-cut the pilot piecemeal).

| File | What it is |
|---|---|
| `script.md` | Full script (~375 words) + cast/voice map + position map + cue sheet |
| `scene-pilot-audio.mp3` | The finished mix (−16.6 LUFS, true peak −1.51 dBTP) |
| `QC.md` | Measured duration/loudness, timestamped timeline, production checklist |
| `FEEDBACK.md` | Aidan's notes (dialogue naturalism — overlaps/reactivity — banked for the Final Cut pass) |
| `mix-build.py` | The rerunnable mix script — the whole scene rebuilds from the files here |
| `audio/lines/` | All 22 generated lines, `NN-character.mp3` (12-lax is the generated inaudible whisper — Lord Lax never speaks) |
| `audio/music-*.mp3` | ElevenLabs-generated score: intro/outro stings, fail sting, underscore bed (non-diegetic only) |
| `audio/sfx-*.mp3` | ElevenLabs-generated SFX: room bed with TV game murmur (diegetic), crowd eruption, phone buzz |

**Not shipped:** the processed per-line stems (`audio/proc/`, ~21 MB of WAV) are
intermediates — `mix-build.py` regenerates them from `audio/lines/` + the
music/SFX files above, so they aren't versioned here.

Voices: Aidan is his real ElevenLabs clone (the canon "Aidan Daly" — see
[`../../voice-casting/CLONES.md`](../../voice-casting/CLONES.md)); everyone else
is an ElevenLabs premade voice cast at Muse's discretion, except Tyrese, who
explicitly requested James Earl Jones — no licensed JEJ voice exists on
ElevenLabs, so he gets the deepest commanding premade register (Brian).
Dialogue is mixed by couch position per the script's position map; the music
sits ≥10 dB under dialogue.
