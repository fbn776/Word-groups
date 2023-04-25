#@fbn776
import json, time

start_time = time.time()
print('Starting...\n')

source_path = 'source-data/words_alpha.txt'

with open(source_path) as source_file:
    lines = source_file.readlines();

    print('No of words =', len(lines))

end_time = time.time()
print(f'Finished task with {round(end_time-start_time, 4)}s')