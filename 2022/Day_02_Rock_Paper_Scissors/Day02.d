#!/usr/bin/env rdmd
// AdventOfCode 2022 - Day 02: Rock Paper Scissors
// Fredrik Boulund 2022-12-02
// Implementation in D (dlang.org)

import std.stdio;

int play_rps(char opponent, char me) 
{
    auto rps_scores = [
        'X': 1,  //Rock
        'Y': 2,  //Paper
        'Z': 3,  //Scissors
    ];
    auto rps_wins = [
        'X': 'C',  //Rock beats Scissors
        'Y': 'A',  //Paper beats Rock
        'Z': 'B',  //Scissors beats Paper
    ];
    auto rps_draws = [
        'X': 'A',
        'Y': 'B',
        'Z': 'C',
    ];

    int score;
    if (opponent == rps_wins[me])
    {
        debug writeln("Win!", opponent, me);
        score = rps_scores[me] + 6;
    }
    else if (opponent == rps_draws[me])
    {
        debug writeln("Draw!", opponent, me);
        score = rps_scores[me] + 3;
    }
    else
    {
        debug writeln("Lost!", opponent, me);
        score = rps_scores[me];
    }
    return score;
}

int main(string[] args)
{
    if (args.length < 2)
    {
        writeln("usage: Day02.d INPUT");
        return 1;
    }

    auto filename = args[1];
    int total_score;
    foreach (line; filename.File.byLine)
    {
        char opponent = line[0], me = line[2];
        total_score += play_rps(opponent, me);

    }
    writeln(total_score);

    return 0;
}
