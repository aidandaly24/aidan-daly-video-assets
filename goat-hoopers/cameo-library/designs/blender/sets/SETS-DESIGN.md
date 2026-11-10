# SETS DESIGN — GOAT Hoopers Blender Sets

Step 2 of the step-by-step design pass (Aidan, 2026-11-10: design first, step by step,
before any building). Companion to `../BLENDER-DESIGN.md` (cast model spec + palette)
and `../RIG-DESIGN.md` (Step 1 — the rigs these sets must fit). The STYLE LOCK from
BLENDER-DESIGN.md governs everything here: the set is the cast's world — smooth stylized
3D, clean surfaces, flat bold colors, warm light. No photoreal rooms, no readable text
or logos on anything, ever.

Status: DESIGN PACKAGE for Aidan's review. Nothing is built yet. Set #1 of the reusable
set library (BLENDER-DESIGN.md §4.4): **The Clubhouse**.

---

## 1. Sheets in this folder

| File | What it shows |
|---|---|
| `clubhouse-plan.png` | Top-down floor plan (deterministic diagram): furniture blocks labeled, the four standard cameras marked, Chef mark, scale bar |
| `clubhouse-wide.png` | Establishing wide — the master-camera read of the whole room |
| `clubhouse-couch.png` | Couch angle: from the TV wall back at the couch (faces side) — banner plane + pennant on the wall behind the couch |
| `clubhouse-tv.png` | TV reverse: over the couch backs toward the TV wall — the screen as story device |
| `clubhouse-kitchen.png` | Doorway reveal angle: the lit kitchen doorway framed as a stage entrance from the living room |

All four renders are EMPTY (no characters — sets are reviewed as sets) and were generated
in the cast's render world: warm grey walls, league navy/red accents, soft warm key.

## 2. Room dimensions & construction

- **Room: 720 W × 540 D × 300 H** (cm, scene units — the cast's heights in
  BLENDER-DESIGN.md §1.6 are in the same units; Hiram at 178 must clear the 240 doorway
  header with the drama intact, and does).
- North wall = TV wall. South wall = camera wall. East wall = kitchen wall.
  West wall = window wall.
- **Modular construction (build note):** the south wall and the ceiling are WILD
  (separate, removable modules) — the master camera lives where the south wall would be.
  The east wall is two modules split at the pass-through so CAM D can also shoot from
  inside the kitchen stub. Every other wall is fixed; all dressing is parented to its
  wall module so a wall can fly with its art still on it.
- **Kitchen stub:** a shallow partial room behind the east wall, 185 deep × 440 long —
  just cabinets, counter, stove and hanging pans (as in `clubhouse-kitchen.png`). It
  exists to be seen THROUGH the doorway/pass-through, never as a full set — Chef Hiram's
  scenes play in the doorway itself, not in a modeled kitchen.
- Floor: one plane, warm wood planks (flat color bands, no photo texture).

## 3. Furniture & dressing (sizes in cm)

| Piece | Size (W×D×H) | Placement (plan) | Notes |
|---|---|---|---|
| **Couch** | 320 × 105 × 95 back | Center-south, facing the TV | See §4 — the hero piece |
| Coffee table | 130 × 70 × 38 | Center, 75 in front of couch | Dark wood; snack-clutter stage |
| Media console | 300 × 45 × 42 | North wall, under TV | The giant wrench lives here (§7) |
| TV | screen plane 190 × 108 | North wall, center at 135 high | Separate content plane — §6 |
| Armchair | 95 × 95 × 95 | West end, angled ~25° to TV | Phil's chair; seat plane also 45 |
| Capybara bed | Ø 70 × 12 | Beside the armchair | The capybara's spot — it is furniture until it isn't |
| Floor lamp | Ø 35 shade, 165 H | NW corner, behind armchair | Practical light source (evening state) |
| Rug | 420 × 270 | Under couch/table zone | Cream #F5F2EC, navy border |
| Trophy shelf | 130 × 25, 3 shelves | North wall, west of TV | 5 simple gold trophy shapes, no engraving |
| Pennant ×2 | 70 × 28 triangle | North wall east of TV; south wall | Blank navy/red — shapes only, NO letters |
| Banner plane | 210 × 62 framed | South wall, centered over couch | Blank cream plane — the show textures it per episode (standings, "GAME OF THE WEEK", etc.) |
| Blank frame | 90 × 62 framed | South wall, east of banner | Second texture-later plane (poster slot) |
| Window | 160 × 140, sill at 80 | West wall | Blinds; the daytime light source |
| Kitchen doorway | 130 W × 240 H opening | East wall, north section | Chef Hiram's proscenium — §5 |
| Pass-through | 140 W × 90 H, sill at 105 | East wall, south of doorway | Kitchen counter hatch; second, sneakier Chef frame |

## 4. THE COUCH — spec and the seat-height decision

The couch is the home base of the whole show: the couch gag, the arguments, the
whisper, the slumps all happen here. It is built to the RIG, not to a furniture catalog.

- **4 seats**, cushion width ~73 each — four humans across at sitcom density, with the
  armchair (Phil), the floor, and Muse's hover spot covering the rest of the ensemble.
  Couch-gag staging: seats are numbered 1–4 west→east; who sits where is a per-episode
  joke the pose library supports, not a fixed assignment.
- **Seat height — DECISION: seat plane at 45 cm (loaded).** Cushions model at 47
  uncompressed and compress to the 45 seat plane under a seated character. Rationale:
  the rig sheets (RIG-DESIGN.md §9) blocked every character's sit on a plain block at
  this height — thigh horizontal, shin vertical, feet planted — and 45 is what makes
  the SHORTEST preset (Griffin, 162, STOCKY) and the TALLEST (Hiram, 178, BROAD) both
  read correctly on the same seat: Griffin's feet still plant, Hiram's knees don't
  spike. One seat plane for the whole cast is the point of the shared rig; the couch
  obeys it.
- Seat depth 62; back height 95 (backs read just below seated shoulder line — faces
  never hide behind the couch back in CAM B); arm height 68, arm width 22 (arms are
  poseable-against: lean, drape, Kearns gripping the armrest mid-volcano).
- Color: league navy #1F2A44 upholstery, two red #C1272D throw cushions at the ends.
  Flat colors, cast material system (roughness 0.9, no fabric texture).

## 5. Camera plan — the three-camera sitcom + one gag cam

Sitcom grammar is the staging logic: scenes are blocked for these four cameras and no
others until Step 3 proves a need.

| Cam | Position (plan) | Lens feel | What it's for |
|---|---|---|---|
| **CAM A — MASTER** | South-center, through the wild wall, eye ~170 | Wide (~24 mm equiv) | The establishing wide + couch-gag lineup; every scene opens or returns here |
| **CAM B — COUCH CAM** | North side, beside the TV, eye ~150 | Medium (~35 mm equiv) | Couch two-shots and singles — faces, arguments, the whisper gag's Vann side; banner plane lives in this frame |
| **CAM C — TV REVERSE** | Just behind/above the couch back, eye ~140 | Medium-wide | Over-the-couch toward the screen: reveals, reactions TO the TV (frozen app, breaking news); heads/shoulders silhouette in lower frame |
| **CAM D — DOORWAY REVEAL** | SW of the room, aimed NE at the kitchen doorway | Medium | Chef Hiram's entrance: he fills the 130×240 doorway with light behind him; also any entrance beat through the pass-through |

Blocking rules that follow: the couch never moves; the coffee table gap (75) is the
crossing lane; the doorway sightline from CAM D must stay clear of the armchair; the
whisper gag plays on the couch's east end (nearest CAM D side) so Lax's lean and Vann's
delivery both read in CAM B without a reset.

## 6. The TV is a story device, not a prop

- The screen is a **separate plane** (`SET_clubhouse_TVscreen`) with its own material
  slot, built to take an image / image-sequence texture at scene time. The set itself
  ships with the screen DARK (as in the sheets) — nothing is ever modeled or baked
  into the screen.
- Content plates are made in the edit, per scene: the frozen Sleeper app (Week 4
  bricking), game broadcasts, breaking-news dressing. Same discipline as the banner
  plane: geometry blank, content swappable.
- A low-intensity area light in front of the screen (the "TV glow") is part of the
  lighting rig and takes the plate's average color, so a frozen blue app and a red
  breaking-news plate light the couch differently. Off in the daytime state.

## 7. Props

Hero props (modeled, reusable, named):
- **The comically large wrench** — stored leaning inside the media console's open
  center bay, visible in CAM C. Muse's "fixing the app" prop (Freeze Night). Oversized
  (~55 long), held via the shared prop-parent system (RIG-DESIGN.md §5).
- **TV remote** — lives on the coffee table; the most fought-over object in the league.
- **Snack set** — 3 bowls (popcorn / pretzels / chips), 4–6 blank cans. Cans are
  UNBRANDED silver or the cast gold #E3A81E (Tommy's can is a character prop; table cans
  are dressing — don't mix them up in close-ups).
- **Game controllers** ×2, plain shapes, on the console.
- **Chef's ladle + toque hook** — a hook on the kitchen side of the doorway; the ladle
  hangs there when Chef Hiram is not holding it. His silhouette check happens against
  the doorway light, not against clutter.

Dressing rules: nothing with readable text or a logo exists on this set (the ONLY
exception in the entire build remains Lax's "65", and he brings it with him). Trophy
shapes are smooth and unengraved. Books are blank-spined color blocks.

## 8. Lighting states

One set, three states — state changes are lighting/prop swaps only, never geometry.

1. **Game-night evening (DEFAULT):** the cast design rig warmed down — key warm
   #FFE3C2 low from the window side, practicals ON (floor lamp + kitchen spill are
   the motivated sources), fill cool #BFD4E6 at 30%, TV glow on. This is the look of
   all four sheets.
2. **Daytime:** window key cool daylight (pale #DCE9F5 family), blinds half-open,
   practicals off, TV glow off, overall exposure up ~1 stop. Morning-after scenes,
   lineup-locking brunches.
3. **Breaking-news (DRAMATIC):** evening base dimmed ~40%, practicals off, TV glow
   becomes the key — red/blue plate colors (#C8102E / #1D3FAE family) washing the
   couch from CAM C's side, kitchen doorway rim #FFC98A for entrances. Reserved for
   news-desk bits and the bricking-incident retellings; if everything is dramatic,
   nothing is.

## 9. Palette (harmonized to BLENDER-DESIGN.md §1.5)

| Element | Hex | Source |
|---|---|---|
| Walls | warm grey family of #8A8378 (studio grey, warmed one step for a lived-in room) | §1.5 |
| Floor | warm wood, #8A5A2B family bands | §1.5 belt brown |
| Couch | #1F2A44 (cast navy) | §1.5 |
| Throw cushions | #C1272D (Phil red, used as the room's red) | §1.5 |
| Rug | #F5F2EC (cast white) + #1F2A44 border | §1.5 |
| Armchair | #C9B18A (khaki) | §1.5 |
| Wood furniture | #8A5A2B / #5E4128 (capybara dark) range | §1.5 |
| Trophy gold | #E3A81E | §1.5 |
| Pennant | #1F2A44 + #C1272D | §1.5 |
| Accents (consoles, TV bezel) | #17181C (cast black) | §1.5 |

League blue/red echo the recap graphics deliberately — the room is dressed like the
show's own lower-thirds.

## 10. What Step 3 still owes this set

- Validate every rig preset's sit against the 45 seat plane ON the couch (not the
  design block): cushion compression, armrest interactions, Griffin's feet, Hiram's
  knees, Lax seated in gear, Muse's hover spot at the couch's east end.
- Couch-gag lineup spacing: tape marks for seats 1–4 + armchair + floor spots for a
  full-cast master (CAM A).
- Walk paths: door→couch lane, kitchen doorway→couch lane (Chef's route), armchair→TV
  lane — all at the shared walk cycle's stride.
- The whisper-gag two-shot blocked on the couch east end for CAM B (Lax lean-in,
  Vann delivery) with CAM D sightline as the alt angle.
- TV-plate timing: how a content plate change (frozen app → news) is keyed against
  the TV-glow light color in a scene.

---

*Review flow: Aidan reviews the sheets + this spec; tweaks land here before any Blender
building starts. Next set candidates after approval (Step 2 continues only if asked):
the League Desk / news set, courtside.*
