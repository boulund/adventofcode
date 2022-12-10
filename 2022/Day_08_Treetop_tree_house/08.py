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

def is_visible(row, col, df):
    tree_height = df[col].loc[row]
    col_lower = df[col] < tree_height
    row_lower = df.loc[row] < tree_height
    up = all(col_lower[:row])
    down = all(col_lower[row+1:])
    left = all(row_lower[:col-1])
    right = all(row_lower[col:])
    if any([up, down, left, right]):
        #print(row, col, tree_height, "is visible")
        return True
    else:
        return False

def scenic_score(row, col, df):
    tree_height = df[col].loc[row]
    col_blocking = list(df[col] >= tree_height)
    row_blocking = list(df.loc[row] >= tree_height)

    def view_distance(viewpath):
        for distance, blocking in enumerate(viewpath, start=1):
            if blocking:
                return distance
        return distance

    up = view_distance(col_blocking[:row][::-1])
    down = view_distance(col_blocking[row+1:])
    left = view_distance(row_blocking[:col-1][::-1])
    right = view_distance(row_blocking[col:])
    scenic_score = up * down * left * right
    return scenic_score


visible = 2*(df.shape[0] + df.shape[1])-4  # Outer rim
scenic_scores = []
for col in df.columns[1:-1]:
    for row in list(df.index)[1:-1]:
        if is_visible(row, col, df):
            visible += 1
        scenic_scores.append(scenic_score(row, col, df))

print(visible)
print(max(scenic_scores))


