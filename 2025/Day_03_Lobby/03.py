#!/bin/env python3
__author__ = "Fredrik Boulund"
__date__ = "2025-12-03"
""" Advent of Code 2025, day 03"""

from sys import argv, exit
from functools import reduce

if len(argv) < 2:
    print("usage: 03.py INPUT")
    exit()

with open(argv[1]) as infile:
    banks = [bank.strip() for bank in infile.readlines()]

max_joltages = []
for bank in banks:
    joltages = [int(joltage) for joltage in bank]
    max1 = joltages.index(max(joltages[:-1]))
    max2 = joltages.index(max(joltages[max1+1:]))
    max_joltage = int(f"{joltages[max1]}{joltages[max2]}")
    max_joltages.append(max_joltage)

print(sum(max_joltages))

all_maxes = []
for bank in banks:
    max_jolts = []
    joltages = [int(joltage) for joltage in bank]
    prev_max = 0
    for pos in range(12):
        range_end = len(joltages)-(11 - len(max_jolts))
        subrange = joltages[prev_max:range_end]
        max_ = subrange.index(max(subrange))
        max_jolts.append(subrange[max_])
        prev_max = prev_max + max_ + 1
    max_joltage = int(reduce(lambda x, y: str(x)+str(y), max_jolts))
    all_maxes.append(max_joltage)

print(sum(all_maxes))

