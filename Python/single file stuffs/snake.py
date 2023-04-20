import math as math
import time as time
from random import randint
import keyboard
import tkinter as tk

## Default params for board
x = 15
y = 15
speed = 0.5
count = 50

## Movement keys
upkey = "w"
leftkey = "a"
downkey = "s"
rightkey = "d"

## st
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
        self.length = 2
        self.poslist = []
        self.length = 5
        self.fruitpos= [math.ceil(x/2), math.ceil(y/2)+2]
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
        ## check pos walls
        if int(self.nextpos[0]) >= x or int(self.nextpos[1]) >= y:
            print("hit positive wall")
            return False
        ## check tail
        elif board[int(self.nextpos[0])][int(self.nextpos[1])] == 1:
            print("hit tail")
            return False
        ## check walls
        elif int(self.nextpos[0])-1 >= x or int(self.nextpos[1])-1 >= y or int(self.nextpos[0]) < 0 or int(self.nextpos[1]) < 0:
            print("hit  wall")
            return False
        ## check fruit
        if board[int(self.nextpos[0])][int(self.nextpos[1])] == 2:
            self.length +=1 
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

def makeWindow ():
    window.geometry("{}x{}".format((x*38), (y*41)))
    for i in range (x):
        for j in range (y):
            box = tk.Button(master=window, state="disabled", height=2, width=4  )
            uigrid.append(box)
            box.grid(row=j, column=i, sticky= tk.EW)
    print (uigrid)


def update_ui():
    update_pos =0 
    print("update ui")
    for i in board:
        for gridpos in i:
            if gridpos == 0:
                uigrid[update_pos].config(bg="White")
            elif gridpos == 1:
                uigrid[update_pos].config(bg="green")
                print("snake",uigrid[count])
            if gridpos == 2:
                uigrid[update_pos].config(bg="red")
                print("fruit",uigrid[count])
            update_pos+=1
            
    
uigrid = []
board = boardgen(x,y)
snake = Snake()
window = 0
direction = "Right"

window=tk.Tk()
window.title("SNEK")

makeWindow()

## game loop
def main_loop():#
    global count
    global direction
    ## slow down loop so it doesnt go brrr
    time.sleep(speed/100)
    count+=1

    ## get keyboard inputs
    if keyboard.is_pressed(upkey) and snake.direction!="Down":
        direction ="Up"
    elif keyboard.is_pressed(leftkey) and snake.direction!="Right":
        direction = "Left"
    elif keyboard.is_pressed(downkey) and snake.direction!="Up":
        direction = "Down"
    elif keyboard.is_pressed(rightkey) and snake.direction!="Left":
        direction = "Right"

    ## if count is more than 75 set direction, move head and update board. this also checks if the snake is alive. and breaks the loop if it is
    if count >= 25:
        count = 0
        snake.direction = direction
        snake.move()
        if snake.check_alive():
            print("---------------------------------------------------------------------------")
            for i in board:
                print (i)
            update_ui()
        else:
            print("game over you are dead")
            return
    ## re-add to mainloop
    window.after(1, main_loop)

window.after (1, main_loop)
window.mainloop()


