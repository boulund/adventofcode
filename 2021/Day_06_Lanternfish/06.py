#!/usr/bin/env python
"""AdventOfCode Day 6: Lanternfish"""
__author__ = "Fredrik Boulund"
__date__ = "2021-12-06"

from sys import argv, exit
from collections import defaultdict
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("problem_input")

    if len(argv) < 2:
        parser.print_help()
        exit(1)
    
    return parser.parse_args()

def parse_input(input_file):
    fish = defaultdict(int)
    with open(input_file) as f:
        for value in f.readline().strip().split(","):
            fish[int(value)] += 1
    return fish

def simulate(fish):
    older_fish = defaultdict(int)
    for age in fish:
        if age-1 < 0:
            # One new fish for every fish of age 0
            older_fish[8] += fish[age] 
            # Restore age of fish that multiplied
            older_fish[6] += fish[age]
        else:
            older_fish[age-1] += fish[age]
    return older_fish
    
if __name__ == "__main__":
    args = parse_args()

    initial_fish = parse_input(args.problem_input)

    days = 80
    fish = initial_fish
    for n in range(days):
        fish = simulate(fish)
    print(sum(fish.values()))

    days = 256
    fish = initial_fish
    for n in range(days):
        fish = simulate(fish)
    print(sum(fish.values()))

    

