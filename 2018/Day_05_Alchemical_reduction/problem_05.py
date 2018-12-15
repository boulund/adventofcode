#!/usr/bin/env python3
# AdventOfCode 2018 Day 05
# Fredrik Boulund 2018

polymer = list(open("input").read().strip())

def react(polymer):
    for idx, a in enumerate(polymer[:-1]):
        if a.swapcase() == polymer[idx+1]:
            del polymer[idx:idx+2]
            #react(polymer)
            break

prev_length = len(polymer)
new_length = 0
while prev_length > new_length:
    prev_length = len(polymer)
    react(polymer)
    new_length = len(polymer)

print(len(polymer))

