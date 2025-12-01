#!/bin/env python3
__author__ = "Fredrik Boulund"
__date__ = "2025-12-01"
""" Advent of Code 2025, day 01"""

from sys import argv, exit

if len(argv) < 2:
    print("usage: 01.py INPUT")
    exit()

with open(argv[1]) as infile:
    sequence = [rotation.strip() for rotation in infile.readlines()]

dial = list(range(0,100))
current_pos = 50
zero_count = 0
for rot in sequence:
    direction, value = rot[0], int(rot[1:])
    if direction == "L":
        current_pos = dial[(current_pos - value) % 100]
    else:
        current_pos = dial[(current_pos + value) % 100]
    if current_pos == 0:
        zero_count += 1
    print(current_pos)
print("Zero count:", zero_count)
