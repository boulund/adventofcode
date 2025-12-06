#!/bin/env python3
__author__ = "Fredrik Boulund"
__date__ = "2025-12-05"
""" Advent of Code 2025, day 05"""

from sys import argv, exit
from collections import deque

if len(argv) < 2:
    print("usage: 05.py INPUT")
    exit()

with open(argv[1]) as infile:
    ranges = []
    ingredients = []
    for line in infile:
        try:
            start, stop = line.strip().split("-")
            ranges.append((int(start),int(stop)))
        except ValueError as e:
            if line.strip():
                ingredients.append(int(line.strip()))
#print(ranges, ingredients)

fresh_ingredients = set()
for ingredient in ingredients:
    for start, end in ranges:
        if ingredient >= start and ingredient <= end:
            fresh_ingredients.add(ingredient)

print(len(fresh_ingredients))#, fresh_ingredients)

ranges = sorted(ranges)
lefts = [a[0] for a in ranges]
rights = [a[1] for a in ranges]
overlaps = [(l-r) < 0 for l, r in zip(lefts[1:], rights[:-1])]
overlaps.append(False) # The last interval never overlaps upwards
print(overlaps)
print(len(overlaps), len(ranges))

total = 0
left = None
for overlap, interval in zip(overlaps, ranges):
    #print(overlap, interval, total)
    if overlap:
        if not left:
            left = interval[0]
            print(f"Starting new interval from {left}")
        else:
            print("Continuing", interval)
    else:
        if left:
            total += interval[1] - left + 1
            print(f"Closing ({left}, {interval[1]})", total)
            left = None
        else:
            total += interval[1] - interval[0] + 1
            print("Singular interval", interval, total)
print(total)

