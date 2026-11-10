# Archive index

Everything in this tree is **superseded** — kept for history and reference, never as a build
source. The canon version of every asset lives outside the archive; this index says what
each archived thing is and what replaced it.

Cleanup pass: **2026-11-10**. Rule applied: byte-identical duplicates were deleted outright
(one canonical copy kept); distinct-but-superseded versions were moved here. A second,
older archive lives at `designs/blender/archive/` (v1/v2 render rounds, before/after
comparisons, and all `media-generation-*.json` generation logs) and is indexed by its own
folder names.

## `designs/blender/` — superseded cast lineup renders

| File | What it is | Replaced by |
|---|---|---|
| `cast-lineup-v4.png` | Cast lineup render, intermediate naming-dodge copy (2026-11-10) — distinct bytes from canon | `designs/blender/final/cast-lineup.png` |
| `cast-lineup-v5.png` | Cast lineup render, intermediate naming-dodge copy (2026-11-10) — distinct bytes from canon | `designs/blender/final/cast-lineup.png` |

(The v3 and v6 lineup files were byte-identical to the canon `final/cast-lineup.png` and
were deleted in the cleanup, not archived.)

## `designs/renders/` — the pre-Blender 2D concept renders

The first design round (2026-11-09): one generated render per member in the earlier
photoreal/cinematic style. Superseded the same week by the locked 3D animated-sitcom
Blender cast. Identity notes from this round still live in `designs/<person>.md`; the
renders themselves are history.

| File | Subject |
|---|---|
| `aedan.png` | Aedan "Kearns" |
| `aidan.png` | Aidan |
| `griffin.png` | Griffin |
| `hiram.png` | Hiram (papichooter) |
| `lord-lax.png` | Lord Lax |
| `phil.png` | Phil |
| `tommy.png` | Tommy |
| `tyrese.png` | Tyrese |
| `vann.png` | Vann |

Replaced by: `designs/blender/final/` (the approved 3D cast renders, incl. Muse and
Chef Hiram, who had no 2D-round render).

## Deleted in this cleanup (byte-identical duplicates — canonical copy kept)

- `designs/blender/{aidan,griffin,hiram,hiram-chef,kearns,lord-lax,muse,phil,tommy,tyrese,vann}.png`
  and `designs/blender/muse-identity-ref.png` — root working copies, identical to `final/`.
- `designs/blender/cast-lineup.png`, `cast-lineup-v3.png`, `cast-lineup-v6.png` — identical
  to `final/cast-lineup.png`.
- `designs/blender/archive/v2/tommy-v3.png` — was byte-identical to the canon
  `final/tommy.png` despite the v3 name; the real superseded Tommy versions are
  `archive/v1/tommy.png`, `archive/v2/tommy.png`, and `archive/v2/tommy-v4-photoreal.png`.
- `designs/blender/archive/v2/hiram-v1.png` — was byte-identical to the canon
  `final/hiram.png` despite the v1 name.

## Consolidated in this cleanup (not archived here)

- All loose `media-generation-*.json` generation logs that were scattered in
  `designs/blender/` and `designs/renders/` were moved into
  `designs/blender/archive/generation-logs/`, joining the logs already filed there.
  Name collisions were kept as separate files with a `--from-renders` / `--from-blender-root`
  suffix. Nothing was deleted.
