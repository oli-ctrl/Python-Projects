import tkinter as tk
from time import sleep



class Board:
    def __init__ (self, playercontrol):
        self.width = 8
        self.height= 8
        self.flips = []
        ## make an empty board
        self.board = [[0 for width in range(self.width)] for height in range(self.height)]
        ## place starting pieces
        self.board[3][3] = 1
        self.board[4][4] = 1
        self.board[3][4] = 2
        self.board[4][3] = 2
        self.player = playercontrol
       
    def countPiece(self, piece):
        count = 0
        for i in self.board:
            for j in i:
                if j == piece:
                    count += 1
        return count

    def placePiece (self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            print("out of bounds")
            return 
        elif self.board[x][y] != 0:
            print("place not empty")
            return
        ## check all directions 
        self.flips = []
        self.flips.append(self.checkDir([x,y], [0,1]))
        self.flips.append(self.checkDir([x,y], [0,-1]))
        self.flips.append(self.checkDir([x,y], [1,0]))
        self.flips.append(self.checkDir([x,y], [-1,0]))
        self.flips.append(self.checkDir([x,y], [1,1]))
        self.flips.append(self.checkDir([x,y], [-1,-1]))
        self.flips.append(self.checkDir([x,y], [1,-1]))
        self.flips.append(self.checkDir([x,y], [-1,1]))
        ## if no flips are found, return
        for i in self.flips:
            if i != []:
                print(f"placed piece ({self.player.turn}) at  ({x},{y})")
                self.board[x][y] = self.player.turn
                for j in i :
                    self.board[j[0]][j[1]] = self.player.turn
                    print(f"placed flip peice at ({j[0]},{j[1]})")
                self.player.changeTurn()
                return 
        print("Not a valid move")
        return
    
    def updateUi(self):
        ## print in terminal, in future will update the ui
        for i in self.board:
            print(i)

    def checkDir(self, startpos, dir):
        pos = startpos
        flips = []
        while True:
            ## move in the direction
            pos = [pos[0] + dir[0], pos[1] + dir[1]]
            ## check if the position is out of bounds
            if pos[0] < 0 or pos[0] >= self.width or pos[1] < 0 or pos[1] >= self.height:
                ## print("hit edge")
                return []
            ## check if the position is empty 
            if self.board[pos[0]][pos[1]] == 0:
                ## print("hit empty")
                return []
            if self.board[pos[0]][pos[1]] == self.player.turn:
                ## print("found")
                return flips
            flips.append(pos)


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

playerHandler = PlayerHandler()
board = Board(playerHandler)

while True:
    board.updateUi()
    print(f"player {playerHandler.turn}'s turn")
    try:
        x = int(input("x: ")) -1  
        y = int(input("y: ")) -1 
        board.placePiece(y,x)
        print("player 1 peices: " + str(board.countPiece(1)))
        print("player 2 peices: " + str(board.countPiece(2)))
    except:
        print("invalid input")
        continue
    

    if board.countPiece(1) + board.countPiece(2) == 64:
        print("game over")
        if board.countPiece(1) > board.countPiece(2):
            print("player 1 wins")
        elif board.countPiece(1) < board.countPiece(2):
            print("player 2 wins")
        break
    sleep(1)