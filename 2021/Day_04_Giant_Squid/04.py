#!/usr/bin/env python
"""AdventOfCode Day 4: Giant Squid"""
__author__ = "Fredrik Boulund"
__date__ = "2021-12-04"

from sys import argv, exit
from itertools import repeat
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
        numbers = [int(n) for n in f.readline().strip().split(",")]
        boards = pd.read_csv(f, delim_whitespace=True, header=None)
        num_boards = int(boards.shape[0] / 5)
        boards_index = [f"Board{n}" 
            for n in range(num_boards)
            for row in range(5)
        ]
        boards.index = boards_index
    return numbers, boards, num_boards
    
def play_bingo(numbers, boards, num_boards):
    for round, _ in enumerate(numbers, start=5):
        drawn = numbers[:round]
        for board_number in range(num_boards):
            bingo = check_for_bingo(drawn, boards.loc[f"Board{board_number}"])
            if bingo:
                return bingo
    return "NO BINGO"

def check_for_bingo(drawn_numbers, board):
    for idx in range(5):
        if all(board.iloc[idx].isin(drawn_numbers)):
            score = compute_bingo_score(drawn_numbers, board)
            return f"{board.index[0]} Row {idx}, score: {score}"
        if all(board.iloc[:,idx].isin(drawn_numbers)):
            score = compute_bingo_score(drawn_numbers, board)
            return f"{board.index[0]} Column {idx}, score: {score}"

def compute_bingo_score(drawn_numbers, board):
    last_number = drawn_numbers[-1]
    sum_unmarked = int(board[~board.isin(drawn_numbers)].sum().sum())
    return sum_unmarked * last_number

if __name__ == "__main__":
    args = parse_args()

    numbers, boards, num_boards = parse_input(args.problem_input)
    bingo = play_bingo(numbers, boards, num_boards)
    print(bingo)



    

