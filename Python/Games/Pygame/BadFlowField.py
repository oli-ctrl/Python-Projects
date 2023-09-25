import pygame
import random
import math
from pythonperlin import perlin

def boardgen(size = (10,10)):
    board = perlin((4,4), dens=int(size[0]/4), seed=None)
    board2 = [[None for width in range(size[0])] for height in range(size[1])]
    ## convert board to cell objects
    currentpos = [0,0]
    for row in board:
        currentpos[1] += 1
        currentpos[0] = 0
        for cell in row:
            currentpos[0] += 1
            board2[currentpos[0]-1][currentpos[1]-1] = Cell(cell, currentpos[0]-1, currentpos[1]-1)
    return board2

def checdirs(pos, b):
    ## cardinal directions
    directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]
                  ]
    ## empty vars get filled later
    all = []
    count = 0
    ## check all directions and add to list if they exist

    for i in directions:
        try:
            ## add value to the lsit of all values
            all.append(b[pos[0]+i[0]][pos[1]+i[1]].vector)
            count+=1
        except:
            ## often when you are on the edge of the board you will get an error so just pass
            pass
    ## return the average of all values
    all0 = []
    all1 = []
    for i in range(len(all)):
        all0.append(all[i][0])
        all1.append(all[i][1])

    average0 = sum(all0)/count
    average1 = sum(all1)/count
    return [average0,average1]

def draw():
    for part in Particlelist:
        part.draw()  
    s = pygame.Surface(size=size)  # the size of your rect
    s.set_alpha(1)                # alpha level
    s.fill((0,0,0))           # this fills the entire surface
    screen.blit(s, (0,0))    # (0,0) are the top-left coordinates

def update():
    for part in Particlelist:
        part.Move()

class Particle:
    def __init__(self, x,y):
        self.position = [x,y]
        self.speed = 1
        self.color = (255, 255, 255)
        self.direction = self.__GetDirection()
        
    def Move(self):
        ## get direction of current cell
        self.direction = self.__GetDirection()
        ## move particle
        self.position[0] += self.direction[0]*self.speed
        self.position[1] += self.direction[1]*self.speed
        if self.position[0] > size[0]*Cellsize:
            self.position[0] = 0
        if self.position[0] < 0:
            self.position[0] = size[0]*Cellsize
        if self.position[1] > size[1]*Cellsize:
            self.position[1] = 0
        if self.position[1] < 0:
            self.position[1] = size[1]*Cellsize
    
    def __GetDirection(self):
        ## get current cell
        currentCell = self.__GetCurrentCell()
        ## get direction of current cell
        currentCellDirection = checdirs(currentCell, board)
        return currentCellDirection

        
    def __GetCurrentCell(self):
        ## get coords of current cell
        currentCell = [math.floor(self.position[0]/Cellsize)-1,math.floor(self.position[1]/Cellsize)-1]
        return currentCell
    

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.position[0],self.position[1]), 1)
        
    
class Cell():
    def __init__(self,noiseValue, x,y):
        self.position = [x,y]
        self.color = (abs(noiseValue*255),abs(noiseValue*255),abs(noiseValue*255))
        self.vector = self.__GetDirection(noiseValue)

    def __GetDirection(self, noiseValue):
        vector = [0,0]
        radians = math.radians(math.degrees(noiseValue*180))
        vector[0] = math.cos(radians)
        vector[1] = math.sin(radians)
        ## normalize direction
        vector[0] = vector[0]/math.sqrt(vector[0]**2+vector[1]**2)
        vector[1] = vector[1]/math.sqrt(vector[0]**2+vector[1]**2)
        return vector
    
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (800,800)
Cellsize = 1
screen = pygame.display.set_mode((size[0]*Cellsize, size[1]*Cellsize))
pygame.display.set_caption("FlowFeild: Loading...")
board = boardgen(size = size)

pygame.display.set_caption("FlowFeild")
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

## spawn particles
Particlelist = []
for x in range(0,500):
    Particlelist.append(Particle(random.randint(0,size[0]*Cellsize),random.randint(0,size[1]*Cellsize)))
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                done=True
 
    # logic
    update()
    

    random.randint(0,size[0])
    # wipe screen
    # screen.fill((0,0,0))
    # --- Drawing code should go here
    draw()
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(600)
 
# Close the window and quit.
pygame.quit()