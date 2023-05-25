import numpy as np
import random

from tabulate import tabulate
from beautifultable import BeautifulTable



# 3 rows of numbers = 3 squares
def line_of_3_squares(board, numb, square, rows):
    '''filling one line of 3x3 squares with numbers'''

    squares1 = sum(square,[])
    squares2 = sum([square[1], square[2], square[0]],[])
    squares3 = sum([square[2], square[0], square[1]],[])

    for i in squares1:  
        board[rows[0],i]= numb[squares1[i]]
    for i in squares2:
        board[rows[1],i]= numb[squares2[i]]
    for i in squares3:
        board[rows[2],i]= numb[squares3[i]]  




def fill_board(board, numb, sq_index, numbers):
    '''filling the array with numbers'''
    line_of_3_squares(board, numb, sq_index, sq_index[0])
    
    nb = numbers.pop(0)
    numbers.insert(8, nb)
    line_of_3_squares(board, numb, sq_index, sq_index[1])
    
    nb = numbers.pop(0)
    numbers.insert(8, nb)
    line_of_3_squares(board, numb, sq_index, sq_index[2])
    

# NAPRAWIC!!! BY 0 NIE UWZGLEDNIAL!!!!
def find_non_unique(board):
    '''finding rows with duplicates'''
    numbers =[1,2,3,4,5,6,7,8,9]
    rows=[]
    for i in range(len(numbers)):
        if board[i] != 0:
            row = np.unique(board[i])
        if len(row)< len(numbers):
            rows.append(i)
    return rows




# -----START--------
def create_nb_board():
    game_board = np.zeros([9,9], dtype = "int")

    numbers =[1,2,3,4,5,6,7,8,9]

    # small squares indices
    sq_index = [[0,1,2], [3,4,5], [6,7,8]]


    # mixing elements
    random.shuffle(numbers)
    random.shuffle(sq_index)


    # creating game_board
    fill_board(game_board, numbers, sq_index, numbers)
    return game_board


#print(game_board)

#table = create_nb_board()
##print(tabulate(table, tablefmt='grid'))
##subtable1 = BeautifulTable()
##subtable2 = BeautifulTable()
##subtable1.append(game_board[0:3,0:3])
##subtable2.append(game_board[0:3,3:6])
##parent_table = BeautifulTable()
##parent_table.append([subtable1, subtable2]) 
##print(parent_table)


##subtable1 = game_board[0:3,0:3]
##subtable2 = game_board[0:3,3:6]
##
##table = [subtable1, subtable2]
#print(tabulate(table, tablefmt='grid'))
##


# checking compliance with sudoku rules

#game_board[2,3]= 9
#game_board[7,5]= 9



def checking_unique(game_board):
    row_num = find_non_unique(game_board)
    col_num = find_non_unique(game_board.transpose())

    if len(row_num) >0:
        print(f"\nWiersze zawierające duplikaty: \n{row_num}")
    else:
        print("\nNie ma wierszy zawierających duplikaty.")

    if len(col_num) >0:
        print(f"Kolumny zawierające duplikaty: \n{col_num}")
    else:
        print("Nie ma kolumn zawierających duplikaty.")
##
##
