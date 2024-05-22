import pygame
import random
import threading

pygame.init()

class Game:
    def __init__(self):
        self.display = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Sand Simulation")
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.draws = []
        gridsize = 10
        x = pygame.display.get_surface().get_width()//gridsize
        y = pygame.display.get_surface().get_height()//gridsize
        self.grid = Grid(x,y, gridsize)

        self.selectedElement = 0
        self.elements = [RedSand, BlueSand, GreenSand]
        self.draws = [self.grid]
        self.eventsList = []
    
    def run(self):
        while True:
            for event in pygame.event.get():
                ## if quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    grid.quit()
            self.update()
            self.draw()
            pygame.display.flip()
            self.dt = self.clock.tick()/1000

    def update(self):
        mousepos = pygame.mouse.get_pos()
        if self.__CheckClick(2):
            self.selectedElement = (self.selectedElement + 1) % len(self.elements)
        
        if pygame.mouse.get_pressed()[0]:
            x, y = self.__MouseToGrid(mousepos[0], mousepos[1])
            self.grid.placeElement(x, y, self.elements[self.selectedElement])
        

        self.__lastClick = pygame.mouse.get_pressed()

    def draw(self):
        grid.getGrid()
        for x in range(len(grid.grid)):
            for y in range(len(grid.grid[x])):
                if grid.grid[x][y] != 0:
                    color, pos, type = grid.grid[x][y].getInfo()
                    pygame.draw.rect(self.display, color, (pos[0]*grid.cell_size, pos[1]*grid.cell_size, grid.cell_size, grid.cell_size))

    def __MouseToGrid(self, x, y):
        return (x//self.grid.cell_size, y//self.grid.cell_size)
    
    def __CheckClick(self, click=0):
        if pygame.mouse.get_pressed()[click] and not self.__lastClick[click]:
            return True
    
    def event_add(self, event):
        self.eventsList.append(event)


class Grid:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = [[emptyElement((x,y)) for x in range(width)] for y in range(height)]
        self.ready = False

        self.allElements = []
        self.updateElements = []
        self.running = True
        self.clock = pygame.time.Clock()
        self.offset = 30
        self.time = 0

    def quit (self):
        self.running = False

    def run(self):
        while self.running:
            if self.offset < self.time:
                self.time = 0
                self.update()
                self.ResetGrid()
            self.time += self.clock.tick(60)
            
    def update(self):
        self.curgrid = self.grid
        for element in self.updateElements:
            element.update(self.curgrid)
        self.grid = self.curgrid

    def placeElement(self, x, y, element):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return
        if self.grid[y][x].type != None:
            return
        self.grid[y][x] = element(pos=(x, y))
        self.allElements.append(self.grid[y][x])
        self.updateElements.append(self.grid[y][x])
    
    def ResetGrid(self):
        for element in self.updateElements:
            element.updated = False
    
    def getGrid(self):
        return list(self.grid)

## parent class for all elements
class emptyElement:
    def __init__(self, pos):
        self.type = None
        self.color = (0, 0, 0)
        self.updated = False
        self.pos = pos

    def update(self, grid):
        pass

    def getInfo(self):
        return self.color, self.pos, self.type

## classic sand element, falls down and can move left or right if there is space, used as parent class for the coloured sand elements 
class SandElement(emptyElement):
    def __init__(self, pos=(0,0)):
        super().__init__(pos)
        col = random.randint(220, 255)
        self.color = (col, col, 0)
        
    def update(self, grid):
        x,y = self.pos
        if not self.updated:
            if y < len(grid) - 1:
                if grid[y+1][x].type == None:
                    y += 1
                    x += 0 ## I know this does nothing, just good for reading
                else:
                    if x < len(grid[y]) - 1 and grid[y+1][x+1].type == None and x > 0 and grid[y+1][x-1].type == None:
                        if random.randint(0, 1) == 0:
                            y += 1
                            x += 1
                        else:
                            y += 1
                            x -= 1
                    elif x < len(grid[y]) - 1 and grid[y+1][x+1].type == None:
                        y += 1
                        x += 1
                    elif x > 0 and grid[y+1][x-1].type == None:
                        y += 1
                        x -= 1

        if self.pos != (x, y):
            oldx, oldy = self.pos
            grid[oldy][oldx] = emptyElement((oldx, oldy))
            grid[y][x] = self
            self.pos = (x, y)
            self.updated = True
        return grid

## coloured sand elements, they inherit the sand element with a different color
class RedSand(SandElement):
    def __init__(self, pos=(0,0)):
        super().__init__(pos)
        self.type = 1
        col = random.randint(50, 150)
        self.color = (random.randint(200,255), col, col)

class BlueSand(SandElement):
    def __init__(self, pos=(0,0)):
        super().__init__(pos)
        self.type = 2
        col = random.randint(50, 150)
        self.color = (col, col, random.randint(200,255))

class GreenSand(SandElement):
    def __init__(self, pos=(0,0)):
        super().__init__(pos)
        self.type = 3
        col = random.randint(50, 150)
        self.color = (col, random.randint(200,255), col)


game = Game()
grid = game.grid
threading.Thread(target=game.run).start()
threading.Thread(target=grid.run).start()

game.run()
