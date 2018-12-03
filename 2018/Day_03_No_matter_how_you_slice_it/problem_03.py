#!/usr/bin/env python3
# AdventOfCode 2018 Day 03
# Fredrik Boulund 2018

from collections import defaultdict

claimed_positions = defaultdict(int)
with open("input") as f:
    for line in f:
        claim_id, at, corner, size = line.strip().split()
        row, column = map(int, corner.rstrip(":").split(","))
        width, height = map(int, size.split("x"))
        for r_pos in range(row, row+height):
            for c_pos in range(column, column+width):
                claimed_positions[(r_pos, c_pos)] += 1

colliding_positions = filter(lambda x: x[1] > 1, sorted(claimed_positions.items(), reverse=True, key=lambda x: x[1]))
print(len(list(colliding_positions)))
