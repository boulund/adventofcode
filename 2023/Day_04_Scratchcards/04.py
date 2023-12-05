#!/usr/bin/env python3
"""AdventOfCode 2023: Day 04 - Scratchcards"""
__author__ = "Fredrik Boulund"
__date__ = "2023"

from sys import argv, exit
from math import floor
from collections import defaultdict

if len(argv) < 2:
    print("usage: 04.py INPUT")
    exit(1)

cards = []

with open(argv[1]) as f:
    for line in f:
        card_n, data = line.split(":")
        draw, winning = data.split("|")
        draw = set(draw.split())
        winning = set(winning.split())
        cards.append((draw, winning))

def score_draw(draw, winning):
    intersection = draw.intersection(winning)
    return floor(2**(len(intersection)-1)), len(intersection)

scores = []
winnings = []
total_cards = defaultdict(int)
for idx, numbers in enumerate(cards, start=1):
    score, num = score_draw(*numbers)
    scores.append(score)
    winnings.append(num)
    total_cards[idx] += 1
print(sum(scores))

for idx, num in enumerate(winnings, start=1):
    for card in range(idx+1, idx+1+num):
        total_cards[card] += total_cards[idx]
print(sum(total_cards.values()))

