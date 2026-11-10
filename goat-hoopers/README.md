# GOAT Hoopers — start here

Everything needed to make the GOAT Hoopers videos, in one folder: the production
pipeline, the working skills, the design system, and the asset library. Pull this
repo down and you can run an episode yourself — the docs assume a competent person
(or their agent) with access to the league data and a video toolchain.

## Reading order

1. **This file** — the map.
2. **[`PRODUCTION.md`](PRODUCTION.md)** — the end-to-end episode pipeline: verified
   data → script → music-first → footage → voiceover → graphics → cameo scenes →
   QC gates → upload package → delivery.
3. **[`skills/`](skills/)** — the two working skills, snapshotted from production:
   - [`skills/fantasy-recap-video-qc/SKILL.md`](skills/fantasy-recap-video-qc/SKILL.md)
     — the recap release gates. This is the law; PRODUCTION.md is the summary.
   - [`skills/goat-hoopers-hype-video/SKILL.md`](skills/goat-hoopers-hype-video/SKILL.md)
     — the beat-synced hype-video playbook (preseason/specials, clip sourcing).
4. **[`ASSET-GENERATION.md`](ASSET-GENERATION.md)** — how every asset is made: the
   cast design flow, the STYLE LOCK, rig sheets, voice casting, the music pool,
   and the repo conventions.
5. **[`cameo-library/`](cameo-library/)** — the assets themselves (below).

## Contents

| Path | What it is |
|---|---|
| `PRODUCTION.md` | The episode pipeline, step by step |
| `ASSET-GENERATION.md` | How the cast, rigs, voices, and graphics get made |
| `skills/fantasy-recap-video-qc/` | Recap release-gates skill (snapshot, synced 2026-11-10) |
| `skills/goat-hoopers-hype-video/` | Hype-video playbook skill (snapshot, synced 2026-11-10) |
| `cameo-library/` | Reference photos + `NOTES.md`, the asset library root |
| `cameo-library/designs/` | The 2D design system: `STYLE.md`, one file per person, `renders/` |
| `cameo-library/designs/blender/` | The locked 3D animated-sitcom cast — start at its `README.md`; `BLENDER-DESIGN.md` is the build spec, `final/` the frozen renders, `RIG-DESIGN.md` + `rig-sheets/` the rig design |
| `../general/music-pool.md` | The shared no-repeat music pool (Hoopers + Emperor) |
| `../general/muse/` | Muse's identity refs (the avatar is Muse's canon design) |
| `../emperor-phil/` | The sister series — same pipeline, its own folder |

## The three rules that outrank everything else

- **Verified or silent:** scores and results come from authenticated leg totals for
  both teams (this is a lock-in league — public feed numbers lie), or they're not
  stated at all.
- **The narrator is Muse,** never first-person-as-Aidan.
- **STYLE LOCK:** never deviate from the cast's render style — all character work
  is an edit anchored on the canon renders in `cameo-library/designs/blender/final/`.

Video masters and upload encodes are **not** in this repo by design (workspace +
Google Drive); see the root README for the repo-wide rules.
