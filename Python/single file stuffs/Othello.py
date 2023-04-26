import tkinter as tk
from time import sleep



class Board:
    def __init__ (self):
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
        
        

    def placePiece (self, x, y, player):
        print(x,y)
        self.board[x][y] = player
    
    def updateUi(self):
        ## print in terminal, in future will update the ui
        for i in self.board:
            print(i)

    def checkplacement(self, player, x,y):
        if self.getvalue(x,y) != 0:
            return False
        
        ## check the up direction
        def checkup(distup):
            currentPos = [x,y]
            temp = []
            for i in range(0, distup):
                temp.append([x,y])
                currentPos[1] -= 1
                print(distup, currentPos)
                if (self.getvalue(currentPos[0], currentPos[1]) == player):
                    return temp
        

        # print(player, x, y)
        ## find distance from edges
        distup = y 
        distdown = self.height - y
        distright = self.width - x
        distleft = x 

        print (f" distup:{distup} \n distdown:{distdown} \n distright:{distright} \n distleft: {distleft}")

        ## get flips 
        self.flips.append(checkup(distup))



        if len(self.flips) >1:
            for i in self.flips:
                self.placePiece(i[0], i[1], player)
                self.flips = []
                return True
        else:
            self.flips = []
            return False
            
    
    def getvalue(self, x,y):
        try:
            return self.board[x][y]
        except:
            print("fucked")


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
    while True:
        try:
            x = int(input("X:"))
            y = int(input("Y:"))
            if y < 8 or x < 8:
                break
            else:
                print("values need to be from 0-7")
                
        except:
            print("one of the inputs was not a valid number")
        if board.checkplacement(playerHandler.turn, x, y):
            break
        print("was not a valid input")
        
    

    sleep(1)
    playerHandler.changeTurn()