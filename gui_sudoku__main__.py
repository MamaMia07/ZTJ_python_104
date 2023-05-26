import tkinter as tk
from tkinter import messagebox
import random
import numpy as np
import sudoku_numbers_board as sb
import sudoku_gui_functions as sf

##def starting_gui_board():
##    skip_row = 0
##    for i in range(3):
##        skip_col = 0
##
##        for j in range(3):
##            frame1 = tk.Frame(frame,relief="groove",borderwidth=1 )
##            frame1.grid(row=i, column=j, padx=1, pady=1)
##
##            for n in range(3):
##                board_row = n + skip_row
##
##                for m in range(3):
##                    board_col = m + skip_col
##                
##                    frameSq = tk.Frame(frame1, relie= "flat", borderwidth=1)
##                    frameSq.grid(row=n, column=m)
##
##                    field = tk.Label(frameSq, width=3, font=('Arial 20'), bg='#FDFCFF', borderwidth=1, relief="groove")
##                    field.grid(row=i, column=j)
##                  
##            skip_col += 3
##        skip_row += 3



##
##
### filling with 0 randomly choosen elements of board (board with numbers)
##def variant_game(board, empty_places):
##    n=board.shape[0]
##    np.put(board, np.random.choice(range(n*n), empty_places, replace=False), 0)
 


##def is_num(ent):
##    if ent.strip() in ["1", "2", "3","4", "5", "6", "7", "8", "9"]:
##       return True
##    else:
##        ent = ""
##        return False
##
##
##
##def fill_gui_board(board, entries, labels):
### wypełnianie tablicy sudoku
### zachowanie entries w liście, przypisanie im i i j z tablicy liczb
##    skip_row = 0
##    for i in range(3):
##        skip_col = 0
##        for j in range(3):
##         
##            frame1 = tk.Frame(frame,relief="groove",borderwidth=1 )
##            frame1.grid(row=i, column=j, padx=1, pady=1)
##        
##            for n in range(3):
##                board_row = n + skip_row
##            
##                for m in range(3):
##                    board_col = m + skip_col
##                
##                    frameSq = tk.Frame(frame1, relief="groove", borderwidth=1)
##                    frameSq.grid(row=n, column=m)
##                                     
##                    if board[board_row,board_col] == 0:                                                
##                       field = tk.Entry(frameSq, width=3, bg='white',relief="flat",
##                                        font=('Arial 20'), justify = "center",
##                                        validatecommand=(frame.register(is_num), "%S"), validate = 'key')
##                       field.grid(row=i, column=j)
##
##                       entries.append([field, board_row, board_col])
##               
##                    if board[board_row,board_col] != 0:
##                        nmb_lbl = tk.Label(frameSq, width=3, font=('Arial 20'),
##                                   relief="flat", text=f'{board[board_row,board_col]}')
##                        nmb_lbl.grid(row=i, column=j)
##
##                        labels.append([nmb_lbl, board_row, board_col])
##          
##            skip_col += 3
##        skip_row += 3
##

# WYWALIC???
##def insert_numbers(board,entries):
##    for ent in entries:
##        field= ent[0]
##        nb = field.get()
##        print(nb)
##        nb = int(nb)
##        i ,j = ent[1], ent[2]
##        board[i,j] = nb



def game_selected():
    global entries, labels, new_board
    entries = []
    labels = []
    new_board = sb.create_nb_board()
    choice  = var.get()
    sf.variant_game(new_board, choice)
    sf.fill_gui_board(new_board, entries, labels,frame)


  
##
##
### insert player's numbers from gui to number_board
##def insert_numbers_to_board():
##   check = tk.messagebox.askyesno("Check", "Do you want to check your solution?")
##   if check == True:
##    if len(entries)>0:
##        for ent in entries:
##            field= ent[0]
##            nb = field.get()
##            nb = nb.strip()
##            if nb in["1", "2", "3","4", "5", "6", "7", "8", "9"]:
##                print(nb)
##                nb = int(nb)
##                i ,j = ent[1], ent[2]
##                new_board[i,j] = nb
##            else:
##                field.delete(0,tk.END)
      


##
##def color_of_line_with_duplicates(lines, i):
##    if len(lines) > 0:
##        for line_nb in lines:
##                for entry in entries:
##                    if entry[i] == line_nb:
##                        entry[0].configure(bg="#EC8686")
##                for label in labels:
##                    if label[i] == line_nb:
##                        label[0].configure(bg="#EC8686")
##    
##
##
##
##
##def color_of_square_with_duplicates(squares):
##    if len(squares) > 0:   # squares  [[[0, 1, 2], [6, 7, 8]], [[6, 7, 8], [3, 4, 5]]]
##        for square_indices in squares:   # square_indices[[0, 1, 2], [6, 7, 8]]
##            for n in range(0,3):
##                for m in range(0,3):
##                    for entry in entries:
##                        if entry[1] == square_indices[0][n] and entry[2] == square_indices[1][m]:
##                            entry[0].configure(bg="#EC8686")
##                    for label in labels:
##                        if label[1] == square_indices[0][n] and label[2] == square_indices[1][m]:
##                            label[0].configure(bg="#EC8686")
##


def check_clicked():
    sf.insert_numbers_to_board(entries, new_board)
    containing_duplicates= sb.checking_unique(new_board)
    #print(containing_duplicates)

    if len(containing_duplicates) > 0:
        rows = containing_duplicates[0]
        sf.color_of_line_with_duplicates(rows, 1, entries, labels)
       # print(len(rows))

        cols = containing_duplicates[1]
        sf.color_of_line_with_duplicates(cols, 2, entries, labels)
        #print(len(cols))

        squares = containing_duplicates[2]
        sf.color_of_square_with_duplicates(squares, entries, labels)
        #print(len(squares))

    if len(rows)==0 and len(cols)==0 and len(squares) == 0:
       msg = tk.messagebox.showinfo("Great!", "   GREAT!\n   GOOD JOB!")




def exit_clicked():
    check = tk.messagebox.askyesno("Exit", "Do you want to Exit?")
    if check == True:
        window.destroy()








window = tk.Tk()
window.title("Sudoku")


# frames
frame = tk.Frame(window, relief="raised", borderwidth=7, bg='#FDFCFF')#, width=150, height=400)
frame.grid(column=0, row=1)

frame2 = tk.Frame(window, relief = "flat")#, width=150, height=400)
frame2.grid(column=4, row=1)

frame3 =tk.Frame(window, relief = "flat")#, width=150, height=400)
frame3.grid(column=0, row=2)


# widgets
title_lbl = tk.Label(window, text="SUDOKU",font='Arial 20 bold' )
title_lbl.grid(column=0, row=0)


check_btn = tk.Button(frame2, text="CHECK\nSOLUTION",font='Ariala 12 bold', fg="green",
                      width = 15, command= check_clicked)
check_btn.grid(column=0, row=5, padx=20, pady=30)


btn_exit = tk.Button(frame3, text="EXIT",font='Arial 12 bold', fg="red", width = 20,
                     command = exit_clicked)
btn_exit.grid(column=0, row=3, sticky="we", padx = 20, pady = 20)


gam_var_lbl = tk.Label(frame2, text="GAME VARIANT:",font='Arial 15 bold')
gam_var_lbl.grid(column=0, row=0,padx=20, pady=10)

# ratio buttons for game variant choosing
var = tk.IntVar()
game_variants = {"very easy" :7, 
	         "easy" : 25, 
	         "medium" : 40, 
	         "difficult" :60 } 

# If you set this option to zero, the indicator disappears, and the entire widget
#becomes a “push-push” button that looks raised when it is cleared and sunken when it is set.

i=1
for (var_game, val) in game_variants.items(): 
    radio_btn = tk.Radiobutton(frame2, text= var_game, variable=var, value= val,
                             command= game_selected, font=('Arial 13'),indicatoron= False,
                             selectcolor= "#BABFDC", width=10)  
    radio_btn.grid(column=0, row=i, padx=60, pady=6, sticky ="w")
    #radio_btn.command = medium_game(board) #variable=v,
    i +=1



new_board= sf.starting_gui_board(frame)
entries = []  
labels = []

window.mainloop()




