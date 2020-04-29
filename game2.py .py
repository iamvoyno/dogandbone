import pygame, sys
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 1000 #decided
SCREEN_HEIGHT = 700  #decided 


SADDLEBROWN=(139,69,19) #decided
BLUE=(0,0,255)
BLACK = (0,0,0) 


#Creating work surface named Display 
DISPLAY=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAY.fill(SADDLEBROWN)
pygame.display.update() #don't know why


#drawing the complete game board
def deploy_game_board():

    ''' Function for drawing the 4 major elements of the game board''' 
    
    #square cell grid
    for i in range (7):
        for j in range (7):
            pygame.draw.rect(DISPLAY,BLUE,((185 + i * 91), (35 + j * 91), 81, 81))

    #vertical fence grid
    for i in range (6):
        for j in range (7):
            pygame.draw.rect(DISPLAY,BLACK, ((266 + i * 91), (35 + j * 91) , 10, 81))

    #horizontal fence grid
    for i in range (7):
        for j in range (6):
            pygame.draw.rect(DISPLAY,BLACK, ((185 + i * 91), (116 + j * 91), 81, 10))

    #small squares grid 
    for i in range (6):
        for j in range (6):
            pygame.draw.rect(DISPLAY,BLACK, ((266 + i * 91), (116 + j * 91), 10, 10))





def main(): 

    ''' Actual game play control area''' 
    while True:

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

        deploy_game_board() 

        pygame.display.update()


main() 