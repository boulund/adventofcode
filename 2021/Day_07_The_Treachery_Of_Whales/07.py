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

def compute_fuel_consumption(positions, target_pos):
    required_fuel = [int(np.abs(pos - target_pos)) for pos in positions]
    return required_fuel
    
if __name__ == "__main__":
    args = parse_args()

    positions = parse_input(args.problem_input)

    target_pos = np.median(positions)
    print(sum(compute_fuel_consumption(positions, target_pos)))





    

