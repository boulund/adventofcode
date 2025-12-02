#!/bin/env python3
__author__ = "Fredrik Boulund"
__date__ = "2025-12-02"
""" Advent of Code 2025, day 02"""

from sys import argv, exit
import re

if len(argv) < 2:
    print("usage: 02.py INPUT")
    exit()

with open(argv[1]) as infile:
    intervals = [interval.split("-") for interval in infile.read().strip().split(",")]

pattern = re.compile(r"(\d+)(\1)")
pattern2 = re.compile(r"(\d+)(\1+)")
invalid_ids = []
invalid_ids_2 = []
for start, end in intervals:
    print(start, end, int(end)-int(start))
    for value in range(int(start), int(end)+1):
        match = re.fullmatch(pattern, str(value))
        if match is not None:
            invalid_ids.append(int(match[0]))
        match2 = re.fullmatch(pattern2, str(value))
        if match2 is not None:
            invalid_ids_2.append(int(match2[0]))


print(sum(invalid_ids))
print(sum(invalid_ids_2))
