#!/usr/bin/env python
"""AdventOfCode Day 3: Binary Diagnostic"""
__author__ = "Fredrik Boulund"
__date__ = "2021-12-03"

from sys import argv, exit
from collections import Counter, defaultdict
import argparse

INVERT_BINARY = str.maketrans("01", "10")

def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("problem_input")

    if len(argv) < 2:
        parser.print_help()
        exit(1)
    
    return parser.parse_args()

def parse_input(input_file):
    with open(input_file) as f:
        for line in f:
            yield line.strip()

def count_bits(problem_input):
    counters = defaultdict(Counter)
    for line in problem_input:
        for pos, value in enumerate(line):
            counters[pos][value] += 1
    return counters

def compute_rate(bit_counts):
    binary_rate = "".join(
        str(counts.most_common()[0][0]) 
        for counts in bit_counts.values()
    )
    return binary_rate

def filter_numbers(numbers, co2_rating=True):
    bitlength = len(numbers[0])
    for pos in range(bitlength):
        numbers = filter_on_pos(numbers, pos, co2_rating)
        if len(numbers) == 1:
            return numbers.pop()

def filter_on_pos(numbers, pos, co2_rating):
    new_set = set()
    bit_counts = count_bits(numbers)[pos]
    if co2_rating:
        most_common = bit_counts.most_common()[0][0]
    else:
        most_common = bit_counts.most_common()[-1][0]
    if (bit_counts["0"] == bit_counts["1"]):
        most_common = "1" if co2_rating else "0"
    for num in numbers:
        if num[pos] == most_common:
            new_set.add(num)
    return new_set


if __name__ == "__main__":
    args = parse_args()

    problem_input = list(parse_input(args.problem_input))

    bit_counts = count_bits(problem_input)

    binary_gamma_rate = compute_rate(bit_counts)
    binary_epsilon_rate = compute_rate(bit_counts).translate(INVERT_BINARY)
    power_consumption = int(binary_gamma_rate, 2) * int(binary_epsilon_rate, 2)
    print(power_consumption)

    CO2_rating = filter_numbers(problem_input)
    O2_rating = filter_numbers(problem_input, co2_rating=False)
    life_support_rating = int(CO2_rating, 2) * int(O2_rating, 2)
    print(life_support_rating)

    


    

