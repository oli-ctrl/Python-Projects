from typing import Any
import pygame
import time
import random
import pathlib

path = pathlib.Path(__file__).parent.absolute()
path = str(path).replace("\\", "/")
# pygame setup
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 30)
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
## colours

sky = pygame.Color("#80CCCC")
ground = pygame.Color("#80CC80")
class particles():
    def __init__(self):
        self.allparticles = []
        self.particlecount = 0
    def draw(self):
        for i in self.allparticles:
            i.draw()
    def remove(self, particle):
        if particle.die():
            self.allparticles.remove(particle)
    def add(self, particle):
        self.allparticles.append(particle)
    def update(self):
        for i in self.allparticles:
            i.update()
    
        
class particle():
    def __init__(self, x, y, size = 5, color = "Red", vertvelocity = 5, horisontalvelocity = random.randint(-5,5), gravity = 0.5, lifetime = 60, bounce = 0, effectedbymovement = False):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.vertvelocity = vertvelocity
        self.horisontalvelocity = horisontalvelocity
        self.gravity = gravity
        self.lifetime = lifetime
        self.bounce = bounce
        self.lifetimer = 0
        self.maxheight = self.y
        self.bouncecooldown = 0
        self.effectedbymovement = effectedbymovement

    def update(self):
        if self.y < self.maxheight:
            self.maxheight = self.y
        self.vertvelocity += self.gravity
        self.y += self.vertvelocity
        self.x += self.horisontalvelocity
        self.bouncecooldown -= 1
        self.lifetimer += 1
        if self.lifetimer > self.lifetime:
            particlecontroller.remove(self)
        if self.y > 680 - self.size and self.bouncecooldown <= 0 and self.vertvelocity > 0.1 and self.bounce != 0:
            self.vertvelocity = -self.vertvelocity*self.bounce
            self.bouncecooldown = 1
            self.horisontalvelocity /= 2
            self.y = 680 - self.size
        if self.effectedbymovement == True and birb.alive == True:
            self.x -= 3
        
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def die(self):
        self.size -= 0.1
        if self.size < 0.1:
            self.size = 0
            return True

class Birb():
    def __init__(self):
        self.x = 300
        self.y = 360
        self.size = 30
        self.velocity = -10
        self.gravity = 0.5
        self.score = 0
        self.direction = 0
        self.picture = pygame.image.load(str(path) + "/Bird.png")
        self.picture = pygame.transform.scale(self.picture, (self.size*2, self.size*2))
        self.deadpicture = pygame.image.load(str(path) + "/DeadBird.png")
        self.deadpicture = pygame.transform.scale(self.deadpicture, (self.size*4.5, self.size*4.5))
        self.alive = True

    def draw(self):
        if self.alive == True:
            orig_rect = self.picture.get_rect()
            rot_image = pygame.transform.rotate(self.picture, -self.direction)
        else:
            orig_rect = self.deadpicture.get_rect()
            rot_image = pygame.transform.rotate(self.deadpicture, -self.direction)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        if self.alive == True:
            screen.blit(rot_image, (self.x-self.size, self.y-self.size+12))
        else:
            screen.blit(rot_image, (self.x-self.size-48, self.y-self.size-45))
        # pygame.draw.circle(screen, "yellow", (self.x, self.y), self.size)
        
    def move(self):
        self.velocity += self.gravity
        self.y += self.velocity
        self.direction = self.velocity*8
        if self.direction > 80:
            self.direction = 80
        if self.direction < -90:
            self.direction = -90    
        
    def jump(self):
        self.velocity = -10
        for i in range (0, 30):
            i = random.randint(200,255)
            particlecontroller.add(particle(self.x, self.y, random.randint(10,20), (i,i,i), random.randint(-5,5), random.randint(-5,5), 0.5, 60, 0.5, True))


    def checkhit(self):
        if self.y > 700: 
            return True
        for i in pipecontroller.pipes:
            if pygame.Rect(self.x-self.size, self.y-self.size, self.size, self.size).colliderect(pygame.Rect(i.x, i.y, i.width/2, i.height)) or pygame.Rect(self.x-self.size, self.y-self.size, self.size, self.size).colliderect(pygame.Rect(i.x, i.y - (i.height + i.gap), i.width/2, i.height)):
                return True
        return False
    
    def die(self):
        global running
        count = 0
        while self.y <= 680:
            if self.direction < 90:
                self.direction += 10
            self.velocity = 10
            self.y += self.velocity
            screen.fill(sky)
            cloudcontroller.move()
            pipecontroller.move()
            cloudcontroller.draw()
            pipecontroller.draw()
            particlecontroller.update()
            particlecontroller.draw()
            drawground()
            drawscore(self.score)
            self.draw()
            pygame.display.flip()
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return True
        self.y = 680
        for i in range (0, 100):
            particlecontroller.add(particle(self.x, self.y, random.randint(3,7), "Brown", random.randint(-15, 5), random.randint(-100,100)/10, 0.5, 120, 0.5))
            particlecontroller.add(particle(self.x, self.y, random.randint(4,6), "yellow", random.randint(-15, 5), random.randint(-100,100)/10, 0.5, 100, 0.5))
        self.alive = False
        while True:
            screen.fill(sky)
            cloudcontroller.move(1)
            cloudcontroller.draw()
            pipecontroller.draw()
            drawground()
            particlecontroller.update()
            particlecontroller.draw()
            drawscore(self.score)
            self.draw()
            pygame.display.flip()
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return True
            count += 1
            if count == 200:
                return True

class Pipes():
    def __init__(self):
        self.pipes = []
    def draw(self):
        for i in self.pipes:
            i.draw()
    def add(self, pipe):
        self.pipes.append(pipe)

    def move(self):
        for i in self.pipes:
            i.move()
    def check(self):
        for i in self.pipes:
            i.check()

class Pipe ():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 500
        self.gap = 200
        self.givenpoint = False
        self.bottompipe = pygame.image.load(str(path) + "/Pipe.png")
        self.bottompipe = pygame.transform.scale(self.bottompipe, (self.width*2, self.height))
        self.toppipe = pygame.image.load(str(path) + "/Pipe.png")
        self.toppipe = pygame.transform.scale(self.toppipe, (self.width*2, self.height))
        self.toppipe = pygame.transform.flip(self.toppipe, False, True)

    def draw(self):
        screen.blit(self.bottompipe, (self.x, self.y))
        screen.blit(self.toppipe, (self.x, self.y - (self.height + self.gap)))

        # pygame.draw.rect(screen, "green", (self.x, self.y, self.width, self.height))
        # pygame.draw.rect(screen, "green", (self.x, self.y - (self.height + self.gap), self.width, self.height))

    def move(self):
        self.x -= 3

    def check(self):
        if self.x <= birb.x and not self.givenpoint:
            birb.score += 1
            self.givenpoint = True
        if self.x < -100:
            pipecontroller.pipes.remove(self)

class clouds():
    def __init__(self):
        self.allclouds = []
    def add(self, cloud):
        self.allclouds.append(cloud)
    def draw(self):
        for i in self.allclouds:
            i.draw()
    def move(self, amount = 3):
        for i in self.allclouds:
            i.move(amount)
    def check(self):
        for i in self.allclouds:
            i.check()

class cloud():
    def __init__(self, x = 1400):
        self.x = x
        self.y = random.randint(0, 300)
        self.size = random.randint(20, 50)
        self.depth = random.randint(1, 5)
        color = 200+ self.depth*5 + random.randint(-10, 10)
        self.color = pygame.Color(color, color, color)
        self.secondcloudpos = []
        self.speed = random.randint(10, 20)
        for i in range(random.randint(5,10)):
            randlim= round(self.size*self.depth/4)
            self.secondcloudpos.append((random.randint(-randlim, randlim), random.randint(-randlim, randlim)))
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size*self.depth/4)
        for i in self.secondcloudpos:
            pygame.draw.circle(screen, self.color, (self.x + i[0], self.y + i[1]), self.size*self.depth/4)

    def move(self, amount = 3):
        self.x -= amount*self.depth/self.speed

    def check(self):
        if self.x < -100:
            cloudcontroller.allclouds.remove(self)
        
def drawground():
    pygame.draw.rect(screen, ground, (0, 680, 1400, 100))

def drawscore(points):
    font = pygame.font.SysFont("Arial", 50)
    text = font.render(f"Points: {points}", True, "black")
    screen.blit(text, (0, 0))


cloudcontroller = clouds()
particlecontroller = particles()

## time stuff for adding pipes and clouds
pipeTime = time.time()
cloudTime = time.time()
firstframe = True
cloudcontroller.add(cloud(100))
cloudcontroller.add(cloud(300))
cloudcontroller.add(cloud(500))
cloudcontroller.add(cloud(700))
cloudcontroller.add(cloud(900))
cloudcontroller.add(cloud(1100))
## gamestate stuff
gamestate = "Playing"
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(sky)
    # RENDER YOUR GAME HERE
    # draw a circle at the mouse position
    ## draw and move the clouds
    
    cloudcontroller.check()
    ## add a cloud every few seconds
    if time.time() - cloudTime >= 2:
        cloudcontroller.add(cloud())
        cloudTime = time.time()
    ## menu stuff
    if gamestate == "Menu":
        cloudcontroller.move(1)
        cloudcontroller.draw()
        firstframe = True
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            gamestate = "Playing"


    ## playing stuff
    elif gamestate == "Playing":
        if firstframe == True:
            firstframe = False
            birb = Birb()
            pipecontroller = Pipes()
            pipecontroller.add(Pipe(1400, random.randint(300,600)))
            pipecontroller.add(Pipe(1000, random.randint(300,600)))
            pipeTime = time.time()
        ## move and check the birb
        if pygame.key.get_pressed()[pygame.K_SPACE] and not pressed:
            birb.jump()
            pressed = True
        else:
            if not pygame.key.get_pressed()[pygame.K_SPACE]:
                pressed = False
        birb.move()
        if birb.checkhit():
            birb.die()
            gamestate = "Menu"
        ## draw and move the clouds
        cloudcontroller.move()
        cloudcontroller.draw()
        ## draw and move the pipes
        pipecontroller.draw()
        pipecontroller.move()
        pipecontroller.check()
        ## add a pipe every 2 seconds
        if time.time() - pipeTime >= 2:
            pipeTime = time.time()
            pipecontroller.add(Pipe(1400, random.randint(300,600)))
        ## particle stuff 
        particlecontroller.update()
        particlecontroller.draw()
        ## draw the birb
        birb.draw()
        ## draw the ground and other menu stuff
        drawground()
        drawscore(birb.score)
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()