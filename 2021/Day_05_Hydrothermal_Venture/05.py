#!/usr/bin/env python
"""AdventOfCode Day 5: Hydrothermal Venture"""
__author__ = "Fredrik Boulund"
__date__ = "2021-12-05"

from sys import argv, exit
from itertools import chain
import argparse

import numpy as np
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
        lines = []
        for line in f:
            lines.append(
                tuple(tuple(int(v) for v in val.split(",")) 
                for val in line.strip().split(" -> "))
            )
    return lines

def draw_lines(lines):
    max_coordinate = max(chain(*chain(*lines)))
    canvas = pd.DataFrame(
        np.zeros((max_coordinate+1, max_coordinate+1), dtype=np.int)
    )
    for coords in lines:
        start, end = sorted(coords)
        horizontal_line = start[0] == end[0] 
        vertical_line = start[1] == end[1]
        if vertical_line:
            canvas.iloc[start[0]:end[0]+1,start[1]] = canvas.iloc[start[0]:end[0]+1,start[1]].apply(lambda x: x+1)
        if horizontal_line:
            canvas.iloc[start[0],start[1]:end[1]+1] = canvas.iloc[start[0],start[1]:end[1]+1].apply(lambda x: x+1)
    return canvas

def compute_overlaps(canvas, num_overlaps=2):
    overlaps = canvas >= num_overlaps
    return overlaps.sum().sum()

    
if __name__ == "__main__":
    args = parse_args()

    lines = parse_input(args.problem_input)

    canvas = draw_lines(lines)
    overlaps = compute_overlaps(canvas)
    print(overlaps)


    

