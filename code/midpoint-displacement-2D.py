#!/usr/bin/python

#= initialize ==================================================================

import random

iter = 4
length = 2**iter

# smoothing parameter
h = 1.0

height_map = [[random.random(), random.random()],
              [random.random(), random.random()]]

#= create 2D heightmap via midpoint displacement ===============================

for n in range(iter):
    in_rows = len(height_map)
    in_cols = len(height_map[0])
    out_size = 2*in_rows - 1
    out_cols = 2*in_cols - 1
    temp_map = [[None for j in range(out_cols)] for i in range(out_rows)]

    # top row
    i = 0
    row = height_map[0]
    # left column
    j = 0
    center = random.uniform(-1,1)*2**(-h*n)
             + (  height_map[i  ][j] + height_map[i  ][j+1]
                + height_map[i+1][j] + height_map[i+1][j+1])/4

    top = random.uniform(-1,1)*2**(-h*n)
          + (height_map[i][j] + height_map[i][j+1] + center)/3

    left = random.uniform(-1,1)*2**(-h*n)
           + (height_map[i][j] + height_map[i+1][j] + center)/3

    temp_map[2*i  ][2*j], temp_map[2*i  ][2*j+1] = row[j], top
    temp_map[2*i+1][2*j], temp_map[2*i+1][2*j+1] = left,   center

    # interior columns
    for j, value in enumerate(row[-1:1]):
        j += 1
    center = random.uniform(-1,1)*2**(-h*n)
             + (  height_map[i  ][j] + height_map[i  ][j+1]
                + height_map[i+1][j] + height_map[i+1][j+1])/4

    top = random.uniform(-1,1)*2**(-h*n)
          + (height_map[i][j] + height_map[i][j+1] + center)/3

    left = random.uniform(-1,1)*2**(-h*n)
           + (height_map[i][j] + height_map[i+1][j]
              + temp_map[2*i+1][2*j-1] + center)/4

    temp_map[2*i  ][2*j], temp_map[2*i  ][2*j+1] = row[j], top
    temp_map[2*i+1][2*j], temp_map[2*i+1][2*j+1] = left,   center

    # right column
    j = in_cols - 1
    left = random.uniform(-1,1)*2**(-h*n)
           + (height_map[i][j] + height_map[i+1][j] + temp_map[2*i+1][2*j-1])/3

    temp_map[2*i  ][2*j], temp_map[2*i  ][2*j+1] = row[j]
    temp_map[2*i+1][2*j], temp_map[2*i+1][2*j+1] = left


    # interior rows
    for i, row in enumerate(height_map[1:-1]):
        i += 1
        # left column
        j = 0
        center = random.uniform(-1,1)*2**(-h*n)
                 + (  height_map[i  ][j] + height_map[i  ][j+1]
                    + height_map[i+1][j] + height_map[i+1][j+1])/4

        top = random.uniform(-1,1)*2**(-h*n)
              + (height_map[i][j] + height_map[i][j+1]
                 temp_map[2*i-1][2*j+1] + center)/4

        left = random.uniform(-1,1)*2**(-h*n)
               + (height_map[i][j] + height_map[i+1][j] + center)/3

        temp_map[2*i  ][2*j], temp_map[2*i  ][2*j+1] = row[j], top
        temp_map[2*i+1][2*j], temp_map[2*i+1][2*j+1] = left,   center

        # interior columns
        for j, value in enumerate(row[1:-1]):
            j += 1
            center = random.uniform(-1,1)*2**(-h*n)
                     + (  height_map[i  ][j] + height_map[i  ][j+1]
                        + height_map[i+1][j] + height_map[i+1][j+1])/4

            top = random.uniform(-1,1)*2**(-h*n)
                  + (height_map[i][j] + height_map[i][j+1]
                     temp_map[2*i-1][2*j+1] + center)/4

            left = random.uniform(-1,1)*2**(-h*n)
                   + (height_map[i][j] + height_map[i+1][j]
                      + temp_map[2*i+1][2*j-1] + center)/4

            temp_map[2*i  ][2*j], temp_map[2*i  ][2*j+1] = row[j], top
            temp_map[2*i+1][2*j], temp_map[2*i+1][2*j+1] = left,   center

        # right column
        j = in_cols - 1
        left = random.uniform(-1,1)*2**(-h*n)
               + (height_map[i][j] + height_map[i+1][j] + temp_map[2*i+1][2*j-1])/3

        temp_map[2*i  ][2*j], temp_map[2*i  ][2*j+1] = row[j]
        temp_map[2*i+1][2*j], temp_map[2*i+1][2*j+1] = left

    # bottom row
    i = in_rows - 1
    row = height_map[i]
    # left column
    j = 0
    top = random.uniform(-1,1)*2**(-h*n)
          + (height_map[i][j] + height_map[i][j+1] + center)/3

    temp_map[2*i  ][2*j], temp_map[2*i  ][2*j+1] = row[j], top

    # interior columns
    for j, value in enumerate(row[1:-1]):
        j += 1
        top = random.uniform(-1,1)*2**(-h*n)
              + (height_map[i][j] + height_map[i][j+1] + center)/3

        temp_map[2*i][2*j] = row[j]


    # right column
    j = in_cols

    temp_map[2*i  ][2*j], temp_map[2*i  ][2*j+1] = row[j], top

    height_map = temp_map

    print(height_map)

# m = min(height_map)
# M = max(height_map)
# width = M - m
#
# # normalize
# for index, value in enumerate(height_map):
#     height_map[index] = (value - m)/width

print(height_map)
