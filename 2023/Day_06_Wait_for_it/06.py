#!/usr/bin/env python3
"""AdventOfCode 2023: Day 06 - Wait for it"""
__author__ = "Fredrik Boulund"
__date__ = "2023"

from sys import argv, exit
from math import prod

if len(argv) < 2:
    print("usage: 06.py INPUT")
    exit(1)

with open(argv[1]) as f:
    times = [int(t) for t in f.readline().split()[1:]]
    distances = [int(d) for d in f.readline().split()[1:]]


def compute_distance(hold_time, max_time):
    travel_time = max_time - hold_time
    distance = hold_time * travel_time
    return distance

wins = []
for max_time, max_distance in zip(times, distances):
    for idx, hold_time in enumerate(range(max_time)):
        if compute_distance(hold_time, max_time) > max_distance:
            wins.append(len(range(0+idx, max_time-idx+1)))
            break
print(prod(wins))

with open(argv[1]) as f:
    time = int(f.readline().strip().replace(" ", "").split(":")[1])
    distance = int(f.readline().strip().replace(" ", "").split(":")[1])

wins = []
for idx, hold_time in enumerate(range(time)):
    if compute_distance(hold_time, time) > distance:
        wins = len(range(0+idx, time-idx+1))
        break
print(wins)
