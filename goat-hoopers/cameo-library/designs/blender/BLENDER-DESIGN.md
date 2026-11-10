# BLENDER CAST DESIGN — GOAT Hoopers, 3D Animated-Sitcom Style

Status: DESIGN PACKAGE for Aidan's review (2026-11-10). No models have been built yet — nothing in this
document is final until Aidan approves the concept renders.
Supersedes: the photoreal/cinematic look in `../STYLE.md` and `../renders/` for all GENERATED SCENES.
Identity (faces, hair, signature outfits, props) carries over from `../<person>.md` and the reference
photos — only the rendering style changes. Versus intros and footage edits are untouched by this doc.

Concept renders in this folder: `muse.png`, `aidan.png`, `kearns.png`, `phil.png`, `vann.png`,
`griffin.png`, `tyrese.png`, `hiram.png`, `lord-lax.png`, `tommy.png`, `cast-lineup.png`.
All ten renders exist (earlier versions kept in `v1/` and `v2/`). Aidan reviewed the cast
2026-11-10 ("fucking great") with fixes, all applied in the current renders + spec: Vann's hair
tighter (§3.6; final v2 render accepted as-is), Tommy and Griffin slimmed twice, STOCKY ×1.22 →
×1.08 (§1.2, §3.5, §3.7), and Muse's render + spec replaced with his true avatar design (§3.1).

---

## 1. GLOBAL STYLE RULES

### 1.1 The one-sentence brief
Prime-time animated-sitcom character design (Family Guy / Bob's Burgers readability) realized as 3D
models with soft cinematic lighting: chunky proportions, bold simple shapes, simple expressive faces,
flat bold outfit colors — the same character, pixel-stable, in every shot of every video.

### 1.2 Proportions (the shared body system — build ONE base rig, scale it)
- Total height = **3.5 heads** for the standard body (head unit = head height incl. hair mass).
- Head width ≈ 0.82 × head height; head is a rounded box/sphere hybrid, wider at the cheeks.
- Neck: short, 0.12 head units — heads sit close to shoulders.
- Torso: one tapered rounded mass, shoulder width ≈ 1.05 head widths. No anatomical pecs/abs.
- Arms: upper+forearm as two tapered capsules; total arm length ≈ 1.15 head units; hands are
  mitten-plus — four fingers + thumb, fingers short and merged at the base, no knuckle detail.
- Legs: two tapered capsules, total leg length ≈ 1.25 head units; feet oversized (≈0.42 head units
  long), simple shoe masses.
- Build variants (scale the base rig, never remodel):
  - **STOCKY** (Tommy, Griffin): height × 0.96, torso width × 1.08, head × 1.03. (Slimmed twice at Aidan's direction, 2026-11-10: × 1.22 → × 1.13 → × 1.08 — "a lil skinnier, just slightly"; solid and stocky, NOT chubby, NOT thin.)
  - **BROAD** (Hiram): height × 1.06, torso width × 1.30, arms × 1.25 thickness.
  - **LEAN** (Phil, Tyrese): height × 1.03, torso width × 0.88, legs × 1.08 length.
  - **STANDARD** (Aidan, Kearns, Vann, Lord Lax): base rig as-is.
- Muse is the exception: no legs planted — stub crystal legs, hovers ~8 cm off the floor (see §3.1).

### 1.3 Face construction (identity without photorealism)
- Eyes: two large vertical ovals, white sclera, dark iris disc ≈ 45% of eye height, one white
  highlight dot upper-left. Eyes sit on the head's horizontal midline, spaced ≈ 0.9 eye-widths apart.
  Eye color = the person's real eye color, simplified to one flat tone (see per-character notes).
- Brows: single tapered capsule shapes above the eyes; brow thickness is an identity dial
  (Hiram/Tyrese heavy, Aidan medium, Griffin light).
- Nose: one small rounded wedge, no nostrils, no bridge shading.
- Mouth: a single curved line (smile / flat / smirk per character's default in §3); a simple dark
  interior + white teeth bar for open/grin variants. No lip geometry, no lip color.
- Ears: simple C-shells at eye level. No inner-ear detail.
- Skin: ONE flat base color per character + a soft blush disc on each cheek at 12% opacity baked
  into the material (not texture). No pores, no stubble texture — facial hair is GEOMETRY (a smooth
  sculpted mass in a flat color), never alpha hair or speckle.
- Hair: sculpted solid masses made of 5–12 big interlocking rounded clumps. No strands, no cards,
  no fur shells. Each character's clump layout is part of their locked model (§3).
- Identity is carried by, in priority order: (1) silhouette, (2) hair mass shape, (3) signature
  outfit + prop, (4) face proportions (face width, eye spacing, brow weight), (5) skin/hair colors.
  If a render still reads as the person with the face blurred, the model is right.

### 1.4 Materials & shading
- Everything is a Principled BSDF with: flat base color (the hexes in §2/§3), roughness 0.85–1.0,
  specular 0.25. Skin roughness 0.7. NO subsurface scattering, NO clearcoat except: Muse's crystal
  (§3.1), glasses lenses (transmission 0.9, thickness thin), Kearns' medal + Tyrese's cross
  (metallic 1.0, roughness 0.3), Lax's helmet shell (roughness 0.35).
- Shading model: soft studio HDRI or 3-point rig (key warm #FFE3C2 at 45°, fill cool #BFD4E6 at
  30% intensity, rim warm #FFC98A from behind-side). One lighting rig for the whole cast, saved in
  the master file — scenes may relight for mood but the design-review renders always use this rig.
- Subtle rim: the rim light above is the rim. No fresnel shader tricks, no outline/toon pass —
  the read comes from shapes and color, not edge lines.
- Fabrics are flat color. Patterns allowed ONLY where they are identity: Tyrese's shirt stripes
  (painted as geometry stripes or a simple two-color repeat texture, stripe width locked in §3.8),
  Tommy's jacket color blocking, Lax's jersey number.

### 1.5 Shared palette (hex — use exactly these)
| Swatch | Hex | Used for |
|---|---|---|
| Studio warm grey (design renders) | #8A8378 | concept/lineup backgrounds |
| Skin — fair | #F2C49B | Aidan, Kearns, Phil, Vann, Griffin |
| Skin — fair-pink | #F0BE96 | Tommy |
| Skin — light tan | #E3AC7E | Tyrese |
| Skin — warm brown | #A9713F | Hiram |
| Hair — dark brown | #3A2417 | Aidan, Phil, Tyrese |
| Hair — near-black brown | #241610 | Vann |
| Hair — light brown | #7A4B26 | Griffin |
| Hair/beard — reddish brown | #8A4A26 | Kearns |
| Hair — black-brown | #1C130E | Hiram (buzz + beard) |
| Cast white | #F5F2EC | tees, sneakers, helmet |
| Cast black | #17181C | Kearns kit, caps, shorts |
| Cast navy | #1F2A44 | Vann sweatshirt, Lax jersey base |
| Denim | #2E4A73 | jeans |
| Khaki | #C9B18A | Tommy pants, Tyrese shorts |
| Gold (medal/can) | #E3A81E | Kearns medal, Tommy can |
| Silver | #C9CDD4 | Tyrese cross, medal ribbon hardware |
| Ribbon red / blue | #C8102E / #1D3FAE | Kearns medal ribbon (+ cast white) |
| Phil red | #C1272D | Phil v-neck |
| ND navy / kelly / gold | #1E3050 / #1E9E4F / #C99700 | Tommy jacket |
| Griffin oxford blue | #A8C6E4 | Griffin shirt |
| Stripe blue | #7FB2E0 | Tyrese shirt stripes |
| Lavender | #C5B3E6 | Hiram polo |
| Hiram pant navy / belt brown | #2E4A7A / #8A5A2B | Hiram |
| Helmet white / maroon | #F2F2F0 / #6E1E2B | Lord Lax |
| Capybara brown / dark | #9A6B43 / #5E4128 | Phil's capybara |
| Muse crystal / deep facet / core | #7FC8F8 / #2E6FB7 / #37E0D8 | Muse |

### 1.6 Height chart (relative design heights — stylized, not real-world measurements)
Tallest → shortest. Heights in cm-units of the scene world; eye-line follows §1.2.

| Character | Height | Build |
|---|---|---|
| Hiram | 178 | BROAD |
| Tyrese | 176 | LEAN |
| Lord Lax | 174 | STANDARD (+ gear bulk; helmet crown is the top) |
| Phil | 172 | LEAN |
| Vann | 170 | STANDARD |
| Kearns | 169 | STANDARD |
| Aidan | 168 | STANDARD |
| Tommy | 166 | STOCKY |
| Griffin | 162 | STOCKY |
| Muse | 150 | hovers; eye-line ≈ 162 in scenes |

### 1.7 BAN LIST (hard — any of these in a model or render = reject and redo)
- No photoreal skin: no pores, wrinkles, stubble speckle, SSS, or photo textures.
- No anime: no anime eyes, no hair spikes-as-strands, no cel outline pass.
- No uncanny detail: no individual teeth, no fingernails, no nostrils, no lip geometry.
- No per-scene redesigns: the approved model IS the character. Costume changes only as separate
  approved variants parented to the same rig.
- No brand logos or text on garments in the 3D builds (the concept renders inherit some from the
  reference photos — e.g. Kearns' cap patch and quarter-zip logos, the crest on Lax's jersey).
  Builds use plain garments; the ONLY text/number allowed is Lax's "65". Tommy's jacket gets the
  leprechaun as a simple flat patch shape, no lettering.
- No face for Lord Lax — ever (see §3.10).
- No cap and gown for Griffin — ever (see §3.7).

---

## 2. HOW TO READ §3
Each spec gives: silhouette, proportions tweak, hair construction, outfit (pieces + hex), props,
face notes, and NEVER notes. Hexes not repeated here are in §1.5.

## 3. PER-CHARACTER MODEL SPECS

### 3.1 MUSE — the commissioner (`muse.png`)
- CANON SOURCE: the Muse design Aidan chose — his avatar (picked 2026-10-24; reference saved in
  this folder as `muse-identity-ref.png`). The first concept render + spec (spiky emerald-cut
  golem, glowing oval eyes, no mouth) were invented and WRONG — Aidan, 2026-11-10: "that is not
  what u look like... u need to look like actually u, the design I have for you." The current
  `muse.png` is generated from the avatar and is the canon render.
- Silhouette: a chubby rounded crystal blob — head and body are ONE faceted icy mass, no neck,
  no separate head. Small faceted arms hang at the sides; short faceted legs and feet. The ONLY
  non-human in the cast; reads instantly.
- Proportions: ~2.5 heads; shortest in the cast (150). Stands on his feet, as the avatar does
  (a hover/bob may be an animation choice, never a model change).
- Construction: body = one rounded, irregularly faceted crystal mass, widest at the belly;
  face = a smooth FROSTED WHITE oval plate set into the front of the mass; a few small clear
  crystal nubs scattered on the body (shoulders, chest, belly, hip).
- Material: translucent blue crystal — pale icy blue at the surface, deeper saturated blue in
  the thick facets (#2E6FB7 family), fine frosted sparkle micro-texture; the face plate is
  frosted white and nearly opaque.
- Face: two BLACK round bead eyes (glossy, small white highlight), a tiny curved smile (thin
  dark line), soft PINK BLUSH marks on both cheeks. Expression = eye shape + smile curve +
  blush intensity.
- NEVER: no spikes or crown; no glowing/emissive eyes; he HAS a mouth (the small smile) — never
  remove it; no human skin/hair/clothes; no separate head/neck; never fully opaque.

### 3.2 AIDAN — roster 1, Reaves Dropper (`aidan.png`)
- Silhouette: round-faced, glasses-forward — the glasses are his outline signature.
- Proportions: STANDARD; face width × 1.04 (roundest standard face).
- Hair: dark brown #3A2417, 7 clumps, **CLEAR MIDDLE PART** — clumps split at the center line and
  sweep to both sides, soft waves, length to mid-ear at the sides. This corrects the side-swept
  hair of the old cinematic render; the middle part is LOCKED (Aidan's correction, 2026-11-09/10).
- Outfit: plain white crew-neck tee #F5F2EC; dark indigo jeans #2E4A73; white sneakers #F5F2EC.
- Props: round tortoiseshell glasses — frame #6B4226 with amber mottling simplified to two-tone,
  lens transmission; glasses sit mid-bridge and are part of the head model, never removed.
- Face notes: brown eyes; medium brows; default mouth = small closed almost-smirk (flat-ish,
  corners up 5%). Skin fair #F2C49B.
- Identity CONFIRMED (Aidan, 2026-11-10): the render looks like him. No changes.
- NEVER: no side part / side sweep; no beard; glasses never off; hair never black (it's brown).

### 3.3 KEARNS (Aedan) — roster 2, Ware the Hoes At? (`kearns.png`)
- Silhouette: cap + beard + the medal disc on the chest — three stacked identifiers.
- Proportions: STANDARD; shoulders × 1.05.
- Hair: mostly hidden by cap; side tufts reddish brown #8A4A26 at the ears. Beard = ONE sculpted
  mass, reddish brown #8A4A26, covering jaw + chin, medium-full, with a connected moustache;
  the beard is geometry, smooth, no texture.
- Outfit: black quarter-zip #17181C (collar standing, zip to mid-chest, PLAIN — no logos in the
  build); black pants #17181C; black sneakers with white soles.
- Props: black baseball cap worn FORWARDS, plain (no patch text in build); gold medal — disc
  Ø ≈ 0.28 head widths, gold #E3A81E metallic, on a red/white/blue ribbon
  (#C8102E / #F5F2EC / #1D3FAE) worn over the quarter-zip. Medal is ALWAYS on.
- Face notes: BLUE eyes (Aidan's correction, 2026-11-10); thick reddish brows; default mouth = grin-ready smile. Skin fair #F2C49B.
- Persona on the model sheet: volcano — his expression set leans hot (brows-down variants matter).
- NEVER: cap never backwards or off; medal never off; beard never black or longer than jaw-line;
  no logos/text anywhere on the build.

### 3.4 PHIL — roster 4, The Fun Guys (`phil.png`)
- Silhouette: lean, backwards cap brim poking behind, red torso block, capybara at his ankle.
- Proportions: LEAN; longest neck of the cast (× 1.1 — still short by §1.2).
- Hair: light-medium brown #4A3220 (from §1.5 dark brown family, use #4A3220), short, mostly under
  the cap; a fringe wedge visible under the front strap.
- Outfit: red v-neck tee #C1272D; black shorts #17181C; white crew socks; white sneakers.
- Props: black cap worn BACKWARDS (brim + strap at back, front panel plain in build); black
  sunglasses hanging from the v-neck collar (two dark rounded-rect lenses on a neck loop);
  blue wristband on left wrist #1D6FAE (from the reference photo — small, keep).
- Sidekick: CAPYBARA — a separate reusable mini-character: one rounded barrel body #9A6B43,
  blunt rectangular head #5E4128 muzzle, tiny ears, dot eyes, sits at Phil's feet at 0.45 × Phil's
  leg height. Include in his model sheet; deploy in scenes "when natural" (standing rule).
- Face notes: light blue-grey eyes; default mouth = unbothered half-smile. Skin fair #F2C49B.
- NEVER: cap never forwards; shirt never another color; capybara never realistic-furry (flat
  colors, same material system as the cast).

### 3.5 TOMMY — roster 3, SierraLeone RebelAlliance (`tommy.png`)
- Silhouette: the widest casual silhouette — big rounded puffer jacket block, can in hand.
- Proportions: STOCKY (height 166, torso width × 1.08 after Aidan's two 2026-11-10 slimming notes); roundest face of the cast (× 1.05).
- Hair: dark brown #33200F CURLS — a mop of tight curls on top, shorter on the sides, no part
  line. (Corrected 2026-11-10 from new photos Aidan sent: the v1–v3 renders' smooth wavy hair
  was wrong — Tommy's hair is curly. Refs: `../../tommy-2.jpg`, `tommy-3.jpg`, `tommy-4.jpg`.)
- Outfit: vintage Notre Dame puffer jacket — body ND navy #1E3050, sleeves and collar trim kelly
  green #1E9E4F, white #F5F2EC side/panel inserts and front placket, high collar popped; simple
  flat leprechaun patch shape on the left chest (green/white/gold shapes only, NO lettering);
  grey crew shirt underneath #6E6E6E; khaki pants #C9B18A; brown shoes #6E4525.
- Props: plain gold drink can #E3A81E (unbranded cylinder, silver top) held in the right hand —
  his default hand prop, part of the model sheet.
- Face notes: brown eyes; light brows; light chin/jaw stubble (from his photos); default mouth
  = big friendly closed smile. Skin fair-pink #F0BE96.
- NEVER: jacket never zipped-down-plain or replaced by a hoodie; no text/logos on jacket or can;
  never slim him down to STANDARD.

### 3.6 VANN — roster 5, Josh Diddy's Roster (`vann.png`)
- Silhouette: the hair IS the silhouette — a curly dome, but TIGHT: curls sit close to the head (Aidan, 2026-11-10: the v1 render was "too poofy — it's a little tighter").
- Proportions: STANDARD.
- Hair: near-black brown #241610, a dense mop of small tight spiral curl clumps, volume extending
  ≈ 0.22 head widths past the head on all sides, fringe curls on the forehead. This is the single
  most recognizable hair in the cast — protect its volume in every variant.
- Outfit: dark navy crewneck sweatshirt #1F2A44 (plain in build — no flag logo); dark jeans
  #24334D; dark sneakers with white soles.
- Face notes: light blue-green eyes; default mouth = the smirk (asymmetric — left corner up 12%,
  right 4%); faint chin stubble is FORBIDDEN as texture — he is clean-shaven in this style, the
  smirk + hair carry him. Skin fair #F2C49B.
- Role note: Vann is Lord Lax's translator (standing gag, §4) — his model needs a clean
  "leaning-in listening" pose in the rig's pose library.
- NEVER: hair never straightened, shortened, or parted; sweatshirt never another color; never
  give him a beard.

### 3.7 GRIFFIN — roster 6, Huff n' Puff (`griffin.png`)
- Silhouette: compact and round — roundest head-to-shoulder read after Tommy, short curls on top.
- Proportions: STOCKY, shortest human (162); face width × 1.05, cheeks full.
- Hair: light brown #7A4B26, short tight curls — 8 small clumps hugging the skull, neat hairline,
  one small curl hook at the front-center (from his photo).
- Outfit: light blue button-down Oxford #A8C6E4, sleeves down, top button open, tucked; dark navy
  chinos #2A3350; brown shoes #6E4525. (Outfit as approved in the previous render set.)
- Face notes: blue eyes; light brows; default mouth = closed-mouth smile (his photo expression —
  lips together, corners up). Skin fair #F2C49B.
- NEVER: **no graduation cap, no gown, no tassel, no diploma — in any scene, ever.** The
  graduation photo is a face reference only (standing hard rule). No beard.

### 3.8 TYRESE "ROBERTSON" — roster 10, T Halibooty (`tyrese.png`)
- Silhouette: tall and lean, vertical stripe block on the torso, cross glint at the chest.
- Proportions: LEAN, 176; face slightly longer (height × 1.05) than the cast standard.
- Hair: dark brown #3A2417, short wavy, 6 clumps, swept up-forward off the forehead, tidy sides.
- Outfit: open button-down shirt — vertical stripes alternating #7FB2E0 and #F5F2EC, stripe width
  ≈ 0.06 head widths, sleeves rolled to the elbow; plain white tee #F5F2EC underneath; light khaki
  shorts #C9B18A (cuffed); white sneakers.
- Props: silver cross pendant #C9CDD4 metallic on a thin chain over the tee — always on.
- Face notes: brown eyes; heavy brows; default mouth = easy closed smile. Skin light tan #E3AC7E.
- Concept-render caveat: his approved concept render (`tyrese.png`) drifted tall (~4.3 heads).
  The BUILD follows §1.2/§1.6 (3.5-head system, 176 height via rig scale) — the render is an
  identity/outfit reference, not a proportion reference.
- NEVER: shirt never buttoned up or in another pattern; cross never removed; never bulk him up.

### 3.9 HIRAM "PAPICHOOTER" — roster 7, NeuralNetanyahu (`hiram.png`)
- Silhouette: the wall — widest shoulders, thickest arms, biggest grin.
- Proportions: BROAD, tallest (178); arms visibly thicker (× 1.25); hands × 1.1.
- Hair: black-brown #1C130E, WAVY and swept back — volume on top, shorter sides, defined
  hairline. Beard = one sculpted mass #1C130E, FULL and neat — jaw + chin + connected
  moustache, comparable fullness to Kearns'. (Corrected 2026-11-10 from a new photo Aidan sent,
  `../../hiram-2.jpg`: the original spec's buzz cut was wrong — Hiram has a full head of hair
  and a full beard.)
- Outfit: lavender polo #C5B3E6 with white #F5F2EC collar/placket trim, two buttons; brown belt
  #8A5A2B; navy pants #2E4A7A; brown shoes #6E4525.
- Face notes: dark brown eyes; heaviest brows in the cast; default mouth = calm confident
  closed smile (full teeth grin lives in the expression set). Skin warm tan #B57E52.
- NEVER: polo never another color; never slim him; never buzz his hair or trim the beard down.

### 3.9b HIRAM — CHEF VARIANT (side model, `hiram-chef.png`)
- Origin: the league group's suggestion, relayed by Aidan 2026-11-10 — "make him like Chef
  from Total Drama Island." A SIDE VERSION of Hiram for SOME scenes (kitchen/cooking bits,
  intimidation gags) — it never replaces the §3.9 base model.
- Build: same head/face/beard as §3.9 on a much bigger frame — towering, heavily muscular
  (arms × 1.5 vs base), tall white toque over his hair, white double-breasted chef's coat with
  sleeves pushed up, long white apron, dark pants, arms crossed, stern unimpressed default
  expression. He is the kitchen's final boss.
- NEVER: never use the chef variant where the bit isn't food/cooking/intimidation; never
  soften the stern default — Chef Hiram does not smile first.

### 3.10 LORD LAX — roster 9, Booze Cruise Collective (`lord-lax.png`)
- Silhouette: helmet dome + cage, padded shoulders/gloves, stick — a knight in the wrong sport.
- Proportions: STANDARD rig (174); gear adds the bulk: shoulder pads under the jersey, gloves
  scale hands × 1.3, helmet makes the head read × 1.15.
- The head: white lacrosse helmet #F2F2F0 with maroon #6E1E2B stripes over the crown, full cage
  face mask (dark grey bars #3A3F45) and a **black opaque visor/interior — zero face, zero skin,
  zero eyes visible at any angle**. Inside the cage is a black void mesh. There is NO head model
  under the helmet; do not build one.
- Outfit: navy lacrosse jersey #1F2A44 base with white #F5F2EC shoulder/side panels over a black
  short-sleeve shirt; **"65" in bold white block numerals on the chest** (the only text in the
  entire cast build); black shorts #17181C; white socks; white cleats.
- Gear: white/maroon gloves (#F2F2F0 / #6E1E2B), white elbow pads with black straps; lacrosse
  stick — white head with simple mesh, light shaft — held upright in the right hand by default.
- Face notes: none. Expression is body language only: helmet tilts (the rig needs generous
  helmet pitch/roll range — his "dialogue" is tilts + the whisper lean toward Vann).
- NEVER: **helmet never comes off; no face is ever designed, implied, or shown; he never speaks
  directly** (standing gag §4); number never changes from 65; gear never swapped for streetwear.

---

## 4. THE FABLE-FILM DISCIPLINE (how these get built and stay good)
Borrowed from the Blender reference film Aidan approved (one character, one room, everything
locked): the quality came from constraint, not detail. Applied here:
1. **Locked models.** Each character is modeled ONCE from §3, approved from stills, then frozen
   in a master `.blend` library. Scenes link (never append-and-edit) the library characters.
2. **One reusable rig.** A single armature + pose/action library shared by all nine humans
   (walk, point, argue, celebrate, facepalm, lean-in-whisper, translate-deliver…). New scenes
   compose poses; they never re-rig. Muse and the capybara get small dedicated rigs.
3. **Stills-first critique.** No scene is animated until its key stills pass review against this
   document: check silhouette, proportions vs §1.6, hex accuracy vs §1.5, ban list §1.7. A scene
   that fails as a still will fail in motion — fix the still.
4. **Sets after people** (Aidan's order): reusable sets (League Desk, living-room couch setup,
   courtside) are designed to the cast's scale and palette only after the cast is approved.
5. **Standing gag is a rig feature, not an edit trick:** LORD LAX WHISPER — Lax leans in, helmet
   to Vann's ear (inaudible); Vann straightens and delivers the line aloud, reluctant. The two
   poses (`whisper_lean`, `translate_deliver`) are named actions in the shared library, used at
   least once per video. Lax never speaks directly, on any rig, in any scene.

## 5. OPEN ITEMS FOR THE BUILD PHASE
- `tommy.png` concept render (generation was refused once; retry or hand-draw before modeling).
- Aidan's approval of this package; any per-character tweaks land in §3 before modeling starts.
- STYLE.md (`../STYLE.md`) still describes the old cinematic look — update it to point here once
  Aidan approves, so future scene work doesn't mix the two systems.
