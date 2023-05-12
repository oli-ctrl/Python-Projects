import tkinter as tk
from time import sleep
from random import randint

## big class for checking placeable, placing, and flipping aswell as the board and managing turns
class Board:
    def __init__(self):
        self.resetBoard()
        
    ## reset the board to the starting position (also called on init)
    def resetBoard(self):
        global playing
        playing = True
        self.turn = 1
        self.board = [[0 for width in range(8)] for height in range(8)]
        self.board[3][3] = 1
        self.board[4][4] = 1
        self.board[3][4] = 2
        self.board[4][3] = 2
        print("board reset")

    ## change the turn
    def changeTurn(self):
        if self.turn == 1:
            self.turn = 2
        else: 
            self.turn = 1 
        print(f"turn changed to: ({self.turn})")

    ## count the number of pieces of a type
    def countPiece(self, piece):
        count = 0
        for i in self.board:
            for j in i:
                if j == piece:
                    count += 1
        if len(str(count)) == 1:
            return "0" + str(count)
        print(f"counted ({count}) peices of type ({piece})")
        return count

    ## place a peice checking in all directions and flipping if needed
    def placePiece (self, x, y):
        ## check if the place is empty and in bounds
        if x < 0 or x >= 8 or y < 0 or y >= 8:
            print("out of bounds")
            return
        elif self.board[x][y] != 0:
            print("place not empty")
            return
        
        ## check all directions 
        self.flips = []
        for direction in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]:
            self.flips.append(self.checkDir([x,y], direction))

        ## if no flips are found, return
        if self.flips == [[],[],[],[],[],[],[],[]]:
            print("no flips found")
            return False
        
        ## place the piece and any following flips
        for i in self.flips:
            if i != []:
                print(f"placed piece ({self.turn}) at: ({x},{y})")
                self.board[x][y] = self.turn
                for j in i :
                    self.board[j[0]][j[1]] = self.turn
                    print(f"placed flip peice at: ({j[0]},{j[1]})")
        return True

    ## iterate through the whole board to find a placeable peice (also checks if the board is full). used for checking if the game is over
    def checkPlaceable(self):
        if int(self.countPiece(0)) == 0:
            print("Board full")
            return False
        for x in range(8):
            for y in range(8):
                if self.board[x][y] == 0:
                    for direction in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]:
                        if self.checkDir([x,y], direction)!= []:
                            print(f"found a placeable peice for ({board.turn}) at: ({x},{y})")
                            return True
        return False
                
    ## check a direction for flips
    def checkDir(self, startpos, dir):
        pos = startpos
        flips = []
        while True:
            ## move in the direction
            pos = [pos[0] + dir[0], pos[1] + dir[1]]
            ## check if the position is edge of the board
            if pos[0] < 0 or pos[0] >= 8 or pos[1] < 0 or pos[1] >= 8:
                return []
            ## check if the position is empty 
            if self.board[pos[0]][pos[1]] == 0:
                return []
            ## check if the position is the same as the turn
            if self.board[pos[0]][pos[1]] == self.turn:
                return flips
            flips.append(pos)

## make the games board
def createButtons():
    ## create board frame 
    boardview = tk.Frame(window)
    boardview.config(bg="green")
    boardview.place(x=10, y=70)
    boardview.config(border=6, bg="black", width=640)
    ## create buttons
    count = 0
    allbuttons = []
    for x in range(8):
        for y in range (8):
            allbuttons.append(tk.Button(boardview, 
                                        background="green",
                                        height=5, 
                                        width=10,
                                        command=lambda x=x, y=y: makeTurn(x,y)))
            allbuttons[count].grid(row=x, column=y)
            count += 1
    return allbuttons

## create all the ui apart from the board      
def createUi():
    # score counters
    scores = tk.Frame(window)
    scores.place(x=25,y=10)
    scores.config(border=2, bg="black", 
                width=640, 
                height=50)
    
    score1 = tk.Label(scores, 
                    text="Black: " + str(board.countPiece(1)), 
                    padx=45, 
                    font=("Courier", 30))
    score1.grid(row=0, column=0)

    score2 = tk.Label(scores, 
                    text="White: " + str(board.countPiece(2)), 
                    padx=45, 
                    font=("Courier", 30))
    score2.grid(row=0, column=1)

    # bottom buttons
    bottom = tk.Frame(window)
    bottom.place(x=40, y=780)
    bottom.config(border=2, bg="black", width=640, height=50)

    ## reset and quit buttons
    # reset button (calls resetBoard() and updateUi())
    reset = tk.Button(bottom, 
                     text="Reset", 
                     command=lambda: [board.resetBoard(), updateUi()],
                     width=40,
                     height=1)
    reset.grid(row=0, column=0)

    ## quit button (calls window.destroy()) 
    quit = tk.Button(bottom, 
                    text="Quit", 
                    command=lambda: window.destroy(),
                    width=40,
                    height=1)
    quit.grid(row=0, column=1)

    ## return all the ui elements
    return score1, score2, reset, quit

## update ui, 
def updateUi():
    global allbuttons
    sleep(0.1)
    place = 0
    ## update board
    for i in range(8):
        for j in range(8):
            if board.board[i][j] == 1:
                allbuttons[place].config(bg="black")
            elif board.board[i][j] == 2:
                allbuttons[place].config(bg="white")
            else:
                if (i + j) % 2 == 0:
                    allbuttons[place].config(bg="green")
                else:
                    allbuttons[place].config(bg="darkgreen")
            place +=1
    ## display current score
    score1.config(text="Black: " + str(board.countPiece(1)))
    score2.config(text="White: " + str(board.countPiece(2)))
    ## display current turn
    if board.turn==1:
        score1.config(bg="lightgreen")
        score2.config(bg="white")
    else:
        score1.config(bg="white")
        score2.config(bg="lightgreen")

## what happens a turn is made
def makeTurn(x,y):
    global playing
    print(f"attempting turn at: ({x},{y})")
    if playing:
        if board.placePiece(x,y):
            print("valid move")
            board.changeTurn()
            updateUi()
            if board.checkPlaceable():
                print(f"found a valid move for: ({board.turn})")
                return
            else:
                ## if no move is found for the current player, change turn
                print(f"no valid moves for: ({board.turn})")
                if board.turn == 1:
                    board.turn = 2
                    score1.config(bg="White")
                    score2.config(bg="Green")
                else:
                    board.turn = 1
                    score1.config(bg="Green")
                    score2.config(bg="White")
                
                ## if no move is found for the other player, end the game
                if not board.checkPlaceable():
                    print("game over")
                    if int(board.countPiece(1)) == int(board.countPiece(2)):
                        score1.config(bg="yellow")
                        score2.config(bg="yellow")
                    elif int(board.countPiece(1)) > int(board.countPiece(2)):
                        score1.config(bg="red")
                        score2.config(bg="green")
                    elif int(board.countPiece(1)) < int(board.countPiece(2)):
                        score1.config(bg="green")
                        score2.config(bg="red")
                    playing = False
                else:
                    print("found alternate player turn")
                return

## create the window and board
window = tk.Tk()
window.title("Othello")
window.geometry("670x820")
window.resizable(False,False)
board = Board()

## create the ui elements and colour the board (by calling updateUi())
allbuttons = createButtons()
score1, score2, reset, quit = createUi()

updateUi()

window.mainloop()