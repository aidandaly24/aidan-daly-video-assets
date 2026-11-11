# GOAT Hoopers — start here

Everything needed to make the GOAT Hoopers videos: the asset library, the pilot
scene, the voice casting, and (one folder up) the production skills. Pull this
repo down and you can run an episode yourself — the docs assume a competent
person (or their agent) with access to the league data and a video toolchain.

## Reading order

1. **This file** — the map.
2. **[`../skills/PRODUCTION.md`](../skills/PRODUCTION.md)** — the end-to-end
   episode pipeline: verified data → script → music-first → footage →
   voiceover → graphics → cameo scenes → QC gates → upload package → delivery.
3. **[`../skills/`](../skills/)** — the production skills, in their own folder
   at the repo root:
   - [`../skills/local-fantasy-recap-video-qc/SKILL.md`](../skills/local-fantasy-recap-video-qc/SKILL.md)
     — the recap release gates. This is the law; PRODUCTION.md is the summary.
   - [`../skills/local-goat-hoopers-hype-video/SKILL.md`](../skills/local-goat-hoopers-hype-video/SKILL.md)
     — the beat-synced hype-video playbook (preseason/specials, clip sourcing).
   - [`../skills/ASSET-GENERATION.md`](../skills/ASSET-GENERATION.md) — how every
     asset is made: the cast design flow, the STYLE LOCK, rig sheets, voice
     casting, the music pool, and the repo conventions.
4. **[`cameo-library/`](cameo-library/)** — the assets themselves (below).
5. **[`scenes/`](scenes/)** and **[`voice-casting/`](voice-casting/)** — the
   animated-sitcom production: the pilot scene and the cast's real voices.

## Contents

| Path | What it is |
|---|---|
| `cameo-library/` | The asset library: reference photos + `NOTES.md` at the root |
| `cameo-library/designs/` | The written design system: `STYLE.md` + one design file per person |
| `cameo-library/designs/blender/` | The locked 3D animated-sitcom cast — start at its `README.md`; `BLENDER-DESIGN.md` is the build spec, `final/` holds the only copies of the approved renders, `RIG-DESIGN.md` + `rig-sheets/` the rig design, `sets/` the set designs |
| `cameo-library/archive/` | Superseded versions (pre-Blender 2D renders, older lineups) — see `archive/INDEX.md` for what each file is and what replaced it |
| `scenes/the-last-possession/` | The pilot sitcom scene, audio production complete: script, finished mix, all lines, generated music + SFX, the rerunnable mix script, QC + Aidan's feedback |
| `voice-casting/` | The clone registry (`CLONES.md`), generated clone test lines, board-era previews, and the voice-sample library — see its `README.md` for what is deliberately excluded |
| `../skills/` | The production skills + pipeline docs (repo root, separate folder) |
| `../general/music-pool.md` | The shared no-repeat music pool |
| `../general/muse/` | Muse's identity refs (the avatar is Muse's canon design) |

## What's NOT here yet

- **No Blender model files exist yet** — no `.blend` / `.fbx` / `.glb` anywhere in
  the repo. The cast and sets are designs (renders + specs + rig sheets +
  photos); the models get built from them and will be committed via Git LFS
  under `cameo-library/designs/blender/`. See the root README's "WHERE THINGS
  LIVE" section.
- No video masters or upload encodes (workspace + Google Drive, by design).
- No raw personal voice recordings — see `voice-casting/README.md`.
- The Emperor Phil series folder was removed 2026-11-10 at Aidan's direction
  and stays out; the shared music pool in `../general/` still covers both series.

## The three rules that outrank everything else

- **Verified or silent:** scores and results come from authenticated leg totals for
  both teams (this is a lock-in league — public feed numbers lie), or they're not
  stated at all.
- **The narrator is Muse,** never first-person-as-Aidan.
- **STYLE LOCK:** never deviate from the cast's render style — all character work
  is an edit anchored on the canon renders in `cameo-library/designs/blender/final/`.
