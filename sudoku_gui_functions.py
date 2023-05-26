import tkinter as tk
from tkinter import messagebox
import random
import numpy as np
import sudoku_numbers_board as sb


# creating sudoku board with empty fields
def starting_gui_board(frame):
    ''' creating the empty sudocu board '''
    skip_row = 0
    for i in range(3):
        skip_col = 0

        for j in range(3):
            frame1 = tk.Frame(frame,relief="groove",borderwidth=1 )
            frame1.grid(row=i, column=j, padx=1, pady=1)

            for n in range(3):
                board_row = n + skip_row

                for m in range(3):
                    board_col = m + skip_col
                
                    frameSq = tk.Frame(frame1, relie= "flat", borderwidth=1)
                    frameSq.grid(row=n, column=m)

                    field = tk.Label(frameSq, width=3, font=('Arial 22'), bg='#FDFCFF',
                                     borderwidth=1, relief="groove")
                    field.grid(row=i, column=j)
                  
            skip_col += 3
        skip_row += 3





# filling with 0 randomly choosen elements of numbers_board 
def variant_game(board, empty_places):
    n=board.shape[0]
    np.put(board, np.random.choice(range(n*n), empty_places, replace=False), 0)
 

# validating the entries chars
def is_num(ent):
    if ent.strip() in ["1", "2", "3","4", "5", "6", "7", "8", "9"]:
       return True
    else:
        ent = ""
        return False


def clearFrame(frameX):
    # destroy all widgets from frame
    for widget in frameX.winfo_children():
       widget.destroy()



    

def fill_gui_board(board, entries, labels, frame):
    ''' filling the sudocu board with numbers'''
    # entries and labels with theit indices ale collected in lists
    #clearFrame(frame)
    skip_row = 0
    for i in range(3):
        skip_col = 0
        for j in range(3):
         
            frame1 = tk.Frame(frame,relief="groove",borderwidth=1 )
            frame1.grid(row=i, column=j, padx=1, pady=1)
        
            for n in range(3):
                board_row = n + skip_row
            
                for m in range(3):
                    board_col = m + skip_col
                
                    frameSq = tk.Frame(frame1, relief="groove", borderwidth=1)
                    frameSq.grid(row=n, column=m)
                                     
                    if board[board_row,board_col] == 0:                                                
                       field = tk.Entry(frameSq, width=3, bg='white',relief="flat",
                                        font=('Arial 20'), justify = "center",
                                        validatecommand=(frame.register(is_num), "%S"), validate = 'key')
                       field.grid(row=i, column=j)

                       entries.append([field, board_row, board_col])
               
                    if board[board_row,board_col] != 0:
                        nmb_lbl = tk.Label(frameSq, width=3, font=('Arial 20'),
                                   relief="flat", text=f'{board[board_row,board_col]}')
                        nmb_lbl.grid(row=i, column=j)

                        labels.append([nmb_lbl, board_row, board_col])
          
            skip_col += 3
        skip_row += 3



##def insert_numbers(board,entries):
##    for ent in entries:
##        field= ent[0]
##        nb = field.get()
##        print(nb)
##        nb = int(nb)
##        i ,j = ent[1], ent[2]
##        board[i,j] = nb



##def game_selected():
##    global entries, labels, new_board
##    #starting_gui_board()
##    entries = []
##    labels = []
##    #new_board = generate_board()
##    new_board = sb.create_nb_board()
##    choice  = var.get()
##    variant_game(new_board, choice)
##    fill_gui_board(new_board, entries, labels)




# insert player's numbers from entries of gui to number_board
def insert_numbers_to_board(entries, new_board):

   check = tk.messagebox.askyesno("Check", "Do you want to check your solution?")
   if check == True:
    if len(entries)>0:
        for ent in entries:
            field= ent[0]
            nb = field.get()
            nb = nb.strip()
            if nb in["1", "2", "3","4", "5", "6", "7", "8", "9"]:
                nb = int(nb)
                i ,j = ent[1], ent[2]
                new_board[i,j] = nb
            else:
                field.delete(0,tk.END)
      


# changing color of widges of rows and columns with duplicate numbers
def color_of_line_with_duplicates(lines, i, entries, labels):
    if len(lines) > 0:
        for line_nb in lines:
                for entry in entries:
                    if entry[i] == line_nb:
                        entry[0].configure(bg="#EC8686")
                for label in labels:
                    if label[i] == line_nb:
                        label[0].configure(bg="#EC8686")
    



# changing color of widges of squares 3x3 with duplicate numbers
def color_of_square_with_duplicates(squares, entries, labels):
    if len(squares) > 0:   
        for square_indices in squares:   
            for n in range(0,3):
                for m in range(0,3):
                    for entry in entries:
                        if entry[1] == square_indices[0][n] and entry[2] == square_indices[1][m]:
                            entry[0].configure(bg="#EC8686")
                    for label in labels:
                        if label[1] == square_indices[0][n] and label[2] == square_indices[1][m]:
                            label[0].configure(bg="#EC8686")



##def check_clicked():
##    insert_numbers_to_board()
##    containing_duplicates= sb.checking_unique(new_board)
##    print(containing_duplicates)
##
##    if len(containing_duplicates) > 0:
##        rows = containing_duplicates[0]
##        color_of_line_with_duplicates(rows, 1)
##        print(len(rows))
##
##        cols = containing_duplicates[1]
##        color_of_line_with_duplicates(cols, 2)
##        print(len(cols))
##
##        squares = containing_duplicates[2]
##        color_of_square_with_duplicates(squares)
##        print(len(squares))
##
##    if len(rows)==0 and len(cols)==0 and len(squares) == 0:
##       msg = tk.messagebox.showinfo("Great!", "   GREAT!\n   GOOD JOB!")



##def exit_clicked():
##    check = tk.messagebox.askyesno("Exit", "Do you want to Exit?")
##    if check == True:
##        window.destroy()








