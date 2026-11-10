# aidan-video-assets

The saved-nicely home for every asset behind Aidan's videos — designs, renders, reference
photos, specs and reusable pieces, versioned in one place.

## Layout

- **`goat-hoopers/`** — GOAT Hoopers fantasy recap videos.
  - `cameo-library/` — the members' reference photos + notes, the 2D design system, and
    `designs/blender/` — the locked 3D animated-sitcom cast (renders, lineup, build spec)
    that the Blender scene pipeline is built from. Start at
    `cameo-library/designs/blender/README.md`.
- **`emperor-phil/`** — Emperor Phil's Slave Camp recap videos (design references, thumbnails).
- **`general/`** — shared across every series:
  - `muse/` — Muse's identity: the avatar Aidan chose + the cast identity reference.
  - `music-pool.md` — the shared no-repeat music pool (a track used in ANY recap is burned).

## Rules

- **Video masters and upload encodes do NOT live here** — they're gigabytes; they live in the
  workspace and Google Drive. This repo holds the assets that *make* the videos.
- Blender project files (`.blend`) are tracked with Git LFS (see `.gitattributes`) once the
  build starts on the Mac.
- When a design is locked, the frozen copy goes in that package's `final/` folder; working
  files stay beside it, earlier versions in `archive/`.
