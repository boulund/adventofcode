import std.stdio;
import std.conv;
import std.algorithm : group;
import std.algorithm.iteration : sum, splitter, map, each, filter;
import std.algorithm.searching : maxElement, minElement;
import std.algorithm.comparison : max, min;
import std.algorithm.mutation : copy;
import std.math : remainder;
import std.string : split;
import std.array;
import std.file : exists;


auto spreadsheet_rows_checksum(string[] input_lines)
{
    int[] rowdiffs;
    foreach (line; input_lines)
    {
        auto ints_line = line.splitter.map!(to!int).array;
        rowdiffs ~= maxElement(ints_line) - minElement(ints_line);
    }
    return sum(rowdiffs);
}


auto even_row_divisions(string[] input_lines)
{
    int[] rowdivs;
    foreach (line; input_lines)
    {
        auto ints_line = line.splitter.map!(to!int).array;
        foreach (i, i1; ints_line)
        {
            foreach (i2; ints_line[i+1..$])
            {
                auto max_value = to!real(max(i1, i2));
                auto min_value = to!real(min(i1, i2));
                if ( remainder(max_value, min_value) == 0)
                {
                    rowdivs ~= to!int(max_value/min_value);
                    break;
                }
            }
        }
    }
    return sum(rowdivs);
}


int main(string[] argv)
{
    File[] input_files;
    if (argv.length < 2)
    {
        input_files = [File("example_input_1")];
    } 
    else 
    {
        if (exists(argv[1]))
        {
            input_files = [File(argv[1])];
        }
        else
        {
            writeln("No such file: ", argv[1]);
            return 1;
        }
    }

    foreach (input_file; input_files)
    {
        auto input_lines = input_file.byLineCopy.array;
        auto rows_checksum = spreadsheet_rows_checksum(input_lines);
        writeln(rows_checksum);
        auto row_divisions = even_row_divisions(input_lines);
        writeln(row_divisions);
    }

    return 0;
}
