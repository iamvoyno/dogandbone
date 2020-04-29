#two player version 

import pygame 
import time 

pygame.init() #what for?

#screen parameters
SW= 730
SH= 702

#grid cell sizes
CW = 100
CH = 100 

factor = 25 * 1.5 #what for? 

#defining color- picked exactly for training
white = (255, 255, 255)
d_white = (250, 250, 250)
black = (0, 0, 0)
teal = (0, 128, 128)
blue_black = (50, 50, 50)
red= #whatever the color is
green= #whatever the color code is

game_display = pygame.display.set_mode((SW, SH)) #why the double brackets?
pygame.display.update() #what for?
clock = pygame.time.Clock() #what for? 

selected_dog = 'red'

class dog_cell: #a separate cell board
    x = 0 #x coordinate
    y = 0 #y coordinate
    family = '' #color of the dog - red , green
    pic = '' #pic of the dog 

    def __init__(self, x_position, y_position, d_family):
        self.x = x_position 
        self.y = y.position 
        self.family = d_family 

class fence_edge: #a separate grid board
    x1 = -1 #coordinates of the first edge
    y1 = -1
    x2 = -1 #coordinated of the second edge
    y2 = -1 
    family = '' 
    on_board = 'False'

    def __init__(self, x1_position, y1_position, x2_position, y2_position, family, on_board):
        self.x1 = x1_position
        self.y1 = y1_position
        self.x2 = x2_position
        self.y2 = y2_position
        self.family = family
        self.on_board = on_board 

selected_dog = dog 
selected_fence = fence 

initial_set_up = [dog_cell(6,3,"red"), fence_edge("red"), fence_edge("red"), fence_edge("red"), fence_edge("red"), fence_edge("red"), fence_edge("red"), fence_edge("red"), fence_edge("red"),
                  dog_cell(0,3,"green"), fence_edge("green"), fence_edge("green"), fence_edge("green"), fence_edge("green"), fence_edge("green"), fence_edge("green"), fence_edge("green"), fence_edge("green"),
                 ]

#printing line which is not relevent up till now

#-------------------------------------important functions------------------------------



def board_draw_cells():
    x= 0 
    y= 0
    game_display.fill(black) 

    selected_family = 'red' 
    for i in range(7):
        if i % 2 == 0:
            j = 0 
        else:
            j = 1 
        while j < 7:
            pygame.draw.rect(game_display, d_white, (i * 50 * 1.5, j * 50 * 1.5, block_width, block_height))
            j += 2 

#---------------------------------------------------------------------------------------

def game(): #not complete yet
    #something
    #something

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = pos[0] // 75 #dont know why?
                b = post[1] // 75 #dont know why?
                pygame.draw.rect()
                pygame.display.update()
                time.sleep(0.03) 

                if not selec:
                    selected_piece = select_block(a,b)
                    selec = True 
                    if selected_piece is not None:
                        print(selected_piece.x, " ", selected_piece.y) 

                    else:
                        selec = False 

                else:
                    if selected_piece is not None:
                        move(selected_piece.x, selected_piece.y, a, b) 
                    selec = False 
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        board_draw() 
        
        initialize_piece()
        myfont = pygame.font.Font("sans.ttf", 30)
        string = selected_family + "'s turn"
        label = myfont.render(string, 1, white)


        game_display.blit(label, (20, 620)) 
        pygame.display.update() 

        clock.tick(20) 

game() 

