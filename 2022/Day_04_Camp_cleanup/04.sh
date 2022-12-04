#!/bin/bash
# AdventOfCode 2022 - Day 04: Camp cleanup
# Fredrik Boulund 2022-12-04

if [ $# -lt 1 ]; then
  echo "usage: 04.sh INPUT"
  exit 1
fi 

contained=0
overlaps=0
while read line || [ -n "$line" ]; do
  e1=${line%,*}
  e1s=${e1%-*}
  e1e=${e1#*-}
  e2=${line#*,}
  e2s=${e2%-*}
  e2e=${e2#*-}
  if ([ $e1s -le $e2s ] && [ $e1e -ge $e2e ]) || ([ $e2s -le $e1s ] && [ $e2e -ge $e1e ]); then
    contained=$((contained + 1))
  fi
  if [ $e1e -le $e2s ]; then
    if [ $e1e -ge $e2s ]; then
      overlaps=$((overlaps + 1))
    fi
  else
    if [ $e2e -ge $e1s ]; then
      overlaps=$((overlaps + 1))
    fi
  fi
done < $1

echo $contained
echo $overlaps