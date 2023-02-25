from math import lcm
from midiutil import MIDIFile


def main(divisors, master_divisor):
    track_names = [str(d) for d in divisors]
    divisors = [d for d in divisors]
    duration = lcm(*divisors)
    file = earmark(track_names)
    for i, d in enumerate(divisors):
        for t in range(duration // d):
            file.addNote(
                track=i,
                channel=0,
                pitch=60 + i,
                time=t*d*master_divisor,
                duration=master_divisor,
                volume=127
            )

    write(file, track_names)


def earmark(track_names):
    file = MIDIFile(numTracks=len(track_names),
                    ticks_per_quarternote=960,
                    eventtime_is_ticks=True)
    for i, track_name in enumerate(track_names):
        file.addTrackName(track=i, time=0, trackName=track_name)
    return file


def write(file, track_names):
    filename = ", ".join(track_names)
    filename = ".".join([filename, "mid"])
    with open(filename, "wb") as output:
        file.writeFile(output)
        print(f"Wrote to file {filename}.")


if __name__ == "__main__":
    divisors = [2, 3, 4, 5, 6, 7, 8, 9]
    master_divisor = 240
    main(divisors, master_divisor)
