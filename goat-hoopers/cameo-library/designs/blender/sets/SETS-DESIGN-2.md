# SETS DESIGN 2 — GOAT Hoopers Blender Sets (Step 2b)

Companion to `SETS-DESIGN.md` (Step 2 — the Clubhouse, APPROVED by Aidan 2026-11-10).
Aidan's direction: "we're going to need even more." Four more sets, designed in the
Clubhouse's exact visual world — smooth-shaded 3D animated-sitcom look, navy
#1F2A44 / red #C1272D / warm-wood #8A5A2B palette, warm practical light, hexes from
`../BLENDER-DESIGN.md` §1.5. Same rules as the Clubhouse: every set EMPTY, and nothing
with readable text, letters, numbers or logos exists on any set — every screen, banner
and board is a blank plane whose content is textured in production.

Status: DESIGN PACKAGE for Aidan's review. Nothing is built yet. Sets #2–#5 of the
reusable set library (BLENDER-DESIGN.md §4.4).

**The seat standard carries over:** wherever a character sits, the seat plane is
**45 cm loaded** (47 modeled) — the height the rig sheets blocked every sit at. One
seat plane for the whole cast, on every set.

**Cross-sheet drift rule (applies to all four sets):** the renders are design sheets,
not geometry. Where two sheets of the same set disagree (chair upholstery color,
room mirroring), the WIDE sheet + this spec are the contract; Step 3 validates on the
built set. Known instances are called out per set below.

---

## 1. Sheets in this folder

| File | Set | What it shows |
|---|---|---|
| `arena-plan.png` | Arena | Top-down plan: court, keys, bleachers, cameras |
| `arena-wide.png` | Arena | Center-court wide down the court — the versus-intro master |
| `arena-hoop.png` | Arena | Low corner angle at the hoop: key, clear backboard, blank scoreboard plane |
| `arena-bleachers.png` | Arena | Behind-the-bleachers reverse: seat rows, ball rack, far hoop |
| `warroom-plan.png` | War Room | Top-down plan: table, board wall, blinds wall, cameras |
| `warroom-wide.png` | War Room | Master wide: long table, blank board, blind-stripes, trophy shelf |
| `warroom-board.png` | War Room | Down-table angle at the board wall |
| `warroom-blinds.png` | War Room | Blinds angle: light striping the table end, phone + mug |
| `newsdesk-plan.png` | News Desk | Top-down plan: desk, backdrop plane, truss, studio cams |
| `newsdesk-wide.png` | News Desk | Straight-on master: curved desk, blank red/navy backdrop screen |
| `newsdesk-desk.png` | News Desk | Closer three-quarter on the desk: mic, mug, blank front panel |
| `newsdesk-reverse.png` | News Desk | Behind-the-desk reverse: anchor chair backs, pedestal camera, blank monitor |
| `commish-plan.png` | Commish | Top-down plan: desk axis, board, long trophy shelf, cameras |
| `commish-wide.png` | Commish | Master wide: exec desk, crystal desk piece, trophy cabinet, blank board |
| `commish-desk.png` | Commish | Reverse over the desk chair: crystal foreground, guest chairs |
| `commish-board.png` | Commish | Side angle: long trophy shelf with crystal among the trophies, blank board |

---

## 2. THE ARENA — streetball court (versus intros, game bits)

The show's second home: versus fight-scene intros play here before each game segment,
and any on-court business (warmups, one-on-one boasts, Lax in full gear on an empty
court) stages on the center circle.

- **Hall: 1500 W × 1100 D × 600 H.** Court 1200 × 800 centered, 150 run-off on all
  sides. North = far hoop (up on the plan).
- **Court floor:** warm honey wood planks (#8A5A2B family, lighter stain than the
  clubhouse floor), painted markings as flat color shapes only — boundary, center
  line, center circle r180, keys 490 × 580 at both ends, 3-point arcs. Paint colors:
  cast white #F5F2EC lines, navy #1F2A44 + red #C1272D key/center fills (as in
  `arena-wide.png`). Markings are stylized-simplified vs a regulation court — that is
  deliberate: shapes read at sitcom distance, and no marking ever carries text.
- **Hoops ×2:** ceiling/wall-mounted at both ends, rim at 305, clear backboard
  180 × 105 with white border + inner square (shapes only), red #C1272D rim, white
  net. The far hoop is the wide shot's vanishing point; the near hoop stays out of
  CAM A's frame top.
- **Bleachers:** both sidelines, 4 rows, 1000 long, seat plane 45 (the standard) —
  bench planks on the north side (navy), molded seats on the south (navy/red mix) is
  sheet drift; **spec: bench planks both sides**, alternating navy/red plank color
  per row. Nobody in the cast sits here mid-scene except crowd-gag cut-ins, and 45
  keeps those legal.
- **Banner planes:** 3 overhead at center court (navy / cream / navy, 220 × 110
  hanging at 420) + swallowtail banners on the end walls (as in
  `arena-bleachers.png`). All blank — versus cards and matchup art are textured in
  production, same discipline as the clubhouse banner plane.
- **Scoreboard plane:** one dark blank plane 240 × 130 high on each side wall
  (visible in `arena-hoop.png`) — a content plane like the clubhouse TV; ships dark.
- **Props:** ball rack (SW corner) with 8 plain orange basketballs — unmarked, no
  brand pebbling logos; a loose ball at center court is the versus-intro hero prop.
- **Cameras:**
  - **CAM A — CENTER COURT (VERSUS):** south sideline at center court, eye ~160,
    wide. The versus master: both players enter from opposite ends and meet on the
    center circle; `arena-wide.png` is this camera.
  - **CAM B — HOOP CAM:** NE corner, low (~90), looking up at the east hoop — dunk/
    boast angles, Lax gear silhouette against the backboard.
  - **CAM C — BLEACHER REVERSE:** behind the north bleachers looking SE across the
    court — entrances from the bleacher side, "empty arena" melancholy beats.
- **Lighting:** brighter and cooler than the clubhouse (game light): warm-white
  ceiling pendants as motivated sources, key #FFE3C2 family at higher exposure,
  bleachers fall off a stop darker so the court glows. Evening state only — the
  arena is never shot "daytime."

## 3. THE WAR ROOM — trade negotiations

Where trades get made and unmade: two managers across a long table, phones, folders,
and a board everyone gestures at and nobody is allowed to read (it's blank).

- **Room: 640 W × 460 D × 300 H.** Board wall = east, windows/blinds = west.
- **Table:** 360 × 130, top at 74, dark warm wood #5E4128–#8A5A2B range, center of
  room. The table is the set's couch: it never moves, and negotiations are blocked
  across its width (CAM A side) or down its length (CAM C side).
- **Chairs ×8:** 3 per long side + 1 at each head; seat plane 45 loaded, navy
  #1F2A44 upholstery. (Sheet drift: `warroom-board.png` / `warroom-blinds.png` render
  the chairs cream — the wide's navy is the contract.)
- **Board plane:** 280 × 150, cream #F5F2EC in a wood frame, center of the east wall
  at 165 high. Blank geometry; trade trees, tier lists and increasingly unhinged
  diagrams are textured per scene in production.
- **Blinds wall:** two tall windows (110 × 190) with venetian blinds on the west
  wall — the set's signature light: one warm late-afternoon state, stripes across
  the table. This is the ONLY lighting state; the war room is always 6:47 PM.
- **Walls:** warm grey #8A8378 family above, navy #1F2A44 wainscot to 110 — the
  office-grammar the War Room shares with the Commissioner's Office (they're
  adjoining rooms in the fiction; the trophy shelf below is the same shelf design).
- **Trophy shelf:** small 2-tier wood shelf, north wall — 4 simple gold #E3A81E
  trophy shapes, unengraved. A deliberate echo of the clubhouse shelf: same league,
  smaller egos (allegedly).
- **Props:** 2 chunky desk phones (cast black #17181C — one per side, the hotline
  gag), blank manila folders ×6, plain mugs ×4, one blank notepad per seat. Phone
  dials are button-dot shapes only — no numerals modeled.
- **Cameras:**
  - **CAM A — MASTER:** SE corner, eye ~150 — table diagonal, board behind the far
    head chair (`warroom-wide.png`).
  - **CAM B — BLINDS ANGLE:** NW corner low — silhouettes against the blinds,
    confessionals and lie-detector lighting.
  - **CAM C — DOWN-TABLE / BOARD:** NE corner down the table's length at the board —
    the "presenting the offer" angle; presenter stands at the board, table
    foreshortened below.

## 4. BREAKING-NEWS DESK — votes & drama studio

The show-within-the-show: polls, votes, rulings and drama get announced from behind
this desk. (The clubhouse's breaking-news LIGHTING state stays for clubhouse scenes;
this is the full studio those bits graduate to.)

- **Studio: 900 W × 620 D × 420 H** — a stage box, not a room: north wall is the
  backdrop, east/west walls are flats, south side is wild (cameras live there).
- **Anchor desk:** curved, 380 wide × 110 deep, top at 76; warm wood + navy
  #1F2A44 body with a **blank cream front panel 240 × 55** — the desk's banner
  plane, textured per segment in production (never modeled with a logo). Desk is
  fixed at center, 260 off the backdrop.
- **Anchor chairs ×2:** behind the desk, seat plane 45, navy. (Sheet drift:
  `newsdesk-desk.png` renders one cream — navy is the contract.) Two chairs because
  the desk is a two-shot machine: Muse + a rotating second anchor.
- **Backdrop screen plane:** 620 × 260 on the north wall, a separate content plane
  like the clubhouse TV — ships showing the plain red #C8102E → navy #1D3FAE block
  gradient from `newsdesk-wide.png`; headlines, polls and BRICKED graphics are
  textured in per segment. A matching glow light takes the plate's average color.
- **Side screen plane:** 140 × 90 on the east flat — the "graphic over the shoulder"
  slot; ships dark navy.
- **Studio furniture (dressing, non-hero):** 3 pedestal studio cameras (cast black,
  lens boxes blank), lighting truss across the ceiling line with 6 warm practical
  heads (visible in frame tops on the wide — that's the look), equipment racks on
  the west flat with button-dot shapes only.
- **Floor:** dark glossy studio floor (#17181C family, roughness low) — the one
  non-wood floor in the library; reflections sell "studio."
- **Cameras:**
  - **CAM A — MASTER:** straight on the desk from the south, eye ~150
    (`newsdesk-wide.png`). Every segment opens here.
  - **CAM B — DESK ANGLE:** SE three-quarter, closer — the two-shot and the
    lean-in (`newsdesk-desk.png`).
  - **CAM C — REVERSE:** behind the desk looking south across the chair backs at
    the pedestal cameras + blank monitor wall (`newsdesk-reverse.png`) — the
    "media circus" reveal and Muse-addresses-the-cameras bits.
- **Lighting:** studio state only: warm key from the truss, backdrop glow as fill,
  floor reflections on. No daytime variant — it's a windowless box.

## 5. COMMISSIONER'S OFFICE — Muse's HQ

Rulings, summonses, and the lock-desk paperwork happen here. Muse presides; the
crystal motif is the room's signature — one desk piece, one shelf piece, never more
(it's an office, not a shrine).

- **Room: 560 W × 460 D × 300 H.** Board wall = north, trophy shelf = west,
  window = east. Shares the War Room's office grammar (warm grey #8A8378 above navy
  #1F2A44 wainscot to 110) — the two rooms are one fictional suite.
- **Exec desk:** 220 × 95, top at 76, dark warm wood, centered on the north–south
  axis facing the door. Muse's hover spot is behind it (the desk chair is
  furniture; Muse presides hovering at chair height, chair pushed in — the chair
  is a joke about the office, not a seat Muse needs).
- **Desk chair:** high-back, navy #1F2A44, seat plane 45 (a summoned manager who
  gets waved into it sits legally). **Guest chairs ×2:** cream/khaki #C9B18A
  armchairs in front of the desk, seat plane 45 — the hot seats; they're the
  clubhouse armchair's office cousins.
- **The crystal desk piece:** translucent light-blue faceted crystal ~28 high on
  the desk's east corner — Muse crystal #7FC8F8 / deep facet #2E6FB7 / core
  #37E0D8, with a low cyan practical glow onto the desktop. Same piece appears on
  the trophy shelf (`commish-board.png`) — one hero prop, two approved spots,
  never both in the same scene.
- **League board plane:** 260 × 140, cream in wood frame, north wall behind the
  desk at 175 high. Blank — standings, rulings and THE LIST are textured in
  production.
- **Trophy shelf (long):** west wall, 300 long × 2 bays, 8 simple gold #E3A81E
  trophy shapes, unengraved — the clubhouse shelf's bigger sibling.
- **Rug:** 300 × 240, cream #F5F2EC + navy border — same rug as the clubhouse,
  deliberate echo.
- **Brass floor lamp** (NE corner, the clubhouse lamp's twin) + window with blinds
  (east) = the two motivated sources; the crystal glow is the third.
- **Door:** south wall, east end — summonings enter here; the doorway in the sheets
  shows a kitchen beyond (generator borrowing the clubhouse stub) — **spec: a plain
  warm-lit hallway stub**, not a kitchen. Chef Hiram does not have an office
  entrance.
- **Cameras:**
  - **CAM A — MASTER:** south-center through the door side, eye ~160 — desk axis,
    board + crystal in frame (`commish-wide.png`). Rulings open here.
  - **CAM B — DESK REVERSE:** over the desk chair's shoulder, crystal foreground,
    guest chairs facing camera (`commish-desk.png`) — the summoned manager's POV
    and Muse's pronouncements to camera.
  - **CAM C — BOARD / SHELF:** SW corner across the shelf + board wall — the
    "trophy testimony" angle, and where the shelf crystal lives.
- **Lighting:** clubhouse evening state, one notch more formal: lamp key warm
  #FFE3C2, window fill cool, crystal glow always on (it's a practical, not an
  effect state).

---

## 6. What Step 3 still owes these sets

- Arena: versus-intro blocking on the center circle for CAM A (entrances from both
  ends at walk-cycle stride), hoop-cam sightlines with Lax's helmet in frame, and
  the banner planes' texture templates sized (220 × 110).
- War Room: the across-table two-shot (both seat rows legal at 45 with the 74 top —
  forearms-on-table pose), presenter-at-board blocking for CAM C, phone-prop hand
  poses.
- News Desk: anchor two-shot spacing at the desk (Muse hover + seated anchor),
  front-panel texture template (240 × 55), backdrop plate timing vs glow light —
  same open question as the clubhouse TV.
- Commish: Muse's hover spot behind the desk vs the chair (chair in/out variants),
  the summoned-manager entrance path door→guest chair, crystal glow intensity
  against the lamp key.
- All four: verify against the built Clubhouse first — the shared wall/floor/wood
  materials must be the same assets, not re-creations.

---

*Review flow: Aidan reviews the sheets + this spec; tweaks land here before any
Blender building starts. Set library after Step 2b: Clubhouse, Arena, War Room,
Breaking-News Desk, Commissioner's Office.*
