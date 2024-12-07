
# !General logic
#! if 'don't' without 'do'  do not catch valid args
#! else catch

# class  init: start of str & matcher for don't().start()
#* match all valid args b/n & set the str[ : don't().start]

# match do().end() & match don't().start 
# *match all valid args in between str[do().end: don't().start]

import re
from d3p1 import find_all_valid_args, read_d3

class SumValidArgs:
    def __init__(self, str_var:str):
        self.str_var = str_var
        self.start = 0
        self.end = 0
        self.end = self.__match_dont()
        self.total_sum = self.__get_valid_args_sum()
        print(self.start, self.end)
    
    def __match_dont(self)->(int,int):
        pattern = r"don't\(\)"
        print('start...', self.start)
        match = re.search(pattern, self.str_var[self.start:])
        return (int(match.end()) + self.start) if match else len(self.str_var) 
    
    def __match_do(self)->(int,int):
        pattern = r"do\(\)"
        match = re.search(pattern, self.str_var[self.end:])
        
        return (int(match.end()) + self.end) if match else len(self.str_var)
    
    def __get_valid_args_sum(self)->int:
        # print(self.__chop_str_var())
        return find_all_valid_args(self.__chop_str_var())
    
    def __chop_str_var(self)->str:
        return self.str_var[self.start:self.end]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        print('end...', self.end)
        if self.end >= len(self.str_var) :
            raise StopIteration()
        self.start = self.__match_do()
        self.end = self.__match_dont()
        self.total_sum += self.__get_valid_args_sum()
        return self.total_sum, self.start, self.end

        
def main():
    str_var = read_d3()
    sum_valid_args = SumValidArgs(str_var)
    for i in sum_valid_args:
        print(i)
    print(sum_valid_args.total_sum)
if __name__ == '__main__':
    main()
    
    # 59097164