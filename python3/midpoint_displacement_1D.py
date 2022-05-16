#!/usr/bin/python

# = initialize ================================================================

import random

iter = 4
length = 2**iter

# smoothing parameter
h = 1.0

height = [random.random(), random.random()]

# = create 1D heightmap via midpoint displacement =============================

for i in range(iter):
    temp_list = []
    for j in range(2**i):
        temp_list.append(height[j])
        temp_list.append((height[j]+height[j+1])/2
                         + random.uniform(-1, 1)*2**(-h*i))
    temp_list.append(height[-1])
    height = temp_list

# normalize
m = min(height)
M = max(height)
width = M - m

for index, value in enumerate(height):
    height[index] = (value - m)/width

print(height)
