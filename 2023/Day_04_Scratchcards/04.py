#!/usr/bin/env python3
"""AdventOfCode 2023: Day 04 - Scratchcards"""
__author__ = "Fredrik Boulund"
__date__ = "2023"

from sys import argv, exit
from math import floor

if len(argv) < 2:
    print("usage: 04.py INPUT")
    exit(1)

cards = {}

with open(argv[1]) as f:
    for line in f:
        card_n, data = line.split(":")
        card = card_n.split()[1]
        draw, winning = data.split("|")
        draw = set(draw.split())
        winning = set(winning.split())
        cards[card] = (draw, winning)

def score(draw, winning):
    intersection = draw.intersection(winning)
    return floor(2**(len(intersection)-1))

scores = []
for card, data in cards.items():
    scores.append(score(*data))
print(sum(scores))
