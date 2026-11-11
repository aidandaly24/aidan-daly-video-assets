# aidan-daly-video-assets

The home for everything behind Aidan's videos — the production skills, reference
photos, character designs, build specs, set designs, the pilot scene, and the
voice casting — versioned in one public repo so anyone (Aidan, a league member,
or their agent) can pull it down and make videos.

Reorganized 2026-11-10: one canonical copy of everything, superseded versions in
`archive/` folders with an index, no duplicate files. The skills live in their
own folder at the root, separate from the assets.

## Map

- **`skills/`** — the video-making skills and pipeline docs, in their own
  folder. **Start at [`skills/README.md`](skills/README.md).**
  - `PRODUCTION.md` — the end-to-end episode pipeline (the operating manual).
  - `ASSET-GENERATION.md` — how every asset is made (cast design flow, STYLE
    LOCK, rig sheets, voice casting, music pool).
  - `local-fantasy-recap-video-qc/` — the recap release gates. The law.
  - `local-goat-hoopers-hype-video/` — the beat-synced hype-video playbook.

- **`goat-hoopers/`** — the GOAT Hoopers fantasy series. **Start at
  [`goat-hoopers/README.md`](goat-hoopers/README.md).**
  - `cameo-library/` — the asset library itself:
    - Reference photos of all nine league members + `NOTES.md` at the root.
    - `designs/` — the written design system: `STYLE.md` + one design file per person.
    - `designs/blender/` — the locked 3D animated-sitcom cast package. Start at its
      `README.md`. Canon renders live in `designs/blender/final/` — that folder only;
      there are no working duplicates. Rig design in `RIG-DESIGN.md` +
      `rig-sheets/`, set designs in `sets/`.
    - `archive/` — superseded versions (pre-Blender 2D renders, older lineup renders),
      each explained in `archive/INDEX.md`. A second, older archive inside
      `designs/blender/archive/` holds the v1/v2 render rounds and all generation logs.
  - `scenes/the-last-possession/` — the pilot sitcom scene, audio production
    complete: script, finished mix, all 22 lines, ElevenLabs-generated music +
    SFX, the rerunnable mix script, QC, and Aidan's feedback.
  - `voice-casting/` — the ElevenLabs clone registry (`CLONES.md`), generated
    clone test lines, board-era previews, and the voice-sample library.

- **`general/`** — shared across every series:
  - `muse/` — Muse's identity: the avatar Aidan chose + the cast identity reference.
  - `music-pool.md` — the shared no-repeat music pool (a track used in ANY recap is burned).

## Where the canon version of a thing lives

| Thing | Canon location |
|---|---|
| Production skills + pipeline docs | `skills/` (repo root) |
| Approved character renders | `goat-hoopers/cameo-library/designs/blender/final/` |
| Cast lineup | `goat-hoopers/cameo-library/designs/blender/final/cast-lineup.png` |
| Character build spec | `goat-hoopers/cameo-library/designs/blender/BLENDER-DESIGN.md` |
| Rig spec + pose/expression sheets | `.../designs/blender/RIG-DESIGN.md`, `.../designs/blender/rig-sheets/` |
| Set designs | `goat-hoopers/cameo-library/designs/blender/sets/` |
| Member reference photos | `goat-hoopers/cameo-library/*.jpg` (+ `NOTES.md`) |
| Per-person written designs | `goat-hoopers/cameo-library/designs/<person>.md` |
| Pilot scene (script, mix, lines) | `goat-hoopers/scenes/the-last-possession/` |
| Voice clone registry + test lines | `goat-hoopers/voice-casting/` (`CLONES.md`) |
| Superseded versions | `goat-hoopers/cameo-library/archive/` (see its `INDEX.md`) and `.../designs/blender/archive/` |

## WHERE THINGS LIVE — the honest version

This repo holds the **design and production assets**: skills, specs, renders,
scripts, generated scene audio, and the voice-casting record. Some things live
elsewhere on purpose:

- **Finished video masters and upload encodes are NOT here.** They're far too
  large for git; they live in the production workspace and in Google Drive.
  This repo holds everything that *makes* the videos, not the finished videos.
- **The Voice Casting Board is a Muse Space, not a repo file.** Its decisions
  are baked into documents here: `goat-hoopers/voice-casting/CLONES.md` for the
  clones, and `VOICES.md` in the Blender design package once scene casting is
  final.
- **Raw personal voice recordings are deliberately excluded.** Only generated
  test lines and the registry are published — the unscripted personal audio a
  clone was trained on stays in the private workspace. See
  `goat-hoopers/voice-casting/README.md`.
- **There are no Blender model files in this repo yet. None.** No `.blend`, no
  `.fbx`, no `.glb` — the characters and sets exist today as *designs*: approved
  renders, written build specs, rig sheets, and reference photos. When the
  Blender build phase produces models, they will land under
  `goat-hoopers/cameo-library/designs/blender/` via **Git LFS** (see
  `.gitattributes`), in the same folders as their designs.
- The Emperor Phil series folder was removed on 2026-11-10 at Aidan's
  direction and stays out.

## Rules

- One canonical copy of every asset. A new version replaces the canon file in place;
  the old one goes to the matching `archive/` with a line in its index.
- When a design is locked, the frozen copy goes in that package's `final/` folder.
- Never commit video masters/encodes.
