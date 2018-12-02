#!/usr/bin/env python3
# AdventOfCode 2018 Day 01
# Fredrik Boulund 2018

freq_changes = [int(change.strip()) for change in open("input").readlines()]
print(sum(freq_changes))


