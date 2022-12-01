#!/usr/bin/env python3
"""Advent Of Code 2022 -- Day 01: Calorie Counting"""
__author__  = "Fredrik Boulund"
__date__ = "2022-12-01"

from sys import argv, exit
from itertools import groupby
from functools import reduce


if __name__ == "__main__":
    if len(argv) < 2:
        print("Need some input!")
        exit(1)

    elves = [list(int(calories) for calories in group) for k, group in groupby(open(argv[1]).readlines(), key=lambda x: bool(x.strip())) if k]
    elven_sums = [sum(elf) for elf in elves]
    print(max(elven_sums))

