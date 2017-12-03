import std.stdio;
import std.conv;
import std.algorithm : group;
import std.algorithm.iteration : sum, splitter, map, each, filter;
import std.algorithm.searching : maxElement, minElement;
import std.string : split;
import std.array;
import std.file : exists;


auto spreadsheet_rows_checksum(File input_file)
{
    int[] rowdiffs;
    foreach (line; input_file.byLine)
    {
        auto ints_line = line.splitter.map!(to!int).array;
        rowdiffs ~= maxElement(ints_line) - minElement(ints_line);
    }
    return sum(rowdiffs);
}


auto even_row_divisions(File input_file)
{
    int[] rowdivs;
    foreach (line; input_file.byLine)
    {
        auto ints_line = line.splitter.map!(to!int).array;
        // Todo: divide each value with values in array
        // until the divison modulo 2 is 0.
    }
}


int main(string[] argv)
{
    File input_file;
    if (argv.length < 2)
    {
        input_file = File("example_input_1");
    } 
    else 
    {
        if (exists(argv[1]))
        {
            input_file = File(argv[1]);
        }
        else
        {
            writeln("No such file: ", argv[1]);
            return 1;
        }
    }

    auto rows_checksum = spreadsheet_rows_checksum(input_file);
    writeln(rows_checksum);
    return 0;
}
