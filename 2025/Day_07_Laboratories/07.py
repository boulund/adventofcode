#!/bin/env python3
__author__ = "Fredrik Boulund"
__date__ = "2025-12-07"
""" Advent of Code 2025, day 07"""

from sys import argv, exit
from math import prod
import pandas as pd

if len(argv) < 2:
    print("usage: 07.py INPUT")
    exit()

rows = [r.strip() for r in open(argv[1]).readlines()]

beams = [False for b in rows[0]]
splitcount = 0
for row in rows:
    for idx, col in enumerate(row):
        if col == "S":
            beams[idx] = True
        elif col == "^" and beams[idx]:
            beams[idx] = False
            beams[max(idx-1, 0)] = True
            beams[min(idx+1, len(beams))] = True
            splitcount += 1
print(splitcount)

