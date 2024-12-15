from typing import List, Tuple, Dict
from os import path, strerror

def get_d5()->(List[Tuple[int]], List[str]):
    file_path =path.join(path.dirname(__file__), 'd5test.txt')
    rules = []
    pages = []
    try:
        with open(file_path, 'rt') as stream:
            jump = False
            for line in stream:
                if line.strip('\n') == '':
                    jump = True
                    continue
                if jump:
                    pages.append(tuple(map(int , line.strip('\n').split(','))))
                else:
                    rules.append(tuple(map(int , line.strip('\n').split('|'))))

    except IOError as exc:
        print(strerror(exc.errno))
    except Exception as e:
        print('Unexpected error', e)
    return create_lookup_table(rules), pages

def create_lookup_table(rules):
    rules_table = dict()
    for page_x, page_y in rules:
        rules_table[page_y].append(page_x)  if rules_table.get(page_y) else rules_table.setdefault(page_y, [page_x])
    return rules_table
    
def sum_correct_pages_mid(rules:Dict[int, List[int]], manuals:List[List[int]]):
    mid_sum = 0
    for man in manuals:
        for i,page in enumerate(man):
            if not is_page_order_correct(rules.get(page, []), man[i + 1:]): #check that no dependencies come after this page
                break 
        else:
            print('man mid .. ',len(man) , (len(man) // 2) )
            mid_sum += man[(len(man) // 2)]
    return mid_sum

def is_page_order_correct(dep_list, rem_pages):
    return all([ dep not in rem_pages for dep in dep_list])
    

def main():
    rules, manuals = get_d5()
    print('rules', rules)
    print('manuals', manuals)
    print('mid sum', sum_correct_pages_mid(rules, manuals))
    
if __name__ == "__main__":
    main()
    
    # 4649 too low