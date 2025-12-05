#!/bin/env python3
__author__ = "Fredrik Boulund"
__date__ = "2025-12-05"
""" Advent of Code 2025, day 05"""

from sys import argv, exit

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
