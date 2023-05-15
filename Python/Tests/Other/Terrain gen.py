from random import randint
try:
    import matplotlib.pyplot as plt
except:
    raise("you need to install matplotlib to use this program")
    


## this is very much a proof of concept and not a finished product
## this is a very simple way of doing this and there are many better ways of doing this
## this is just to show how you can use smoothing to make a more realistic looking map from a random array
## if you want to use this for a game or something you will need to do a lot more work to make it look good by likely using multiple of these maps layered on top of each other 
## or by using a different method entirely
## please feel free to use this code for whatever you want
## it will be very slow for large boards so you will need to use a different method for that but if your game is grid based it should be fine (especially if not written in python)


## blur the whole array passed to it
def smooth(board):
    new = board
    for x in range(len(board)):
        for y in range(len(board[x])):
            new[x][y] = (checdirs([x,y], board))
    return new
    
## check the 8 directions around a point and return the average of these values (if they exist) 
def checdirs(pos, b):
    ## cardinal directions
    directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    ## empty vars get filled later
    all = []
    count = 0
    ## check all directions and add to list if they exist
    for i in directions:
        try:
            ## add value to the lsit of all values
            all.append(b[pos[0]+i[0]][pos[1]+i[1]])
            count+=1
        except:
            ## often when you are on the edge of the board you will get an error so just pass
            pass

    ## return the average of all values
    average = sum(all)/count
    return average

def generate():
    ## make a board of either 0 or 1
    print ("generating noise")
    board = [[randint(0,1) for a in range(width)] for b in range(height)]
    ## treespots 
    print ("generating tree spots")
    treespots = [[randint(1,100) for a in range(width)] for b in range(height)]


    ## dispaly (a copy of board but all 0)
    display = [[0 for a in range(width)] for b in range(height)]

    ## blur the board the specified times
    for i in range(blurcount):
        print(f"generating map: {round(i/blurcount*100,2)}%")
        board = smooth(board)
    print ("generating map: 100%")
    print ("placing trees and water")
    ## add trees and seperate land from water (if this was a game you could do this a much better way)
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] > 0.5: 
                ## if the spot is a tree make it a 1.5
                if treespots[x][y] < treecover:
                    display[x][y] = board[x][y] = 1.5
                ## if the spot is land increase height by 0.5 meaning all land area is above 1
                else:
                    display[x][y] = board[x][y] + 0.5 

            ## anything else bonk here (pass orig value to display)
            else:
                display[x][y] = board[x][y]
    print ("done")
    return display


## funny config stuff
width = 2000
height = 2000

## how many times to blur the board (more = smoother but slower) for a 100x100 board 5 is good for interesting terrain, but if you want more defined terrain use a higher number

blurcount = 5

## tree cover is example or randomly scattering points over the board
## 1 = 1% 100 = 100% 0 = 0%
treecover = 5 

## generate the board
display = generate()
## display the board (this is just a visual representation of the board) if this was a game you would use your own graphics/ system for placing peices
plt.figure(figsize=(8, 6), dpi=80)
plt.xlim(1000, 1000)
plt.ylim(1000, 1000)
plt.imshow(display)
plt.show()