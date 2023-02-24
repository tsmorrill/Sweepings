from math import lcm
from midiutil import MIDIFile


def main(bpm, duration):
    voices = range(len(bpm))
    period_max = lcm(*bpm)
    tick = 60 / period_max
    periods = [period_max // n for n in bpm]
    rest = [False for i in voices]

    file = earmark(bpm)

    for t in range(duration * period_max):
        triggers = [t % period for period in periods]
        if triggers != rest:
            for i in voices:
                if triggers[i]:
                    file.addNote(
                        track=i,
                        channel=0,
                        pitch=60,
                        time=t * tick,
                        duration=tick,
                        volume=127,
                    )

    write(file, bpm, duration)


def earmark(bpm):
    file = MIDIFile()
    for i, bpm in enumerate(bpm):
        file.addTrackName(track=i, time=0.0, trackName=f"{bpm} bpm")
    return file


def write(file, bpm, duration):
    filename = ", ".join(str(n) for n in bpm)
    filename += f"; {duration} s.mid"
    with open(filename, "wb") as output:
        file.writeFile(output)
        print(f"Wrote to file {filename}.")


if __name__ == "__main__":
    bpm = [64]
    duration = 120
    main(bpm, duration)
