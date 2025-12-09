#!/bin/env python3
__author__ = "Fredrik Boulund"
__date__ = "2025-12-00"
""" Advent of Code 2025, day 09"""

from sys import argv, exit
from itertools import combinations

if len(argv) < 2:
    print("usage: 09.py INPUT")
    exit()

points = [list(map(int,coordinate.strip().split(","))) for coordinate in open(argv[1])]

max_area = [0, None]
pairs = list(combinations(points, 2))
for pair in pairs:
    x = abs(pair[0][0] - pair[1][0]) + 1
    y = abs(pair[0][1] - pair[1][1]) + 1
    area = x * y
    if area > max_area[0]:
        max_area = [area, pair]
    #print(pair, x, y, x*y)
print(max_area)

