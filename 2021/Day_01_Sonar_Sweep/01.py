#!/usr/bin/env python
"""AdventOfCode Day 1: Sonar Sweep"""
__author__ = "Fredrik Boulund"
__date__ = "2021-12-01"

from sys import argv, exit
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("problem_input")

    if len(argv) < 2:
        parser.print_help()
        exit(1)
    
    return parser.parse_args()

def parse_input(input_file):
    with open(input_file) as f:
        problem_input = [int(value.strip()) for value in f.readlines()]
    return problem_input

def count_increases(problem_input):
    return sum([cur - prev > 0 for prev, cur in zip(problem_input, problem_input[1:])])

def sum_triplets(problem_input):
    return [sum(triplet) for triplet in zip(problem_input, problem_input[1:], problem_input[2:])]

if __name__ == "__main__":
    args = parse_args()

    problem_input = parse_input(args.problem_input)
    print(count_increases(problem_input))
    print(count_increases(sum_triplets(problem_input)))

