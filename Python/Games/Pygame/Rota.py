# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

def getclick(piece):
    if board.turn == piece.color or board.turn == None:
        if pygame.mouse.get_pressed()[0] == 1:
            if piece.x - 20 <= pygame.mouse.get_pos()[0] <= piece.x + 20 and piece.y - 20 <= pygame.mouse.get_pos()[1] <= piece.y + 20 or piece==board.selected:
                return True
    return False
class piece():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.position = None
        self.firstmove = True
        self.movedict = {0: [0,1,2,3,4,5,6,7,8], 1: {0,9,2}, 2:{0,1,3}, 3:{0,2,4}, 4:{0,3,5}, 5:{0,4,6}, 6:{0,5,7}, 7:{0,6,8}, 8:{0,7,1}}    
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 20)
        pygame.draw.circle(screen, "black", (self.x, self.y), 20, 2)

class Board():
    def __init__(self):
        self.selected = None
        self.pieces = []
        self.turn = None
        for i in range (0,6):
            if i%2 == 0:
                self.addpiece(piece(100, 100 + (i * 100), "Black"))
            else:
                self.addpiece(piece(200, 100 + (i * 100), "white"))
                       ## center         ## top           ## bottom       ## left          ## right       ## top left    ## top right    ## bottom left  ## bottom right
        self.places = [[(640, 360),(0)], [(640, 60),(1)], [(640, 660),5], [(340, 360),7], [(940, 360),3], [(440,160),9], [(840, 160),2], [(440, 560),6], [(840, 560),4]]
    def draw(self):
        ## draw board circles
        pygame.draw.rect(screen, "gray", (0,0,1280,720))
        pygame.draw.rect(screen, "white", (0,0,1280,720), 10)
        pygame.draw.circle(screen, "white", (640, 360), 300, 10)

        ## draw board lines
        ## up/down, left/right
        pygame.draw.line(screen, "white", (640,60), (640, 660), 10)
        pygame.draw.line(screen, "white", (340, 360), (940,360), 10)
        ## diagonals
        pygame.draw.line(screen, "white", (440,160), (840, 560), 10)
        pygame.draw.line(screen, "white", (840, 160), (440, 560), 10)
        ## draw places
        for i in self.places:
            pygame.draw.circle(screen, "gray", (i[0]),40)
            pygame.draw.circle(screen, "white", (i[0]),40, 10)
        ## draw pieces
        for i in reversed(self.pieces):
            i.draw()
    
    def addpiece(self, piece):
        self.pieces.append(piece)
    
    def checksnap(self, piece):
        try:
            if piece.firstmove == True:
                for i in self.places:
                    if i[0][0] - 40 <= piece.x <= i[0][0] + 40 and i[0][1] - 40 <= piece.y <= i[0][1] + 40:
                        piece.x = i[0][0]
                        piece.y = i[0][1]
                        piece.position = i
                        piece.firstmove = False
                        if self.turn == None:
                            self.turn = piece.color
                        self.switchturn()
                        return True
            else:
                for i in self.places:
                    if i[0][0] - 40 <= piece.x <= i[0][0] + 40 and i[0][1] - 40 <= piece.y <= i[0][1] + 40:
                        if piece.position[1] in piece.movedict[i[1]]:
                            piece.x = i[0][0]
                            piece.y = i[0][1]
                            piece.position = i
                            piece.firstmove = False
                            self.switchturn()
                            return True
                        else:
                            piece.x = piece.position[0][0]
                            piece.y = piece.position[0][1]
                            return False
            return False
        except:
            return False
    def switchturn(self):
        if self.turn == "Black":
            self.turn = "white"
        else:
            self.turn = "Black"

board=Board()
board.selected = None

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")
    # RENDER YOUR GAME HERE
    # draw a circle at the mouse position
    board.draw()
    gotclick = False
    for i in board.pieces:
        if getclick(i):
            board.selected = i
            board.pieces.remove(i)
            board.pieces.insert(0,i)
            if not gotclick:
                gotclick = True
            break
    if not gotclick:
        board.checksnap(board.selected)
        board.selected = None
    if board.selected != None:
        board.selected.x = pygame.mouse.get_pos()[0]
        board.selected.y = pygame.mouse.get_pos()[1]
        
            


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()