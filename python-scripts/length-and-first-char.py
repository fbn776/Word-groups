#@fbn776
"""
Python script to convert 'words_alpha.txt' to the given file at `modified_path` based on its length and then on its first character.
Each word is categorized based on its length and then inside this its sorted based on its first character. It is in the format of:
{
    <length>: {
        'a': <list of all word that start with `a` and has the given length>
        'b': <list of all word that start with `a` and has the given length>
        ...
    },...
}
"""

import json, time

start_time = time.time()

print('Starting...\n')

#Path of the text file that contains all the words
source_path = 'source-data/words_alpha.txt'
#File path for the output file
modified_path = 'modified-data/length-and-first-char-sort.json'

#`result` has the final converted or organized data;
result = {}
"""
For organizing text file at `source_path` that is delimited by `\n` to a dict (`result`)
with key-value pair as:
    <length>: <dict that has key: value pair as <first-char>: <list of all word starting with given `first-char` and has the given length>>
"""
with open(source_path) as source_file:
    lines = source_file.readlines()
    for i in lines:
        #For removing the newline character at the end;
        i = i.strip()

        length = len(i)
        #For root sorting
        if length not in result:
            result[length] = {}

        first_char = i[0]
        #For sorting based on first char;
        if first_char not in result[length]:
            result[length][first_char] = [i]
        else:
            result[length][first_char].append(i)


"""
Convert the data in `result` to json and writes this data to the file at `modified_path`
"""
with open(modified_path, 'w') as output:
    print(f'Creating new file at `{modified_path}`\n')
    output_json = json.dumps(result, indent=4, sort_keys=True)
    output.write(output_json)
    print(f'Wrote newly generated data to the file at `{modified_path}`\n')

end_time = time.time()
print(f'Finished task with {round(end_time-start_time, 4)}s')