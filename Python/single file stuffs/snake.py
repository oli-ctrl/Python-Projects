import math as math
from random import randint
import keyboard
import tkinter as tk

## need to import keyboard and tkinter to run this


## __read below to change settings__

## if you want to change the size of the board, change the x and y variables
## if you want to change the starting length of the snake, change the lenght variable
## if you want to change the keys, change the upkey, leftkey, downkey and rightkey variables
## if you want to change the starting direction, change the direction variable
## if you want to change the amount of fruit, change the fruit_count variable


## Default params for board
x = 15
y = 15

## snake start params (maybe change speed depending on pc speed, 75 is good for me, on a slower machine it was good at 10)
score = 0
speed = 10
direction = "Right"
lenght = 2
fruit_count = 5

## Movement keys
upkey =    ["w","up_arrow"]
leftkey =  ["a","left_arrow"]
downkey =  ["s","down arrow"]
rightkey = ["d","right_arrow"]

## start criteria
count = 0
direction = "Right"


## make a 2d array with given size
def boardgen(x, y):
    board = [[0 for width in range(x)] for height in range(y)]
    return board


class Snake:
    def __init__(self):
        self.pos = [math.ceil(x / 2), math.ceil(y / 2)]
        self.nextpos = self.pos
        self.direction = None
        self.length = lenght
        self.poslist = []
        ##place fruit, making sure its an empty location.
        for i in range(fruit_count):
            while True:
                pos = [randint(0, x - 1), randint(0, y - 1)]
                if board[pos[0]][pos[1]] == 0:
                    board[pos[0]][pos[1]] = 2
                    break

    ## function to move the snake and do nothing if it is dead
    def move(self):
        nextpos = self.pos
        ## depending on direction, increase position
        if self.direction == "Right":
            self.nextpos[0] += 1
        elif self.direction == "Left":
            self.nextpos[0] -= 1
        elif self.direction == "Up":
            self.nextpos[1] -= 1
        elif self.direction == "Down":
            self.nextpos[1] += 1
        elif self.direction == "Dead":
            print("Snake is Dead")

        ## check if next pos is valid, this will return true if it is
        if self.checkValid():
            ## set pos to next pos, then add the pos to the end of the poslist
            self.pos = nextpos
            self.poslist.append(list(self.pos))
            ## set the board to be 1
            board[int(self.pos[0])][int(self.pos[1])] = 1

            ## cleanup the trail
            self.cleanup()
        else:
            self.direction = "Dead"

    ## funcion to remove the tail of the snake, all all trailing squares are stored in a poslist.
    def cleanup(self):
        ## if lenght of the poslist is longer than the snakes lenght, remove first element and set that to 0 on the board
        if len(self.poslist) > self.length:
            clean = self.poslist.pop(0)
            board[int(clean[0])][int(clean[1])] = 0

    ## function to check what the snake will hit on its next move, returns true if it is a valid move, and deals with fruit placement and re-placment
    def checkValid(self):
        global score
        ## check if next move hits the walls (broken)
        if (
            int(self.nextpos[0]) >= x
            or int(self.nextpos[1]) >= y
            or int(self.nextpos[0]) < 0
            or int(self.nextpos[1]) < 0
        ):
            print("hit wall")
            return False

        ## check if next move hits the tail
        elif board[int(self.nextpos[0])][int(self.nextpos[1])] == 1:
            print("hit tail")
            return False

        ## check if next move hits any fruit
        if board[int(self.nextpos[0])][int(self.nextpos[1])] == 2:
            self.length += 1
            score += 1
            ## replace fruit, making sure its an empty location.
            while True:
                pos = [randint(0, x - 1), randint(0, y - 1)]
                if board[pos[0]][pos[1]] == 0:
                    board[pos[0]][pos[1]] = 2
                    break
        return True

    ## returns false if snake is dead
    def check_alive(self):
        if self.direction != "Dead":
            return True
        else:
            return False


## make window and populate it with the disabled buttons
def makeWindow():
    for i in range(x):
        for j in range(y):
            box = tk.Button(
                master=window, state="disabled", height=2, width=4, bg="white"
            )
            uigrid.append(box)
            box.grid(row=j, column=i, sticky=tk.EW)  #


## update ui
def update_ui():
    update_pos = 0
    ## iterate over the entire board
    for i in board:
        for gridpos in i:
            if gridpos == 0:
                uigrid[update_pos].config(bg="White")
            elif gridpos == 1:
                uigrid[update_pos].config(bg="green")
            elif gridpos == 2:
                uigrid[update_pos].config(bg="red")
            if snake.direction == "Dead":
                uigrid[update_pos].config(bg="red")
            update_pos += 1


##  if snake.direction == "Dead":
##      uigrid[int(math.ceil(len[uigrid]/2))].config(bg = "white", text = score)

## variables and init snake and windows
uigrid = []
board = boardgen(x, y)
snake = Snake()

window = tk.Tk()
window.title("SNEK")
window.resizable(0, 0)
window.geometry("{}x{}".format((x * 38), (y * 41)))
## make window, them move snake once, then update ui so its not *too* laggy
makeWindow()
snake.move()
update_ui()


## game loop
def main_loop():
    global count
    global direction
    ## slow down loop so it doesnt go brrr

    count += 1

    ## get keyboard inputs and check they wont turn the snake 180
    if any((keyboard.is_pressed(key) for key in upkey)) and snake.direction != "Down":
        direction = "Up"
    elif any((keyboard.is_pressed(key) for key in leftkey)) and snake.direction != "Right":
        direction = "Left"
    elif any((keyboard.is_pressed(key) for key in downkey)) and snake.direction != "Up":
        direction = "Down"
    elif any((keyboard.is_pressed(key) for key in rightkey)) and snake.direction != "Left":
        direction = "Right"

    ## add some key rollover code soon:tm: should allow for 2 keys to be pressed in succession without missing one of them

    ## if count is more than 300 (resets to 275, this is to add a delay before the snake moves the first time) set direction, move head and update board. this also checks if the snake is alive. and breaks the loop if it is
    if count >= speed + 275:
        count = 275
        snake.direction = direction
        snake.move()
        update_ui()

        # exitloop if snake not alive
        if not snake.check_alive():
            return
    ## re-add to mainloop
    window.after(1, main_loop)


window.after(1, main_loop)
window.mainloop()
