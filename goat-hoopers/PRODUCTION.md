# GOAT Hoopers — Recap Production Pipeline

How a weekly GOAT Hoopers recap episode gets made, end to end. This is the operating
manual; the enforceable detail lives in the two skills, and the visual canon lives in the
design package. Read this first, then follow the links.

- **Release gates (the law):** [`skills/fantasy-recap-video-qc/SKILL.md`](skills/fantasy-recap-video-qc/SKILL.md)
- **Hype / special videos (preseason, beat-synced):** [`skills/goat-hoopers-hype-video/SKILL.md`](skills/goat-hoopers-hype-video/SKILL.md)
- **How every asset is generated:** [`ASSET-GENERATION.md`](ASSET-GENERATION.md)
- **The cast and design canon:** [`cameo-library/`](cameo-library/) — start at
  `cameo-library/designs/blender/README.md` for the 3D cast.
- **Music pool:** [`../general/music-pool.md`](../general/music-pool.md)

The same pipeline produces the Emperor Phil's Slave Camp NFL recaps (see
`../emperor-phil/`), with the differences the QC skill spells out — storyline spine
instead of the Hoopers structure, hard 5:30–6:30 runtime, no generated packaging.
Everything below is written for Hoopers; the gates skill marks where Emperor differs.

---

## 0. Ground rules

- **No script-approval gate.** A recap request authorizes production straight through to
  a finished video. Report progress as work actually done, never as "ready for approval."
- **Start the morning after the week closes**, and only once the firing mechanism exists
  (a scheduled job or an actual started build — never announce a start that lives only
  in prose). Begin clip downloads at the start and space them through production.
- **Never trust a build report.** Whoever produces the episode, the releasing person
  personally runs the gates on the final file (§8). Two past builds falsely reported
  completion; verification is not optional.

## 1. Verified data pull

Wait until the week's last game is final. Then pull, from Sleeper:

- Scores, records, week highs/lows, standings.
- The full transaction log (waiver claims and trades come **only** from here).
- League chat messages (the saga and the chat quotes come from the real chat).

**Lock-in league warning (this league's scoring is not standard):** each starter scores
ONE locked game per week; an unlocked player auto-counts his final game. Sleeper's
public REST matchup points show each player's *latest* game, not the locked games that
count — results read from the public feed have been wrong before and caused a public
correction. State a score, win, or loss **only from authenticated leg totals for both
teams**. If you can't get both legs, give no numbers at all.

Build a **data manifest** from the pull before any graphics work: every score, record,
and stat that will appear on screen lives in the manifest. Nothing is ever hand-typed
into graphics code.

Cross-check every game result destined for the script against the pull. Omit any claim
that cannot be verified instead of drafting it from memory or inference.

## 2. Script

- **The narrator is Muse.** Write in Muse's voice. Never write first-person as
  Aidan, and never call Aidan "the host" — he is a third-person manager like everyone
  else ("Aidan", "his starters", "he's 3-6"). Muse's own "I" is only for Muse's own
  observations and Muse's own team (NeuralNets). This rule exists because an Emperor
  episode shipped with six segments narrated as Aidan and had to be pulled and remade.
- **Game of the Week:** pick it by default on the evidence — closest finish or marquee
  clash. Never ask Aidan to referee the pick. Name it explicitly in narration and on
  screen, cover it **exactly once** in its own deep segment, and take it out of the
  general rundown (a one-line pointer on the results board at most).
- **Tone check before production:** read the final script and count the profanity —
  the count must be above zero, and the jokes must land on specific players and results
  from that week, not generic filler.
- **Runtime discipline:** if the script runs long, cut words. Never speed up or
  compress the voiceover delivery to hit a number.

### The Week 3 structure (approved 2026-11-03 — the template)

1. Intro / cold open — crystal Muse in action, fresh every week
2. Rollcall, with chat quotes landing
3. Results board — all five finals, one line each, GOTW row a pointer only
4. Game of the Week, in depth, once
5. Other matchups as quick hits
6. Monsters
7. Studs & Chuds (player awards from the weekly receipt + team awards by official leg
   totals — both, per Aidan's 2026-11-06 definition)
8. The saga, told through actual chat and trade messages
9. Confession — Muse's own team's verified result
10. Clean standings board
11. Next-week face-offs + outro — crystal Muse doing something cool, fresh every
    week, never a static endcard

Chat call-outs and clipped real chat quotes are **woven throughout** the whole runtime
(opening, middle, and closing thirds) — never grouped into one segment.

## 3. Music — first, from the shared pool

Choose the tracks **before any editing**; the music dictates the edit. Use more than
one track per episode.

- One shared no-repeat pool covers Hoopers **and** Emperor: a track used in ANY prior
  recap is burned for every series. The pool of record is
  [`../general/music-pool.md`](../general/music-pool.md) — check every candidate
  against it before proposing or locking a slate.
- **No Kendrick Lamar, ever** — no tracks by him, none featuring him.
- When the episode ships, add its tracks to the pool in the same commit as the
  delivery bookkeeping. Burned means burned: never re-list a burned track as a
  candidate.

## 4. Footage — fresh, matched, provenanced

- Pull every game clip **fresh from that week's actual games**, matched to the player
  being narrated at that moment. Never reuse a clip from an earlier episode, never
  substitute generic filler, never loop a clip to fill time.
- Keep a **provenance list** for every clip: source game + the player it illustrates.
  It ships with the delivery report.
- Spread downloads across production (throttling stacks up if you pull everything at
  delivery time). For highlight-style sourcing (hype videos), the yt-dlp route,
  spacing, and validation rules are in
  [`skills/goat-hoopers-hype-video/SKILL.md`](skills/goat-hoopers-hype-video/SKILL.md).
- Game-clip natural sound is ducked hard under narration in the mix — and **measured**
  separately from the music bed at the gate (§8).

## 5. Voiceover and captions

- Render all recap VO with the one verified configuration: `tts speak`,
  voice `avocado_v2:MAI_03`. Both series use it. A different configuration is a
  failed gate, not a style choice — and never attribute a voice-quality difference
  to the model without comparing configurations first; the one time that claim was
  made, the real cause was natural sound burying the narration.
- Music sits at **one steady level** under the voice — no pumping or breathing.
- Captions come from **forced alignment of the final script text to the VO audio**,
  never from speech-recognition on your own voiceover. Diff caption text against the
  final script: word-for-word, 100%.

## 6. Graphics — designed boards, one system

Emperor gets exactly the same design treatment as Hoopers; there is no second-tier
pass. Build from the manifest only:

- Designed results board, playoff/standings board, Stud/Chud and desk cards — full
  designed boards, not overlays improvised per segment.
- Score bugs per segment; player info top-left; stat pills bottom-right, **fired on
  the timestamp of their spoken word**, never on a fixed timer, and never overlapping.
- All text/writing screens are **completely stable** — no panning, drifting, or slow
  zooms. Kinetic captions are the Hoopers house style.
- No black screens, ever: something visible at all times.

## 7. Cameo scenes and versus intros (Hoopers)

The animated world is canon in [`cameo-library/`](cameo-library/); how it's generated
is in [`ASSET-GENERATION.md`](ASSET-GENERATION.md). In each episode:

- ~4–6 **ensemble scenes**, 20–45 s each, woven throughout: multiple members
  interacting, written comedy structure (setup → bit → payoff), league-specific
  humor, Muse in the scenes, every member appearing across the set. No one-solo-scene
  per member, no silent reaction shots, no decorative appearances. Regenerate or
  restage anything sloppy — never ship it.
- A **versus intro** (the matchup's X vs Y, in the locked character designs)
  immediately before each previous-week game segment.
- The **Lord Lax whisper gag, at least once**: someone asks Lax a question, he
  whispers inaudibly into Vann's ear, and Vann delivers it aloud as the reluctant
  translator. Lax never speaks directly, in any episode, ever.

## 8. QC release gates

Run every gate **personally on the final master file** — a builder's report is not
verification. The full gate list is the QC skill's "Run the final master gates"
section; the ones that have actually caught failures:

- Scores/records in script, captions, and graphics match the post-final pull — zero
  discrepancies; every waiver/trade claim traces to the transaction log.
- Captions match the final script 100% (report matched/total counts).
- Every on-screen figure traces to the manifest (report checked/total; zero
  hand-typed numbers).
- `blackdetect`: zero black gaps longer than 0.5 s.
- Mix, **measured in the final master** (integrated LUFS alone is not evidence):
  music bed 10–12 dB under VO; game natural sound ≥ 12 dB under VO — report both
  deltas (nat sound: minimum and median).
- Narrator-persona grep (§2): zero first-person-as-Aidan hits. Report the count.
- Clip provenance covers every clip; zero reused / filler / looped clips.
- Chat quotes land in all three thirds (report timestamps); GOTW callout present in
  narration and on screen, covered once; intro + outro present and fresh.
- `ffprobe`: video/audio durations match within 0.5 s at the intended resolution.
- Tracks checked against the burned pool: zero repeats.
- Cameo scenes, versus intros, and the whisper gag confirmed with timestamps.
- Watch spot frames from every segment and listen to sections of the actual master
  yourself. Fix any failed gate, re-render, re-run that gate. Report gate results
  as **counts, not adjectives**.

## 9. Upload package

Three deliverables, always together:

1. **Master** — 1920×1080, high-quality encode (crf16 class). Masters live in the
   workspace / Google Drive, **never in this repo** (see the root README's rules).
2. **Upload encode** — sized to stay grant-eligible. Hard-won lesson: browser file
   grants cap out somewhere between ~103 MB and ~161 MB, and remote storage caps
   below 161 MB too. The working pattern is a 2-pass encode around 1150 kbps video
   + 128k AAC (≈56 MB for a ~6-minute episode). If a long episode can't fit without
   wrecking quality, upload the encode to Aidan's Google Drive instead and let him
   upload to Studio from his own device — do not degrade the quality to force the
   browser route.
3. **Thumbnail** — part of the package, designed in the same system as the episode's
   boards. An episode does not ship without one.

Upload settings (the standing pattern): title
`GOAT Hoopers Week N Recap — "<Episode Name>"`, blank description, custom thumbnail,
"No, it's not made for kids," **UNLISTED**, no playlist, no end screens or cards.
Check Studio for a stale draft of the same title before uploading a replacement —
a halted upload once left one behind.

## 10. Delivery

Deliver the master, the live unlisted link, and the thumbnail together, with the
gate results as counts and the clip provenance list. Then do the bookkeeping in the
same pass:

- Burn the episode's tracks into [`../general/music-pool.md`](../general/music-pool.md).
- File any new design assets in `cameo-library/` (and the frozen copies in `final/`
  where the package uses one).
- If production changed a standing rule, update the skill it belongs to — the repo
  snapshots get re-synced from Muse's canonical skills.
