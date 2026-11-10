# EMOTION AUDIT — rig sheets vs the cast-wide canonical set

Audit date: 2026-11-10. Standard: RIG-DESIGN §8 (Aidan's ruling, 2026-11-10) — every
character carries the SAME eight expressions: **Neutral (spec default), Celebrating,
Fired Up, Angry (capped ~6/10), Deadpan, Dejected, Menacing, Surprised.** Personas
flavor only the default. Every sheet below was viewed panel by panel (both rows —
pose-row faces count toward coverage, expression-row close-ups are the standard's home).

**Intensity calibration used throughout:** at-cap Angry = closed mouth, brows down,
scowl/pout (~6–7/10, reads "annoyed"). Outlier = open-mouth scream, teeth-bared
grimace, or nose-scrunched rage (~8–10/10, reads "enraged") — the thing Aidan flagged
on Kearns' original sheet.

## Regenerated to the canonical set — PASS

| Sheet | Before | After (verified panel by panel) |
|---|---|---|
| `rig-kearns.png` | "Volcano" set: Angry at ~9–10/10 (grimace, bared teeth) + a full scream in the point pose; no distinct Celebrating, Dejected or Menacing | All 8 canonical close-ups in order; Angry is closed-mouth annoyed (~6/10); point pose is a cheerful point-laugh; plain cap and quarter-zip (no text/logos); medal, blue eyes, beard, cap-forwards locked in every panel. Minor note: bust close-ups crop at the collar, so the medal ribbon shows in the pose row only. Old sheet: `archive/rig-sheets/rig-kearns-v1-volcano.png`. A first regen attempt added cap/brand logos and a broken layout — rejected, at `archive/rig-sheets/rig-kearns-v2-rejected-logos-layout.png`. |
| `rig-hiram-chef.png` | Stern in every panel; rage scream close-up ~9/10 + grimace ~8/10; no Celebrating, Dejected or Surprised | Stern DEFAULT kept (§3.9b) + all 8 canonical close-ups in order; Angry closed-mouth ~6/10; point pose is a firm stern point, no shout; toque/coat/apron plain, build unchanged. Minor note: close-ups crop the toque to its band (full toque in the pose row). Old sheet: `archive/rig-sheets/rig-hiram-chef-v1-hot-set.png`. |

## Substantially conforms — left as-is

| Sheet | Coverage | Gaps / notes |
|---|---|---|
| `rig-hiram.png` | Neutral (teeth grin) ✓, Celebrating ✓ (laugh + wink variant), Deadpan ✓ (flat panel), Angry ✓ (~7/10 heavy glare, closed mouth — at-cap side), Menacing ✓ (the same heavy-brow glare panel doubles), Fired Up ~partial (fist-pump point pose) | Missing: Dejected, Surprised. Closest sheet in the cast; the two gaps are noted for the build-time re-render rather than a design regen. |
| `rig-lord-lax.png` | CONFORMS BY DESIGN. No face — ever (§3.10 hard lock). The bottom row is helmet states (level / down / whisper lean / up / shrug) and emotion plays through helmet tilt + body language: Neutral = level, Dejected = down-tilt, Surprised = up-tilt, Celebrating = fists-up state | Not a failure and not regenerated — drawing him a face would break the package's hardest lock. Expanding the helmet-state row is a possible future pass if Aidan wants it. |

## Fails the canonical set — regeneration QUEUED

All six human sheets below share the pre-canonical template row (Neutral / eyes-closed
content / Celebrating laugh / Angry pout-scowl / Deadpan) and are missing the same
emotions. None has a Kearns-style scream/grimace outlier; the template Angry is a
closed-mouth scowl at ~6–7/10 (Tyrese's runs hottest, ~7–8 on brow angle).

| Sheet | Present | Missing | Status |
|---|---|---|---|
| `rig-aidan.png` | Neutral ✓, Celebrating ✓, Angry ✓ (~7 pout-scowl), Deadpan ✓ | Fired Up, Dejected, Menacing, Surprised | Regen attempted 2026-11-10: the generator collapsed the expression block into one row of 5 close-ups (Deadpan / Dejected / Angry / Menacing / Surprised — Angry correctly capped, glasses locked throughout), leaving Fired Up unshown and Neutral/Celebrating only in the pose row. Archived as a partial at `archive/rig-sheets/rig-aidan-v2-partial-five-panel.png`; the v1 sheet stays live and Aidan stays QUEUED. |
| `rig-phil.png` | Neutral ✓ (unbothered half-smile), Celebrating ✓, Angry ✓ (~7), Deadpan ✓ | Fired Up, Dejected, Menacing, Surprised | QUEUED |
| `rig-vann.png` | Neutral ✓ (smirk), Celebrating ✓, Angry ✓ (~6–7), Deadpan ✓ (half-lid translator face) | Fired Up, Menacing, Surprised; Dejected weak (flat panel only) | QUEUED |
| `rig-tommy.png` | Neutral ✓, Celebrating ✓, Angry ✓ (~7), Deadpan ✓ | Fired Up, Dejected, Menacing, Surprised | QUEUED |
| `rig-griffin.png` | Neutral ✓ (small sad smile), Celebrating ✓, Angry ✓ (~6–7), Deadpan ✓, Dejected ✓ (close-up + slumped sit — the only queued sheet that has it) | Fired Up, Menacing, Surprised | QUEUED — closest of the queued sheets |
| `rig-tyrese.png` | Neutral ✓, Celebrating ✓, Angry ✓ (~7–8, hottest of the template set — brow angle; closed mouth), Deadpan ✓ | Fired Up, Dejected, Menacing, Surprised | QUEUED — regen should also pull Angry down to the ~6 cap |
| `rig-muse.png` | Neutral ✓, Celebrating ✓ (happy arcs, arms-up pose, blush panel), Surprised ✓ (wide eyes, o-mouth), Deadpan ✓ (skeptical half-lid) | Fired Up, Angry, Dejected; Menacing not distinct from the skeptical panel | QUEUED — regen must anchor on the §3.1 avatar design (`../muse-identity-ref.png`): the set expressed only through bead eyes, smile curve and blush; no mouth interior, ever |

## Regeneration recipe (for the queued sheets)

Same pattern that produced the two PASS sheets: edit anchored on the existing sheet
plus the character's canon render in `../final/` (STYLE LOCK — never a fresh generation
from photos). Layout: top row keeps the 5 poses and their content; the expression block
becomes two rows of 4 close-ups in canonical order (Neutral, Celebrating, Fired Up,
Angry → Deadpan, Dejected, Menacing, Surprised). Prompt must state: exactly 13 panels;
Angry mid-intensity, mouth tight and CLOSED, no scream/grimace/bared teeth anywhere;
absolutely no text, letters, numbers, logos or patches (plain garments); the
character's identity locks named explicitly. Archive the outgoing sheet to
`../archive/rig-sheets/` with a clear name before replacing, and view the result panel
by panel before calling it done — the generator's known failure modes are logo/text
invention (Kearns attempt 1) and collapsing the two expression rows into one (Aidan
attempt 1).
