import pygame, sys
from pygame.locals import *

SCREEN_WIDTH = 1000 #decided
SCREEN_HEIGHT = 700  #decided 



def main():

    pygame.init()

    DISPLAY=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    SADDLEBROWN=(139,69,19) #decided
    BLUE=(0,0,255)
    BLACK = (0,0,0) 


#--------------------------CHANGE THE DAMN COLORS---------------------------------------
    DISPLAY.fill(SADDLEBROWN) 
    
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


    #putting in the red_dog 
    red_dog_pic = pygame.image.load('reddog.jpg')
    red_dog_pic = pygame.transform.scale(red_dog_pic, (81,81))
    DISPLAY.blit(red_dog_pic, (185,308))

    #moving the dog around 
    # no freaking idea after procrastinating for 2 days...

    #clearing funciton- redrawing the background 


    #checking the dog position
    def dog_check(x_i, y_i, x_f, y_f):
        moveValid = False 

        if x_i + 1 == x_f and y_i == y_f:
            moveValid = True 
        if x_i - 1 == x_f and y_i == y_f:
            moveValid = True 
        if x_i == x_f and y_i + 1 == y_f:
            moveValid = True
        if x_i == x_f and y_i - 1 == y_f:
            moveValid = True 
        return moveValid 
    
    #moving the fucking dog which I dont know how 
    #def move(x_initial, y_initial, x_final, y_final):
    #    if dog_check(x_initial, y_initial, x_final, y_final):
    #        red_dog_x = x_final 
    #        red_dog_y = y_final 


    #selecting dogs (not selecting cells) 
    #def select_dog_cell(x_cursor, y_cursor):
    #    selected_dog = None 
    #    if red_dog_x == x_cursor and red_dog_y == y_cursor:
    #        return 'red_dog'


    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type== pygame.MOUSEBUTTONUP:

                #final position
                pos = pygame.mouse.get_pos() 
                x_final = str(pos[0])
                y_final = str(pos[1])
                print("The positons are" + x_final + y_final)
                #input() 
                x_final = int(x_final) 
                y_final = int(y_final) 
                x_fcell = (x_final - 185) // 91
                y_fcell = (y_final - 35) // 91
                print(x_fcell) 
                print(y_fcell)
                #input() 

                #checking valid move 
                valid = dog_check(0, 3, x_fcell, y_fcell) 
                if valid:
                    print ("valid") 
                    DISPLAY.blit(red_dog_pic, ( (x_fcell * 91 + 185), (y_fcell * 91 + 35)))
                    pygame.draw.rect(DISPLAY,BLUE,(185, 308, 81, 81))
                else: 
                    print ("not valid") 
        pygame.display.update()

main()