from math import sin, cos, pi

MajorCircle = ['C', 'G', 'D', 'A', 'E', 'B', 'Gb/F#', 'Db', 'Ab', 'Eb', 'Bb', 'F']
MinorCircle = ['a', 'e', 'b', 'f#', 'c#', 'g#', 'eb/d#', 'bb', 'f', 'c', 'g', 'd']

MajorRadius = 18
MinorRadius = 15

row = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

for i in range(19):
    row[i] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

for i, key in enumerate(MajorCircle):
    x = int((MajorRadius*cos(i*pi/6 - pi/2) + MajorRadius))
    y = int((MajorRadius*sin(i*pi/6 - pi/2) + MajorRadius)/2)
    for j, character in enumerate(key):
        row[y][x + j] = character

for i, key in enumerate(MinorCircle):
    x = int((MinorRadius*cos(i*pi/6 - pi/2) + MajorRadius))
    y = int((MinorRadius*sin(i*pi/6 - pi/2) + MajorRadius)/2)
    for j, character in enumerate(key):
        row[y][x + j] = character

for i in range(19):
    string = ''
    for character in row[i]:
        string += character
    print(string)
