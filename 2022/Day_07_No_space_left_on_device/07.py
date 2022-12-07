#!/usr/bin/env python3
"""AdventOfCode 2022 - Day 07: No space left on device"""
__author__ = "Fredrik Boulund"
__date__ = "2022-12-07"

from sys import argv, exit

if len(argv) < 2:
    print("usage: 07.py INPUT")
    exit(1)

root = {"name": "/", "type": "d", "size": 0, "children": [], "parent": {}}

in_listing = False
with open(argv[1]) as f:
    cwd = root
    for line in f.readlines()[1:]:
        if line.startswith("$ cd"):
            _, _, name = line.strip().split()
            if name == "..":
                cwd = cwd["parent"]
            elif name == "/":
                cwd = root
            else:
                new_dir = {"name": name, "type": "d", "size": 0, "children": [], "parent": cwd}
                cwd["children"].append(new_dir)
                cwd = new_dir
        elif line.startswith("$ ls"):
            in_listing = True
        elif in_listing:
            ts, name = line.strip().split()
            if ts != "dir":
                new_file = {"name": name, "type": "f", "size": int(ts), "children": None, "parent": cwd}
                cwd["children"].append(new_file)
                

def calculate_node_totals(node, l=0):
    #print(f"{'  '*l}{node['name']} {node['type']} {node['size']}")
    if node["children"]:
        for c in node["children"]:
            size = calculate_node_totals(c, l=l+1)
            node["size"] += size
    return node["size"]

calculate_node_totals(root)
#print(root["size"])

def get_dir_sizes(node):
    node_sizes = {}
    if node["children"]:
        for c in node["children"]:
            node_sizes = {**node_sizes, **get_dir_sizes(c)}
    if node["type"] == "d":
        node_sizes[f"{node['parent'].get('name')}/{node['name']}"] = node["size"]
    return node_sizes

dir_sizes = dict(sorted(get_dir_sizes(root).items(), key=lambda item: item[1]))

required_space = 3e7
consumed_space = 7e7 - list(dir_sizes.values())[-1]
total = 0
for dirname, size in dir_sizes.items():
    if size <= 100000:
        total += size
        #print(dirname, size)
    if size > (required_space - consumed_space):
        print(dirname, size)
        break

print(total)
