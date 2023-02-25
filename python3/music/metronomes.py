from math import lcm
from midiutil import MIDIFile


def main(divisors):
    duration = lcm(*divisors)
    file = earmark(divisors)
    for i, d in enumerate(divisors):
        for t in range(duration // d):
            file.addNote(
                track=i,
                channel=0,
                pitch=60 + i,
                time=t*d,
                duration=1,
                volume=127
            )

    write(file, divisors)


def earmark(divisors):
    file = MIDIFile(numTracks=len(divisors),
                    ticks_per_quarternote=960,
                    eventtime_is_ticks=True)
    for i, d in enumerate(divisors):
        file.addTrackName(track=i, time=0, trackName=f"/{d}")
    return file


def write(file, divisors):
    filename = ", ".join(str(d) for d in divisors)
    filename = ".".join([filename, "mid"])
    with open(filename, "wb") as output:
        file.writeFile(output)
        print(f"Wrote to file {filename}.")


if __name__ == "__main__":
    divisors = [8, 9, 10, 11, 12, 13, 14, 15, 16]
    master_divisor = 120
    divisors = [master_divisor * d for d in divisors]
    main(divisors)
