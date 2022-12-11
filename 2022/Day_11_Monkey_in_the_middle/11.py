#!/usr/bin/env python3
"""Advent of Code 2022 - Day 11: Monkey in the Middle"""
__author__ = "Fredrik Boulund"
__date__ = "2022-12-11"

from sys import argv, exit
from itertools import zip_longest
from functools import reduce

def grouper(iterable, n):
    args = [iter(iterable)] * n
    return zip_longest(*args)

if len(argv) < 2:
    print("usage: 11.py INPUT")
    exit(1)


class Monkey():
    def __init__(self, items, operation, test_value, dest_true, dest_false):
        self.items = items
        self.op = lambda item: eval(operation)
        self.test = lambda item: not bool(item % test_value)
        self.destination = {True: dest_true, False: dest_false}
        self.inspections = 0
    def inspect(self, item):
        worry = self.op(item)
        self.inspections += 1
        return worry
    def throw(self, item, monkeys):
        destination = self.destination[self.test(item)]
        monkeys[destination].items.append(item)
    def __repr__(self):
        return f"<Monkey: {self.items}, inspections: {self.inspections}>"


def parse_input(notes):
    with open(notes) as f:
        lines = f.readlines()

    monkeys = []
    divisors = []
    for monkey, stats in enumerate(grouper(lines, 7)):
        items = [int(i.strip()) for i in stats[1].split(":")[1].split(",")]
        operation = stats[2].split("=")[1].strip().replace("old", "item")
        test_value = int(stats[3].split()[-1])
        dest_true = int(stats[4].split()[-1])
        dest_false = int(stats[5].split()[-1])
        monkeys.append(Monkey(items, operation, test_value, dest_true, dest_false))
        divisors.append(test_value)
    return monkeys, divisors

def monkey_around(monkeys, rounds=20, worry_reduction=False):
    for round_ in range(rounds):
        for monkey in monkeys:
            for idx, item in enumerate(monkey.items):
                if worry_reduction:
                    monkey.items[idx] = int(monkey.inspect(item) % worry_reduction)
                else:
                    monkey.items[idx] = int(monkey.inspect(item) // 3)
                monkey.throw(monkey.items[idx], monkeys)
            monkey.items = []  # All items thrown

monkeys, divisors = parse_input(argv[1])

monkey_around(monkeys, rounds=20)

for monkey in monkeys:
    print(monkey)

sorted_monkeys = sorted(monkeys, reverse=True, key=lambda m: m.inspections)
monkey_business = sorted_monkeys[0].inspections * sorted_monkeys[1].inspections
print(monkey_business)


### PART 2

monkeys, divisors = parse_input(argv[1])

wrf2 = reduce(lambda x,y: x*y, divisors)  # Find common divisor to reduce size of item values
monkey_around(monkeys, rounds=10000, worry_reduction=wrf2)

for monkey in monkeys:
    print(monkey)

sorted_monkeys = sorted(monkeys, reverse=True, key=lambda m: m.inspections)
monkey_business = sorted_monkeys[0].inspections * sorted_monkeys[1].inspections
print(monkey_business)
