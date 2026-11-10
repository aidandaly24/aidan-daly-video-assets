# GOAT Hoopers — Blender Cast Package

The locked 3D animated-sitcom cast for the GOAT Hoopers recap scenes, designed 2026-11-10
and approved by Aidan ("this is amazing") after three rounds of fixes.

## What's canon

- **`final/`** — the approved character renders (10) + `cast-lineup.png` + `muse-identity-ref.png`.
  Build from these and from `BLENDER-DESIGN.md`, nothing else.
- **`BLENDER-DESIGN.md`** — the full build spec: shared proportions, one base rig with build
  variants, per-character specs, palette, ban list. If a render and the spec disagree, the spec
  wins — except Muse, whose canon is the avatar design (see spec §3.1).
- **Working renders** in this folder's root are the same images as `final/` (root = working
  copies, `final/` = the frozen approved set).

## Review history (2026-11-10)

- v1: first full cast. Aidan: "fucking great" — with Vann's hair too poofy, Tommy + Griffin a
  lil too chubby, and Muse's render not matching Muse's real design.
- v2 (`archive/v2/`): Vann's hair tightened (accepted as final), Tommy/Griffin slimmed once.
- v3 (current): Tommy/Griffin slimmed a further step (STOCKY torso ×1.22 → ×1.08 in spec);
  Muse regenerated from Aidan's actual avatar design — the frosted-face crystal, not the
  invented spiky golem in the v1/v2 renders (`archive/`).
- Late additions (2026-11-10): Kearns' eyes corrected to blue (kept). Tommy and Hiram were
  remodeled from new photos Aidan sent — both drifted OFF the cast's render style, and Aidan
  reverted both the same day ("It's extremely important u don't deviate from style ever" —
  see the STYLE LOCK in BLENDER-DESIGN.md). The photoreal attempts are in `archive/`; the
  photos stay in the library. `hiram-chef.png` (Chef-Hatchet-style side version, the league
  group's suggestion, spec §3.9b) was rebuilt as an in-style edit of the base Hiram.

## Key identity locks

- Muse = Aidan's chosen avatar design: chubby rounded faceted translucent-blue crystal,
  frosted white face, black bead eyes, tiny smile, pink blush. Reference: `muse-identity-ref.png`.
- Aidan: middle part + tortoiseshell glasses (his render is confirmed to look like him).
- Kearns: black quarter-zip, gold medal, black cap. Phil: red shirt, backwards cap, capybara.
- Lord Lax: full lacrosse gear, helmet on, face never invented. Whisper gag is standing
  (see `../../NOTES.md`).
- No garment text/logos in the build (source-photo artifacts) — only Lax's "65" survives.

## Also in this package

- **`RIG-DESIGN.md`** — the rig spec: one base armature, per-character presets, face rig,
  Muse's control rig, props.
- **`rig-sheets/`** — the rig design sheets (2026-11-10): one pose/expression sheet per
  character (`rig-aidan.png`, `rig-kearns.png`, `rig-phil.png` with the capybara,
  `rig-vann.png`, `rig-tommy.png`, `rig-griffin.png`, `rig-tyrese.png`, `rig-hiram.png`,
  `rig-hiram-chef.png`, `rig-lord-lax.png`, `rig-muse.png`) plus `rig-skeleton.png`, the
  base armature drawn over the canon Aidan render. Each sheet is an edit anchored on the
  canon render (STYLE LOCK) and is the §8 acceptance test in design form — see
  RIG-DESIGN.md §9.

## Next

Sets get the same treatment (renders + spec in a `sets/` folder here) for Aidan's review
before any Blender building starts.
