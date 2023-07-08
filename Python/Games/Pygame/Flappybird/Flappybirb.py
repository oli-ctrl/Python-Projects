from typing import Any
import pygame
import time
import random
import pathlib

## path to assets folder
path = pathlib.Path(__file__).parent.absolute()
path = str(F"{path}/assets/").replace("\\", "/")

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

## particle controller
class particles():
    def __init__(self):
        self.allparticles = []
        self.particlecount = 0

    ## draws all particles
    def draw(self):
        for i in self.allparticles:
            i.draw()
    ## removes a particle from the list if it is dead
    def remove(self, particle):
        if particle.die():
            self.allparticles.remove(particle)
    ## cleares all particles from the screen
    def removeall(self):
        self.allparticles = []
    ## adds a particle to the list to iterate over and draw
    def add(self, particle):
        self.allparticles.append(particle)
    ## updates all particles
    def update(self):
        for i in self.allparticles:
            i.update()
    
## particle class 
class particle():
    ## generates a particle with the given parameters
    def __init__(self, x, y, size = 5, color = "Red", vertvelocity = 5, horisontalvelocity = random.randint(-5,5), gravity = 0.5, lifetime = 60, bounce = 0, effectedbymovement = False, decayrate= 0.1):
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
        self.bouncecooldown = 0
        self.effectedbymovement = effectedbymovement
        self.decayrate = decayrate
        self.wallbounce = False

    def update(self):
        ## update velocity, position and bounce cooldown
        self.vertvelocity += self.gravity
        self.y += self.vertvelocity
        self.x += self.horisontalvelocity
        self.bouncecooldown -= 1
        
        ## decay particle
        self.lifetimer += 1
        if self.lifetimer > self.lifetime:
            particlecontroller.remove(self)

        ## ground collisions
        if self.y > 680 - self.size and self.bouncecooldown <= 0 and self.vertvelocity > 0.1 and self.bounce != 0:
            self.vertvelocity = -self.vertvelocity*self.bounce
            self.bouncecooldown = 1
            self.horisontalvelocity /= 2
            self.y = 680 - self.size

        ## wall/pipe collisions
        if self.wallbounce == True and self.bouncecooldown <= 0:
            for i in pipecontroller.pipes:
                ## check collsion with top of pipe
                if pygame.Rect(self.x-self.size, self.y-self.size, self.size, self.size).colliderect(pygame.Rect(i.x, i.y, i.width, i.height/2)) or pygame.Rect(self.x-self.size, self.y-self.size, self.size, self.size).colliderect(pygame.Rect(i.x, i.y - (i.height + i.gap), i.width, i.height/2)):
                    self.vertvelocity = -self.vertvelocity*self.bounce
                    self.bouncecooldown = 1
                    self.horisontalvelocity /= 2
                    break

                ## check collsion with left side of pipe
                if pygame.Rect(self.x-self.size, self.y-self.size, self.size, self.size).colliderect(pygame.Rect(i.x-i.width/2, i.y, i.width/2, i.height)) or pygame.Rect(self.x-self.size, self.y-self.size, self.size, self.size).colliderect(pygame.Rect(i.x-i.width/2, i.y - (i.height + i.gap), i.width/2, i.height)):
                    self.horisontalvelocity= -abs(self.horisontalvelocity*self.bounce)
                    self.bouncecooldown = 1
                    break

                ## check collsion with right side of pipe
                if pygame.Rect(self.x-self.size, self.y-self.size, self.size, self.size).colliderect(pygame.Rect(i.x+i.width/2, i.y, i.width/2, i.height)) or pygame.Rect(self.x-self.size, self.y-self.size, self.size, self.size).colliderect(pygame.Rect(i.x+i.width/2, i.y - (i.height + i.gap), i.width/2, i.height)):
                    self.horisontalvelocity = abs(self.horisontalvelocity*self.bounce)
                    self.bouncecooldown = 1
                    break
        
        ## moves particle with birb
        if self.effectedbymovement == True and birb.alive == True:
            self.x -= 3
        
    ## draws the particle
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

    ## returns true if particle is dead and should be removed, otherwise slowly shrinks the particle
    def die(self):
        self.size -= self.decayrate
        if self.size < 0.1:
            self.size = 0
            return True

class Birb():
    def __init__(self):
        self.size = 30
        self.velocity = -10
        self.gravity = 0.5
        self.direction = 0
        self.picture = pygame.image.load(str(path) + "Bird.png")
        self.picture = pygame.transform.scale(self.picture, (self.size*2, self.size*2))
        self.deadpicture = pygame.image.load(str(path) + "DeadBird.png")
        self.deadpicture = pygame.transform.scale(self.deadpicture, (self.size*2.5, self.size*2.5))
        self.reset()

    ## resets the bird
    def reset(self):
        self.direction = 0
        self.x = 300
        self.y = 360
        self.score = 0
        self.alive = True

    ## draws the bird
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
            screen.blit(rot_image, (self.x-self.size, self.y-self.size))
        else:
            screen.blit(rot_image, (self.x-self.size+10, self.y-self.size-18))
        if debug:
            pygame.draw.circle(screen, "yellow", (self.x, self.y), self.size)
    
    ## makes the bird fall down when called
    def move(self):
        self.velocity += self.gravity
        self.y += self.velocity
        self.direction = self.velocity*8
        if self.direction > 80:
            self.direction = 80
        if self.direction < -90:
            self.direction = -90    
        
    # makes the bird jump when called also some particle effects
    def jump(self):
        self.velocity = -10
        for i in range (20,50):
            i = random.randint(200,255)
            particlecontroller.add(particle(self.x, self.y, random.randint(10,20), (i,i,i), random.randint(-50,50)/10, random.randint(-50,50)/10, 0.5, 1, 0.5, True, 1))
            particlecontroller.allparticles[-1].wallbounce = True

    ## checks if the bird hits a pipe, or the ground
    def checkhit(self):
        if self.y > 700: 
            return True
        for i in pipecontroller.pipes:
            if pygame.Rect(self.x-self.size, self.y-self.size, self.size, self.size).colliderect(pygame.Rect(i.x, i.y, i.width/2, i.height)) or pygame.Rect(self.x-self.size, self.y-self.size, self.size, self.size).colliderect(pygame.Rect(i.x, i.y - (i.height + i.gap), i.width/2, i.height)):
                return True
        return False
    
    ## death animation
    def die(self):
        global running
        count = 0
        for i in range (0,25):
            particlecontroller.add(particle(self.x, self.y, random.randint(3,7), "red", random.randint(-20,20)/10, random.randint(-20,20)/10, 0.5, 40, 0.5, True, 0.6))
        while self.y <= 680:
            particlecontroller.add(particle(self.x, self.y, random.randint(3,7), "red", random.randint(-10,10)/10, random.randint(-10,10)/10, 0.5, 20, 0.5, True, 0.6))
            if self.direction < 90:
                self.direction += 10
            self.velocity = 10
            self.y += self.velocity
            screen.fill(sky)
            cloudcontroller.move()
            pipecontroller.move()
            self.x -= 3.1
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
            particlecontroller.add(particle(self.x, self.y, random.randint(3,7), "Brown", random.randint(-50, 50)/10, random.randint(-100,100)/10, 0.5, 120, 0.2))
            particlecontroller.add(particle(self.x, self.y, random.randint(4,6), "yellow", random.randint(-50, 50)/10, random.randint(-100,100)/10, 0.5, 100, 0.2))
        self.alive = False
        while True:
            particlecontroller.add(particle(self.x, self.y, random.randint(3,7), "red", random.randint(-10,10)/10, random.randint(-10,10)/10, 0.5, 20, 0.5, True, 0.6))
            if count % 5 == 0:
                particlecontroller.add(particle(self.x, self.y, random.randint(3,7), "red", -10, random.randint(-10,10)/10, 0.5, random.randint(20,40), 0.5, True, 0.6))
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
            count += 1
            if count >= 100:
                return True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return True

## pipe controller class
class Pipes():
    def __init__(self):
        self.pipes = []
    def draw(self):
        for i in self.pipes:
            i.draw()
    def add(self, pipe):
        self.pipes.append(pipe)
    def reset(self):
        self.pipes = []
    def move(self):
        for i in self.pipes:
            i.move()
    def check(self):
        for i in self.pipes:
            i.check()

## pipe class
class Pipe ():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 500
        self.gap = 200
        self.givenpoint = False
        self.bottompipe = pygame.image.load(str(path) + "Pipe.png")
        self.bottompipe = pygame.transform.scale(self.bottompipe, (self.width*1.5, self.height))
        self.toppipe = pygame.image.load(str(path) + "Pipe.png")
        self.toppipe = pygame.transform.scale(self.toppipe, (self.width*1.5, self.height))
        self.toppipe = pygame.transform.flip(self.toppipe, False, True)

    ## draw the pipe
    def draw(self):
        screen.blit(self.bottompipe, (self.x-15, self.y))
        screen.blit(self.toppipe, (self.x-15, self.y - (self.height + self.gap)))
        if debug:
            pygame.draw.rect(screen, "green", (self.x , self.y, self.width, self.height))
            pygame.draw.rect(screen, "green", (self.x , self.y - (self.height + self.gap), self.width, self.height))

    ## move the pipe
    def move(self):
        self.x -= 3
    
    ## check if the pipe is off the screen or the bird has passed
    def check(self):
        if self.x <= birb.x and not self.givenpoint:
            birb.score += 1
            self.givenpoint = True
        if self.x < -100:
            pipecontroller.pipes.remove(self)

## main menu controller class
class mainmenu():
    def __init__(self):
        self.allbuttons = []
        self.alltexts = []
        self.other = []
    def draw(self):
        for i in self.allbuttons:
            i.draw()
            i.check()
        for i in self.alltexts:
            i.render()
        for i in self.other:
            i.render()
    def construct(self):
        self.allbuttons.append(playButton())

## play button class
class playButton():
    def __init__(self):
        self.x = 300
        self.y = 300
        self.imagewidth = 75
        self.imageheight = 50
        self.width = 150
        self.height = 100
        self.Image = pygame.image.load(str(path) + "PlayButton.png")
        self.Image = pygame.transform.scale(self.Image,(self.imagewidth*2, self.imageheight*2))
        self.clicked = False
    def draw(self):
        screen.blit(self.Image, (self.x, self.y))
        if debug:
            pygame.draw.rect(screen, "red", (self.x, self.y, self.width, self.height))
    def check(self):
        if pygame.mouse.get_pos()[0] > self.x and pygame.mouse.get_pos()[0] < self.x + self.width:
            if pygame.mouse.get_pos()[1] > self.y and pygame.mouse.get_pos()[1] < self.y + self.height:
                self.hover = True
                if pygame.mouse.get_pressed()[0]:
                    self.onclick()
    def onclick(self):
        self.clicked = True

## cloud controller class  
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

## cloud class
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
        
## class for fading the screen in and out
class fades():  
    def __init__(self):
        self.fade = pygame.Surface((1400, 800))
        self.fade.fill((0,0,0))
        self.fade.set_alpha(0)
    def fadeout(self):
        for alpha in range(1, 255, 1):
            self.fade.set_alpha(alpha)
            screen.blit(self.fade, (0,0))
            pygame.display.flip()
            pygame.time.delay(5)
        return True
    def fadein(self):
        for alpha in range(255, 1, -3):
            if alpha <250:
                screen.fill(sky)
            else:
                screen.fill((0,0,0))
            cloudcontroller.draw()
            birb.draw()
            particlecontroller.draw()
            particlecontroller.update()
            pipecontroller.draw()
            drawground()
            drawscore(birb.score)
            self.fade.set_alpha(alpha)
            screen.blit(self.fade, (0,0))
            pygame.display.flip()
            pygame.time.delay(5)
        self.fade.set_alpha(0)
        return True

## simple functions
def drawground():
    pygame.draw.rect(screen, ground, (0, 680, 1400, 100))

def drawscore(points):
    font = pygame.font.SysFont("Arial", 50)
    text = font.render(f"Points: {points}", True, "black")
    screen.blit(text, (0, 0))

def drawfps():
    font = pygame.font.SysFont("Arial", 50)
    text = font.render(f"FPS: {round(clock.get_fps())}", True, "black")
    screen.blit(text, (0, 50))

def toggledebug():
    global debug
    if debug:
        debug = False
    else:
        debug = True

## class inits  
cloudcontroller = clouds()
particlecontroller = particles()
pipecontroller = Pipes()
birb = Birb()
fade = fades()
menu = mainmenu()
menu.construct()

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
bloodcount = 0
## gamestate stuff
gamestate = "Menu"
debug = False
debugtimer = 0
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(sky)
    # RENDER YOUR GAME HERE
    ## draw and move the clouds
    cloudcontroller.check()
    if time.time() - cloudTime >= 2:
        cloudcontroller.add(cloud())
        cloudTime = time.time()

    ## debug stuff
    debugtimer -= 1
    if pygame.key.get_pressed()[pygame.K_d] and debugtimer <= 0:
        debugtimer = 10
        toggledebug()
    if debug:
        drawfps()
   
    ## menu stuff
    if gamestate == "Menu":
        ## draw background stuff 
        cloudcontroller.move(1)
        cloudcontroller.draw()
        pipecontroller.draw()
        particlecontroller.draw()
        particlecontroller.update()
        drawground()
        ## draw the birb bleeding if its dead
        if not birb.alive:
            birb.draw()
            bloodcount += 1
            if bloodcount >= 5:
                particlecontroller.add(particle(birb.x, birb.y, random.randint(3,7), "red", -10, random.randint(-10,10)/10, 0.5, random.randint(20,40), 0.5, True, 0.6))
                bloodcount = 0

        ## draw the menu
        menu.draw()

        ## return to game 
        if pygame.key.get_pressed()[pygame.K_SPACE] or menu.allbuttons[0].clicked:
            fade.fadeout()
            menu.allbuttons[0].clicked = False
            gamestate = "Playing"
            firstframe = True
            pygame.display.flip()
            particlecontroller.removeall()
            
    ## playing stuff
    elif gamestate == "Playing":
        if firstframe == True:
            firstframe = False
            pressed = False
            birb.reset()
            pipecontroller.reset()
            pipecontroller.add(Pipe(1400, random.randint(300,600)))
            pipecontroller.add(Pipe(1000, random.randint(300,600)))
            birb.jump()
            fade.fadein()
            birb.jump()
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


    # after drawing, flip the display
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()