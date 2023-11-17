import pygame

class Tail:
    def __init__(self, pos = (0,0), age = 0, direction = (0,0), color = (255,255,255)):
        self.position = pos
        self.age = age
        self.color = color
        self.direction = direction
        self.alive = True

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.position[0]+5,self.position[1]+5,cellsize-10,cellsize-10))
        if self.direction[0] == 1:
            pygame.draw.rect(screen, self.color, (self.position[0]+10,self.position[1]+5,cellsize-10,cellsize-10))
        elif self.direction[0] == -1:
            pygame.draw.rect(screen, self.color, (self.position[0],self.position[1]+5,cellsize-10,cellsize-10))   

        if self.direction[1] == 1:
            pygame.draw.rect(screen, self.color, (self.position[0]+5,self.position[1]+10,cellsize-10,cellsize-10)) 
        elif self.direction[1] == -1:
            pygame.draw.rect(screen, self.color, (self.position[0]+5,self.position[1],cellsize-10,cellsize-10))


    def update(self):
        self.age -= 1
        self.position = (self.position[0]+self.direction[0]*cellsize, self.position[1]+self.direction[1]*cellsize)
        if self.age == 0:
            self.alive = False
        
class Snake:
    def __init__(self):
        self.position = (0,0)
        self.direction = (0,0)
        self.tails = []
        self.color = (255,255,255)
        self.age = 0

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.position[0]+5,self.position[1]+5,cellsize-10,cellsize-10))
        if self.direction[0] == 1:
            pygame.draw.rect(screen, self.color, (self.position[0]+10,self.position[1]+5,cellsize-10,cellsize-10))
        elif self.direction[0] == -1:
            pygame.draw.rect(screen, self.color, (self.position[0],self.position[1]+5,cellsize-10,cellsize-10))   

        if self.direction[1] == 1:
            pygame.draw.rect(screen, self.color, (self.position[0]+5,self.position[1]+10,cellsize-10,cellsize-10)) 
        elif self.direction[1] == -1:
            pygame.draw.rect(screen, self.color, (self.position[0]+5,self.position[1],cellsize-10,cellsize-10))

        for tail in self.tails:
            tail.draw()
    
    def update(self):
        self.age += 1
        self.position = (self.position[0]+self.direction[0]*cellsize, self.position[1]+self.direction[1]*cellsize)
        for tail in self.tails:
            tail.update()
            if not tail.alive:
                self.tails.remove(tail)
        if self.age % 10 == 0:
            self.tails.append(Tail(self.position, 10, self.direction, self.color))

    def changeDirection(self, direction):
        self.direction = direction





pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

cellsize = 20

if running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            print("w")
        if keys[pygame.K_a]:
            print("a")
        if keys[pygame.K_s]:
            print("s")
        if keys[pygame.K_d]:
            print("d")
    screen.fill((255,255,255))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()