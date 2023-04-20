import math as math
import time as time
from random import randint
import keyboard
import tkinter as tk

## Default params for board
x = 20
y = 20
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
            self.nextpos[1] +=1
        elif self.direction == "Left":
            self.nextpos[1] -=1
        elif self.direction == "Up":
            self.nextpos[0] -=1
        elif self.direction == "Down":
            self.nextpos[0] +=1
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
        ## check pos walls
        elif int(self.nextpos[0])-1 >= x or int(self.nextpos[1])-1 >= y:
            print("hit positive wall")
            return False
        ## check negative walls
        elif int(self.nextpos[0]) < 0 or int(self.nextpos[1]) < 0:
            print("hit negative wall")
            return False
        if board[int(self.nextpos[0])][int(self.nextpos[1])] == 2:
            self.length +=1 
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
         
## init board and snake
board = boardgen(x,y)
snake = Snake()

## game loop
while True:
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
    if count >= 50:
        count = 0
        snake.direction = direction
        snake.move()
        if snake.check_alive():
            print("---------------------------------------------------------------------------")
            for i in board:
                print (i)
        else:
            print("game over you are dead")
            break
    



