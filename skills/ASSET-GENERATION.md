# GOAT Hoopers — How the Assets Get Made

Every image, model, voice, and track behind the videos, and the process that produces
it. The point of this repo: pull it down and you have not just the assets but the
method. Production itself is in [`PRODUCTION.md`](PRODUCTION.md); this doc is about
where the pieces come from.

Everything below lives under [`goat-hoopers/cameo-library/`](../goat-hoopers/cameo-library/) unless noted.

---

## 1. Reference photos — the input layer

`goat-hoopers/cameo-library/*.jpg` — photos of each league member, supplied by Aidan (ask him for
the specific pics an episode needs; don't invent a person from nothing).
[`goat-hoopers/cameo-library/NOTES.md`](../goat-hoopers/cameo-library/NOTES.md) explains each photo: who it is,
which are extra angles (`tommy-2/3/4.jpg`, `hiram-2.jpg`), and what each is used for.
Photos are reference, never canon — canon is the locked design (§3), and when the two
disagree, the design wins (see the STYLE LOCK, §4).

## 2. The 2D design system

`goat-hoopers/cameo-library/designs/` — the original design pass (Nov 9, 2026):

- [`designs/STYLE.md`](../goat-hoopers/cameo-library/designs/STYLE.md) — the shared style rules.
- One file per person (`designs/aidan.md`, `designs/aedan.md`, …) — written identity
  and look per character.
- `designs/renders/` — the approved 2D renders of the cast in that system.

These designs feed the versus intros and any 2D generation. Every member is rendered
in one consistent look across all scenes, backed by their written design file.

## 3. The 3D cast — the Blender design package

`goat-hoopers/cameo-library/designs/blender/` — the animated-sitcom cast the scene pipeline is
built from. Start at its [`README.md`](../goat-hoopers/cameo-library/designs/blender/README.md)
(package manifest + review history). The flow that produced it:

1. **Generate model renders from the reference photos** — one full-body render per
   character in a shared system: 3.5-head stylized proportions, one base design
   language, warm-grey studio presentation. Muse is the exception: his canon is the
   avatar Aidan chose for him (chubby rounded faceted translucent-blue crystal,
   frosted white face, black bead eyes, tiny smile, pink blush) — reference at
   `designs/blender/muse-identity-ref.png`, also in `../general/muse/`. An early
   pass invented a different Muse; Aidan rejected it and the avatar design replaced
   it everywhere.
2. **Aidan review rounds** — v1 approved with notes ("fucking great": Vann's hair
   tighter; Tommy and Griffin slimmer), v2/v3 applied two slimming rounds
   (STOCKY torso ×1.22 → ×1.08), Kearns' eyes corrected to blue. Rounds are kept in
   `designs/blender/archive/` (v1, v2, comparisons, generation logs).
3. **Lock** — the approved set is frozen in `designs/blender/final/`, with
   `cast-lineup.png` as the full-cast reference. The build spec is
   [`designs/blender/BLENDER-DESIGN.md`](../goat-hoopers/cameo-library/designs/blender/BLENDER-DESIGN.md):
   shared proportions, per-character specs (§3.x), palette, identity locks, ban list.
   **If a render and the spec disagree, the spec wins** — except Muse, whose canon
   is the avatar.
4. **Side variants are edits, not new characters** — Chef Hiram
   (`designs/blender/hiram-chef.png`, spec §3.9b) is base Hiram re-dressed and
   scaled up for kitchen/intimidation bits; he never replaces base Hiram.

Identity locks worth knowing before generating anything: Lord Lax is always in full
lacrosse gear with the helmet ON — his face is never invented, the gear *is* the
identity, and "65" is the only garment number that survives (all other garment
text/logos are stripped in the build). Aidan's hair is a middle part. Phil travels
with a capybara sidekick.

## 4. THE STYLE LOCK

**Never deviate from the cast's render style. Ever.** (Aidan, 2026-11-10:
"extremely important.")

- All character work is an **edit anchored on the existing canon renders** — pose
  sheets, variants, new scenes take a canon render as the canvas.
- **Never generate a character fresh from photos.** Twice in one day, photo-based
  remodels (Tommy, then Hiram) came out in a more realistic render style than the
  cast; Aidan reverted both, and the originals stand. The failed attempts are kept
  in `designs/blender/archive/` as the cautionary tale, and the photos stayed in
  the library as references only.
- Style consistency **outranks photo accuracy**: where a real feature conflicts
  with the locked look, the locked look wins and the fact is noted in the spec
  (BLENDER-DESIGN.md §3.5 and §3.9 carry exactly these notes).

## 5. Rig sheets and the skeleton

`goat-hoopers/cameo-library/designs/blender/rig-sheets/` — one pose/expression sheet per
character (`rig-<name>.png`), each generated as an in-style edit anchored on that
character's canon render, plus `rig-skeleton.png`: the shared base armature drawn
deterministically (PIL) over the canon Aidan render — no generation involved, so it
can't drift. The rig spec (one base armature, per-character presets, the face rig,
Muse's control rig, props) is
[`designs/blender/RIG-DESIGN.md`](../goat-hoopers/cameo-library/designs/blender/RIG-DESIGN.md);
its §8 acceptance test is a pose sheet per character, and §9 maps the sheets to it.

Design proceeds step by step with Aidan's review at each step, people first:
Step 1 (rig design) is locked. **Step 2 (sets design) is in progress** — a `sets/`
folder inside `designs/blender/` with renders + spec, produced the same way.
Step 3 is pose/motion design. Only after the designs are approved does any Blender
building start (on Aidan's Mac, where Blender lives).

## 6. Voice casting

The cast's voices follow one model (Aidan's correction, 2026-11-10): **one set base
voice per character** — a consistent identity — with **emotion as a per-line
modulation on top of it**, expressed as offsets to pitch / speed / energy / grit /
warmth. Never assign a character a fixed emotion; the same voice plays angry,
deadpan, or celebrating as offsets from its base settings.

- Aidan casts the voices himself in the **Voice Casting Board** (a Muse Space):
  a shortlist of 16 real production voices, each with a playable sample of the same
  line, per-character sliders (pitch, speed, energy, grit, warmth), and emotion
  preset chips that show the effective settings.
- Once cast, the assignments are baked into **VOICES.md in
  `goat-hoopers/cameo-library/designs/blender/`** — the production source of truth for who sounds
  like what.
- **Muse's voice is fixed**: Helio, `avocado_v2:MAI_03` — the same configuration
  that narrates the recaps (see PRODUCTION.md §5).
- **Lord Lax has no voice**: the whisper gag is structural. He is never given a
  voice, in casting or in episodes.

## 7. Music

Tracks are not generated; they're selected — music-first, before editing — from the
shared no-repeat pool: [`../general/music-pool.md`](../general/music-pool.md). One
pool for every series; a track used in any recap is burned for all of them; no
Kendrick Lamar, ever. The pool file is the record: check it before proposing,
append on delivery. (Hoopers and Emperor share the pool — an Emperor burn once
killed a planned Hoopers slot, which is why it's one list.)

## 8. Thumbnails and graphics

Thumbnails are designed per episode in the same type system as the episode's boards
(one system per episode: designed results board, score bugs, player strips, cards —
see PRODUCTION.md §6) and ship as part of the upload package. Graphics are always
built from the episode's data manifest, never hand-typed numbers.

## 9. Repo conventions

- **Video masters and upload encodes never go in git** — gigabytes; they live in
  the workspace and Google Drive. This repo holds the assets that *make* the videos
  plus the docs and skills that describe how. (Root README states the rule.)
- **`.blend` / `.fbx` / `.glb` are Git LFS-tracked** (see the root `.gitattributes`)
  for when the Blender build starts.
- `final/` folders hold frozen, approved copies; working renders sit beside them;
  superseded versions go in `archive/`, including the generation-log JSONs
  (`archive/generation-logs/`) so any render can be traced to how it was made.
- When a design locks, update its spec in the same pass — a render and its spec
  must never silently disagree (the spec wins, §3, so a stale spec is a bug).
- The skill packages in the repo-root `skills/` folder (where this doc lives) are
  re-synced from Muse's canonical working skills when production rules change;
  each package is the full working skill — SKILL.md + skill.yaml — not a summary.
