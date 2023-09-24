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
        self.direction = self.__BlendVectors(self.direction, self.__GetDirection())
        self.position[0] += self.direction[0]*random.randint(0,self.speed*100)/100
        self.position[1] += self.direction[1]*random.randint(0,self.speed*100)/100
        if self.position[0] > size[0]*Cellsize:
            self.position[0] = 0
        if self.position[0] < 0:
            self.position[0] = size[0]*Cellsize
        if self.position[1] > size[1]*Cellsize:
            self.position[1] = 0
        if self.position[1] < 0:
            self.position[1] = size[1]*Cellsize

        return True
    
    def __GetDirection(self):
        ## get current cell
        currentCell = self.__GetCurrentCell()
        ## get direction of current cell
        currentCellDirection = board[currentCell[0]-1][currentCell[1]-1].vector
        return currentCellDirection

        
    def __GetCurrentCell(self):
        ## get coords of current cell
        currentCell = [math.floor(self.position[0]/Cellsize),math.floor(self.position[1]/Cellsize)]
        return currentCell
    
    def __BlendVectors(self, vec1,vec2):
        if vec1[0] > vec2[0]:
            vec1[0] -= vec1[0]-vec2[0]/10
        elif vec1[0] < vec2[0]:
            vec1[0] += vec2[0]-vec1[0]/10
        if vec1[1] > vec2[1]:
            vec1[1] -= vec1[1]-vec2[1]/10
        elif vec1[1] < vec2[1]: 
            vec1[1] += vec2[1]-vec1[1]/10
        
        return vec1
        
    
    def draw(self):
        s = pygame.Surface((3,3))  # the size of your rect
        s.set_alpha(28)               # alpha level
        s.fill(self.color)           # this fills the entire surface
        screen.blit(s, (self.position))    # (0,0) are the top-left coordinates
        
    
class Cell():
    def __init__(self,noiseValue, x,y):
        self.position = [x,y]
        self.direction = [0,0]
        self.color = (abs(noiseValue*255),abs(noiseValue*255),abs(noiseValue*255))
        self.vector = self.__GetDirection(noiseValue)

    def __GetDirection(self, noiseValue):
        vector = [0,0]
        radians = math.radians(math.degrees(noiseValue*180))
        vector[0] = math.cos(radians)
        vector[1] = math.sin(radians)
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
for x in range(0,10000):
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
    clock.tick(500)
 
# Close the window and quit.
pygame.quit()