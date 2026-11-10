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
| `rig-aidan.png` | Pre-canonical template row; missing Fired Up, Dejected, Menacing, Surprised; an earlier same-day partial attempt collapsed the layout (archived) | All 8 canonical close-ups in order in a 4+4 block under the unchanged 5 poses; Angry closed-mouth ~6/10; glasses on in every panel, middle part locked; no text/logos. Old sheet: `archive/rig-sheets/rig-aidan-v1-five-expression.png`; partial attempt: `archive/rig-sheets/rig-aidan-v2-partial-five-panel.png`. |
| `rig-phil.png` | Template row; missing Fired Up, Dejected, Menacing, Surprised | All 8 canonical close-ups in order; cap backwards and plain in every panel, capybara beside the neutral pose standing. First attempt of the completion pass produced a 15-panel grid (duplicated Neutral + sad) — rejected at `archive/rig-sheets/rig-phil-v2-rejected-fifteen-panel.png`; second attempt exact. Minor note: close-ups crop at the collar, so the sunglasses/wristband read in the pose row. Old sheet: `archive/rig-sheets/rig-phil-v1-pre-canonical.png`. |
| `rig-vann.png` | Template row; missing Fired Up, Menacing, Surprised; Dejected weak (flat panel only) | All 8 canonical close-ups in order; Dejected is now a full sad panel; tight-curl dome and seated lean intact, clean-shaven. Minor note: faint chin shading on the Angry/Menacing close-ups reads as form shadow — re-check against the no-stubble rule at build time. Old sheet: `archive/rig-sheets/rig-vann-v1-pre-canonical.png`. |
| `rig-tommy.png` | Template row; missing Fired Up, Dejected, Menacing, Surprised | All 8 canonical close-ups in order; puffer blocking exact, flat leprechaun patch (shapes only, no lettering), gold can in the neutral pose. Took four attempts in the completion pass — three layout failures archived (`rig-tommy-v2-rejected-collapsed-row.png`, `rig-tommy-v3-rejected-fourteen-panel.png`, `rig-tommy-v4-rejected-fourteen-panel.png`); the passing attempt anchored the layout on the Kearns PASS sheet as a grid template. Old sheet: `archive/rig-sheets/rig-tommy-v1-pre-canonical.png`. |
| `rig-griffin.png` | Template row + Dejected; missing Fired Up, Menacing, Surprised (closest of the queued sheets) | All 8 canonical close-ups in order; slumped couch sit kept; Oxford, chinos and tight curls locked; no graduation items anywhere. Old sheet: `archive/rig-sheets/rig-griffin-v1-pre-canonical.png`. |
| `rig-tyrese.png` | Template row; missing Fired Up, Dejected, Menacing, Surprised; Angry hottest of the template set (~7–8) | All 8 canonical close-ups in order; Angry pulled down to the ~6 cap, closed mouth; stripes + cross locked (cross visible in all 5 poses; close-ups crop at the collar). Completion pass: attempt 1 collapsed to one row of 5 — archived as `archive/rig-sheets/rig-tyrese-v2-rejected-collapsed-row.png`; attempt 2's output file was lost by the generation pipeline (reported path never written to disk); attempt 3, anchored on the Kearns PASS layout, is exact. Old sheet: `archive/rig-sheets/rig-tyrese-v1-pre-canonical.png`. |
| `rig-muse.png` | Five-state sheet: Neutral, Celebrating, Surprised, Deadpan present; Fired Up, Angry, Dejected missing; Menacing not distinct from the skeptical panel | All 8 canonical close-ups in order, expressed only in the §3.1 plate language (bead-eye shapes, smile curve, blush — no mouth interior anywhere); 5 hover/bob poses on top (neutral hover, bobbing drift, arms-up, point, standing planted). Angry angled and closed-mouth at the ~6 cap. Re-dispatch pass: attempt 1 put small open mouths on two pose-row figures — rejected (mouth-interior ban), archived as `archive/rig-sheets/rig-muse-v2-rejected-open-mouths.png`; attempt 2 fixed only the mouths and is exact. Minor note: the Menacing plate keeps a faint blush where the prompt asked for none — the slanted side-glance carries the read. Old sheet: `archive/rig-sheets/rig-muse-v1-five-state.png`. |

## Substantially conforms — left as-is

| Sheet | Coverage | Gaps / notes |
|---|---|---|
| `rig-hiram.png` | Neutral (teeth grin) ✓, Celebrating ✓ (laugh + wink variant), Deadpan ✓ (flat panel), Angry ✓ (~7/10 heavy glare, closed mouth — at-cap side), Menacing ✓ (the same heavy-brow glare panel doubles), Fired Up ~partial (fist-pump point pose) | Missing: Dejected, Surprised. Closest sheet in the cast; the two gaps are noted for the build-time re-render rather than a design regen. |
| `rig-lord-lax.png` | CONFORMS BY DESIGN. No face — ever (§3.10 hard lock). The bottom row is helmet states (level / down / whisper lean / up / shrug) and emotion plays through helmet tilt + body language: Neutral = level, Dejected = down-tilt, Surprised = up-tilt, Celebrating = fists-up state | Not a failure and not regenerated — drawing him a face would break the package's hardest lock. Expanding the helmet-state row is a possible future pass if Aidan wants it. |

## Regeneration queue — EMPTY

The completion pass (2026-11-10) regenerated all six human sheets from the original
queue — Aidan, Phil, Vann, Tommy, Griffin, Tyrese — and the final re-dispatch the
same day regenerated Muse, the last sheet in the queue. Every sheet in the cast is
now resolved: nine regenerated to the canonical set (PASS table above), Hiram
substantially conforming with two gaps noted for the build-time re-render, and Lord
Lax conforming by design (helmet states, no face — ever). Nothing remains queued.

## Regeneration recipe (the pattern used for every sheet above)

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
