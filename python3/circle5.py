from math import sin, cos, pi

MajorCircle = ['C',     'G',  'D',  'A',  'E',  'B',
               'Gb/F#', 'Db', 'Ab', 'Eb', 'Bb', 'F']
MinorCircle = ['a',     'e',  'b',  'f#', 'c#', 'g#',
               'eb/d#', 'bb', 'f',  'c',  'g',  'd']

MajorRadius = 18
MinorRadius = 13

blank_row = [' ' for _ in range(48)]
array = [blank_row.copy() for _ in range(19)]


if __name__ == "__main__":
    for i, key in enumerate(MajorCircle):
        x = int((MajorRadius*cos(i*pi/6 - pi/2) + MajorRadius))
        y = int((MajorRadius*sin(i*pi/6 - pi/2) + MajorRadius)/2)
        for j, character in enumerate(key):
            array[y][x + j] = character

    for i, key in enumerate(MinorCircle):
        x = int((MinorRadius*cos(i*pi/6 - pi/2) + MajorRadius))
        y = int((MinorRadius*sin(i*pi/6 - pi/2) + MajorRadius)/2)
        for j, character in enumerate(key):
            array[y][x + j] = character

    for row in array:
        print(''.join(row))
