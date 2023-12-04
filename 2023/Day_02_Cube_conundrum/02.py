#!/usr/bin/env python3
"""AdventOfCode 2023: Day 2 - Cube conundrum"""
__author__ = "Fredrik Boulund"
__date__ = "2023"

from sys import argv, exit
from collections import defaultdict
from math import prod

if len(argv) < 2:
    print("usage: 02.py INPUT")
    exit(1)

games = defaultdict(list)
with open(argv[1]) as f:
    for line in f:
        game_no, sets = line.split(":")
        for _set in sets.split(";"):
            counts = {c: int(n) for n, c in (nc.split() for nc in _set.strip().split(", "))}
            games[int(game_no.split()[1])].append(counts)

def possible_power(game):
    impossible = False
    cubes = {"red": 12, "green": 13, "blue": 14}
    colors = defaultdict(int)
    for _set in game:
        for color, num in _set.items():
            if cubes[color] < num:
                impossible = True
            colors[color] = max(colors[color], num)
    return impossible, prod(colors.values())

possible = []
powers = []
for game_no, game in games.items():
    is_impossible, power = possible_power(game)
    if not is_impossible:
        possible.append(game_no)
    powers.append(power)
print(sum(possible))
print(sum(powers))

