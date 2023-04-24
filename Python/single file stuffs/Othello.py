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
    
    def updateUi(self):
        for i in self.board:
            print(i)

    def checkplacement(self, player, x,y):
        print(player, x, y)

        ### some thing to check all cardinal directions and diagonals
     



class PlayerHandler:
    def __init__ (self):
        self.turn = 1

    def changeTurn(self):
        if self.turn == 1:
            self.turn = 2
        else: 
            self.turn = 1 


allbuttons = []
count = 0

board = Board()
playerHandler = PlayerHandler()

while True:
    print ("Player", playerHandler.turn, "'s turn")
    board.updateUi()
    x = int(input("X:"))
    y = int(input("Y:"))
    board.checkplacement(playerHandler.turn, x, y)
    sleep(1)
    playerHandler.changeTurn()