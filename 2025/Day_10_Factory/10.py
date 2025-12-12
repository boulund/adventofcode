#!/bin/env python3
__author__ = "Fredrik Boulund"
__date__ = "2025-12-10"
""" Advent of Code 2025, day 10"""

from sys import argv, exit

if len(argv) < 2:
    print("usage: 10.py INPUT")
    exit()

machines = []
for line in open(argv[1]):
    lights = set([idx-1 for idx, value in enumerate(line.split(" ")[0]) if value == "#"])
    buttons = [set(map(int, b.strip("()").split(","))) for b in line.split(" ")[1:-1]]
    joltage_requirements = list(map(int, line.strip().split(" ")[-1].strip("{}").split(",")))
    machines.append([lights, buttons, joltage_requirements])

def flatten(items):
    if isinstance(items, list):
        for item in items:
            yield from flatten(item)
    else:
        yield items


def press_buttons(states, buttons):
    new_states = []
    for state in states:
        new_state = []
        for button in buttons:
            new_state.append(state.symmetric_difference(button))
        new_states.append(new_state)
    return set(flatten(new_states))

def search(buttons, lights):
    level = 0
    states = [frozenset()]
    while True:
        level += 1
        states = press_buttons(states, buttons)
        for status_lights in states:
            if status_lights == lights:
                print(f"SUCCESS in {level} button presses")
                return level

button_presses = []
for lights, buttons, joltage_requirements in machines:
    print(lights, buttons)
    button_presses.append(search(buttons, lights))
print(sum(button_presses))



