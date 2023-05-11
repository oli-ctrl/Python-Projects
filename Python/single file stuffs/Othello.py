import tkinter as tk
from time import sleep



class Board:
    def __init__ (self, playercontrol):
        self.width = 8
        self.height= 8
        self.flips = []
        ## make a player handler
        self.player = playercontrol
        ## make an empty board
        self.resetBoard()

       
    def resetBoard(self):
        self.player.reset()
        self.board = [[0 for width in range(self.width)] for height in range(self.height)]
        self.board[3][3] = 1
        self.board[4][4] = 1
        self.board[3][4] = 2
        self.board[4][3] = 2
    
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
        if self.flips == [[],[],[],[],[],[],[],[]]:
            print("no flips found")
            return
        ## place the piece
        for i in self.flips:
            if i != []:
                print(f"placed piece ({self.player.turn}) at  ({x},{y})")
                self.board[x][y] = self.player.turn
                for j in i :
                    self.board[j[0]][j[1]] = self.player.turn
                    print(f"placed flip peice at ({j[0]},{j[1]})")
                    self.player.changeTurn()
        return
    
    def checkPlaceable(self):
        print("checking placeable")
        for x in range(self.width):
            for y in range(self.height):
                flips = []
                flips.append(self.checkDir([x,y], [0,1]))
                flips.append(self.checkDir([x,y], [0,-1]))
                flips.append(self.checkDir([x,y], [1,0]))
                flips.append(self.checkDir([x,y], [-1,0]))
                flips.append(self.checkDir([x,y], [1,1]))
                flips.append(self.checkDir([x,y], [-1,-1]))
                flips.append(self.checkDir([x,y], [1,-1]))
                flips.append(self.checkDir([x,y], [-1,1]))
                if flips != [[],[],[],[],[],[],[],[]]:
                    print(f"found placeable at ({x},{y})")
            
                    return True
        return flips
    
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
    
    def reset(self):
        self.turn = 1

allbuttons = []
count = 0

playerHandler = PlayerHandler()
board = Board(playerHandler)


## __game loop for playing the game in the terminal (if you use this comment everything below out) missing some features__

# while True:
#     board.updateUi()
#     print(f"player {playerHandler.turn}'s turn")
#     try:
#         x = int(input("x: ")) -1  
#         y = int(input("y: ")) -1 
#         board.placePiece(y,x)
#         print("player 1 peices: " + str(board.countPiece(1)))
#         print("player 2 peices: " + str(board.countPiece(2)))
#     except:
#         print("invalid input")
#         continue
    

#     if board.countPiece(1) + board.countPiece(2) == 64:
#         print("game over")
#         if board.countPiece(1) == board.countPiece(2):
#             print("Its a Tie ")
#             break
#         elif board.countPiece(1) > board.countPiece(2):
#             print("player 1 wins")
#             break
#         print("player 2 wins")
#         break
#     sleep(1)



## __game loop for playing the game in the ui (if you use this comment everything above out)__

## create the window
window = tk.Tk()
window.title("Othello")
window.geometry("670x820")
window.resizable(False,False)



## update ui, 
def updateUi():
    sleep(0.1)
    place = 0
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
    score1.config(text="Black: " + str(board.countPiece(1)))
    score2.config(text="White: " + str(board.countPiece(2)))
    if playerHandler.turn==1:
        score1.config(bg="lightgreen")
        score2.config(bg="white")
    else:
        score1.config(bg="white")
        score2.config(bg="lightgreen")
    
    



## create board frame 
boardview = tk.Frame(window)
boardview.config(bg="green")
boardview.place(x=10, y=70)
boardview.config(border=6, bg="black", width=640)

# score frame
scores = tk.Frame(window)
scores.place(x=20,y=10)
scores.config(border=2, bg="black", 
              width=640, 
              height=50)

score1 = tk.Label(scores, 
                  text="Black: " + str(board.countPiece(1)), 
                  padx=60, 
                  font=("Courier", 30))
score1.grid(row=0, column=0)

score2 = tk.Label(scores, 
                  text="White: " + str(board.countPiece(2)), 
                  padx=60, 
                  font=("Courier", 30))
score2.grid(row=0, column=1)


# reset and quit buttons
bottom = tk.Frame(window)
bottom.place(x=40, y=780)
bottom.config(border=2, bg="black", width=640, height=50)

reset = tk.Button(bottom, 
                  text="Reset", 
                  command=lambda: [board.resetBoard(), updateUi()],
                  width=40,
                  height=1)
reset.grid(row=0, column=0)

quit = tk.Button(bottom, 
                 text="Quit", 
                 command=lambda: window.destroy(),
                 width=40,
                 height=1)
quit.grid(row=0, column=1)


## make the game buttons
for x in range(8):
    for y in range (8):
        allbuttons.append(tk.Button(boardview, 
                                    background="green",
                                    height=5, 
                                    width=10,
                                    command=lambda x=x, y=y: buttonPress(x,y)))
        allbuttons[count].grid(row=x, column=y)
        count += 1

def buttonPress(x,y):
    print(x,y)
    board.placePiece(x,y)
    if board.checkPlaceable() == []:
        playerHandler.changeTurn()
    if board.checkPlaceable() == []:
        print("game over")
        if board.countPiece(1) == board.countPiece(2):
            print("Its a Tie ")
        elif board.countPiece(1) > board.countPiece(2):
            print("player 1 wins")
        else:
            print("player 2 wins")
        return
    updateUi()


updateUi()

window.mainloop()