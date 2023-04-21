#@fbn776
"""
Python script to convert 'words_alpha.txt' to the given file at `modified_path` based on first character and then on its length.
Each word is categorized based on its first character and then inside this its sorted with based on its length. It is in the format of:
{
    'a': {
        '1': <list of all word that start with `a` and has length `1`>
        '2': <list of all word that start with `a` and has length `12`>
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
modified_path = 'modified-data/first-char-and-length-sort.json'

#`result` has the final converted or organized data;
result = {}
"""
For organizing text file at `source_path` that is delimited by `\n` to a dict (`result`)
with key-value pair as:
    <first-char>: <dict that has key: value pair as <length>: <list of all word starting with given `first-char` and has the given length>>
"""
with open(source_path) as source_file:
    lines = source_file.readlines()
    for i in lines:
        #For removing the newline character at the end;
        i = i.strip()
        first_char = i[0]

        #For root sorting
        if first_char not in result:
            result[first_char] = {}

        #For sorting based on length;
        length = len(i)
        if length not in result[first_char]:
            result[first_char][length] = [i]
        else:
            result[first_char][length].append(i)


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