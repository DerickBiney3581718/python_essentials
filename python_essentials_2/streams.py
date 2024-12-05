import sys
from os import strerror, getcwd, path, sep

# !helps translate exc.errno to err msg
# ! streams preopened and made available to you: stderr, stdin, stdout
dir_path = path.dirname(__file__)
try:
    counter = 0
    stream = open(f'{dir_path}{sep}init.txt', 'rt', encoding='utf-8')
    line = stream.readline()
    while line != '':
        print(line)
        counter += 1
        line = stream.readline()  
    stream.close()
    print('\ntotal characters:', counter)
except IOError as e:
    print(strerror(e.errno))