import tkinter as tk
from time import sleep

width = 8
height= 8


class Board:
    def __init__ (self):
        ## make an empty board
        self.board = [[0 for width in range(width)] for height in range(height)]
        ## place starting pieces
        self.board[3][3] = 1
        self.board[4][4] = 1
        self.board[3][4] = 2
        self.board[4][3] = 2

    def placePiece (self, x, y, player):
        self.board[x][y] = player



class PlayerHandler:
    def __init__ (self):
        self.turn = 1

    def changeTurn(self):
        if self.turn == 1:
            self.turn = 2
        else: 
            self.turn = 1 

window = tk.Tk()
        
grid = tk.Canvas(master=window)
allbuttons = []
window.geometry("{}x{}".format((width*100), (height*100)))
count = 0

## make window
for i in range(width):
    for j in range(height):
        ## make the button and add it to the grid aswell as giving it a command to run when clicked, and a position for future checks.
        btn = tk.Button(master=grid,state="active" , height= 3, width=6 ,fg="black", command=lambda i=count: button(allbuttons[i]))
        btn.grid(row=j, column=i, sticky= tk.EW)
        count += 1
        ## add the button to a list of all buttons, this is so that it can be checked and change later using the position
        allbuttons.append(btn)
        
        grid.pack()
        
window.after(main_loop, 100)


def button(self, button):
    print(button)

def updateUi (self):
    for i in board.board:
        print (i)

def main_loop():
    print ("Player", playerHandler.turn, "'s turn")
    updateUi()
    playerHandler.changeTurn()
    sleep(1)
    window.after(1, main_loop)


board = Board()
playerHandler = PlayerHandler()


window.mainloop()