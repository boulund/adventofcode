#!/bin/env python3
__author__ = "Fredrik Boulund"
__date__ = "2025-12-04"
""" Advent of Code 2025, day 04"""

from sys import argv, exit

if len(argv) < 2:
    print("usage: 04.py INPUT")
    exit()

with open(argv[1]) as infile:
    grid = []
    grid = [row.strip() for row in infile.readlines()]

#for row in grid:
#    print(row)
movable_rolls = 0
for rowidx, row in enumerate(grid):
    for colidx, location in enumerate(row):
        if location == "@":
            nearby_rolls = -1
            rows = range(max(rowidx-1, 0), min(rowidx+2, len(grid)))
            cols = range(max(colidx-1, 0), min(colidx+2, len(grid)))
            for ridx in rows:
                for cidx in cols:
                    if grid[ridx][cidx] == "@":
                        nearby_rolls += 1
            if nearby_rolls < 4:
                movable_rolls += 1
print(movable_rolls)
