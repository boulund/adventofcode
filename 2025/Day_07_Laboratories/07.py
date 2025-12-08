#!/bin/env python3
__author__ = "Fredrik Boulund"
__date__ = "2025-12-07"
""" Advent of Code 2025, day 07"""

from sys import argv, exit

if len(argv) < 2:
    print("usage: 07.py INPUT")
    exit()

rows = [r.strip() for r in open(argv[1]).readlines()]

beams = [False for b in rows[0]]
timelines = [0 for b in rows[0]]
splitcount = 0
for row in rows:
    for idx, col in enumerate(row):
        if col == "S":
            beams[idx] = True
            timelines[idx] = 1
        elif col == "^" and beams[idx]:
            beams[idx] = False
            beams[max(idx-1, 0)] = True
            beams[min(idx+1, len(beams))] = True
            splitcount += 1
            timelines[idx-1] += timelines[idx]
            timelines[idx+1] += timelines[idx]
            timelines[idx] = 0
print(splitcount)
print(sum(timelines))

