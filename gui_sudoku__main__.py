import tkinter as tk
from tkinter import messagebox
import random
import numpy as np
import sudoku_numbers_board as sb
import sudoku_gui_functions as sf


def game_selected():
    global entries, labels, new_board
    entries = []
    labels = []
    new_board = sb.create_nb_board()
    choice  = var.get()
    sf.variant_game(new_board, choice)
    sf.fill_gui_board(new_board, entries, labels,frame)




def check_clicked():
    sf.insert_numbers_to_board(entries, new_board)
    containing_duplicates= sb.checking_unique(new_board)
    
    if len(containing_duplicates) > 0:
        rows = containing_duplicates[0]
        sf.color_of_line_with_duplicates(rows, 1, entries, labels)
      
        cols = containing_duplicates[1]
        sf.color_of_line_with_duplicates(cols, 2, entries, labels)
       
        squares = containing_duplicates[2]
        sf.color_of_square_with_duplicates(squares, entries, labels)
       
    if len(rows)==0 and len(cols)==0 and len(squares) == 0:
       msg = tk.messagebox.showinfo("Great!", "  GREAT! GOOD JOB!  ")





def exit_clicked():
    check = tk.messagebox.askyesno("Exit", "Do you want to Exit?")
    if check == True:
        window.destroy()






window = tk.Tk()
window.title("Sudoku")


# frames
frame = tk.Frame(window, relief="raised", borderwidth=7, bg='#FDFCFF')
frame.grid(column=0, row=1)

frame2 = tk.Frame(window, relief = "flat")
frame2.grid(column=4, row=1)

frame3 =tk.Frame(window, relief = "flat")
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

i=1
for (var_game, val) in game_variants.items(): 
    radio_btn = tk.Radiobutton(frame2, text= var_game, variable=var, value= val,
                             command= game_selected, font=('Arial 13'),indicatoron= False,
                             selectcolor= "#BABFDC", width=10)  
    radio_btn.grid(column=0, row=i, padx=60, pady=6, sticky ="w")
    i +=1




new_board= sf.starting_gui_board(frame)
entries = []  
labels = []

window.mainloop()





