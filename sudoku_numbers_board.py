import numpy as np
import random


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
    


# checking if there is 0 in row or doubled numbers
def find_non_unique(board):
    '''finding rows with duplicates or with 0'''
    numbers =[1,2,3,4,5,6,7,8,9]
    rows=[]
    for i in range(len(numbers)):

        if any(nb== 0 for nb in board[i]):
            rows.append(i)

        else:
            row = np.unique(board[i])
            if len(row)< len(numbers):
                rows.append(i)
    return rows




# checking the 3x3 squares
def check_small_square(board):
    '''finding squares 3x3 with duplicates'''
    square = np.array([],[])
    squares_nonunique = []
   
    for i in range(0,9,3):
        for j in range(0,9,3):
            square = board[0+i:3+i, 0+j:3+j]
           
            nb = np.unique(square)
            if len(nb) < board.shape[0]:
                squares_nonunique.append([[0+i, 1+i,2+i],[0+j, 1+j, 2+j]])
   
    return squares_nonunique
    



def create_nb_board():
    game_board = np.zeros([9,9], dtype = "int")
    numbers =[1,2,3,4,5,6,7,8,9]

    # small squares indices
    sq_index = [[0,1,2], [3,4,5], [6,7,8]]

    # shuffle the elements
    random.shuffle(numbers)
    random.shuffle(sq_index)

    # creating game_board
    fill_board(game_board, numbers, sq_index, numbers)
    return game_board




# retyrns numbers of rows, columns and indices of squares
# with nonunique numbers
def checking_unique(game_board):
    row_num = find_non_unique(game_board)
    col_num = find_non_unique(game_board.transpose())
    square_indices = check_small_square(game_board)

    return (row_num, col_num, square_indices)     



