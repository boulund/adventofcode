import std.stdio;
import std.conv;
import std.algorithm : group;
import std.algorithm.iteration : sum, splitter, map, each, filter;
import std.algorithm.searching : maxElement, minElement;
import std.string : split;
import std.array;
import std.file : exists;


unittest{
    int[string] example_input_1 = ["5 1 9 5\n7 5 3\n2 4 6 8": 18];
    foreach (example_string, expected_output; example_input_1)
    {
    }

}


auto spreadsheet_rows_checksum(int[][] input_ints)
{
    input_ints ~= input_ints[0];
}


int main(string[] argv)
{
    File input_file;
    if (argv.length < 2)
    {
        input_file = File("example_sheet.txt");
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

    int[] rowdiffs;
    foreach (line; input_file.byLine)
    {
        auto ints_line = line.splitter.map!(to!int).array;
        rowdiffs ~= maxElement(ints_line) - minElement(ints_line);
    }
    writeln(sum(rowdiffs));
    return 0;
}
