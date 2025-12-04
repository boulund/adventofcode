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
exactly_zero = 0
zero_count = 0
for rotation in sequence:
    direction, value = rotation[0], int(rotation[1:])
    full_rotations = value // 100
    zero_count += full_rotations
    value = value % 100  # Remainder after full rotations
    if direction == "L":
        new_pos = current_pos - value
        if current_pos != 0 and new_pos <= 0: 
            zero_count += 1
        current_pos = dial[new_pos % 100]
    else:
        new_pos = current_pos + value
        current_pos = dial[new_pos % 100]
        if new_pos >= 100:
            zero_count += 1
    if current_pos == 0:
        exactly_zero += 1
    #print(rotation, current_pos, zero_count)

print("Exactly zero count:", exactly_zero)
print("Passing zero count:", zero_count)
