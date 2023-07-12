import pygame
import time

# pygame setup
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 30)
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

## game setup
pressed = False
def getclick():
    global pressed
    for i in board.places:
        if pygame.mouse.get_pressed()[0] and pygame.Rect(i[0][0]-40, i[0][1]-40, 80, 80).collidepoint(pygame.mouse.get_pos()) and not pressed:
            pressed = True
            print(f"clicked spot{i[1]}")
            return i[1]
        if pygame.mouse.get_pressed()[0] == False:
            pressed = False
    return None

## peice class
class piece():
    def __init__(self, color):
        self.color = color
        self.position = None
        self.firstmove = True
        self.size = 20
        self.movedict = {0: [0,1,2,3,4,5,6,7,8], 1: {0,8,2}, 2:{0,1,3}, 3:{0,2,4}, 4:{0,3,5}, 5:{0,4,6}, 6:{0,5,7}, 7:{0,6,8}, 8:{0,7,1}}    
    def draw(self):
        if self.position != None:
            for i in board.places:
                if i[1] == self.position:
                    pygame.draw.circle(screen, self.color, (i[0]), self.size)
                    pygame.draw.circle(screen, "black", (i[0]), self.size, 2)
    def select(self):
        for i in range(0,10):
            self.size = self.size + i/3
            self.draw()
            pygame.display.flip()
    def deselect(self):
        self.size = 20
        self.draw()

class Board():
    def __init__(self):
        self.allpieces = []
        self.wins = {"Black": 0, "White": 0}
        self.selected = None
        self.turn = "Black"
        self.opposites = {1: 5, 2: 6, 3: 7, 4: 8, 5: 1, 6: 2, 7: 3, 8: 4}
                       ## center         ## top           ## bottom       ## left          ## right       ## top left    ## top right    ## bottom left  ## bottom right
        self.places = [[(640, 360),(0)], [(640, 60),(1)], [(840, 160),2], [(940, 360),3], [(840, 560),4], [(640, 660),5], [(440, 560),6], [(340, 360),7], [(440,160),8]]

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

        ## draw text
        text = my_font.render(f"Black: {self.wins['Black']}", False, (0, 0, 0))
        screen.blit(text, (10, 10))
        text = my_font.render(f"White: {self.wins['White']}", False, (0, 0, 0))
        screen.blit(text, (10, 40))
        text = my_font.render(f"{self.turn}'s Turn", False, (0, 0, 0))
        screen.blit(text,(1100, 10))
            

        ## draw pieces
        for i in reversed(self.allpieces):
            i.draw()
    ## swaps turn
    def changeturn(self):
        board.draw()
        self.checkwin()
        if self.turn == "Black":
            self.turn = "White"
        else:
            self.turn = "Black"

    ## logic for checking if the board is in a win state
    def checkwin(self):
        self.boardstate=[None,None,None,None,None,None,None,None,None]
        prev = None
        for i in self.allpieces: 
            self.boardstate.pop(i.position)
            self.boardstate.insert(i.position, i.color)
        if self.boardstate[0] != None:
            print("checking for 3 in a row around center")
            count = 0
            for type in self.boardstate:
                if count == 0:
                    pass
                elif type == None:
                    pass
                elif type == self.boardstate[self.opposites[count]]:
                    if self.boardstate[0] == type:
                        print(f"{board.turn} wins") 
                        board.reset(board.turn)
                        return
                else:
                    pass
                count += 1


        print("checking for 3 in a row around edge")
        ## logic to remove the seem from the list
        self.boardstate.pop(0)
        self.boardstate = self.boardstate + self.boardstate 
        count = 0
        for i in self.boardstate:
            if i == None:
                prev = None
                count = 0
            elif prev == i:
                count = count + 1
            else:
                count = 0
            prev = i
            if count == 2:
                print(f"{board.turn} wins")
                board.reset(board.turn)
                return
            
    def reset(self,color):
        board.draw()
        pygame.display.flip()
        time.sleep(1)
        board.allpieces = []
        board.selected = None
        board.turn = color
        board.wins[color] += 1
                
def gamelogic():
    click = getclick()
    if click == None:
        pass
    else:
        if len(board.allpieces) < 6:
            if click not in [i.position for i in board.allpieces]:
                print ("empty space")
                print("placing peices")
                if board.turn == "Black":
                    board.allpieces.append(piece("Black"))
                else:
                    board.allpieces.append(piece("White"))
                board.allpieces[-1].position = click
                board.changeturn()
        else:
            try:
                board.selected.deselect()
            except:
                pass
            print("all peices placed")
            if board.selected == None:
                for i in board.allpieces:
                    if i.position == click:
                        if i.color == board.turn:
                            print("selected")
                            board.selected = i
                            board.selected.select()
            else:
                print("moving")
                if board.selected.color == board.turn:
                    if click in board.selected.movedict[board.selected.position]:
                        print ("valid move")
                        if click not in [i.position for i in board.allpieces]:
                            print ("empty space")
                            board.selected.position = click
                            board.changeturn()
                board.selected = None



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
    gamelogic()


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()