#!/usr/bin/env python3
"""AdventOfCode 2023: Day 2 - Cube conundrum"""
__author__ = "Fredrik Boulund"
__date__ = "2023"

from sys import argv, exit
from collections import defaultdict

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

def is_impossible(game):
    cubes = {"red": 12, "green": 13, "blue": 14}
    for _set in game:
        for color, num in _set.items():
            if cubes[color] < num:
                return True
    return False

possible = []
for game_no, game in games.items():
    if not is_impossible(game):
        possible.append(game_no)
print(sum(possible))
