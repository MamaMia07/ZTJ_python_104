import tkinter as tk
from tkinter import messagebox
import random
import numpy as np
import time

# zmiana  obramowania okienka entry
##master = tk.Tk()
##nameentryframe = tk.Frame(master = master, background = 'BLACK', borderwidth = 20, relief = tk.SUNKEN)
##nameentry = tk.Entry(nameentryframe)
##nameentryframe.pack()
##nameentry.pack()
##       
##master.mainloop()


def starting_gui_board():

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

                    field = tk.Label(frameSq, width=3, font=('Arial 20'), bg='#FDFCFF', borderwidth=1, relief="groove")
                    field.grid(row=i, column=j)
                
                  
            skip_col += 3
        skip_row += 3






def generate_board():
    board = np.array([1,2,3,4,5,6,7,8,9])
    board = np.resize(board,(9,9))
    return board



# filling with 0 randomly choosen elements of board (board with numbers)
def variant_game(board, empty_places):
    n=board.shape[0]
    np.put(board, np.random.choice(range(n*n), empty_places, replace=False), 0)
   




def is_num(ent):
    
    if ent.strip() in ["1", "2", "3","4", "5", "6", "7", "8", "9"]:
       return True
    else:
        ent = ""
        return False



def fill_gui_board(board, entries):
    # wypełnianie tablicy sudoku
# zachowanie entries w liście, przypisanie im i i j z tablicy liczb

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
                                        font=('Arial 18'), justify = "center",
                                        validatecommand=(frame.register(is_num), "%S"), validate = 'key')
                       field.grid(row=i, column=j)

                       entries.append([field, board_row, board_col])
                
               
                    if board[board_row,board_col] != 0:
                        nmb_lbl = tk.Label(frameSq, width=3, font=('Arial 20'),
                                   borderwidth=1, relief="flat", text=f'{board[board_row,board_col]}')
                        nmb_lbl.grid(row=i, column=j)

                        labels.append([nmb_lbl, board_row, board_col])

          
            skip_col += 3
        skip_row += 3









def insert_numbers(board,entries):
    for ent in entries:
        field= ent[0]
        nb = field.get()
        print(nb)
        nb = int(nb)
        i ,j = ent[1], ent[2]
        board[i,j] = nb




def game_selected():
    global entries, labels, new_board

    entries = []
    labels = []
    new_board = generate_board()
    choice  = var.get()
    variant_game(new_board, choice)
    fill_gui_board(new_board, entries)


##    for ent in entries:
##        ent[0].configure(validatecommand=is_num, validate = 'focus')

    print(new_board)
    print(entries[0][1:3])
    print(len(labels))
    



def check_clicked():
   check = tk.messagebox.askyesno("Check", "Do you want to Submit")
   if check == True:
       for ent in entries:
           field= ent[0]
           nb = field.get()
           nb = nb.strip()
           if nb in["1", "2", "3","4", "5", "6", "7", "8", "9"]:
               print(nb)
               nb = int(nb)
               i ,j = ent[1], ent[2]
               new_board[i,j] = nb
           else:
               field.delete(0,tk.END)
           
       print(new_board)







window = tk.Tk()
window.title("Sudoku")


# frames
##frame0 = tk.Frame(window,relief = "flat")
##frame0.grid(column=0, row=0, pady = 5)

frame = tk.Frame(window, relief="raised", borderwidth=7, bg='#FDFCFF')
frame.grid(column=0, row=1)

frame2 = tk.Frame(window, relief = "flat")#, width=150, height=400)
frame2.grid(column=4, row=1)

frame3 =tk.Frame(window, relief = "flat")#, width=150, height=400)
frame3.grid(column=0, row=2)


#widgets
title_lbl = tk.Label(window, text="SUDOKU",font='Arial 20 bold' )
title_lbl.grid(column=0, row=0)


check_btn = tk.Button(frame2, text="CHECK\nTHE SOLUTION",font='Ariala 12 bold', fg="green",
                      width = 15, command= check_clicked)
check_btn.grid(column=0, row=5, padx=20, pady=30)


btn_exit = tk.Button(frame3, text="EXIT",font='Arial 12 bold', fg="red", width = 20)
btn_exit.grid(column=0, row=3, sticky="we", padx = 20, pady = 20)


gam_var_lbl = tk.Label(frame2, text="GAME VARIANT:",font='Arial 15 bold')
gam_var_lbl.grid(column=0, row=0,padx=20, pady=10)

# ratio buttons for game variant choosing
var = tk.IntVar()
game_variants = {"very easy" : 10, 
	         "easy" : 25, 
	         "medium" : 40, 
	         "difficult" :60 } 

# If you set this option to zero, the indicator disappears, and the entire widget
#becomes a “push-push” button that looks raised when it is cleared and sunken when it is set.

i=1
for (var_game, val) in game_variants.items(): 
    radio_btn=tk.Radiobutton(frame2, text= var_game, variable=var, value= val,
                             command= game_selected, font=('Arial 13'),indicatoron = False,
                             selectcolor= "blue", width=10)  
    radio_btn.grid(column=0, row=i, padx=60, pady=6, sticky ="w")
    #radio_btn.command = medium_game(board) #variable=v,
    i +=1



new_board= starting_gui_board()
entries = []  
labels = []

window.mainloop()


#board = generate_board()


##def fill_board(board):
##    # wypełnianie tablicy sudoku
##    for i in range(9):
##        for j in range(9):
##            #if board[i,j] == 0:
##            field = tk.Entry(master=frame, width=3, font=('Arial 18'))
##            field.grid(row=i, column=j)
##            #field.insert(0,f'{board[i,j]}') 
##            if board[i,j] != 0:
##                nmb_lbl = tk.Label(master=frame, width=3, font=('Arial 18'), text=f'{board[i,j]}')
##                nmb_lbl.grid(row=i, column=j)
##    




