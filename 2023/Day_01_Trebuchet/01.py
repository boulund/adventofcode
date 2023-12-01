#!/usr/bin/env python3
"""AdventOfCode 2023: Day 01"""
__author__ = "Fredrik Boulund"
__date__ = "2023"

from sys import argv, exit

if len(argv) < 2:
    print("usage: 01.py input")
    exit(1)

all_digits = []
for line in open(argv[1]).readlines():
    all_digits.append([d for d in line if d.isdigit()])

print(sum(int(f"{digit[0]}{digit[-1]}") for digit in all_digits))

