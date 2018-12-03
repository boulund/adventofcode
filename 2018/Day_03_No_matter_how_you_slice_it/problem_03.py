#!/usr/bin/env python3
# AdventOfCode 2018 Day 03
# Fredrik Boulund 2018

from collections import defaultdict

claims = []
claimed_positions = defaultdict(int)
with open("input") as f:
    for line in f:
        claim_id, at, corner, size = line.strip().split()
        row, column = map(int, corner.rstrip(":").split(","))
        width, height = map(int, size.split("x"))
        claims.append((claim_id, row, column, width, height))
        for r_pos in range(row, row+width):
            for c_pos in range(column, column+height):
                claimed_positions[(r_pos, c_pos)] += 1
                 
colliding_positions = filter(lambda x: x[1] > 1, sorted(claimed_positions.items(), reverse=True, key=lambda x: x[1]))
print(f"Solution 1: {len(list(colliding_positions))}")

uncontested_claim = -1
for claim_id, row, column, width, height in claims:
    max_for_claim = max(claimed_positions[r, c] for r in range(row, row+width) for c in range(column,column+height))
    if max_for_claim == 1:
        print(claim_id, max_for_claim) 


