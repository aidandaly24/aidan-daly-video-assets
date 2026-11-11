# Voice clones (ElevenLabs IVC) — registry

| Person | voice_id | Source | Cloned | Status |
|---|---|---|---|---|
| Aidan | dR3nyDNtgOehM6hFVppi | Gramercy.m4a (2:05 — 3 scripted takes + ~100s natural talk) | 2026-11-10 | Aidan's verdict: close, but too raspy — the clone averaged in the rougher end-of-day stretches of the memo. DELETED 2026-11-10 at Aidan's direction (verified gone). |
| Aidan Clean (v2) | bOVCvLBPiUDwbKwnx9FL | aidan-clean-source.wav — cleanest 70s of the same memo (0–15, 25–50, 55–60, 80–100, 110–115), selected by per-window harmonics-to-noise | 2026-11-10 | Pitch check: 118.5 Hz vs original 117.6 Hz. Test lines: v2-normal (defaults), v2-smooth (stability 0.65 / similarity 0.6), v2-hype. Better than v1, still lost to the self-made clone. DELETED 2026-11-10 at Aidan's direction (verified gone). |
| **Aidan Daly (self-made) — CANON** | sMn0hBXKAv51Hv74thbb | Created by Aidan himself in the ElevenLabs web UI clone flow, reading the passage ElevenLabs provides there | 2026-11-10 | Aidan's verdict: "way better" — the clear winner. Sole Aidan clone on the account. Aidan's read on why: the provided passage is better source material than a free-form memo. |

Lessons for later members:
- IVC bakes in whatever texture dominates the source — relaxed/late-night fry in the tail of a memo becomes the clone's default rasp. Prefer cloning from the cleanest stretches, not the whole file.
- The winning recipe was the ElevenLabs web clone flow's own provided passage, read fresh and steady. Member memos should mirror it: a clear, steady read of one full phonetically varied passage, plus the energy takes — not free talk alone.

Test files (this folder): original-aidan-clubhouse.mp3 (his real take, cut from the memo), test-aidan-normal.mp3 / test-aidan-hype.mp3 / test-aidan-annoyed.mp3 (v1), test-aidan-v2-*.mp3 (v2), test-aidan-selfmade.mp3 (canon clone reading the clubhouse line).

Process per member: receive memo per the scripted ask → clone via the elevenlabs helper → generate the same 3 test lines → A/B against the original take → record verdict here → bake final picks into VOICES.md (designs/blender/).
