from os import path, strerror
from typing import List, Tuple

# #?find all xmas instances
# # ! iterate through matrix: r:0,c:0
# # search directions with conditions:
XMAS_LEN  = len('XMAS')
XMAS = 'XMAS'
# # COL_LEN = len(col)
# # ROW_LEN = len(row)
# # |^ : r>= XMAS_LEN - 1
# # |v : r <= COL_LEN - XMAS_LEN
# # <- : C >= XMAS_LEN - 1
# # -> : C <= ROW_LEN - XMAS_LEN

# # ^\ : r>= XMAS_LEN - 1 && C >= XMAS_LEN - 1
# # /^ : r>= XMAS_LEN - 1 && ROW_LEN - XMAS_LEN 
# # /v :  r <= COL_LEN && C >= XMAS_LEN - 1
# # v\ :  r <= COL_LEN && C <= ROW_LEN - XMAS_LEN
# # 
def get_d4()->List[str]:
    file_path = path.join(path.dirname(__file__), 'd4test.txt')
    matrix = []
    try:
        with open(file_path, 'rt') as stream:
            return [line.strip() for line in stream.readlines()]
            
    except IOError as exc:
        print(strerror(exc.errno))
        return []
    except Exception as exc:
        print("you don't fucked up", exc)
        return []
# class Break(Exception):
#     pass 
# def find_xmases(matrix:List[str])->int:
#     total_count = 0
#     XMAS = 'XMAS'
#     XMAS_LEN  = len('XMAS')
#     COL_LEN = len(matrix[0])
#     ROW_LEN = len(matrix)
#     allowed_dirs = {'up': False, 'back': False, 'down': True, 'forw': True }
#     for row_ind, row in enumerate(matrix):
#         print('row', row_ind, len(row), row)
#         allowed_dirs['up'] = row_ind >= XMAS_LEN - 1
#         allowed_dirs['down'] = row_ind <= ROW_LEN - XMAS_LEN
#         for col_ind, col in enumerate(row):
#             allowed_dirs['forw'] =  col_ind <= COL_LEN - XMAS_LEN
#             allowed_dirs['back'] =  col_ind >= XMAS_LEN - 1
#             print('col', col_ind,  col,'curr ele', matrix[row_ind][col_ind], allowed_dirs)
#             if matrix[row_ind][col_ind] == 'X':
#                 if allowed_dirs['up']:
#                     for word_row,xmas in zip(range(row_ind,row_ind - 4, -1),XMAS):
#                         if matrix[word_row][col_ind] != xmas:
#                             break
#                     else:
#                         total_count += 1
#                         print('up', total_count)
                        
#                     if allowed_dirs['forw']:
#                         diag_indices =  [ (word_row, word_col) for word_row,word_col in zip(range(row_ind,row_ind - 4, -1),range(col_ind, col_ind + 4))]
#                         for (word_row, word_col), xmas in zip(diag_indices, XMAS):
#                             print('word_row', word_row, 'world col', word_col , matrix[word_row][word_col] , xmas)
#                             if matrix[word_row][word_col] != xmas:
#                                 print('breaking...')
#                                 break
#                         else:
#                             total_count += 1 
#                             print('up forw', total_count)
                            
#                     if allowed_dirs['back']:
#                         diag_indices =  [ (word_row, word_col) for word_row,word_col in zip(range(row_ind,row_ind - 4, -1),range(col_ind, col_ind - 4, -1))]
#                         for (word_row, word_col), xmas in zip(diag_indices, XMAS):
#                             print('word_row', word_row, 'world col', word_col , matrix[word_row][word_col] , xmas)
#                             if matrix[word_row][word_col] != xmas:
#                                 print('breaking...')
#                                 break
#                         else:
#                             total_count += 1 
#                             print('up back', total_count)
                        
                        
#                 if allowed_dirs['down']:
#                     for word_row, xmas in zip(range(row_ind, row_ind + 4), XMAS):
#                         if matrix[word_row][col_ind] != xmas:
#                             break
#                     else:
#                         total_count += 1 
#                         print('down', total_count)
                    
#                     if allowed_dirs['forw']:
#                         diag_indices =  [ (word_row, word_col) for word_row,word_col in zip(range(row_ind,row_ind + 4),range(col_ind, col_ind + 4))]
#                         for (word_row, word_col), xmas in zip(diag_indices, XMAS):
#                             print('word_row', word_row, 'world col', word_col , matrix[word_row][word_col] , xmas)
#                             if matrix[word_row][word_col] != xmas:
#                                 print('breaking...')
#                                 break
#                         else:
#                             total_count += 1 
#                             print('down', total_count)
                            
#                     if allowed_dirs['back']:
#                         diag_indices =  [ (word_row, word_col) for word_row,word_col in zip(range(row_ind,row_ind + 4 ),range(col_ind, col_ind - 4, -1))]
#                         for (word_row, word_col), xmas in zip(diag_indices, XMAS):
#                             print('word_row', word_row, 'world col', word_col , matrix[word_row][word_col] , xmas)
#                             if matrix[word_row][word_col] != xmas:
#                                 print('breaking...')
#                                 break
#                         else:
#                             total_count += 1 
#                             print('down', total_count)
                                    
#                 if allowed_dirs['forw']:
#                     for word_col, xmas in zip(range(col_ind, col_ind + 4), XMAS):
#                         if matrix[row_ind][word_col] != xmas:
#                             break
#                     else:
#                         total_count += 1 
#                         print('forw', total_count)
                        
#                 if allowed_dirs['back']:
#                     for word_col, xmas in zip(range(col_ind, col_ind - 4 , -1), XMAS):
#                         if matrix[row_ind][word_col] != xmas:
#                             break
#                     else:
#                         total_count += 1 
#                         print('back', total_count)
#             print('count after col', col_ind, total_count)
#     return total_count
            
            
# def main():
#     matrix = get_d4()
#     print('matrix ? ', matrix)
#     print(find_xmases(matrix))
# if __name__ == '__main__':
#     main()

def is_valid_index(row: int, col: int, rows: int, cols: int) -> bool:
    return 0 <= row < rows and 0 <= col < cols

def get_indices(row: int, col: int, direction: Tuple[int, int], length: int) -> List[Tuple[int, int]]:
    d_row, d_col = direction
    return [(row + i * d_row, col + i * d_col) for i in range(length)]

def check_direction(matrix: List[str], row: int, col: int, direction: Tuple[int, int]) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    indices = get_indices(row, col, direction, XMAS_LEN)
    if all(is_valid_index(r, c, rows, cols) for r, c in indices):
        return all(matrix[r][c] == XMAS[i] for i, (r, c) in enumerate(indices))
    return False

def find_xmases(matrix: List[str]) -> int:
    """Finds all occurrences of XMAS in the matrix across all directions."""
    total_count = 0
    rows, cols = len(matrix), len(matrix[0])
    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, 1),   # Forward
        (0, -1),  # Backward
        (-1, 1),  # Up-Forw
        (-1, -1), # Up-Back
        (1, 1),   # Down-Forw
        (1, -1)   # Down-Back
    ]
    
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 'X':
                total_count += sum(check_direction(matrix, row, col, direction) for direction in directions)
    return total_count

def find_xmasses(matrix: List[str])->int:
    directions = (
        (1, 0), # down
        (-1,0), #up
        (0,1), #front
        (0, -1) , #back
        (1,1),  #down front
        (-1,1), #up front
        (1,-1), #down back
        (-1, -1) #up back
    )
    rows = len(matrix)
    cols = len(matrix[0])
    total_sum = 0 
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 'X':
                for direction in directions: # ! for every possible direction
                    total_sum += int(check_dir(row, col , direction, rows, cols, matrix))
    return total_sum    
                    
def check_dir(row:int, col:int, direction: Tuple, rows:int , cols:int , matrix:List[str]):
    # ! get range of a direction
    pos_matrix = get_ranges(row, col, direction,rows, cols)
    return is_pos_matrix_valid(pos_matrix, rows, cols , matrix)
    
def get_ranges(row:int, col:int, direction:Tuple, rows:int, cols:int)->List[Tuple]:
    row_dir , col_dir = direction
    return  [(row + (pos * row_dir) , col + ( pos * col_dir)) for pos in range(len(XMAS))]
    
def is_pos_matrix_valid(pos_matrix:List[Tuple], rows:int, cols:int, matrix:List[str]):
    return all([ is_within_matrix(row, col, rows, cols) and matrix[row][col] == XMAS[i] for i,(row,col) in enumerate(pos_matrix)])

def is_within_matrix(row:int, col:int,  rows:int, cols:int):
    return  0 <= row < rows and 0 <= col < cols

def main():
    matrix = get_d4()
    if matrix:
        print("Total XMAS found:", find_xmasses(matrix))

if __name__ == '__main__':
    main()
