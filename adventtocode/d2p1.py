from typing import List
from os import path, sep , strerror

# !levels are all decreasing or all increasing
# !levels are differ 1 -> 3 interval

def get_d2_input()->List[List[int]]:
    try:
        file_path = f"{path.dirname(__file__)}{sep}d2p1.txt"
        with open(file_path, 'rt') as streamInput:
            return [ list(map(int, phr.strip().split(' '))) for phr in streamInput.readlines()]
    except IOError as e:
        print(strerror(e.errno))
        return []
    except Exception as e:
        print(e)
        return []

def is_report_safe(report: List[int])->int:
    num_of_levels = len(report)
    first_two_levs = report[0] - report[1]

    direction_of_increment, start, stop = (1,0,num_of_levels) if first_two_levs  >= 0 else (-1,num_of_levels - 1,-1)
    
    for lev in range(start,stop,direction_of_increment):
        if (lev + direction_of_increment) >= num_of_levels or (lev + direction_of_increment) < 0:
            break
        
        lev_diff = report[lev] - report[lev + direction_of_increment]
        
        if lev_diff not in range(1,4):
            return False
    return True

def main():
    print(len(list(filter(is_report_safe, get_d2_input()))))
if __name__ == "__main__":
    main()