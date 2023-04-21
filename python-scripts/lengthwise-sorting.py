"""
Python script to convert 'words_alpha.txt' to the given file at `modified_path` based on length of each word.
Each word is categorized based on its length and is stored as a json file as a dict with key: value pair as <length>: <list of all words with this length>
"""
import json, time

start_time = time.time()

print('Starting...\n')

#Path of the text file that contains all the words
source_path = 'source-data/words_alpha.txt'
#File path for the output file
modified_path = 'modified-data/length-wise-sort.json'

#`result` has the final converted or organized data;
result = {}
"""
For organizing text file at `source_path` that is delimited by `\n` to a dict (`result`)
with key-value pair as:
    <length>: <list of words having that length>
"""
with open(source_path) as source_file:
    lines = source_file.readlines()
    for i in lines:
        #For removing the newline character at the end;
        i = i.strip()
        length = len(i)

        if length in result:
            result[length].append(i)
        else:
            result[length] = [i]


#To sort individual lits of each value in the dict `result`
for key in result:
    result[key].sort()

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