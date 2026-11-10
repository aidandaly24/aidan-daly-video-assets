# aidan-daly-video-assets

The home for every asset behind Aidan's videos — reference photos, character designs,
build specs, set designs, and the production docs — versioned in one public repo so
anyone (Aidan, a league member, or their agent) can pull it down and make videos.

Reorganized 2026-11-10: one canonical copy of everything, superseded versions in
`archive/` folders with an index, no duplicate files.

## Map

- **`goat-hoopers/`** — the GOAT Hoopers fantasy recap series. **Start at
  [`goat-hoopers/README.md`](goat-hoopers/README.md)** — the pipeline, the skills, and
  the design docs for making the videos yourself all start there.
  - `PRODUCTION.md` — the end-to-end episode pipeline.
  - `ASSET-GENERATION.md` — how every asset is made (cast design flow, STYLE LOCK,
    rig sheets, voice casting, music pool).
  - `skills/` — the two working production skills, snapshotted from production.
  - `cameo-library/` — the asset library itself:
    - Reference photos of all nine league members + `NOTES.md` at the root.
    - `designs/` — the written design system: `STYLE.md` + one design file per person.
    - `designs/blender/` — the locked 3D animated-sitcom cast package. Start at its
      `README.md`. Canon renders live in `designs/blender/final/` — that folder only;
      there are no working duplicates anymore. Rig design in `RIG-DESIGN.md` +
      `rig-sheets/`, set designs in `sets/`.
    - `archive/` — superseded versions (pre-Blender 2D renders, older lineup renders),
      each explained in `archive/INDEX.md`. A second, older archive inside
      `designs/blender/archive/` holds the v1/v2 render rounds and all generation logs.
- **`general/`** — shared across every series:
  - `muse/` — Muse's identity: the avatar Aidan chose + the cast identity reference.
  - `music-pool.md` — the shared no-repeat music pool (a track used in ANY recap is burned).

## Where the canon version of a thing lives

| Thing | Canon location |
|---|---|
| Approved character renders | `goat-hoopers/cameo-library/designs/blender/final/` |
| Cast lineup | `goat-hoopers/cameo-library/designs/blender/final/cast-lineup.png` |
| Character build spec | `goat-hoopers/cameo-library/designs/blender/BLENDER-DESIGN.md` |
| Rig spec + pose/expression sheets | `.../designs/blender/RIG-DESIGN.md`, `.../designs/blender/rig-sheets/` |
| Set designs | `goat-hoopers/cameo-library/designs/blender/sets/` |
| Member reference photos | `goat-hoopers/cameo-library/*.jpg` (+ `NOTES.md`) |
| Per-person written designs | `goat-hoopers/cameo-library/designs/<person>.md` |
| Superseded versions | `goat-hoopers/cameo-library/archive/` (see its `INDEX.md`) and `.../designs/blender/archive/` |

## WHAT'S NOT HERE YET — read this before you pull

- **There are no Blender model files in this repo. None.** No `.blend`, no `.fbx`, no
  `.glb` — the characters and sets exist today as *designs*: approved renders, written
  build specs, rig sheets, and reference photos. The actual 3D builds happen later,
  on Aidan's Mac, working from these designs.
- So if you pull this repo today (e.g. to mess around with your own character), what
  you get is everything needed to *build or brief* the models — not posable models
  themselves.
- When the builds exist, model files will be committed here via **Git LFS** (see
  `.gitattributes`) in the same folders as their designs.
- **Video masters and upload encodes are not here either** — they're gigabytes; they
  live in the workspace and Google Drive. This repo holds the assets that *make* the
  videos, not the finished videos.

## Rules

- One canonical copy of every asset. A new version replaces the canon file in place;
  the old one goes to the matching `archive/` with a line in its index.
- When a design is locked, the frozen copy goes in that package's `final/` folder.
- Never commit video masters/encodes.
