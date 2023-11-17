import pygame 
 
pygame.init()
## set up display
display = pygame.display.set_mode((800, 600))

## set up clock
clock = pygame.time.Clock()

while True:
    ## get events
    for event in pygame.event.get():
        ## if quit
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    ## update display
    display.fill((0,0,0))

    ## game logic here
    
    ## draw here 
    pygame.draw.rect(display, (255,0,0), (0,0,50,50))

    ## update display
    pygame.display.flip()

    ## set fps + tick
    clock.tick(60)

