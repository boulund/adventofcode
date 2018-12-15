#!/usr/bin/env python3
# AdventOfCode 2018 Day 04
# Fredrik Boulund 2018

from collections import defaultdict

sorted_guardnotes = sorted(open("input").readlines())

current_guard = None
sleeping_records = defaultdict(lambda: defaultdict(int))
for guardnote in sorted_guardnotes:
    date, time, *note = guardnote.split()
    if note[0].startswith("G"):
        current_guard = int(note[1][1:])
    if note[0].startswith("f"):
        start_sleep = int(time[3:5])
    if note[0].startswith("w"):
        stop_sleep = int(time[3:5])
        for minute in range(start_sleep, stop_sleep):
            sleeping_records[current_guard][minute] += 1

most_sleeping_guards = sorted(((guard, sum(minutes.values())) for guard, minutes in sleeping_records.items()), reverse=True, key=lambda x: x[1])
most_sleeping_guard = most_sleeping_guards[0][0]
guard_sleeping_minutes = sorted(sleeping_records[most_sleeping_guard].items(), key=lambda x: x[0])
most_slept_minute, times_slept = max(guard_sleeping_minutes, key=lambda x: x[1])
print(f"Guard {most_sleeping_guard}: slept most minute {most_slept_minute} ({times_slept} times)")
print(f"Solution 1: {most_sleeping_guard * most_slept_minute}")


most_slept_minutes_per_guard = sorted(((guard, max(minutes.items(), key=lambda x: x[1])) for guard, minutes in sleeping_records.items()), reverse=True, key=lambda x: x[1][1])
print(f"Guard {most_slept_minutes_per_guard[0][0]} most asleep ({most_slept_minutes_per_guard[0][1][1]} times) a specific minute ({most_slept_minutes_per_guard[0][1][0]})")
print(f"Solution 2: {most_slept_minutes_per_guard[0][0] * most_slept_minutes_per_guard[0][1][0]}")

