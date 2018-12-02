#!/usr/bin/env python3
# AdventOfCode 2018 Day 02
# Fredrik Boulund 2018

from collections import Counter
from itertools import product

box_ids = [line.strip() for line in open("input").readlines()]
letter_counts = [Counter(box_id.strip()) for box_id in box_ids]
counts_of_counts = [Counter(letter_counts_.values()) for letter_counts_ in letter_counts]

twos, threes = 0, 0
for counts in counts_of_counts:
    if counts[2] > 0:
        twos += 1
    if counts[3] > 0:
        threes += 1
print(f"Solution 1: {twos*threes}")


def hamming_distance(s1, s2):
    return sum(0 if c1 == c2 else 1 for c1, c2 in zip(s1, s2))

hamming_distances = ((box1, box2, hamming_distance(box1, box2)) for box1, box2 in product(box_ids, repeat=2))
for box1, box2, hdist in hamming_distances:
    if hdist == 1:
        print(f"Solution 2: {''.join(c1 for c1, c2 in zip(box1, box2) if c1 == c2)}")
        print(f"{'':12}Boxes:\n{'':12}{box1}\n{'':12}{box2}")
        break

