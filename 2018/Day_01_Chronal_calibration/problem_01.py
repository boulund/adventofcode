#!/usr/bin/env python3
# AdventOfCode 2018 Day 01
# Fredrik Boulund 2018

from itertools import cycle, accumulate

freq_changes = [int(change.strip()) for change in open("input").readlines()]
print(f"Solution 1: {sum(freq_changes)}")

observed_freqs = set()
for freq in accumulate(cycle(freq_changes)):
    if freq in observed_freqs:
        break
    observed_freqs.add(freq)
print(f"Solution 2: {freq}")

