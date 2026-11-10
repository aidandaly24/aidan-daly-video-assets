> **Repo snapshot — read this first.** This file is a snapshot of the working skill Muse
> uses in production, synced **2026-11-10**. The canonical source lives with Muse and
> keeps evolving; this repo copy is the shareable / self-serve version, so anyone who
> pulls the repo can run the same playbook. If the two ever disagree, Muse's copy
> governs live production.

# GOAT Hoopers Hype Video Playbook

## Choose the music and treatment

- Send Aidan 2 to 3 music options with links before editing and wait for his approval on the track.

- Skip Cant Hold Us because Aidan rejected it as normie and treat FE!N cautiously because he second guessed it as too chaotic for clean beat synced cuts.

- Propose a four act structure built on setup, contenders, a wildcard turn and a final call, then wait for approval on the treatment.

- Write the voiceover script after the treatment is approved and match its beats to the approved structure.

- Confirm the draft is fully complete before finalizing a preseason video because Aidan sends it only after the draft is done.

- Keep hype videos private to the league and never treat them as public posts.

## Source and validate clips

- Download a 25 second highlight section per player from 00:05 to 00:30 with `yt-dlp --js-runtimes node --extractor-args "youtube:player_client=android" --download-sections "*00:05-00:30" -o "%(title)s.%(ext)s" "ytsearch1:[player name] highlights [season]"` run by `muse.exec`.

- Accept the 360p limit of the android client for fast cut B-roll under overlays and do not chase a higher resolution that this route blocks.

- Space downloads 90 to 180 seconds apart because throttling grows after about six downloads and retries succeed after a cooldown.

- Fall back to a full download with retries and an http chunk size, then cut locally with `ffmpeg`, when section downloads die mid stream.

- Validate every clip by file size over 1 MB, by duration and by a content spot check, and replace corrupt or empty files.

## Map the beat and the story

- Extract the track audio and run onset detection so every significant transient, drop and section change has an exact timestamp.

- Map energy in half second windows across the full track to find drops, breakdowns and beat switches.

- Listen through the track and annotate repeating motifs, vocal entrances, build ups and drops that automated detection missed.

- Build a timestamped beat sheet that maps every significant hit to a planned visual and never assigns generic filler to a repeated motif.

## Edit and caption the video

- Cut hard on transients and use controlled speed ramps on the beat, with no dissolves, wipes or other cheesy transitions.

- Use one clean condensed sans type family, consistent lower thirds and one unified color grade across all clips.

- Target about 80 seconds of voiceover for a preseason video, adjusted to the approved runtime, and land narration in musical breathing room rather than over drops.

- Duck music 6 to 10 dB under the voiceover, keep the voiceover clear and present, and normalize the final master.

- Give every team section a bold title card, a clip of a named player from that team with face or jersey number visible, a matching lower third and a matching caption.

- Log every clip used per section and never reuse one clip in two sections.

- Spell caption names as Giannis, LaMelo, Dybantsa, Vann, Shai Gilgeous-Alexander, Acuff, Wembanyama, Aidan, Lord Lax, Lendeborg, Devin Booker, Jaylen Brown, Banchero, Adebayo, De'Aaron Fox, papichooter and Luka Doncic.

- Split captions into per team segments aligned to the voiceover and end each caption before its section title card appears, using dark frame detection on the final video to find true title card times.

- Verify after any caption edit that no two caption events overlap and that no single caption line holds more than one Dialogue event.

- Build the closing with a draft board flash, rivalry week face off cards, a 1 to 10 power rankings graphic, a final hook over hype clips and an end card.

- Add a short post credits gag only when the approved treatment calls for one.

- Use the Muse character cameo sparingly and only in the NeuralNets section when it genuinely elevates the cut, with its own voiceover moment, the main voiceover paused and the main captions blanked.

## Verify the final file and deliver

- Never deliver on a subagent or build report alone because the v5 and v7 builds falsely reported completion.

- Run `ffprobe` on the final file and confirm the video and audio durations match within 0.5 seconds and the resolution is 1920 by 1080.

- Extract 2 to 3 frames from every team section of the final file and confirm the player, lower third, title card and caption all agree.

- Extract frames at 3 or more timestamps in the closing and confirm motion instead of frozen frames.

- Read the caption file and confirm no overlapping timestamps, no merged dialogue lines and no misspelled names.

- Watch the full video once at full speed, fix any failed check and re-verify the final file before delivering.

- Attach the final MP4 in chat and keep a dated copy under `~/workspace/goat-hoopers/videos/`.

- Report the track used, the runtime and any deviation from the approved treatment in the delivery message.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [YouTube](https://www.youtube.com/) for finding player highlight footage. Carry the player name and season into the search and verify the clip shows the right player before downloading.

## Alternatives for better results

- Use the local fantasy recap video QC skill instead when the video is a weekly recap, because recaps carry fact gates this hype workflow does not.

- Prefer section downloads over full highlight compilations, because compilations add hundreds of megabytes for the same 25 seconds of usable footage.

- Shorten the track or the treatment when clip supply runs thin rather than loosening beat sync or repeating clips.
