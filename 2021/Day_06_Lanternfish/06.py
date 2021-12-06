#!/usr/bin/env python
"""AdventOfCode Day 6: Lanternfish"""
__author__ = "Fredrik Boulund"
__date__ = "2021-12-06"

from sys import argv, exit
import argparse

import pandas as pd


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("problem_input")

    if len(argv) < 2:
        parser.print_help()
        exit(1)
    
    return parser.parse_args()

def parse_input(input_file):
    with open(input_file) as f:
        values = [int(n) for n in f.readline().strip().split(",")]
        fish = pd.Series(name="Lanternfish", data=values)
    return fish

def simulate(fish):
    older_fish = fish - 1
    mother_fish = older_fish < 0
    baby_fish = pd.Series(8).repeat(mother_fish.sum())
    older_fish = older_fish.append(baby_fish)
    older_fish[older_fish < 0] = 6
    return older_fish
    
if __name__ == "__main__":
    args = parse_args()

    initial_fish = parse_input(args.problem_input)

    days = 80
    fish = initial_fish
    for n in range(days):
        fish = simulate(fish)
    print(fish.shape[0])


    

