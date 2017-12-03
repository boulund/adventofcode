import std.stdio;
import std.conv;
import std.algorithm : group;
import std.algorithm.iteration : sum, splitter, map, each, filter;
import std.string : split;
import std.array;


unittest{
    int[string] example_input_1 = ["1122": 3,
                                   "1111": 4, 
                                   "1234": 0, 
                                   "91212129": 9];
    foreach (example_string, expected_output; example_input_1)
    {
        auto example_ints = example_string.splitter("").map!(to!int).array;
        assert(sum_adjacent_pairs(example_ints) == expected_output);
    }

    int[string] example_input_2 = ["1212": 6, 
                                   "1221": 0,
                                   "123425": 4,
                                   "123123": 12,
                                   "12131415": 4];
    foreach (example_string, expected_output; example_input_2)
    {
        auto example_ints = example_string.splitter("").map!(to!int).array;
        assert(sum_halfway_pairs(example_ints) == expected_output);
    }
}


auto sum_adjacent_pairs(int[] input_ints)
{
    input_ints ~= input_ints[0];

    int[] to_sum;
    auto pairs = input_ints.group.filter!("a[1] > 1");
    
    foreach (p; pairs)
    {
        for (int n = 1; n < p[1]; n++)
        {
            to_sum ~= p[0];
        }
    }
    return sum(to_sum);
}


auto sum_halfway_pairs(int[] input_ints)
{
    int[] to_sum;
    foreach (i, input_int; input_ints)
    {
        auto lookahead = (i + input_ints.length/2) % input_ints.length; 
        if (input_int == input_ints[lookahead])
        {
            to_sum ~= input_int;
        }
    }
    return sum(to_sum);
}


void main(string[] argv)
{
    foreach (input_string; argv[1..$])
    {
        //write(input_string, ": ");
        auto input_ints = input_string.splitter("").map!(to!int).array;
        auto first_sum = sum_adjacent_pairs(input_ints);
        write(first_sum, " ");
        auto second_sum = sum_halfway_pairs(input_ints);
        writeln(second_sum, " ");
    }
}
