import re
from os import path, strerror
def read_d3():
    str_var = ''
    file_path = path.join(path.dirname(__file__), 'd3.txt')
    try:
        with open(file_path, 'rt', encoding='utf-8') as stream_input:
            str_var = stream_input.read()
    except IOError as exc:
        print(strerror(exc.errno))
    except Exception as exc:
        print('Was not io', exc)
    return str_var

def find_all_valid_args(str_var:str)->int:
    pattern = 'mul\((\d*,\d*)\)'
    list_args = re.findall(pattern, str_var)
    total_sum = 0
    for each_set in list_args:
        [int1, int2] = each_set.split(',')
        total_sum += int(int1) * int(int2)
    return total_sum

def main():
    str_var = read_d3()
    print(find_all_valid_args(str_var))
    
if __name__=='__main__':
    main()