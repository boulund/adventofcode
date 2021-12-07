#!/usr/bin/env python
"""AdventOfCode Day 7: The Treachery of Whales"""
__author__ = "Fredrik Boulund"
__date__ = "2021-12-07"

from sys import argv, exit
import argparse

import numpy as np

def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("problem_input")

    if len(argv) < 2:
        parser.print_help()
        exit(1)
    
    return parser.parse_args()

def parse_input(input_file):
    with open(input_file) as f:
        positions = [int(n) for n in f.readline().strip().split(",")]
    return positions

def compute_steps(positions, target_pos):
    required_steps = [int(np.abs(pos - target_pos)) for pos in positions]
    return required_steps

def compute_weighted_fuel_requirement(positions, target_pos):
    required_steps = compute_steps(positions, target_pos)
    required_fuel = [np.add.reduce(range(n+1)) for n in required_steps]
    return int(sum(required_fuel))

    
if __name__ == "__main__":
    args = parse_args()

    positions = parse_input(args.problem_input)

    target_pos = int(np.median(positions))
    required_fuel = sum(compute_steps(positions, target_pos))
    print(required_fuel)

    weighted_target_pos = int(np.round(np.mean(positions)))
    reqs = []
    for tpos in np.arange(max(weighted_target_pos-100, 0), weighted_target_pos+100):
        reqs.append(compute_weighted_fuel_requirement(positions, tpos))
    print(reqs.index(min(reqs)), min(reqs))

    weighted_fuel_requirement = compute_weighted_fuel_requirement(positions, weighted_target_pos)
    print(weighted_target_pos, weighted_fuel_requirement)




    

