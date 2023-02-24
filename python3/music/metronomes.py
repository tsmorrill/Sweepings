from datetime import datetime
from midiutil import MIDIFile
from numpy import lcm

def main(bpm, duration):
    file = earmark(bpm)

    LCM = lcm(bpm)
    tick = 60 / LCM
    periods = [LCM // n for n in bpm]
    voices = enumerate(periods)
    duration *= LCM
    
    for t in range(duration):
        for i, period in voices:
            if t % period == 0:
                file.addNote(track=i,
                             channel=0,
                             pitch=60,
                             time=t*tick,
                             duration=tick,
                             volume=127)

    write(file)


def earmark(bpm):
    file = MIDIFile()

    for i, val in enumerate(bpm):
        file.addTrackName(track=i,
                          time=0.0,
                          trackName=str(val))
    
    return file


def write(file):
    dt = datetime.now()
    filename = dt.strftime("%Y-%m-%d_%H%M%S")
    filename = f"{filename}.mid"
    with open(filename, "wb") as output:
        file.writeFile(output)
        print(f"Wrote to file {filename}.")

        
if __name__ == "__main__":
    bpm = [64]
    duration = 120
    main(bpm, duration)
