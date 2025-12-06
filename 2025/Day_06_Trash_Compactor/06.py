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

with open(argv[1]) as infile:
    rows = [list(row.strip("\n")) for row in infile.readlines()]
df2 = pd.DataFrame(rows)
#print(df2)
running_total = []
grand_total = 0
for col in df2.columns[::-1]:
    number = "".join(list(df2[col])[:-1]).strip()
    if number:
        running_total.append(int(number))
    func = df2[col].iloc[-1]
    if func == "+":
        grand_total += pd.Series(running_total).sum()
        running_total = []
    elif func == "*":
        grand_total += pd.Series(running_total).prod()
        running_total = []
print(grand_total)
