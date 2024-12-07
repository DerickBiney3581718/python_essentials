from typing import List, Tuple
from d4p1 import get_d4

def find_x_mases(matrix:List[str]):
    # when point == 'A'
    # [(row - 1, col  - 1), (row + 1 , col + 1)]   [(row + 1, col - 1), (row - 1 , col + 1)]
    total_sum = 0
    rows , cols = len(matrix), len(matrix[0])
    
    for row in range(1,rows - 1):
        for col in range(1,cols - 1):
            if matrix[row][col] == 'A':
                total_sum += ''.join(sorted([matrix[row - 1][col - 1] , matrix[row + 1][col + 1]])) == 'MS' and ''.join(sorted([matrix[row + 1][col - 1] , matrix[row - 1][col + 1]])) == 'MS'
    return total_sum


def main():
    matrix = get_d4()
    print('total cross masses', find_x_mases(matrix))
    
if __name__ == "__main__":
    main()