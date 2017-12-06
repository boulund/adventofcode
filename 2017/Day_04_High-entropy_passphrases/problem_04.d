import std.stdio;
import std.conv;
import std.algorithm : group;
import std.algorithm.iteration : sum, splitter, map, each, filter;
import std.algorithm.searching : any, all, count;
import std.algorithm.mutation : copy;
import std.algorithm.sorting : sort;
import std.math : remainder;
import std.string : split, representation;
import std.array;
import std.file : exists;


bool valid_passphrase(string[] passphrase)
{
    bool[string] words;
    bool* seen_before;
    foreach (word; passphrase)
    {
        seen_before = (word in words);
        if (seen_before is null)
        {
            words[word] = true;
        } else {
            words[word] = false;
        }
    }
    return all(words.byValue.array);
}


bool valid_passphrase_2(string[] passphrase)
{
    bool[string] words;
    bool* seen_before;
    char[] sorted_word_array;
    string sorted_word;
    write(passphrase, ": ");
    foreach (word; passphrase)
    {
        sorted_word_array = to!(char[])(word.representation); // The plan is to sort this array, but I can't figure out how just now.
        sorted_word = to!string(sorted_word_array);
        seen_before = (sorted_word in words);
        write(sorted_word_array, " ", sorted_word, " ", seen_before, ".");
        if (seen_before is null)
        {
            words[sorted_word] = true;
        } else {
            words[sorted_word] = false;
        }
    }
    writeln();
    return all(words.byValue.array);
}


auto parse_passphrases(string[] lines)
{
    string[][] passphrases;
    foreach (line; lines)
    {
        passphrases ~= line.splitter(" ").array;
    }
    return passphrases;
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
        auto passphrases = parse_passphrases(input_lines);
        int valid_passphrases;
        int valid_passphrases_2;
        foreach (passphrase; passphrases)
        {
            if (passphrase.valid_passphrase)
            {
                valid_passphrases += 1;
            }
            if (passphrase.valid_passphrase_2)
            {
               valid_passphrases_2 += 1;
            }
        }
        writeln(valid_passphrases);
        writeln(valid_passphrases_2);
    }

    return 0;
}
