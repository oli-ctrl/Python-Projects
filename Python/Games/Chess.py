import tkinter as tk

## IMPORTANT STUFF
## install this font https://www.dafont.com/chess.font




## piece class that all other pieces inherit from
class piece():
    def __init__(self):
        self.position = None
        self.color = None
        self.type = None
        self.icon = None
        self.moves = []

## Pawn class    
class Pawn(piece):
    ## sets its type and firstmove, which is used to determine if it can move 2 spaces, also inherets from piece
    def __init__(self):
        super().__init__()
        self.type = "pawn"
        self.firstmove = True

    ## sets its icon based on its color (gets from chess font)
    def seticon(self):
        if self.color == "white":
            self.icon = "p"
        else:
            self.icon = "o"

    ## calculates its moves based on its color
    def movecalc(self):
        self.moves = []
        if self.color == "white":
            if self.firstmove == True:
                self.moves.append([0, 2])
                self.moves.append([0, 1])
            else:
                self.moves.append([0, 1])
        else:
            if self.firstmove == True:
                self.moves.append([0, -2])
                self.moves.append([0, -1])
            else:
                self.moves.append([0, -1])
        self.spots = []
        for i in self.moves:
            self.spots.append([self.position[0] + i[0], self.position[1] + i[1]])
        
    ## calculates its attacks based on its color (diagonals when taking a piece)
    def attackcalc(self):
        self.moves = []
        if self.color == "white":
            self.moves.append([1, 1])
            self.moves.append([-1, 1])
        else:
            self.moves.append([1, -1])
            self.moves.append([-1, -1])
        self.attacks = []
        for i in self.moves:
            self.attacks.append([self.position[0] + i[0], self.position[1] + i[1]])
            self.attacks.append(self.spots)

## Rook class 
class Rook(piece):
    def __init__(self):
        super().__init__()
        self.type = "rook"

    ## sets its icon based on its color (gets from chess font)
    def seticon(self):
        if self.color == "white":
            self.icon = "r"
        else:
            self.icon = "t"
    
    ## calculates its moves based, stopping when it hits a piece
    def movecalc(self):
        self.moves = []
        up = True
        down = True
        left = True
        right = True
        self.upmoves = []
        self.downmoves = []
        self.rightmoves = []
        self.leftmoves = []

        ## loops through each direction, stopping when it hits a piece
        for pos in range(1,8):
            if up == True:
                self.upmoves.append([pos, 0])
                for i in board.allpieces:
                    if ([self.position[0] + self.upmoves[-1][0], self.position[1] + self.upmoves[-1][1]]) == i.position:
                        up = False
                        break
            if down == True:
                self.downmoves.append([-pos, 0])
                for i in board.allpieces:
                    if ([self.position[0] + self.downmoves[-1][0], self.position[1] + self.downmoves[-1][1]]) == i.position:
                        down = False
                        break
            if left == True:
                self.leftmoves.append([0, pos])
                for i in board.allpieces:
                    if ([self.position[0] + self.leftmoves[-1][0], self.position[1] + self.leftmoves[-1][1]]) == i.position:
                        left = False
                        break
            if right == True:
                self.rightmoves.append([0, -pos])   
                for i in board.allpieces:
                    if ([self.position[0] + self.rightmoves[-1][0], self.position[1] + self.rightmoves[-1][1]]) == i.position:
                        right = False
                        break

            if self.position[0] + pos > 7:
                up = False
            if self.position[0] - pos < 0:
                down = False
            if self.position[1] + pos > 7:
                left = False
            if self.position[1] - pos < 0:
               right = False
        self.moves = self.upmoves + self.downmoves + self.rightmoves + self.leftmoves
        
        self.spots = []
        for i in self.moves:
            self.spots.append([self.position[0] + i[0], self.position[1] + i[1]])
        
    ## calculates its attacks (same as moves)
    def attackcalc(self):
        self.moves = []
        self.movecalc()
        self.attacks = []
        for i in self.moves:
            self.attacks.append([self.position[0] + i[0], self.position[1] + i[1]])
            self.attacks.append(self.spots)

## Knight class
class Knight(piece):
    def __init__(self):
        super().__init__()
        self.type = "knight"
    def seticon(self):
        if self.color == "white":
            self.icon =  "h"
        else:
            self.icon = "j"
    def movecalc(self):
        self.moves = []
        self.moves.append([1, 2])
        self.moves.append([2, 1])
        self.moves.append([-1, 2])
        self.moves.append([-2, 1])
        self.moves.append([1, -2])
        self.moves.append([2, -1])
        self.moves.append([-1, -2])
        self.moves.append([-2, -1])
        self.spots = []
        for i in self.moves:
            self.spots.append([self.position[0] + i[0], self.position[1] + i[1]])
        
    def attackcalc(self):
        self.moves = []
        self.movecalc()
        self.attacks = []
        for i in self.moves:
            self.attacks.append([self.position[0] + i[0], self.position[1] + i[1]])
            self.attacks.append(self.spots)

## Bishop class
class Bishop(piece):
    def __init__(self):
        super().__init__()
        self.type = "bishop"
    def seticon(self):
        if self.color == "white":
            self.icon = "b"
        else:
            self.icon = "n" 
    def movecalc(self):
        upright = True
        upleft = True
        downright = True
        downleft = True

        self.uprightmoves = []
        self.upleftmoves = []
        self.downrightmoves = []
        self.downleftmoves = []

        for pos in range(1,8):
            if upright == True:
                self.uprightmoves.append([pos, -pos])
                for i in board.allpieces:
                    if ([self.position[0] + self.uprightmoves[-1][0], self.position[1] + self.uprightmoves[-1][1]]) == i.position:
                        upright = False
                        break
            if upleft == True:
                self.upleftmoves.append([pos, pos])
                for i in board.allpieces:
                    if ([self.position[0] + self.upleftmoves[-1][0], self.position[1] + self.upleftmoves[-1][1]]) == i.position:
                        upleft = False
                        break

            if downright == True:
                self.downrightmoves.append([-pos, -pos])
                for i in board.allpieces:
                    if ([self.position[0] + self.downrightmoves[-1][0], self.position[1] + self.downrightmoves[-1][1]]) == i.position:
                        downright = False
                        break

            if downleft == True:
                self.downleftmoves.append([-pos, pos])
                for i in board.allpieces:
                    if ([self.position[0] + self.downleftmoves[-1][0], self.position[1] + self.downleftmoves[-1][1]]) == i.position:
                        downleft = False
                        break
            if self.position[0] + pos > 7 or self.position[1] - pos < 0:
                upright = False
            if self.position[0] + pos > 7 or self.position[1] + pos > 7:
                upleft = False
            if self.position[0] - pos < 0 or self.position[1] - pos < 0:
                downright = False
            if self.position[0] - pos < 0 or self.position[1] + pos > 7:
                downleft = False

        self.moves = self.uprightmoves + self.upleftmoves + self.downrightmoves + self.downleftmoves
        self.spots = []
        for i in self.moves:
            self.spots.append([self.position[0] + i[0], self.position[1] + i[1]])

    def attackcalc(self):
        self.moves = []
        self.movecalc()
        self.attacks = []
        for i in self.moves:
            self.attacks.append([self.position[0] + i[0], self.position[1] + i[1]])
            self.attacks.append(self.spots)

## Queen class    
class Queen(piece):
    def __init__(self):
        super().__init__()
        self.type = "queen"
    def seticon(self):
        if self.color == "white":
            self.icon = "q"
        else:
            self.icon = "w"
    
    ## calculates its moves based on its color (diagonals)
    def movecalc(self):
        self.moves = []
        up = True
        down = True
        left = True
        right = True

        upright = True
        upleft = True
        downright = True
        downleft = True

        self.upmoves = []
        self.downmoves = []
        self.rightmoves = []
        self.leftmoves = []
        
        self.uprightmoves = []
        self.upleftmoves = []
        self.downrightmoves = []
        self.downleftmoves = []

        for pos in range(1,8):
            if up == True:
                self.upmoves.append([pos, 0])
                for i in board.allpieces:
                    if ([self.position[0] + self.upmoves[-1][0], self.position[1] + self.upmoves[-1][1]]) == i.position:
                        up = False
                        break
            if down == True:
                self.downmoves.append([-pos, 0])
                for i in board.allpieces:
                    if ([self.position[0] + self.downmoves[-1][0], self.position[1] + self.downmoves[-1][1]]) == i.position:
                        down = False
                        break
            if left == True:
                self.leftmoves.append([0, pos])
                for i in board.allpieces:
                    if ([self.position[0] + self.leftmoves[-1][0], self.position[1] + self.leftmoves[-1][1]]) == i.position:
                        left = False
                        break
            if right == True:
                self.rightmoves.append([0, -pos])   
                for i in board.allpieces:
                    if ([self.position[0] + self.rightmoves[-1][0], self.position[1] + self.rightmoves[-1][1]]) == i.position:
                        right = False
                        break

            ## diagonals
            if upright == True:
                self.uprightmoves.append([pos, -pos])
                for i in board.allpieces:
                    if ([self.position[0] + self.uprightmoves[-1][0], self.position[1] + self.uprightmoves[-1][1]]) == i.position:
                        upright = False
                        break
            if upleft == True:
                self.upleftmoves.append([pos, pos])
                for i in board.allpieces:
                    if ([self.position[0] + self.upleftmoves[-1][0], self.position[1] + self.upleftmoves[-1][1]]) == i.position:
                        upleft = False
                        break

            if downright == True:
                self.downrightmoves.append([-pos, -pos])
                for i in board.allpieces:
                    if ([self.position[0] + self.downrightmoves[-1][0], self.position[1] + self.downrightmoves[-1][1]]) == i.position:
                        downright = False
                        break

            if downleft == True:
                self.downleftmoves.append([-pos, pos])
                for i in board.allpieces:
                    if ([self.position[0] + self.downleftmoves[-1][0], self.position[1] + self.downleftmoves[-1][1]]) == i.position:
                        downleft = False
                        break
            
            if self.position[0] + pos > 7:
                up = False
            if self.position[0] - pos < 0:
                down = False
            if self.position[1] + pos > 7:
                left = False
            if self.position[1] - pos < 0:
               right = False
            if self.position[0] + pos > 7 or self.position[1] - pos < 0:
                upright = False
            if self.position[0] + pos > 7 or self.position[1] + pos > 7:
                upleft = False
            if self.position[0] - pos < 0 or self.position[1] - pos < 0:
                downright = False
            if self.position[0] - pos < 0 or self.position[1] + pos > 7:
                downleft = False


        self.moves = self.upmoves + self.downmoves + self.rightmoves + self.leftmoves + self.uprightmoves + self.upleftmoves + self.downrightmoves + self.downleftmoves
        self.spots = []
        for i in self.moves:
            self.spots.append([self.position[0] + i[0], self.position[1] + i[1]])
        
    def attackcalc(self):
        self.moves = []
        self.movecalc()
        self.attacks = []
        for i in self.moves:
            self.attacks.append([self.position[0] + i[0], self.position[1] + i[1]])
        self.attacks = self.attacks + self.spots

## king class
class King(piece):
    def __init__(self):
        super().__init__()
        self.type = "king"

    ## sets its icon based on its color (gets from chess font)
    def seticon(self):
        if self.color == "white":
            self.icon = "k"
        else:
            self.icon = "l"
    
    ## calculates its moves based on its color (diagonals)
    def movecalc(self):
        self.moves = []
        self.moves.append([1, 1])
        self.moves.append([-1, 1])
        self.moves.append([1, -1])
        self.moves.append([-1, -1])
        self.moves.append([0, 1])
        self.moves.append([0, -1])
        self.moves.append([1, 0])
        self.moves.append([-1, 0])
        self.spots = []
        for i in self.moves:
            self.spots.append([self.position[0] + i[0], self.position[1] + i[1]])
    
    ## calculates its attacks (same as moves)
    def attackcalc(self):
        self.moves = []
        self.movecalc()
        self.attacks = []
        for i in self.moves:
            self.attacks.append([self.position[0] + i[0], self.position[1] + i[1]])
            self.attacks.append(self.spots)

class Board():
    def __init__(self):
        self.state = "playing"
        self.setup()
        

    ## sets up the peices
    def setup(self):
        self.state = "playing"
        self.turn = "white"
        ## setup the board
        self.allpieces = []
        self.blacktakes = []
        self.whitetakes = []
        #pawns
        for i in range(8):
            self.allpieces.append(Pawn())
            self.allpieces[i].position = [i, 1]
            self.allpieces[i].color = "white"
        for i in range(8):
            self.allpieces.append(Pawn())
            self.allpieces[i+8].position = [i, 6]
            self.allpieces[i+8].color = "black"
        
        #knights
        self.allpieces.append(Knight())
        self.allpieces[16].position = [1, 0]
        self.allpieces[16].color = "white"
        self.allpieces.append(Knight())
        self.allpieces[17].position = [6, 0]
        self.allpieces[17].color = "white"
        self.allpieces.append(Knight())
        self.allpieces[18].position = [1, 7]
        self.allpieces[18].color = "black"
        self.allpieces.append(Knight())
        self.allpieces[19].position = [6, 7]
        self.allpieces[19].color = "black"

        #rooks
        self.allpieces.append(Rook())
        self.allpieces[20].position = [0, 0]
        self.allpieces[20].color = "white"
        self.allpieces.append(Rook())
        self.allpieces[21].position = [7, 0]
        self.allpieces[21].color = "white"
        self.allpieces.append(Rook())
        self.allpieces[22].position = [0, 7]
        self.allpieces[22].color = "black"
        self.allpieces.append(Rook())
        self.allpieces[23].position = [7, 7]
        self.allpieces[23].color = "black"

        #bishops
        self.allpieces.append(Bishop())
        self.allpieces[24].position = [2, 0]
        self.allpieces[24].color = "white"
        self.allpieces.append(Bishop())
        self.allpieces[25].position = [5, 0]
        self.allpieces[25].color = "white"
        self.allpieces.append(Bishop())
        self.allpieces[26].position = [2, 7]
        self.allpieces[26].color = "black"
        self.allpieces.append(Bishop())
        self.allpieces[27].position = [5, 7]
        self.allpieces[27].color = "black"

        #kings and queens
        self.allpieces.append(Queen())
        self.allpieces[28].position = [3, 0]
        self.allpieces[28].color = "white"
        self.allpieces.append(Queen())
        self.allpieces[29].position = [3, 7]
        self.allpieces[29].color = "black"
        self.allpieces.append(King())
        self.allpieces[30].position = [4, 0]
        self.allpieces[30].color = "white"
        self.allpieces.append(King())
        self.allpieces[31].position = [4, 7]
        self.allpieces[31].color = "black"
        for i in self.allpieces:
            i.seticon()
   
    ## removes a piece from the board
    def removepiece(self, piece):
        if piece.type == "king":
            print("game over")
            if piece.color == "white":
                self.state = "black wins"
            else:
                self.state = "white wins"
            board.changeTurn()
        if piece.color == "white":
            self.whitetakes.append(piece.icon)
        else:
            self.blacktakes.append(piece.icon)
        self.allpieces.remove(piece)


    def checkpromotable(self, piece, position):
        if piece.type == "pawn":
            if position[1] == 7 or position[1] == 0:
                self.allpieces.remove(piece)
                self.allpieces.append(Queen())
                self.allpieces[-1].position = position
                self.allpieces[-1].color = piece.color
                self.allpieces[-1].seticon()

    ## moves a piece to a position (+ some other logic)
    def movepiece(self, piece, position):              
        ## check if it is the right turn
        if piece.color != self.turn:
            print(f"not your turn, {self.turn}")
            return False
        print("moving piece")
        print (position)
        piece.movecalc()
        piece.attackcalc()
        for places in piece.attacks + piece.spots:
            if places == position:
                print ("valid move")
                for pieces in self.allpieces:
                    if pieces.position == position:
                        print("Found a piece at that position")
                        if pieces.color == piece.color:
                            print("Can't move there, same piece")
                            return False
                        else:
                            if position in piece.attacks:
                                print("Can move there, attacking")
                                self.removepiece(pieces)
                                piece.position = position
                                self.changeTurn()
                                self.checkpromotable(piece, position)
                                return True
                            print("cant attack, not in attack list")
                            return False
                for location in piece.spots:
                    if location == position:
                        piece.position = position
                        try:
                            piece.firstmove = False
                        except:
                            pass
                        self.changeTurn()
                        self.checkpromotable(piece, position)
                        return True

    ## super simple function for changing turns       
    def changeTurn(self):
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"
        print("turn changed to " + self.turn)
        return True

## class for managing the window
class twindow():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Chess")
        self.window.geometry("800x910")
        self.window.resizable(0, 0)
        self.window.configure(background="white")
        self.buttons = []
        self.selected = None
    
    def createboard(self):
        self.boardpart = tk.Frame(width=800, height=800, bg="white", border=4, relief="solid")
        for y in range (0,8):
            for x in range (0,8):
                if (x+y)%2 == 0:
                    self.buttons.append(tk.Button(master = self.boardpart, 
                                                  text="", 
                                                  width=3,
                                                  height=3, 
                                                  bg="white",
                                                  fg="black", 
                                                  font=("Chess",17),
                                                  command=lambda x=x, y=y: self.buttoncallback(x, y)))
                else:
                    self.buttons.append(tk.Button(master = self.boardpart, 
                                                  text="", 
                                                  width=3,
                                                  height=3, 
                                                  bg="grey",
                                                  fg="black",
                                                  font=("Chess", 17),
                                                  
                                                  command=lambda x=x, y=y,: self.buttoncallback(x, y)))
                self.buttons[-1].grid(row=y, column=x)

        self.turnlabel = tk.Label(width=800, height=1, bg="white", font = ("lucida", 20), text="White's turn", anchor="center", border=4, relief="solid")
        self.resetbutton = tk.Button(master = self.window,
                                     text="Reset",
                                     width=10,
                                     height=2,
                                     bg="white",
                                     fg="black",
                                     command=lambda:[board.setup(), self.displaypieces(board)])
        
        self.takenframe = tk.Frame(width=800, height=50, bg="white", border=4, relief="solid")
        self.blacktaken = tk.Label(master = self.takenframe,
                                     width=50,
                                     height=1,
                                     bg="black",
                                     fg="white",
                                     font=("Chess", 17),
                                     anchor="e")
        self.whitetaken = tk.Label(master = self.takenframe,
                                        width=50,
                                        height=1,
                                        bg="white",
                                        fg="black",
                                        font=("Chess", 17),
                                        anchor="e")
        ## pack everything
        self.blacktaken.pack()
        self.whitetaken.pack()
        self.turnlabel.pack()
        self.boardpart.pack()
        self.takenframe.pack()
        self.resetbutton.pack()
        return True

    def buttoncallback(self, x, y):
        self.displaypieces(board)
        if board.state != "playing":
            return False
        self.buttons[x+y*8].configure(fg="red")
        for i in board.allpieces:
            if i.position == [x, y]:
                    print (f"button {x}, {y} pressed, {i}")
                    print (f"selected {self.selected}")
                    if self.selected == None:
                        print("no piece selected")
                        self.selected = i
                    elif self.selected.color == i.color:
                        print("same color piece selected, swapping ")
                        self.selected = i
                    else:
                        print("different color piece selected, attacking")
                        board.movepiece(self.selected, [x, y])
                        self.selected = None
                        self.displaypieces(board)
                    return True
        else:
            if self.selected == None:
                print (f"button {x}, {y} pressed, no piece")
            else:
                print(f"trying to move {self.selected}")
                print (f"button {x}, {y} pressed, {self.selected.type}")
                board.movepiece(self.selected, [x, y])
                self.selected = None
                self.displaypieces(board)
        return True
    
    def displaypieces(self, board):
        allpeicedisplay = []
        for i in self.buttons: 
            i.config(text="", fg="black")
        for piece in board.allpieces:
            self.buttons[piece.position[0]+piece.position[1]*8].config(text=piece.icon)
            allpeicedisplay.append((piece.position, piece.type, piece.color, piece.icon))
        print (allpeicedisplay)
        if board.turn == "white":
            self.turnlabel.config(text="White's turn", fg="black", bg="white")
        else:
            self.turnlabel.config(text="Black's turn", fg="white", bg="black")

        self.blacktaken.config(text=board.blacktakes)
        self.whitetaken.config(text=board.whitetakes)
        if board.state != "playing":
            self.turnlabel.config(text=board.state)

        return True


display = twindow()
display.createboard()
board = Board()


display.displaypieces(board)
display.window.mainloop()