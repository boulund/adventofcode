#!/usr/bin/env rdmd
// AdventOfCode 2018, Day 01, Fredrik Boulund 2018

import std.stdio, std.conv, std.algorithm;

void main() {
    auto input = File("input");
    auto freq = input
        .byLine
        .map!(to!int)
        .sum;
    writeln(freq);
}
