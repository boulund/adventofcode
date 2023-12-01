#!/usr/bin/env python3
"""AdventOfCode 2023: Day 01"""
__author__ = "Fredrik Boulund"
__date__ = "2023"

from sys import argv, exit

if len(argv) < 2:
    print("usage: 01.py input")
    exit(1)

nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0,
}

all_digits = []
for line in open(argv[1]).readlines():
    digits = []
    for idx, _ in enumerate(line):
        for num, number in nums.items():
            if line[idx:].startswith(num):
                digits.append(number)
        if line[idx].isdigit():
            digits.append(int(line[idx]))
    all_digits.append(digits)

print(sum(int(f"{digit[0]}{digit[-1]}") for digit in all_digits))

