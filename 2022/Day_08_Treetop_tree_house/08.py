#!/usr/bin/env python3
"""Advent of Code 2022 - Day 08: Treetop Tree House"""
__author__ = "Fredrik Boulund"
__date__ = "2022-12-08"

from sys import argv, exit
import pandas as pd

if len(argv) < 2:
    print("usage: 08.py INPUT")
    exit(1)

df = pd.read_csv(argv[1], header=None, dtype=str)[0].str.split("", expand=True)
# Remove outer leftmost and rightmost columns due to strange 
# expansion behavior with zero-length splitting string
df = df[df.columns[1:-1]] 

#print(df)
#print(df.shape)

visible = 2*(df.shape[0] + df.shape[1])-4  # Outer rim
for col in df.columns[1:-1]:
    for row in list(df.index)[1:-1]:
        tree_height = df[col].loc[row]
        col_lower = df[col] < tree_height
        row_lower = df.loc[row] < tree_height
        up = all(col_lower[:row])
        down = all(col_lower[row+1:])
        left = all(row_lower[:col-1])
        right = all(row_lower[col:])
        if any([up, down, left, right]):
            #print(row, col, tree_height, "is visible")
            visible += 1

print(visible)


