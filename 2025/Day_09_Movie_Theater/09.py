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


x_points = {p[1]: set() for p in points}
y_points = {p[0]: set() for p in points}
for x, y in points:
    y_points[x].add(y)
    x_points[y].add(x)

max_area2 = [0, None]
for point in points:
    min_x = min(x_points[point[1]])
    max_x = max(x_points[point[1]])
    min_y = min(y_points[point[0]])
    max_y = max(y_points[point[0]])
    if point[0] == min_x and point[1] == min_y:
        # point is Top left corner
        opposite_y = max(y_points[min_x])
        opposite_x = max(x_points[opposite_y])
        print("", point, opposite_x, opposite_y)
    elif point[0] == min_x and point[1] == max_y:
        # point is Top right corner
        opposite_y = min(y_points[min_x])
        opposite_x = min(x_points[opposite_y])
        print("", point, opposite_x, opposite_y)
    else:
        continue
    x = abs(point[0] - opposite_x) + 1
    y = abs(point[1] - opposite_y) + 1
    area = x * y
    if area > max_area2[0]:
        max_area2 = [area, point, [opposite_x, opposite_y]]

print(max_area2)
     


