#!/bin/env python3
__author__ = "Fredrik Boulund"
__date__ = "2025-12-08"
""" Advent of Code 2025, day 08"""

from sys import argv, exit
from itertools import combinations
from math import prod

if len(argv) < 2:
    print("usage: 08.py INPUT")
    exit()

jboxes = [tuple(map(int, coords.strip().split(","))) for coords in open(argv[1]).readlines()]

#print(jboxes)
pairs = list(combinations(jboxes, r=2))
#print(len(pairs))

def distance(a, b):
    """Squared distance; no need to sqrt"""
    dist = (a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2
    return dist

circuits = []
distances = {(a,b): distance(a, b) for a, b in pairs}
for num, (pair, dist) in enumerate(sorted(distances.items(), key=lambda x: x[1])):
    #print(pair, dist)
    for circuit in circuits:
        if pair[0] in circuit:
            circuit.add(pair[1])
            break
        elif pair[1] in circuit:
            circuit.add(pair[0])
            break
    else:
        circuits.append(set())
        circuits[-1].add(pair[0])
        circuits[-1].add(pair[1])
    if num == 1000:
        break

#for circuit in sorted(circuits, reverse=True, key=lambda x: len(x)):
#    print(len(circuit), circuit)
print(prod(sorted([len(circuit) for circuit in circuits], reverse=True)[:3]))

