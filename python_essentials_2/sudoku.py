def sudoku_checker(sudoku):
    list_sudoku = sudoku.split('\n')
    list_sudoku_int = [[int(n) for n in row] for row in list_sudoku]
    sum_sudoku = 45 
    print('sudoku int: ', list_sudoku_int)
    passed = True
    for ind, row in enumerate(list_sudoku_int):
        print('row', row, 'ind', ind)
        start_row = (ind % 3 * 3)
        start_col = (ind // 3) * 3 if ind != 0 else ind
        passed = sum([char for char in row]) == sum_sudoku  #row check
        passed = sum([row[ind] for row in list_sudoku_int])  == sum_sudoku #column check
        passed = sum([sum(row[start_row: start_row + 3]) for row in list_sudoku_int[start_col: start_col + 3]]) == sum_sudoku  
        if not passed:
            break
    print('yes') if passed else print('no')    

        
param = f"""295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672"""

param2= f"""195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671"""
sudoku_checker(param2)