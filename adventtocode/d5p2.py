
#! if dependencies come after like [97,13,75,29,47] -> [97,75,47,29,13]
#! new list = [97,75, 29, 47, 13] -> [97, 75, 47,29, 13]
#! indices list = [0 1 2 3 4 ] -> 
#! second_scan_start : init ind(curr_number) + 1  -> second_scan_end -> ind(second_curr_number| number being check if a dep)
#! move chunk with 
from d5p1 import get_d5, is_page_order_correct
from typing import List, Tuple, Dict

def is_page_a_dependency(dep_list:List[int], page:int)->bool:
    return page in dep_list

def update_positions(curr_ind:int, dep_list: List[int], manual: List[int], positions: List[int]) -> List[int]:
    new_ind = curr_ind
    for ind,page in enumerate(manual[curr_ind + 1: ], start=1):
        # print('before check', page , dep_list)
        if is_page_a_dependency(dep_list, page):
            new_ind = curr_ind + ind
            # print('after check',new_ind, curr_ind )
    u_positions = positions
    if new_ind > curr_ind:
        print('changing', curr_ind, positions[curr_ind], '->', new_ind)
        start,end = positions[curr_ind], positions[new_ind]

        u_positions = [ val - 1 if start <= val <= end else val for val in positions]
        u_positions[curr_ind] = end
        print('updated...', u_positions)
    return u_positions

def sort_manual(manual: List[int], positions: List[int])->List[int]:
    return [page for _,page in sorted(zip(positions, manual))]

def correct_and_sum_mids(rules:Dict[int, List[int]], manuals:List[List[int]]):
    mid_sum = 0
    for man in manuals:
        reshuffle = False
        for i,page in enumerate(man):
            if not is_page_order_correct(rules.get(page, []), man[i + 1:]): #check that no dependencies come after this page
                reshuffle = True
                break
            
        if reshuffle:
            positions = list(range(len(man)))
            print('b',positions , man)
            for i, page in enumerate(man):
                positions = update_positions(i, rules.get(page, []), man, positions)
            man = sort_manual(man, positions)
            
            print('a',positions,man)
            mid_sum += man[(len(man) // 2)]
    return mid_sum

def main():
    rules, manuals = get_d5()
    print('rules', rules)
    print('manuals', manuals)
    print('mid sum', correct_and_sum_mids(rules, manuals))
    
if __name__ == '__main__':
    main()
# 4597 is too low
# 4649 too low