try:
    import tkinter as tk
except:
    raise ImportError("tkinter not found, please install it")

from time import sleep
from random import randint
import base64 as b64
try:
    import ctypes as ct
except:
    print("ctypes not found, no dark mode support")

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
        # print("board reset")

    ## change the turn
    def changeTurn(self):
        if self.turn == 1:
            self.turn = 2
        else: 
            self.turn = 1 
        # print(f"turn changed to: ({self.turn})")

    ## count the number of pieces of a type
    def countPiece(self, piece):
        count = 0
        for i in self.board:
            for j in i:
                if j == piece:
                    count += 1
        if len(str(count)) == 1:
            return "0" + str(count)
        # print(f"counted ({count}) peices of type ({piece})")
        return count

    ## place a peice checking in all directions and flipping if needed
    def placePiece (self, x, y):
        ## check if the place is empty and in bounds
        if x < 0 or x >= 8 or y < 0 or y >= 8:
            # print("out of bounds")
            return
        elif self.board[x][y] != 0:
            # print("place not empty")
            return
        
        ## check all directions 
        self.flips = []
        for direction in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]:
            self.flips.append(self.checkDir([x,y], direction))

        ## if no flips are found, return
        if self.flips == [[],[],[],[],[],[],[],[]]:
            # print("no flips found")
            return False
        
        ## place the piece and any following flips
        for i in self.flips:
            if i != []:
                # print(f"placed piece ({self.turn}) at: ({x},{y})")
                self.board[x][y] = self.turn
                for j in i :
                    self.board[j[0]][j[1]] = self.turn
                    # print(f"placed flip peice at: ({j[0]},{j[1]})")
        board.changeTurn()
        return True

    ## iterate through the whole board to find a placeable peice (also checks if the board is full). used for checking if the game is over
    def checkPlaceable(self):
        if int(self.countPiece(0)) == 0:
            # print("Board full")
            return False
        for x in range(8):
            for y in range(8):
                if self.board[x][y] == 0:
                    for direction in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]:
                        if self.checkDir([x,y], direction)!= []:
                            # print(f"found a placeable peice for ({board.turn}) at: ({x},{y})")
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
                                        height=74, 
                                        width=74,
                                        bd=2,
                                        fg="white",
                                        image=darkgreen,
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
    bottom.place(x=40, y=730)
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
    showmoves = tk.Button(bottom, 
                    text="Show Moves", 
                    command=lambda: toggleShowMoves(),
                    width=40,
                    height=1)
    showmoves.grid(row=0, column=2)

    ## return all the ui elements
    return score1, score2, reset, showmoves

## toggles show moves
def toggleShowMoves():
    global showmovesbool
    if showmovesbool:
        showmovesbool = False
    else:
        showmovesbool = True
    updateUi()
    return showmovesbool

## update ui, 
def updateUi():
    global allbuttons
    global showmovesbool
    sleep(0.1)
    place = 0
    ## update board
    for i in range(8):
        for j in range(8):
            ## set the button to the correct colour
            if (i + j) % 2 == 0:
                allbuttons[place].config(bg="#0CBF18",
                                            image=lightgreen,
                                            activebackground="#0CBF18")              
            else:
                allbuttons[place].config(bg="#087A0F",
                                            image=darkgreen,
                                            activebackground="#087A0F")
            ## place peices on the board
            if board.board[i][j] == 1:
                allbuttons[place].config(image=black)
            elif board.board[i][j] == 2:
                allbuttons[place].config(image=white)
            ## if showmoves is true, show all possible moves
            if showmovesbool:
                for direction in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]:
                    if board.checkDir([i,j], direction) != []:
                        if board.board[i][j] == 0:
                            if board.turn == 1:
                                allbuttons[place].config(image=blackplace)
                            else:
                                allbuttons[place].config(image=whiteplace)
            place +=1
    ## display current score
    if playing:
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
    # print(f"attempting turn at: ({x},{y})")
    if playing:
        if board.placePiece(x,y):
            updateUi()
            # print("valid move")
            if board.checkPlaceable():
                # print(f"found a valid move for: ({board.turn})")
                pass
            else:
                ## if no move is found for the current player, change turn
                # print(f"no valid moves for: ({board.turn})")
                if board.turn == 1:
                    board.turn = 2
                    updateUi()
                    score1.config(bg="lightgreen")
                    score2.config(bg="pink")
                else:
                    board.turn = 1
                    updateUi()
                    score1.config(bg="lightgreen")
                    score2.config(bg="pink")
                
                ## if no move is found for the other player, end the game
                if not board.checkPlaceable():
                    # print("game over")
                    if int(board.countPiece(1)) == int(board.countPiece(2)):
                        score1.config(bg="yellow")
                        score2.config(bg="yellow")
                    if int(board.countPiece(1)) > int(board.countPiece(2)):
                        score1.config(bg="Green")
                        score2.config(bg="Red")
                    if int(board.countPiece(1)) < int(board.countPiece(2)):
                        score1.config(bg="Red")
                        score2.config(bg="Green")
                    playing = False
                else:
                    # print("found alternate player turn")
                    pass
            return
    # print("game over already")

def darkTitleBar(window):
    try:
        ## thank you (https://gist.github.com/Olikonsti/879edbf69b801d8519bf25e804cec0aa)
        window.update()
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
        get_parent = ct.windll.user32.GetParent
        hwnd = get_parent(window.winfo_id())
        rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
        value = 2
        value = ct.c_int(value)
        set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))
        #Changes the window size
        window.geometry(str(window.winfo_width()+1) + "x" + str(window.winfo_height()+1))
        #Returns to original size
        window.geometry(str(window.winfo_width()-1) + "x" + str(window.winfo_height()-1))
    except:
        print("Dark mode not supported")

## create the window and board
window = tk.Tk()
window.title("Othello")
window.geometry("670x770")
window.resizable(False,False)
board = Board()
window.config(bg="gray21")
## make the bar at the top dark
darkTitleBar(window)


## images
black = tk.PhotoImage(data=b64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAACXBIWXMAAA7EAAAOxAGVKw4bAAADF0lEQVR4nO2bMWgUQRSGv5tiEREJwUYNohIOOVRCtAgWwSJYRBALQQmHSOpgYWFhIVhIKiuRICmsRBAsRFREg6SwUCEKgqcBxQii0ZyiIiaaU4t3y+mRvbu925k3m/ODvziS4v/f7s7szL7JYB8DZIFeYBuwEVgHdAAryn+fB74A74HXQAF4XNa8A4+JsxoYAi4Bs8DvJvUdmACOIYXznn7gIvCN5kNHqQRMIoUNXAVqlH3AfZIPHaUZYAQPCtGDXBVXwav1AthvPeUSBMAo8DOGWZu6igysTugGHloO1Iw+II+iVQaAonLQWioBJ2yFPwQseBCyEZ1F3i8SI48/z3ujGk+qCAdSGD7UuVaL0I+8jWkHaUWnmg2/gdZeY31RCRm/YhEA9zwwn5Q+EXMtcdID00lrggbHgxzpme7i6nAjBbjtgVFbeoss1SMZ8MCkbdV8U9Rc2blSkYi7oMcDc640slQBxjww5kqF6vABfq/ybGgnVObF3UBndVWWOQehUoC9ika0GATIlH88AbbqeVFjvUGmhJy2EyX6DDL9Jbp7kiJ2GGCLtgtFsgbYpO1CkW6Dw/10D+kIB8G2xQCrtE1oYoBFbROa/C8A8FHbhCYGaUtpV+YM8o29XXllgGltF4o8M8AU8EvbiRKPwuVwgfZcE6wNV4F3VG3o8BR4FxbguqYTJW78/SNAemy0Nypdqg8qGyE/gMtNVDGtTAMP4N+doDHaZzYYJyLrLfRvTdv6CqyJqswuDwza1mhU+JBrHpi0pVmkTb8mWdLfGBWl4XrhQ5Zji8wkMbb/A9y2v9vWZ6THORZZpLtK23wSGoobPmQP6W+YOt1s+JAh0tsqe56EPvsNp7AIF5IKH5InPY9DYle+mkFkRNUOGKUS0hxt9Wt3Dmmo0A5brSLS2u+ElcAZ/BkXbgJdVhNH0ItuV/kMDq96FKZswuVj8QY4ipw99gaDvDhdwc5sUULutjwenBitRydwBClGK3uNC8Bd4Diw2YbRTP1/aRmDzBzbqRyf70IaM8LehEXkI+0c8BJ4jhydn8Ly8fk/aXUsRbNKhZYAAAAASUVORK5CYII="))
white = tk.PhotoImage(data=b64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAACXBIWXMAAA7EAAAOxAGVKw4bAAADvklEQVR4nO2bX2iVZRzHP7/3YowQGRJRJuJALEbFVIrwYoiMXWiNLgaTsoJuIhJvvDHvduOuuiqJGGIEiUQKEUuiUJYolKGC0GqkbEEkuoWNwjW3fbt4zrtztr07jO193t92jp+rc56X8/L9/t7nOe/z5/czIiMpAbYBO4BngS3ARqAJaAQSYAIYB+4AvwODwHXguplNxNRnMW4qaT3wEvAysAd4bJm3mgAuA/3AWTMbzkVgLCS1SfpM0r/Kn2lJA5JeldTg7XUOkjol/RDB9GKMSDroHghJraWn4sVNSa94GG+Q1CvpgaP5Sr6UtLEo81slXXE2nMVdSZ2xzbdLGnM2Wo1pSUdjmd8v6T9ng0vlA4X5R27mD2j1jPel0qc8giCpS2vPfMpxrSQIChOb+84mVkpPNY+LToUlbQausPxp7GphBnjNzE5nXcwMgMIM6wKwK6KwIrkHbM9aSyw2Po5QO+YhrDxPKOP/YEEPkNQCXANW14IjH940s08rG7IC8C3QXpikYrkNPGVm42nDnC4hqZ3aNQ/wOHCwsmFOD5A0ALQVqciBv4DmtBfM9gBJrdS+eYANwBvpl8oh8HbxWtx4N/1gMPve/5MQnXrheTP7Ke0Bu6kv8wDdUB4C+xyFeLEXykPgBvCMqxwfnkwU9vBbvJU48WICtLL4mqDW2ZkAT3urcGRbAjR7q3Bka0I4qKxXmhJgvbcKTxJgnbcITxJgyluEJw8DQFgf1y0JIS2lXhlNgJveKhwZToAhbxWO/JIAVwmnJ/XItXQ5PEh9rgmeSFeB37nK8OFnM7udBqDfVYoPX0N5H+A8MOqnxYUzUAqAmU0Cn7vKKZYh4EeYuxP0EfXzNugzsxlYeDT2DdDhIqk4/iEcjY3Cwr3AqukkNcKHqXnIPh7/ipDpXYvcIRyP30sbsnaDDxPS1GuR9yrNQ0YAzGwI6C1MUnF8D3wyv7FaktRF4IW4mgpjHNhpZr/Nv5B5IFKaF7xOyK6qBd7JMg9VToRKQ6EbmIylqiCOmdmpZf9aoURlrabKfqyc8oXf0toLwklFyBhfK+ny+Tz5jCDslfS3s7lqTEvqUQzzFUFokXTD12cmY5K6ohmfF4RHJL2v1fO/cE7SpkLMzwvEDkmXHI2PqKinXiUIiUJVSZHD4g9JhyQ1upqvpBSIDklnFOdtMa3Q2w4ox4rRWMXTG4BOQvF0G/DoMm81SSiePgd8YWa38lFYJkoAKlF4JbUAz1Eun99ESMxIcxOmCIe0o8At4FdC+fzV2OXz/wMZcEHJGpp3GwAAAABJRU5ErkJggg=="))
whiteplace = tk.PhotoImage(data=b64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAFV0lEQVR4nN2bf2iVVRjHv+dFxhCRi4yQIbJijBgmYibDPxb0Y4TV6I/9EWMskSgKKZAIkRj4h0iE/yVSESIlEfSDkLWsLKQULDIhck3ZUmvm2lZoPzY37z79ce5183b3nvPe+/649YHLBuc9z3me533f533OOc8xShggkNQiab2kOyQ1SWqUlJNULymQNC3pqqRfJV2UNCjptKTTxpjpJPUzSQgFlkt6SNLDku6RdEuFoqYlnZDUL+k9Y8z5WBRMCqAdOAT8RfzkgWNAN1CXta03AXQCJxMwejEuANsydwSwrnBXsmIYeCQLw+uAPcBshsYv5AOgMS3jm4GvMza4HONAZ9LG3wdMxqDsbMkvX/hVSx7YGcUm788g8Kikg5IqCTwjkj6WdFzSV5IuSZqTzQGKvyWyuUGTpDZJ9xf+VjLey5KeNcbMVdD33wA9RH/fR4HdwJoqxm0AnqCyV+41bBJWtfFdEY0fBrYA9VUPfrMe7cDnEZ2wryonFAad8hxsCnghbsPL6NQF/BTBCbsqHWg1MOY5yPfA2phtDdOtAXjfU7c8Nn5FGqAOOO45wGFs7p8qQAD04ff1+B1oiiK8z9P4N8g4HcUGSZ8YdRSfeAC0Atc8jV+Sgo1OgMfxexJ6fYR94iHoCFlPREoAdnro/Qthrys203NxDsilaJsX2Jjwlof+i2eKuGd214CNKdoVCSAH/OiwYZJyTwF2auvixQzsigTwgIcd28p13O/oNAosy8CmyGCnx2EMlnaowz3LezojeyKDfZpdX4UNCzt0OC4eB5ZmaFNkgAGHTS9JdhoqSQ865L1pjPk7WZVjZ7+jffON/4DvHN6q2ci/GEA97te6McB+ElpDZF2WdColvWOjsKHykeOytkDSOs2/CuX40hhzPTbN0uWoo/3OQNLtjou+iUmZLDjhaG8JJN3quOhMTMpkwYikmZD25kB2ozKMn+PTJ12MMTOS/gy5JBdIci1mTMSnUiaExq9Akiu9TXR7OgVCl8YDOTz0f8fHATW18FEBoctggaTfHAJqbvEjIqHLdoFsWUoYq+PTJV2wy3ZhMW4ikDTskONKlGqZ2xT+Cp8PJJ11CLkrPn1Sp83R/kMgO9EJ+1S0E8cmYzbc62j/VpIEDDqmjRscgmoO/Fa5Vhbv7KcOeY8lrXACdEhaEdJ+xhhzueiAfoewHv4jC6ILeNLR/uGN/wqPy7jjcdmerL7xAazBvV/YVtppn6PDGBnsAlcC7q3zIUoDe8FrrqXkvRnZ5A12e89lx3OLdT7i6DhLDS+QAsuxJTph/AE0LCZgk6MzhQHComsmYDdHD3nov8cl6LCHkH5qb3v8eQ+9x3DtbAMt+BVGHaRGMkRsVZpPgcRWX4G+JTIHyL5EZgt+JTLHvG8YNi/wLX/PskhqB353/grQHHWAFmx1lQ9DpFsmlwPe9tQNoLvSgTrwK5gCGzf6SL5QshN7YMKX3dUO2E20UtlzQC8xV5ABG3HnKaW8Qkz1wlsjOgFsvrADqHhJDfuo9wJfEL2c/oCP8VHK5Xskva7oq8RzskfgPpN0Unar7ZKkq8Vy9oKiyySt1PwRu7slbZI9WheVVyU9FVu5fBFgMzaiVkseGzOuYAPtFPEcv8kDu0gyP8FWkroKKrJgEuhKzPASJywF9lI7h6YGgFWpGF/iiPX4V5UnwQXSuushTgiwhxjSfC1GgWdIOOeIRMERHcC7+CdPUchjn7YeYpx/JHV4eoWkTtnD0+2Syi9AuJmRLXMZkPSOMWYkHg3nScQBC8F+klolrdX88flVsoUZxZXm67KbtBOyZS1DsrnDqaSPz/8D61U9P2+UR20AAAAASUVORK5CYII="))
blackplace = tk.PhotoImage(data=b64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAEzUlEQVR4nNWbXWgVRxSAPwe5iEi4SB6KiLQilxKiBLVS+pAXQyi2SCk+FAltkOJDER9EpIgIfZBSQp9EQumDFCvigxSRItKGIv2BUqqC1DSVtP4Fm5o09DfG5HZ9OHsxbHPnzO6d2d37wXDvZe7MnDO7c/bMmbPLCI8BasBmYCPwNLAGqAIr4vqHwJ/Ab8AdYBS4FpeHOcjonQ5gN3AGmASijGUWGAEOIBNXenqB08A/ZFe6WakDl5GJreSlkCs7gW/xr3SzchvYRwkmoge5KnkpnizjwCvBtVyCCvAuMJ9C2JDlPGJYc2ED8F1ghbKUB8hSDEofMO1B2PlEqcel1X7rwOFQyr8GzGUUbBwYBgYQn2AVsDL+7EB8gk7k7uoDjiC2Jet4xxH/whsDpF/vE8AxoLuFcTuBvWRbch/iaRJ2kU75cWAQ8fJ80gt8kUKOCDhBi5PQi3hjLoPNIreub8WT7ALuOsoUAe9kHWgd7m7sD8CmrANloBP4xFG2OmK/UlEBvnYc4AJiyPLGAEdxe3rMkHIvcdSh0wg4RfHu6F7cbNQIjvagC7fHzylguT89WuJN3O6E1106+8yho0sUf+WTHEaX+z7Kcu1z6OQm4riUDYPEHzT5rZ6itrObA7YFEd8PVeAX7DpM0+Qu6FEaRsB7QcX3w4voeuxbquGw0mgC8d3bgfPYdRlNNqig7/LeykFwX/SgPxW2Lm7Qr/z5AbJ7aycuYtdpCJ44Bi8pnX0M/BtEzHAMK/U7Fv+4jn22ymz5m7ECfVmvAXkk2NbLfcrj8aXlNPYJeNUgBsPmI38FLISVMxgjSv0WAzyr/Ol7T8IUwTdKfc0Azyh/uuFJmCL4GXhkqd9g0OPp9/zJkzuPgL8t9VWDHsyY8idPIVjtl0F3b9vyeHoR/9kqDe1r4b3gMgFlC3ykxRoGM8DvSgdlDH6kwerEGSQtxcY6f7LkTgW7jZsyyEmODc1RKjPrsS/hWwb4SenkOX/y5M7zSv2PBriC/VHRi+eT1hzZrtRfbXwZJUX0pE1wiXI91biynyudvRFIyJD0A6st9TeAXxs/tEjqDO0TEG1wAYeQWIMKEvezNTiQk+A+6EY/L/yfgTyhNJikmFPgLGhH52MsYdi70UPJ74eXvWX60PU42KzxJaXhPOUOkHYgjp1Nh7+QBIsleUFpHMUD2KxrURj0IGiEJHha0axnBHxK+XaJh9DlnsRhc1fDLTHqI8rjIQ7iliCxx7VD1xSZkxR/JwziliJzmRQXrIJ7+nuRSVJv43bl/0CyUFNRQzxAl0kYI980uSpw1lG2CHnJIhP9uOfrziJLJ3Si5E7khQlX5Y+1OuBu0qXK3kSysXyfJ25D91OS5QM8Geo9pE+WHkfWaCshtSoymV+SPp3+JAEyxrOkr9eR88UhJM+3K1ZssXCNA5oa8DKylEZwz1MOduWT7EAsahahkpMyG/c1E3/38fpNHUmODuqfdKEnVBRRppE7LBdWIjvDsrw0dRFYG1TjJmzGPas8RLlNjle9GSYWIs9lMQHsJ7zPkQqDOE7nyP6yk63UkbttgOL3HyqrkU3KOfRYo63MIe8JHUJOebyzLESnCQzy5NjEk9fn1yLP/UakeQE5pJ1C0lrGkFfnrxA4P+ExMuCFWQegxVoAAAAASUVORK5CYII="))
darkgreen = tk.PhotoImage(data=b64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAEdUlEQVR4nO2bX2gcRRzHP1nPMhbplqKiVkSxVAkqNdoiwgaRPNVaFJT4oEIRDEWhD/FBV3yoD6PFp2JBjAgt/sNSixSj9Q8qnpQiklZarAaNJWCVGkqn+DBXlujD7N5tkr3c7d3ezt2tn6fc7szkO7+dndnfzO83QIcRvusA64Eh4DbgBuBaYDUgAAfQwAXgLDALnAKOA8e1VLqT+gY60ajw3VXAFuAB4D7gqhab0sARYBI4qKU6nYnAGJkaQPjuMDAGPAiszLJtYB74DngDOKCluphFo5kYQPjuVuAFYFMW7TXBLPAqMNGuIdoygPDdDcBuYLiddtpgBhjXUn3UagMtGUD47gpgJ/AsUGr1n2fIIWC7lupM2oqpDSB8dx3wPnBX2rodZg54Ukt1KE2lS9IUFr47AnwG3JSmXk6sBEZLngiCcqXcbKWmR4Dw3UeBfcCKFsTlzR5gh5ZqvlHBpkaA8N3HMJ2/tE1hebEJWFvyxGRQrvy7XMGGBhC++zDwNt0x2aVhCLiy5InDyxlhWQOEHzYH6Y1hn8RGYCAoV76pV6CuAYTvXg98AbjZ68oVr+SJ6aBcOZl0M3ESDNf5r4F7OqksR84DdyT5Ek6dCs/RP50H43m+FXqmC1jyCgjfHQTeTbrX49wIzATlyo/xi0kjYDe9O+k1YlfoqldZYIDwS28kV0n5cjXwTPzC4hHwYn5arDEeHwVVA4SurS23Nk/WAE9EP+IjYCx/LdZ4OvpjAKrr/p8Y6xSFjVqqH6IRcC/F6jzAKNRegfstCrHFZqi9AieAW63KscNaJ1wSBm0rscTdDrCB+j5Bv3OnA9xiW4VF1jsYJ6GorHMwB5VFZbUDrGpYrI9xgMtti7CJAwS2RdjkfwMA52yLsImDCUspKnMO8JttFRY57QDTtlVY5GcHmMLE3xSRY5E7fIpi+gTXRF7gl1Zl2OEnLdVfkQEmrUqxwydQ2wf4ChNjUyQ+hNAAYazdfqty8mUa+B4W7gS9TnFWgzej+KGqAbRUJynGZPgPsDf6sXgvcGeuUuywR0tVne8WGEBLdQT4OHdJ+XEW2BW/kLQbPI4JU+9HntdSnY9fWGIALdU08HJukvLjW2LvfkS984BXCJeJPuECJo54ySqXaIDwu+BxTHRVP7BdS/Vr0o26J0LhqzAKZJKZYRGppXqv3s1lj8S0VJ8D2+jdfcMJGoT9NAyFC8qVEyVP/IE5Qu+lM8S9wFONIsabigUMypVjJU/8jskE64X4wQma6DykeKJaqneAhzAzarcyD7yEmfSa8mtaSZkZBD6g+wIqzgFjWqoDaSqlHs5BufJ3yRP7gMsw4ejdMC8cBjZrqY6mrdhu2twQ8Br2AqtnMWlzqZ56nLaenpZqCvCAR4DEePwOcQbYAdzcTuchw9TZMBR9BBNwuYXsA67ngaOYjZv9XZU6uxjhu2uArZjk6WHgihabuohJnv4Uky88k43CGh0xQJxwZAwCt1NLn78OE5gRxSYEmFl8DpMO+wsmfX6q0+nz/wF0uyWlj+Xh6AAAAABJRU5ErkJggg=="))
lightgreen = tk.PhotoImage(data=b64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAEQklEQVR4nO3bW4hVVRzH8c/sQiI2IhKxuxAFYjF0McuKIGmLT2VSUBhkQfQwSIUP9tCFHuyhkiCQpMhuCtFFzEKyIqIdEVIZJiRaUiI+2EZERPaDiAw97H1mzoxnLmfOmbPOzOn7NGefvdf5rd+sy15r/f99ppk4SyIsxGLcgKtxOebhIkQ4g9M4jqM4iH3YV6T5menU1zcdhcZZMhcrcB+W4dIpFnUGu7ELO4o0P9IWgXW01YA4S5ZiAPfj4naWjUH8hLexvUjzs+0otC0GxFmyEi/gtnaUNwmO4jVsbtWIlgyIs2QRNmJpK+W0wGGsK9L8i6kWMCUD4iyZg/V4BhdO9cfbyE6sKdL8WLMPNm1AnCUL8DFubfbZaeYEnijSfGczD0XN3BxnyXL8ovsqD5fg8zhLnm/moUm3gDhLHsZWzGlSWAg2YW2R5oMT3TgpA+IsWY0PdEd/nyzvYmAiEyY0IM6SB5V9fiZVvsabeHo8Ey4Y7+nqxWaHmdHsG7EEfWe3Fj+MdcOYLSDOkquwx9RfY7uFQTxSpPknjb5saEA1z2e4cxqFdZJTuLnRWmKsafBZs6fylCvP96qV6QjOuxBnSb/yvX62sQyrR19s1AI2mrmD3kRsqJbqQ4wwoHrTW95RSZ0lwVP1F0a3gBc7pyUY6+pbwZAB1dI21LK2k8zHY7UP9S1goPNagvFk7Y8+hub9f5Xu9ApLijT/rdYC7tZblYdVDHeBewMKCcU9DHeBP3B9UDlhuCKqpoT+0EoCcUeERZrcGptF3BLhutAqArIwwjWhVQRkQaQ8qOxV5kWYO+Fts5gIcWgRIYlwLrSIkPxvAE6GFhGSSBmW0quciPBPaBUBORLhUGgVAfkzwl7l6Ukv8nttOXxQb64JLqutAr8LKiMMB4o0z2sG7AoqJQxfMbwP8L0yxqaX+IzKgCrWbltQOZ3lEH5l5E7QW3pnNninFjUyZECR5vv1xmBYYEvtw+i9wPUdlRKGTUWaD413Iwwo0nw3vuy4pM5xHBvqLzTaDV6nDFOfjTxXpPmp+gvnGVCk+SG80jFJneNHdX2/xljnAa+qpolZwmllHPF5s1xDA6r3gkeV0VWzgTVFmv/d6IsxT4SqrrAKbcnMCMjLRZp/NNaX4x6JFWn+LR43c/cNN5sg7GfCM8HKvQEzz4QtyqY/7tvtpA5FizR/X9kSZkp32GyMQW80kz4VLtL8QzygHFG7lUG8ZBL/+RpTSZnpx6e6L6DipDI/YHszDzUdF1Ck+QHcjtd1z7jwDW5qtvK0nja3GG8IF1h9VJk213TFa7QUGVKk+V7chYewv5WymuQY1uLaVipPG1Nnq1D05copc4X2B1wP4mflxs22rkqdHU2cJfOxUpk8vVSZ0jYVziqTp79W5gsfbo/CYabFgHqqltGPGw2nz1+pDMyoxSacU47iJ5TpsH8p0+f3Tnf6/H8B8RelBNjWywAAAABJRU5ErkJggg=="))
logo = tk.PhotoImage(data= b64.b64decode("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"))

window.iconphoto(False,logo)

## create the ui elements and colour the board (by calling updateUi())
showmovesbool = False
allbuttons = createButtons()
score1, score2, reset, showmoves = createUi()
updateUi()

window.mainloop()