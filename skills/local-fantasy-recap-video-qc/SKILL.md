# Fantasy Recap Video Release Gates

## Verify facts before scripting

- Wait until the week has fully ended before scripting a recap.

- Pull scores, records, week highs and lows, and standings from Sleeper after the last game is final.

- Cross-check every game result in the script against that pull and never lock a script from pre-final or in-progress scores.

- Build the waiver section only from the league transaction log and the trades segment only from logged trades.

- Omit any claim that cannot be verified in the log instead of drafting it from memory or inference.

## Produce without an approval gate

- Write the script and go straight into production without asking Aidan to approve the script.

- Never present finished scripts as ready for approval and never hold editing until Aidan says to start.

- Treat a recap request as authorization to deliver the finished video, subject only to the release gates in this skill.

- Produce only the Emperor Phil recap for the NFL leagues, because Aidan discontinued the BC League recap series on 2026-10-29 and Week 7 was its last episode.

- Never start, schedule, or deliver a BC League recap unless Aidan explicitly restarts the series in words.

- Report progress as work actually done, such as script written, edit built, or gates run, rather than as a pending approval.

- Start production the morning after the week closes and begin clip downloads then, spacing downloads through production so throttling does not stack up at delivery time.

- Announce a production start only after the mechanism that fires it exists, such as a scheduled job, and never let a start live only in prose.

## Build from verified records

- Choose the music tracks before any editing and use more than one song where the episode calls for it, because the music dictates the edit.

- Check standing artist exclusions in memory before proposing or locking any track, including featured artists, and never use a track by or featuring an excluded artist.

- Treat Kendrick Lamar as a hard exclusion, with no tracks by him and no tracks featuring him in any recap soundtrack.

- Keep one shared burned track list across GOAT Hoopers and Emperor Phil recaps and check every candidate track against it before proposing or locking a slate.

- Treat a track used in any prior recap in either series as burned and never propose, list, or reuse it for a later episode.

- Record each delivered track on the shared burned list when the episode ships, so the check survives across episodes and builders.

- Build the edit in the Hoopers recipe, where real footage and music carry stretches with no narration and the voiceover works as tight seasoning rather than a wall of talk.

- Weight segment length by the drama of each game instead of giving every game equal time, and let music forward tails play after segments instead of filling them with more narration.

- Build each GOAT Hoopers episode on the Week 3 structure Aidan approved on 2026-11-03, in order: intro video or cold open, rollcall with chat quotes landing, results board with the Game of the Week row as a pointer only, the Game of the Week once in depth, the other matchups as quick hits, Monsters, Studs and Chuds, the saga told through actual chat and trade messages, Confession, a clean standings board, and next week face-offs plus the outro video, with chat woven throughout.

- Build each Emperor Phil episode on a storyline spine with rollcall, results board, and confession style anchors, rather than a run of near equal game segments. Give the Game of the Week the most room and reduce the other games to quick hits that feed that spine.

- Pick the Game of the Week by default from the evidence, choosing the closest finish or the marquee clash, and never ask Aidan to referee the pick. Treat the obvious game on the evidence as the pick and put it first.

- Open every recap with a fresh intro video featuring crystal Muse in action and close every recap with a fresh outro video featuring crystal Muse doing something cool. Never end an episode on a static endcard alone and never reuse the same intro or outro sequence from an earlier week.

- Cut narration words to hit the runtime target and never speed up or compress the delivery of the voiceover to fit.

- Use no generated plates, stingers, or stings and no throne or regicide theming in Emperor Phil recaps, because real game footage carries the whole episode.

- Build a data manifest before graphics so every on-screen number, score, record, and stat pill comes from verified data and is never hand-typed into graphics code.

- Fire stat pills on the timestamp of their spoken word rather than on a fixed timer and check that pills in a segment do not overlap each other.

- Generate captions by forced alignment of the final script text to the voiceover audio and never by transcribing your own voiceover with speech recognition when the exact script exists.

- Diff the caption text against the final script and require a word for word match before delivery.

- Write the narration in Muse's own voice as the narrator, never in first person as Aidan and never calling Aidan "the host" or "your host", because Aidan flagged on 2026-11-10 that first-person-as-Aidan narration through six Emperor Week 9 segments made the video weird and had it pulled before delivery. Aidan appears in the third person by name like every other manager ("Aidan", "his starters", "he's 3-6"), and Muse's own "I" appears only for Muse's own observations and Muse's own team.

- Render every recap voiceover with the same verified GOAT Hoopers voice configuration, `tts speak` with avocado_v2:MAI_03, for both Hoopers and Emperor Phil episodes. A different verified configuration is a failed gate, not a style choice.

- Verify the actual render configuration of both episodes before attributing any voice quality difference to the voice model, and never state a guessed cause as fact. When the configurations match, investigate the mix first, because the Emperor Week 8 complaint on 2026-11-03 came from game natural sound burying the narration while both episodes used the same configuration and a re-render came back byte identical.

- Keep the voiceover clearly on top at all times, duck game clip natural sound hard under narration, and keep music at one steady level under the voice with no pumping or breathing.

- Check the script tone before production by reading the final script and counting its profanity, requiring a count above zero and jokes that land on specific players and results from that week rather than generic filler lines.

- Pull every game clip fresh from that week and its actual games and match each clip to the player being narrated at that moment.

- Never reuse a clip from an earlier episode, substitute generic filler footage, or loop a clip to fill time.

- Keep a provenance list for every clip that names its source game and the player it illustrates, and include that list in the delivery report.

- Spread league chat call-outs and clipped real chat quotes across the whole runtime in GOAT Hoopers recaps instead of grouping them in one segment, planning chat beats for the opening, middle, and closing thirds before editing begins, because the league loved them in the Week 1 recap and they are a permanent feature there.

- Name the Game of the Week explicitly in the narration and on screen and give that game its own called out segment, rather than treating it as just another game in the run of segments.

- Cover the Game of the Week exactly once, in its own segment only: take it out of the general rundown entirely (a one-line pointer on a results board at most), because Aidan flagged the Week 2 Hoopers v2 on 2026-11-03 for covering the papichooter and Vann game both in the front rundown and again in the GOTW segment.

- Keep every screen where text is being written onto the screen completely stable, with no panning, drifting, or slow zoom on any such screen.

- Create the thumbnail as part of the delivery package and never ship an episode without one.

## Build ensemble cameo scenes and versus intros

- Weave generated cameo scenes throughout every GOAT Hoopers recap instead of confining them to fixed slots, cutaways, or one solo scene per member.

- Build about four to six ensemble scenes per episode, each 20 to 45 seconds long, with multiple league members together interacting in the same scene.

- Write each cameo scene with a comedy structure of setup, bit, and payoff, using league specific humor, and include crystal Muse as a character in the scenes.

- Cover every league member across the ensemble scenes and give no member a silent reaction shot or a decorative appearance.

- Regenerate or restage any cameo generation that reads as sloppy instead of shipping it.

- Ask Aidan for the specific member photos a planned episode needs before building its scenes.

- Save every member photo Aidan sends to the persistent cameo library at ~/workspace/goals/goat-hoopers-hype-videos/hidden_files/cameo-library/ and reuse the saved library in later weeks instead of asking again for a photo already saved.

- Place a versus fight scene intro before each previous week game segment, showing that matchup as one manager against the other, instead of anime style rollcall cards.

- Render every member in one consistent look across all scenes and versus intros, in the same design style as the existing crystal Muse scenes, backed by a written design file for each person.

- Stage the Lord Lax whisper gag at least once in every GOAT Hoopers recap, where someone asks Lord Lax a question, he whispers the answer inaudibly into Vann ear, and Vann delivers it aloud as the reluctant translator.

- Never stage Lord Lax speaking directly to camera or to another character.

## Run the final master gates

- Run every gate in this section personally on the delivered file, because a subagent report or build log is not verification.

- Confirm every score, record, and week high or low in the script, captions, and graphics matches the post-final Sleeper pull with zero discrepancies.

- Confirm every waiver and trade claim traces to an entry in the league transaction log with zero unverified claims.

- Confirm caption words match the final script at 100 percent and report the matched and total counts.

- Confirm every on-screen figure traces to the data manifest and report the checked and total counts with zero hand-typed numbers.

- Run `ffmpeg` with `blackdetect` on the master and require zero black gaps longer than 0.5 seconds, counting a dark background plate with no clip on top as black rather than visible content.

- Spot-check narration over the loudest game clips in each segment and confirm the voiceover is intelligible everywhere and the music level stays steady under it.

- Measure the music level against the voiceover level in the actual final mix and require the music bed to sit about 10 to 12 dB below the voiceover, because an integrated loudness figure alone does not pass this gate.

- Measure the game-clip natural sound against the voiceover in the actual final mix at the loudest clips in each segment and require every measured passage to sit at least 12 dB below the voiceover, and report the measured natural-sound delta alongside the music-bed delta, because Aidan flagged on 2026-11-03 that Emperor Week 8 game audio ran a touch too loud where the measured bed floor was 10.8 dB under the voice. Report the minimum and median natural-sound deltas as well as the music-bed delta.

- Confirm the delivered voiceover was rendered with the verified GOAT Hoopers voice configuration and report the configuration used in the delivery message. Report a voice model difference only when a configuration comparison proves one, and otherwise report the measured mix cause.

- Grep the final script and caption text for first-person-as-Aidan narration and require zero hits: no "your host", "my starters", "I traded", "trade with me", "beat me", "my team" (when the team is Aidan's), "I claimed", or "I scored" in any segment. Muse narrates; Aidan is a third-person manager. Report the grep result count in the delivery message.

- Confirm the clip provenance list covers every clip in the master and shows zero clips reused from earlier episodes, zero generic filler clips, and zero looped clips.

- Confirm from a timestamp list that chat call-outs appear in the opening, middle, and closing thirds of the runtime and that no single segment holds all of the chat material, and report those timestamps in the delivery message.

- Confirm the Game of the Week callout appears explicitly in both the narration and on screen and report its timestamp in the delivery message.

- Confirm the Game of the Week game is covered in only one segment, its own, with no full second pass in the general rundown, and report the rundown pointer (if any) in the delivery message.

- Confirm the Game of the Week pick matches the evidence by reporting the finish margin or the marquee basis for the pick in the delivery message, with no pick referred to Aidan for a decision.

- Confirm the intro video and the outro video are both present by reporting their timestamps, that each features crystal Muse in action, that neither is reused from an earlier week, and that the master does not end on a static endcard alone.

- Confirm the storyline spine is present by reporting the segment list and durations, requiring the Game of the Week segment to be the longest game segment and the other game segments to read as quick hits rather than near equal blocks.

- Confirm every writing screen in the master is stable by checking motion across its duration, requiring zero writing screens with panning, drifting, or a slow zoom, and report the number of writing screens checked.

- Confirm an Emperor Phil master lands between 5:30 and 6:30 and treat any master over 7:00 as not delivered, sending it back for a re-cut that removes narration instead of speeding it up.

- Confirm the runtime matches the natural pace of the final script and that narration was not sped up or compressed to hit a runtime number.

- Use `ffprobe` to confirm video and audio durations match within 0.5 seconds at the intended resolution.

- Confirm the delivery package includes the thumbnail beside the master file.

- Watch spot frames from every segment and listen to sections of the actual master yourself before delivery, rather than relying on a builder report of the frames or the mix.

- Fix any failed gate, re-render, and re-run that gate before delivering, and report the gate results as counts rather than adjectives in the delivery message.

- Confirm every track in the master was checked against the shared burned track list covering both series and report zero repeat tracks in the delivery message.

- Confirm the cameo scenes by reporting their count, durations, and timestamps spread across the runtime, that each scene holds multiple members interacting, and that every member appears across the scenes.

- Confirm a versus intro appears before each previous week game segment and that each member rendering matches that member written design file.

- Confirm the Lord Lax whisper gag appears at least once by reporting its timestamp, with Vann delivering the answer aloud and Lord Lax never speaking directly.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Start data verification and music selection in parallel with scripting when the week has ended, so production is not serialized behind either one.

- Deliver the finished video with its gate counts instead of a script summary when Aidan asks whether a recap is ready.

- Shorten the script before touching the edit when a draft runs long, because word count is the cheapest runtime lever and preserves the natural pace gate.
