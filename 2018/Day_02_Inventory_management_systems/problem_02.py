#!/usr/bin/env python3
# AdventOfCode 2018 Day 02
# Fredrik Boulund 2018

from collections import Counter

letter_counts = [Counter(box_id.strip()) for box_id in open("input").readlines()]
counts_of_counts = [Counter(letter_counts_.values()) for letter_counts_ in letter_counts]

twos, threes = 0, 0
for counts in counts_of_counts:
    if counts[2] > 0:
        twos += 1
    if counts[3] > 0:
        threes += 1
print(f"Solution 1: {twos*threes}")
