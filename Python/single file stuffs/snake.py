import math as math
import time as time
from random import randint
import keyboard
import tkinter as tk

## Default params for board
x = 15
y = 15

## snake start params
score = 0
speed = 0.1
direction = "Right"
lenght = 2

## Movement keys
upkey = "w"
leftkey = "a"
downkey = "s"
rightkey = "d"

## start criteria
count = 0
direction = "Right"




## make a 2d array with given size
def boardgen(x,y):
    board = [[0 for width in range(x)]for height in range (y)]
    return board


class Snake:
    def __init__(self):
        self.pos = [math.ceil(x/2), math.ceil(y/2)]
        self.nextpos = self.pos
        self.direction = None
        self.length = lenght
        self.poslist = []
        self.fruitpos= [math.ceil(x/2), math.ceil(y/2)+3]
        board [self.pos[0]][self.pos[1] + 3] = 2
    
        
    def move(self):

        nextpos = self.pos
        ## depending on direction, increase position 
        if self.direction == "Right":
            self.nextpos[0] +=1
        elif self.direction == "Left":
            self.nextpos[0] -=1
        elif self.direction == "Up":
            self.nextpos[1] -=1
        elif self.direction == "Down":
            self.nextpos[1] +=1
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
            self.direction="Dead"  





    def cleanup (self):
        ## if lenght of the poslist is longer than the snakes lenght, remove first element and set that to 0 on the board
        if len(self.poslist) > self.length:
            clean = self.poslist.pop(0)
            board[int(clean[0])][int(clean[1])] = 0


        
    def checkValid(self):
        global score
        ## check walls (broken)
        if int(self.nextpos[0])-1 >= x or int(self.nextpos[1])-1 >= y or int(self.nextpos[0]) >= x or int(self.nextpos[1]) >= y:
            print("hit  wall")
            return False
        

        ## check tail
        elif board[int(self.nextpos[0])][int(self.nextpos[1])] == 1:
            print("hit tail")
            return False

        ## check fruit
        if board[int(self.nextpos[0])][int(self.nextpos[1])] == 2:
            self.length +=1 
            score += 1
            ## replace fruit, making sure its an empty location. 
            while True:
                pos=[randint(0,x-1),randint(0,y-1)]
                if board[pos[0]][pos[1]] == 0:
                    board[pos[0]][pos[1]]= 2
                    break
        return True
        
    ## returns false if snake is dead
    def check_alive(self):
        if self.direction != "Dead":
            return True
        else:
            return False
        
## make window and populate it with the disabled buttons
def makeWindow ():
    window.geometry("{}x{}".format((x*38), (y*41)))
    for i in range (x):
        for j in range (y):
            box = tk.Button(master=window, state="disabled", height=2, width=4, bg="white" )
            uigrid.append(box)
            box.grid(row=j, column=i, sticky= tk.EW)#

## update ui
def update_ui():
    update_pos =0 
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
            update_pos+=1
##  if snake.direction == "Dead":
##      uigrid[int(math.ceil(len[uigrid]/2))].config(bg = "white", text = score)
            
## variables and init snake and windows
uigrid = []
board = boardgen(x,y)
snake = Snake()

window=tk.Tk()
window.title("SNEK")
## make window, them move snake once, then update ui so its not *too* laggy
makeWindow()
snake.move()
update_ui()

## game loop
def main_loop():
    ## set geomentry every cycle to stop size changing
    window.geometry("{}x{}".format((x*38), (y*41)))


    global count
    global direction
    ## slow down loop so it doesnt go brrr
    time.sleep(speed/100)
    count+=1

    ## get keyboard inputs and check they wont turn the snake 180
    if keyboard.is_pressed(upkey) and snake.direction!="Down":
        direction ="Up"
    elif keyboard.is_pressed(leftkey) and snake.direction!="Right":
        direction = "Left"
    elif keyboard.is_pressed(downkey) and snake.direction!="Up":
        direction = "Down"
    elif keyboard.is_pressed(rightkey) and snake.direction!="Left":
        direction = "Right"
    
    
    ## if count is more than 300 (resets to 275, this is to add a delay before the snake moves the first time) set direction, move head and update board. this also checks if the snake is alive. and breaks the loop if it is
    if count >= 300:
        count = 275
        snake.direction = direction
        snake.move()
        update_ui()


        ## print board to terminal (it is differently oriented than the ui)
        if snake.check_alive():
            print("---------------------------------------------------------------------------")
            for i in board:
                print (i)
        else:
            return
    ## re-add to mainloop
    window.after(1, main_loop)

window.after (1, main_loop)
window.mainloop()


