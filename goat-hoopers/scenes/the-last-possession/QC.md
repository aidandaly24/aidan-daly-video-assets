# QC — "The Last Possession" pilot scene audio

**Final mix:** `scene-pilot-audio.mp3` (this folder) · 192 kbps stereo mp3 · built by `mix-build.py` (rerunnable)

## Measured results

| Check | Result |
|---|---|
| Final duration | **149.5s (2:29.5)** — target 2:15–2:45 ✓ |
| Integrated loudness | **−16.6 LUFS** (target ≈ −16) ✓ |
| True peak | **−1.51 dBTP** — no clipping anywhere ✓ |
| Dialogue word count | ~375 (target 330–390) ✓ |
| Underscore under dialogue | Dialogue RMS −22.2 dB vs underscore mixed at −35.2 dB RMS = **13 dB under** (≥10 required) ✓ |
| Room bed | Set 25 dB under dialogue RMS; diegetic, looped full scene ✓ |
| Segment spot-checks | Crowd climax window RMS −14.6 dB (loudest moment ✓) · whisper window −25.9 dB (present, deliberately near-inaudible ✓) · Muse closer window −23.3 dB (clean, dry ✓) |

## Checklist

- [x] Every character present: Aidan (6 lines), Kearns (2), Phil (2), Griffin (2), Vann (3), Tyrese (2), Hiram (1, kitchen), Tommy (1), Muse (2), Lord Lax (whisper SFX — no voice, per the rule)
- [x] Aidan has the most lines; his real ElevenLabs clone used (`sMn0hBXKAv51Hv74thbb`)
- [x] Tyrese = Brian, deepest premade, stability 0.6, slow weighty lines ×2 (defensive rebound, garbage-time free throw) — the James Earl Jones register he requested (no licensed JEJ voice exists on ElevenLabs)
- [x] Whisper gag complete: injury-report ask → inaudible whisper → Vann's self-serving "translation" (Giannis trade) → call-out → Vann admits the real translation
- [x] Griffin 0–6 beat: raises his own game, waved off with one word, self-aware about it
- [x] Kearns deadpan stat line (the lead "has a mailing address")
- [x] Climax: final shot misses (pre-made crowd eruption), whistle, Tyrese free-throw eulogy, second smaller eruption (−6 dB, trimmed) as the FT drops — Phil wins by 0.6
- [x] Button: generated sad-brass fail sting → dry Muse closer → generated playful outro sting
- [x] Music is non-diegetic score only (intro sting / underscore / fail sting / outro sting); the only diegetic bed is the room/TV ambience
- [x] Spatial mix per position map: constant-power pans, Hiram lowpassed at 6 kHz + reverb + −3 dB (kitchen), Tyrese light reverb +presence (the boom), Phil slight reverb (armchair, back), whisper ×0.35 at Lax's seat; **pitch untouched on every line**
- [x] Pre-made intro sting and crowd eruption reused, not regenerated
- [x] No line clipped: every line processed from its full generated file; final peak −1.51 dBTP

## Final timeline (seconds)

| Time | Element |
|---|---|
| 0.00 | Intro sting (fades out 6.0–8.0) |
| 7.30–19.51 | 01 Aidan — cold open |
| 19.91–27.67 | 02 Kearns — mailing address |
| 28.07–34.66 | 03 Phil — emperor |
| 35.01–44.47 | 04–06 Griffin / Vann / Griffin — 0–6 beat |
| 44.97–51.71 | 07 Tyrese — the rebound |
| 52.16–59.03 | 08 Hiram — wings (kitchen) |
| 59.43–65.00 | 09 Tommy — week two |
| 65.40–71.30 | 10 Muse — very bad night |
| 70.20 | Phone buzz |
| 71.90–78.72 | 11 Aidan — injury report ask |
| 79.27–82.27 | 12 Lord Lax — whisper (inaudible) |
| 82.72–100.00 | 13–15 Vann / Aidan / Vann — translation, call-out, real translation |
| 100.60–105.01 | 16 Aidan — he's pulling up |
| 104.91 | Crowd eruption #1 — the miss |
| 107.21–109.53 | 17 Aidan — premature celebration |
| 109.88–119.74 | 18–19 Kearns whistle → Tyrese free-throw eulogy |
| 120.09 | Crowd eruption #2 — the free throw drops |
| 121.79–127.45 | 20 Phil — coronation |
| 127.90–133.05 | 21 Aidan — ceremonial free throw |
| 133.55–137.57 | Fail sting |
| 137.83–142.66 | 22 Muse — closer |
| 143.16–149.19 | Outro sting |

## Notes

- Underscore (45s) is looped once under the dialogue at −13 dB relative; the loop seam is masked by the room bed and dialogue.
- Processed per-line stems live in `audio/proc/` for the Blender stage; `mix-raw.wav` was removed (regenerable via `mix-build.py`).
- Tommy's seat wasn't in the original position map; mixed at pan −0.05 (couch, just left of center), dry.
- All ElevenLabs calls succeeded; no permission or rate-limit errors. Account usage after this production: well under the 131,000-character plan limit.
