# RIG DESIGN — GOAT Hoopers Blender Cast

Step 1 of the step-by-step design pass (Aidan, 2026-11-10: design first, step by step,
before any building). Companion to `BLENDER-DESIGN.md` (the model spec — proportions,
identity locks, palette). The STYLE LOCK from that file governs everything here: the rig
serves the locked models, it never restyles them.

## 1. One base armature for the whole cast

A single humanoid armature (~42 bones) shared by all nine humans, so every pose and action
is built once and works on everyone:

- **Root/COG** → hips → spine → chest → neck → head.
- **Arms:** clavicle → upper arm → forearm → hand, IK with pole targets + FK switch.
- **Legs:** thigh → shin → foot → toe, IK, foot-roll control (heel/toe/ball), knee poles.
- **Hands:** stylized 4-digit (thumb + 3 fingers), one curl control per finger + a hand
  pose library (open, fist, point, grip-can, grip-stick, phone).
- **Head extras:** jaw bone, eye look-at target, brow controls.
- Stretchy-limb toggle (cartoon squash) on arms/legs, off by default.

Muse is the exception: no armature deformation of the crystal mass. His "rig" is a control
rig — root with hover offset + bob, squash-and-stretch scale on the body mass, and drivers
for eyes / smile curve / blush (see §4).

## 2. Variant system — one rig, ten bodies

Per-character presets scale the base rig to the BLENDER-DESIGN proportions instead of
building ten skeletons:

| Character | Height | Preset | Rig-level deltas |
|---|---|---|---|
| Hiram | 178 | BROAD | arms ×1.25, hands ×1.1 |
| Kearns | 175 | STANDARD | — |
| Lord Lax | 174 | STANDARD | gear meshes rigid on bones (no cloth sim) |
| Aidan | 173 | STANDARD | head ×1.02 (glasses sit on head bone) |
| Tyrese | 173 | LEAN | — (model corrected to the shared system at build) |
| Phil | 171 | STANDARD | capybara = separate mini-rig (§5) |
| Vann | 170 | STANDARD | hair mass rigid on head bone |
| Tommy | 166 | STOCKY | torso width ×1.08 (post-slimming canon) |
| Griffin | 162 | STOCKY | torso width ×1.08, shortest human |
| Muse | 150 | CUSTOM | control rig only (§4) |

Chef Hiram is a preset on Hiram: torso/arm scale up (arms ×1.5 vs base), outfit swap,
same face rig. No new skeleton.

## 3. Face rig — where the acting lives

Sitcom acting is faces, so the face system is uniform across the cast:

- **Eyes:** blink by lid scale; look-at target per character; half-lid and wide variants
  as shape keys.
- **Brows:** independent L/R brow controls (raise/lower/angle) — Kearns' volcano set and
  Vann's deadpan depend on these.
- **Mouths:** shape-key set per character built from their spec defaults (Hiram's teeth
  grin, Vann's asymmetric smirk, Kearns' grin + shout shapes, Griffin's small sad smile)
  + shared phoneme-ish set (open, wide, O, closed-flat) for dialogue.
- **Dialogue workflow:** lines are TTS audio first (VOICES.md, one voice per character);
  mouth shapes are keyed to the audio by hand on the hero lines and cycled on coverage.

## 4. Muse's control rig

- Root control: hover height (default ~8 cm), idle bob (±1.5 cm, 4 s), tilt-into-motion.
- Face = the frosted plate: eye shape keys (dot → happy arc → wide → skeptical angle),
  smile curve control, blush intensity slider. No mouth interior, no jaw.
- Body: squash-and-stretch on the crystal mass + the small arms as simple 2-bone chains;
  feet dangle in hover, plant in his rare standing poses.

## 5. Props and attachments

- **Bone-parented, always-on identity props:** Kearns' medal + cap, Aidan's glasses
  (modeled on the head, never removed), Tommy's gold can (right-hand grip pose + a
  free-prop version for table shots), Phil's backwards cap, Lax's helmet/cage/stick
  (rigid; the cage never opens and there is no head under it).
- **The capybara** gets its own tiny quadruped rig (body, head, 4 legs, ear twitch) —
  Phil's scenes are incomplete without it.
- Prop hand-offs (can, phone, remote, the comically large wrench) use a shared
  prop-parent constraint so any hand can hold any prop.

## 6. Pose/action library (designed with the rig, built right after)

Per-character idles (Phil unbothered slouch, Kearns coiled, Griffin slump, Chef Hiram
arms-crossed default), walk cycle on the base rig, couch-sit set (the clubhouse couch is
the home set — sits must work at couch height for every preset), point/shout/facepalm
standards, and the **whisper-gag staging**: Lax turns to Vann, head tilt + lean-in (no
audio, no mouth — there is no face), Vann's reluctant-translator reaction set.

## 7. Files and naming

- Library file: `characters.blend` (one collection per character, linkable into scene
  files); actions in `actions.blend`; everything under the repo at
  `goat-hoopers/blender-project/` in **aidan-video-assets** (Git LFS already configured
  for `.blend`).
- Naming: `CH_<name>_rig`, `CH_<name>_mesh`, `ACT_<character>_<action>`.

## 8. "Rig ready" = acceptance test

Each character passes a one-page pose sheet render — neutral, arms crossed, point, sit,
shout/laugh, walk frame — checked against the canon renders for identity and style.
No character enters a scene until their sheet passes. Chef Hiram and the capybara get
sheets too.
