#!/usr/bin/env python3
"""Build the spatial mix for 'The Last Possession' pilot scene.
Processes each line with its position treatment (constant-power pan, level,
distance EQ / reverb — pitch never touched), lays everything on a timeline,
mixes, and masters to -16 LUFS integrated. Run: python3 mix-build.py
"""
import subprocess, json, math, os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
LINES = os.path.join(BASE, 'audio', 'lines')
AUD = os.path.join(BASE, 'audio')
PROC = os.path.join(AUD, 'proc')
os.makedirs(PROC, exist_ok=True)

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print('FAILED:', ' '.join(cmd[:6]), '...\n', r.stderr[-1500:]); sys.exit(1)
    return r

def dur(path):
    out = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                          '-of', 'csv=p=0', path], capture_output=True, text=True).stdout.strip()
    return float(out)

def rms_db(path):
    r = subprocess.run(['ffmpeg', '-i', path, '-af', 'astats=metadata=1', '-f', 'null', '-'],
                       capture_output=True, text=True)
    m = re.findall(r'RMS level dB: (-?[\d.]+)', r.stderr)
    return float(m[-1]) if m else -23.0

def gains(p):
    a = math.radians((p + 1) * 45.0)
    return math.cos(a), math.sin(a)

# filename -> (pan, volume, lowpass_or_None, aecho_or_None)
TREAT = {
    '01-aidan.mp3':   (-0.15, 1.00, None, None),
    '02-kearns.mp3':  (-0.30, 1.00, None, None),
    '03-phil.mp3':    ( 0.60, 0.92, None, 'aecho=0.8:0.65:90:0.18'),
    '04-griffin.mp3': (-0.50, 0.90, None, None),
    '05-vann.mp3':    ( 0.20, 1.00, None, None),
    '06-griffin.mp3': (-0.50, 0.90, None, None),
    '07-tyrese.mp3':  ( 0.45, 1.05, None, 'aecho=0.8:0.7:60:0.25'),
    '08-hiram.mp3':   ( 0.50, 0.70, 6000, 'aecho=0.8:0.7:130:0.35'),
    '09-tommy.mp3':   (-0.05, 1.00, None, None),
    '10-muse.mp3':    ( 0.00, 1.00, None, None),
    '11-aidan.mp3':   (-0.15, 1.00, None, None),
    '12-lax.mp3':     ( 0.30, 0.35, None, None),
    '13-vann.mp3':    ( 0.20, 1.00, None, None),
    '14-aidan.mp3':   (-0.15, 1.00, None, None),
    '15-vann.mp3':    ( 0.20, 1.00, None, None),
    '16-aidan.mp3':   (-0.15, 1.00, None, None),
    '17-aidan.mp3':   (-0.15, 1.10, None, None),
    '18-kearns.mp3':  (-0.30, 1.00, None, None),
    '19-tyrese.mp3':  ( 0.45, 1.05, None, 'aecho=0.8:0.7:60:0.25'),
    '20-phil.mp3':    ( 0.60, 0.92, None, 'aecho=0.8:0.65:90:0.18'),
    '21-aidan.mp3':   (-0.15, 1.00, None, None),
    '22-muse.mp3':    ( 0.00, 1.00, None, None),
}
ORDER = sorted(TREAT.keys())

# ---- 1. process lines -------------------------------------------------------
proc, durs = {}, {}
for fn in ORDER:
    pan, vol, lp, echo = TREAT[fn]
    gl, gr = gains(pan)
    chain = [f'aformat=channel_layouts=mono',
             f'pan=stereo|c0={gl:.3f}*c0|c1={gr:.3f}*c0']
    if lp: chain.append(f'lowpass=f={lp}')
    chain.append(f'volume={vol}')
    if echo: chain.append(echo)
    src = os.path.join(LINES, fn)
    out = os.path.join(PROC, fn.replace('.mp3', '.wav'))
    run(['ffmpeg', '-y', '-v', 'error', '-i', src, '-af', ','.join(chain), '-ar', '44100', out])
    proc[fn], durs[fn] = out, dur(out)
    print(f'processed {fn}: {durs[fn]:.2f}s pan={pan:+.2f} vol={vol}')

# phone buzz, panned to Lax's seat, quiet
gl, gr = gains(0.30)
buzz = os.path.join(PROC, 'buzz.wav')
run(['ffmpeg', '-y', '-v', 'error', '-i', os.path.join(AUD, 'sfx-phone-buzz.mp3'),
     '-af', f'aformat=channel_layouts=mono,pan=stereo|c0={gl:.3f}*c0|c1={gr:.3f}*c0,volume=0.5',
     '-ar', '44100', buzz])

# ---- 2. timeline ------------------------------------------------------------
GAP = {'01-aidan.mp3': .40, '02-kearns.mp3': .40, '03-phil.mp3': .35, '04-griffin.mp3': .10,
       '05-vann.mp3': .30, '06-griffin.mp3': .50, '07-tyrese.mp3': .45, '08-hiram.mp3': .40,
       '09-tommy.mp3': .40, '10-muse.mp3': .60, '11-aidan.mp3': .55, '12-lax.mp3': .45,
       '13-vann.mp3': .30, '14-aidan.mp3': .35, '15-vann.mp3': .60}
start, end = {}, {}
t = 7.30  # first line starts as the intro sting resolves
for fn in ORDER[:16]:  # 01..16 sequential
    start[fn] = t
    end[fn] = t + durs[fn]
    t = end[fn] + GAP.get(fn, 0.40)
crowd1_start = end['16-aidan.mp3'] - 0.10
start['17-aidan.mp3'] = crowd1_start + 2.30
end['17-aidan.mp3'] = start['17-aidan.mp3'] + durs['17-aidan.mp3']
start['18-kearns.mp3'] = end['17-aidan.mp3'] + 0.35
end['18-kearns.mp3'] = start['18-kearns.mp3'] + durs['18-kearns.mp3']
start['19-tyrese.mp3'] = end['18-kearns.mp3'] + 0.55
end['19-tyrese.mp3'] = start['19-tyrese.mp3'] + durs['19-tyrese.mp3']
crowd2_start = end['19-tyrese.mp3'] + 0.35
start['20-phil.mp3'] = crowd2_start + 1.70
end['20-phil.mp3'] = start['20-phil.mp3'] + durs['20-phil.mp3']
start['21-aidan.mp3'] = end['20-phil.mp3'] + 0.45
end['21-aidan.mp3'] = start['21-aidan.mp3'] + durs['21-aidan.mp3']
fail_start = end['21-aidan.mp3'] + 0.50
fail_dur = dur(os.path.join(AUD, 'music-fail-sting.mp3'))
start['22-muse.mp3'] = fail_start + fail_dur + 0.25
end['22-muse.mp3'] = start['22-muse.mp3'] + durs['22-muse.mp3']
outro_start = end['22-muse.mp3'] + 0.50
outro_dur = dur(os.path.join(AUD, 'music-outro-sting.mp3'))
total = outro_start + outro_dur + 0.40
buzz_start = start['11-aidan.mp3'] - 1.70

print('\nTIMELINE')
for fn in ORDER:
    print(f'  {start[fn]:7.2f} -> {end[fn]:7.2f}  {fn}')
print(f'  crowd1 @{crowd1_start:.2f}  crowd2 @{crowd2_start:.2f}  buzz @{buzz_start:.2f}')
print(f'  fail @{fail_start:.2f}  outro @{outro_start:.2f}  TOTAL {total:.2f}s')

# ---- 3. bed levels (>=10 dB under dialogue) ---------------------------------
dlg = [rms_db(os.path.join(LINES, fn)) for fn in ORDER if fn != '12-lax.mp3']
dlg_rms = sum(dlg) / len(dlg)
und_rms = rms_db(os.path.join(AUD, 'music-underscore.mp3'))
room_rms = rms_db(os.path.join(AUD, 'sfx-room-bed.mp3'))
und_vol = 10 ** ((dlg_rms - 13.0 - und_rms) / 20)
room_vol = 10 ** ((dlg_rms - 25.0 - room_rms) / 20)
print(f'\ndialogue RMS {dlg_rms:.1f} dB | underscore src {und_rms:.1f} dB -> vol {und_vol:.3f} '
      f'({dlg_rms - 13.0:.1f} dB target) | room src {room_rms:.1f} dB -> vol {room_vol:.3f}')

# ---- 4. mix ------------------------------------------------------------------
inputs, filters = [], []
def add_input(path, loop=False):
    if loop: inputs.extend(['-stream_loop', '-1'])
    inputs.extend(['-i', path])
    return (len(inputs) - 1) // 1 and sum(1 for x in inputs if x == '-i') - 1

idx = {}
for fn in ORDER:
    idx[fn] = sum(1 for x in inputs if x == '-i')
    inputs.extend(['-i', proc[fn]])
def next_idx(path, loop=False):
    i = sum(1 for x in inputs if x == '-i')
    if loop: inputs.extend(['-stream_loop', '-1'])
    inputs.extend(['-i', path])
    return i
i_intro = next_idx(os.path.join(AUD, 'music-intro-sting.mp3'))
i_crowd1 = next_idx(os.path.join(AUD, 'sfx-crowd-erupt.mp3'))
i_crowd2 = next_idx(os.path.join(AUD, 'sfx-crowd-erupt.mp3'))
i_buzz = next_idx(buzz)
i_fail = next_idx(os.path.join(AUD, 'music-fail-sting.mp3'))
i_outro = next_idx(os.path.join(AUD, 'music-outro-sting.mp3'))
i_und = next_idx(os.path.join(AUD, 'music-underscore.mp3'), loop=True)
i_room = next_idx(os.path.join(AUD, 'sfx-room-bed.mp3'), loop=True)

labels = []
def seg(i, pre, start_s, label):
    d = int(round(start_s * 1000))
    filters.append(f'[{i}:a]{pre}adelay={d}|{d}[{label}]' if pre else f'[{i}:a]adelay={d}|{d}[{label}]')
    labels.append(label)

for n, fn in enumerate(ORDER):
    seg(idx[fn], '', start[fn], f'l{n}')
seg(i_intro, 'afade=t=out:st=6.0:d=2.0,', 0.0, 'intro')
seg(i_crowd1, 'afade=t=out:st=4.2:d=1.8,', crowd1_start, 'crowd1')
seg(i_crowd2, 'atrim=0:3.5,volume=0.5,afade=t=out:st=2.5:d=1.0,', crowd2_start, 'crowd2')
seg(i_buzz, '', buzz_start, 'buzz')
seg(i_fail, '', fail_start, 'fail')
seg(i_outro, '', outro_start, 'outro')
und_span = (fail_start + 0.3) - 6.8
seg(i_und, f'atrim=0:{und_span:.2f},volume={und_vol:.4f},afade=t=in:st=0:d=1.5,'
           f'afade=t=out:st={und_span - 2.0:.2f}:d=2.0,', 6.8, 'und')
seg(i_room, f'atrim=0:{total:.2f},volume={room_vol:.4f},afade=t=out:st={total - 3.0:.2f}:d=3.0,', 0.0, 'room')

fc = ';'.join(filters) + ';' + ''.join(f'[{l}]' for l in labels) + \
     f'amix=inputs={len(labels)}:duration=longest:normalize=0[mix]'
raw = os.path.join(BASE, 'mix-raw.wav')
run(['ffmpeg', '-y', '-v', 'error'] + inputs + ['-filter_complex', fc,
     '-map', '[mix]', '-c:a', 'pcm_f32le', raw])
print(f'\nraw mix written: {dur(raw):.2f}s')

# ---- 5. loudnorm two-pass to -16 LUFS ---------------------------------------
r = subprocess.run(['ffmpeg', '-i', raw, '-af',
                    'loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json', '-f', 'null', '-'],
                   capture_output=True, text=True)
m = json.loads(re.search(r'\{\s*"input_i".*?\}', r.stderr, re.S).group(0))
ln = (f"loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
      f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
final = os.path.join(BASE, 'scene-pilot-audio.mp3')
run(['ffmpeg', '-y', '-v', 'error', '-i', raw, '-af', ln, '-c:a', 'libmp3lame', '-b:a', '192k', final])
print(f'final: {final}  duration {dur(final):.2f}s')
print('MEASURED', json.dumps(m))
