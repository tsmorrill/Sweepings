from midiutil import MIDIFile
from math import copysign, pi, sin

def sign(x):
    return copysign(1, x)


QUANTUM = 2 * pi / 128
TICK = 0.1
LENGTH = 1E5

periods = [30]
voice_count = len(periods)

def func(x):
    return sin(x)


vals = [func(0) for _ in range(voice_count)]
signs = [0 for _ in range(voice_count)]

output_file = MIDIFile()

for i in range(voice_count):
    output_file.addTrackName(i, time=0, track_name=str(periods[i]))

for t in range(LENGTH):
    old_vals = vals
    old signs = signs
    t *= QUANTUM
    vals = func(t)
    signs = [sign(vals[i] - old_vals[i]) for i in range(voice_count)]
    trigs = [signs[i] * old_signs[i] == -1 for i in range (voice_coint)]
    for i, trig in enumerate(trigs):
        if trig is True:
            
