#!/usr/bin/env python3
"""AdventOfCode 2023: Day 06 - Wait for it"""
__author__ = "Fredrik Boulund"
__date__ = "2023"

from sys import argv, exit
from math import prod, sqrt, ceil, floor

if len(argv) < 2:
    print("usage: 06.py INPUT")
    exit(1)

with open(argv[1]) as f:
    times = [int(t) for t in f.readline().split()[1:]]
    distances = [int(d) for d in f.readline().split()[1:]]


def compute_winning_interval(max_time, distance):
    T = max_time/2
    s = sqrt(T**2 - distance)
    t1 = T - s
    t2 = T + s
    print(t1, t2)
    return int(t2) - int(t1)

wins = []
for max_time, max_distance in zip(times, distances):
    print(compute_winning_interval(max_time, max_distance))
#print(prod(wins))
#
#time = int("".join(str(t) for t in times))
#distance = int("".join(str(d) for d in distances))
#
#wins = []
#for idx, hold_time in enumerate(range(time)):
#    if compute_distance(hold_time, time) > distance:
#        wins = len(range(0+idx, time-idx+1))
#        break
#print(wins)
