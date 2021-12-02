#!/usr/bin/env python
"""AdventOfCode Day 2: Dive!"""
__author__ = "Fredrik Boulund"
__date__ = "2021-12-02"

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
        problem_input = [line.strip().split() for line in f.readlines()]
    return [(direction, int(distance)) for direction, distance in problem_input]

class Submarine():
    def __init__(self):
        self.depth = 0
        self.horizontal_pos = 0
        self.aim = 0
    
    def process_moves(self, moves):
        for direction, distance in moves:
            if direction == "down":
                self.depth += distance
            elif direction == "up":
                self.depth -= distance
            elif direction == "forward":
                self.horizontal_pos += distance
    
    def aim_and_move(self, moves):
        for direction, distance in moves:
            if direction == "down":
                self.aim += distance
            elif direction == "up":
                self.aim -= distance
            elif direction == "forward":
                self.horizontal_pos += distance
                self.depth += (self.aim * distance)


if __name__ == "__main__":
    args = parse_args()

    problem_input = parse_input(args.problem_input)
    submarine = Submarine()
    submarine.process_moves(problem_input)
    print(submarine.depth * submarine.horizontal_pos)

    submarine.__init__()
    submarine.aim_and_move(problem_input)
    print(submarine.depth * submarine.horizontal_pos)

    

