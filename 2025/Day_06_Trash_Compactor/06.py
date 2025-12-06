#!/bin/env python3
__author__ = "Fredrik Boulund"
__date__ = "2025-12-06"
""" Advent of Code 2025, day 06"""

from sys import argv, exit
import pandas as pd

if len(argv) < 2:
    print("usage: 06.py INPUT")
    exit()

df = pd.read_csv(argv[1], header=None, delimiter="\s+")
df.columns = df.iloc[-1]
df.drop(df.index[-1], inplace=True)
df.rename(columns={"+": "sum", "*":"prod"}, inplace=True)
df = df.apply(pd.to_numeric)
#print(df)
totals = []
for function, col in df.items():
    total = col.apply(func=function)
    totals.append(total)
print(sum(totals))

