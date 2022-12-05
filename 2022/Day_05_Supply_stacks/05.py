#!/usr/bin/env python3
"""AdventOfCode - Day 05: Supply stacks"""
__author__ = "Fredrik Boulund"
__date__ = "2022-12-05"

from sys import argv, exit
from copy import deepcopy

if len(argv) < 2:
    print("usage: 05.py INPUT")
    exit(1)

def create_stacks(stack_data):
    stacks = {int(n): [] for n in stack_data[0]}
    for row in stack_data[1:]:
        for n, crate in enumerate(row, start=1):
            if crate != " ":
                stacks[n].append(crate)
    return stacks

def parse_input(infile):
    stack_data = []
    instructions = []
    with open(infile) as f:
        lines = f.readlines()
        for rownum, line in enumerate(lines):
            if not line.strip():
                break
            stack_data.append(line[1:-1:4])
        for line in lines[rownum+1:]:
            _, num, _, src, _, dest = line.split()
            instructions.append((int(num), int(src), int(dest)))
    return create_stacks(stack_data[::-1]), instructions

def execute(stacks, instructions, step2=False):
    for num, src, dest in instructions:
        if step2:
            crates = []
            for n in range(num):
                crates.append(stacks[src].pop())
            stacks[dest].extend(crates[::-1])
        else:
            for n in range(num):
                stacks[dest].append(stacks[src].pop())
    return stacks


stacks, instructions = parse_input(argv[1])

result = execute(deepcopy(stacks), instructions)
print("".join([l[-1] for s, l in result.items()]))

result2 = execute(stacks, instructions, step2=True)
print("".join([l[-1] for s, l in result2.items()]))
