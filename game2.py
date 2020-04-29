
#phase 4: Dog and Fence Interaction

import pygame, sys
from pygame.locals import *
import time 

pygame.init()

SCREEN_WIDTH = 1000 #decided 
SCREEN_HEIGHT = 700  #decided 
FENCE_RANGE = 7 #will go from 7 to 0  


SADDLEBROWN=(139,69,19) #decided
BLUE = (0, 0, 255)
BLACK = (0, 0, 0) 
LESSBLACK = (1,1,1) 
SQUAREBLACK = (2,2,2)
GREEN = (0, 255, 0)

selectedColor = 'red'

#Creating work surface named Display 
DISPLAY=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAY.fill(SADDLEBROWN)
pygame.display.update()

clock = pygame.time.Clock() 

#Making the dog class
#Position is the small integer denoted by cellPos 
#Coordinate is the big integer denoted by cellCor
class Dog:

    def __init__(self, color, image, xScale, yScale, xPosition, yPosition): 
        self.color = color 
        self.image = image
        self.xScale = xScale
        self.yScale = yScale
        self.cellPos = [xPosition, yPosition]
        self.fcount = FENCE_RANGE - 1  
        
    def display(self, screen, xPosition, yPosition):
        imageContainer = pygame.image.load(self.image)
        imageContainer = pygame.transform.scale(imageContainer, (self.xScale, self.yScale)) 
        self.cellPos = [xPosition, yPosition]
        cellCor = [(self.cellPos[0] * 91 + 185), (self.cellPos[1] * 91 + 35)]
        screen.blit(imageContainer, (cellCor[0], cellCor[1]))

redDog = Dog('red', 'reddog.jpg', 81, 81, 0, 3)
blueDog = Dog('blue', 'bluedog.jpg', 81, 81, 6, 3)
selectedDog = Dog(None, None, None, None, None, None) 


#making the fence class 
class Fence:

    def __init__(self, onBoard, xPos1, yPos1, xPos2, yPos2, align):
        self.onBoard = onBoard 
        self.align = align  
        self.gridPos1 = [xPos1, yPos1]
        self.gridPos2 = [xPos2, yPos2]
        self.bredth = 10 
        self.length = 172

    def display(self, screen, xPos1, yPos1, allignment):
        if allignment == 'v':
            self.align = allignment
            xCoor1 = (xPos1 * 91) + 266
            yCoor1 = (yPos1 * 91) + 35
            pygame.draw.rect(screen, GREEN, (xCoor1, yCoor1, 10, 172))
        elif allignment == 'h':
            self.align = allignment
            xCoor1 = (xPos1 * 91) + 185
            yCoor1 = (yPos1 * 91) + 116
            pygame.draw.rect(screen, GREEN, (xCoor1, yCoor1, 172, 10)) 
        else:
            '''the fence could not be printed cuz it was just initiated'''
            pass 



#Keeping track of where the dogs are and checking if the damn cell is free 
dogPositions = [redDog.cellPos , blueDog.cellPos]
def cellFree(cell):
    cellOccupied = False 
    if cell in dogPositions:
        cellOccupied = True 
        return cellOccupied   

#Is there a fence between your intial postion and final position
def checkFence(x_i, y_i, x_f, y_f):
    global boardFenceCellsV
    global boardFenceCellsH
    check = True 

    #vertical movement, checking horizontal fences
    if x_i == x_f:
        if y_i == y_f - 1 : #you are going down and no dog is nearby - working
            fccheck = list((x_i, y_i))
            if fccheck in boardFenceCellsH:
                check = False
                return check
            else:
                 return check

        elif y_i == y_f + 1 : #you are going up and no dog is nearby - working 
            fccheck = list((x_i, y_i - 1))
            if fccheck in boardFenceCellsH:
                check = False
                return check
            else:
                 return check 

        elif y_i == y_f - 2: #you are going down and there is a dog directly below you
            fccheck1 = list((x_f, y_f - 1))
            fccheck2 = list((x_i, y_i))
            if fccheck1 in boardFenceCellsH or fccheck2 in boardFenceCellsH:
                check = False
                return check
            else:
                 return check 

        elif y_i == y_f + 2: #you are going up and there is a dog directly above you
            fccheck1 = list((x_f, y_f))
            fccheck2 = list((x_i, y_i - 1))
            if fccheck1 in boardFenceCellsH or fccheck2 in boardFenceCellsH:
                check = False
                return check 
            else:
                 return check 


    #horizontal movement, checking vertical fences 
    elif y_i == y_f: 
        if x_i == x_f + 1 : #you are going back and no dog is nearby
            fccheck = list((x_i - 1, y_i))
            if fccheck in boardFenceCellsV:
                check = False
                return check 
            else:
                 return check 


        elif x_i == x_f - 1: # you are going forth and no dog is nearby 
            fccheck = list((x_i, y_i))
            if fccheck in boardFenceCellsV:
                check = False
                return check 
            else:
                 return check 


        elif x_i == x_f + 2: #you are going back and there is a dog directly behind you 
            fccheck1 = list((x_f, y_f))
            fccheck2 = list((x_i - 1, y_i))
            if fccheck1 in boardFenceCellsV or fccheck2 in boardFenceCellsV:
                check = False
                return check 
            else:
                 return check 


        elif x_i == x_f - 2: #you are going forward and there is a dog directly ahead of you 
            fccheck1 = list((x_f - 1, y_f)) 
            fccheck2 = list((x_i, y_i))
            if fccheck1 in boardFenceCellsV or fccheck2 in boardFenceCellsV:
                check = False
                return check 
            else:
                 return check 


#Is the opposing dog nearby- returns up, down, left, right, nowhere and hold 
def dogNearby(dog, x_i, y_i):
    status = 'hold'  

    if dog.color == 'red':
        comparePos = blueDog.cellPos
    elif dog.color == 'blue':
        comparePos = redDog.cellPos

    if comparePos[0] == x_i and comparePos[1] == y_i + 1 :
            status = 'down' 
            return status  
    elif comparePos[0] == x_i and comparePos[1] == y_i -1:
            status = 'up' 
            return status  
    elif comparePos[1] == y_i and comparePos[0] == x_i - 1:
            status = 'left'
            return status 
    elif comparePos[1] == y_i and comparePos[0] == x_i + 1:
            status = 'right' 
            return status  
    else: 
        status = 'nowhere'
        return status

    return status 


def checkDog(dog, x_i, y_i, x_f, y_f, color): 
    moveValid = False
    global selectedColor

    #checking if the target cell is blue
    if color == BLUE and dog.color == selectedColor:

        #checking dog nearby
        status = dogNearby(dog, x_i, y_i)
        if status == 'nowhere':
            '''Dog isolated'''

            if x_i + 1 == x_f and y_i == y_f:
               moveValid = True 
            if x_i - 1 == x_f and y_i == y_f:
                moveValid = True 
            if x_i == x_f and y_i + 1 == y_f:
                moveValid = True
            if x_i == x_f and y_i - 1 == y_f:
                moveValid = True 
            return moveValid

        elif status == 'up':
            '''Another dog is up the dog'''
            if x_i + 1 == x_f and y_i == y_f:
               moveValid = True 
            if x_i - 1 == x_f and y_i == y_f:
                moveValid = True 
            if x_i == x_f and y_i + 1 == y_f:
                moveValid = True
            if x_i == x_f and y_i - 2 == y_f:
                moveValid = True 
            return moveValid 

        elif status == 'down':
            '''Another dog is below the dog'''
            if x_i + 1 == x_f and y_i == y_f:
               moveValid = True 
            if x_i - 1 == x_f and y_i == y_f:
                moveValid = True 
            if x_i == x_f and y_i + 2 == y_f:
                moveValid = True
            if x_i == x_f and y_i - 1 == y_f:
                moveValid = True 
            return moveValid  

        elif status == 'left':
            '''Another dog is left of the dog'''
            if x_i + 1 == x_f and y_i == y_f:
               moveValid = True 
            if x_i - 2 == x_f and y_i == y_f:
                moveValid = True 
            if x_i == x_f and y_i + 1 == y_f:
                moveValid = True
            if x_i == x_f and y_i - 1 == y_f:
                moveValid = True 
            return moveValid 

        elif status == 'right':
            '''Another dog is right of the dog'''
            if x_i + 2 == x_f and y_i == y_f:
               moveValid = True 
            if x_i - 1 == x_f and y_i == y_f:
                moveValid = True 
            if x_i == x_f and y_i + 1 == y_f:
                moveValid = True
            if x_i == x_f and y_i - 1 == y_f:
                moveValid = True 
            return moveValid 

    else:
        print('Error: Either the pixel is not blue or its not your chance')
        return moveValid

    return moveValid 


def moveDog(dog, final, screen, color):

    global selectedColor
    x_i = dog.cellPos[0]
    y_i = dog.cellPos[1]
    x_f = final[0]
    y_f = final[1]
    valid = checkDog(dog, x_i, y_i, x_f, y_f, color)    

    if valid:
        valid = checkFence(x_i, y_i, x_f, y_f)
        
        if valid: 
            dog.display(screen, x_f, y_f)
            pygame.draw.rect(screen, BLUE, ((x_i * 91 + 185), (y_i * 91 + 35), 81, 81))
            dog.cellPos = [x_f, y_f]
            pygame.display.update() 

            global dogPositions
            dogPositions = [redDog.cellPos , blueDog.cellPos]

            if dog.color == 'red':
                selectedColor = 'blue'
            else:
                selectedColor = 'red' 

        else:
            print('Error: Your move for the dog was not valid because there is a fence in between')


    else:
        print('Error: Your move for the dog was not valid')


def selectDog(dogClick_ipos): 
    selectedDog = None 
    if redDog.cellPos[0] == dogClick_ipos[0] and redDog.cellPos[1] == dogClick_ipos[1]:
        return redDog

    elif blueDog.cellPos[0] == dogClick_ipos[0] and blueDog.cellPos[1] == dogClick_ipos[1]:
        return blueDog 


def selectFence(x):
    global selectedColor 
    selectedFence = False 
    if x < 185:
        if redDog.fcount > -1 and selectedColor == 'red': 
            selectedFence = True
            return selectedFence
        else:
            return selectedFence 

    elif x > 815: 
        if blueDog.fcount > -1 and selectedColor == 'blue':
            selectedFence = True
            return selectedFence 
        else: 
            return selectedFence


def vorh(x, y):

    allignment = 'hold'
    color = tuple(DISPLAY.get_at((x, y))[:3])
    if color == BLACK:
        allignment = 'v'
        return allignment  
    elif color == LESSBLACK:
        allignment = 'h'
        return allignment  
    else:
        print('Error: Select a proper block for the fence')
        return allignment  

boardFence = []
boardFenceCellsV = []
boardFenceCellsH = []
boardFencel = 0
def addOnBoard(gridPos1, gridPos2, align):
    global boardFencel
    global boardFenceCellsV
    global boardFenceCellsH

    fence = Fence(True, gridPos1[0], gridPos1[1], gridPos2[0], gridPos2[1], align)
    boardFence.append(fence) 

    if fence.align == 'v':
        boardFenceCellsV.append(fence.gridPos1)
        boardFenceCellsV.append(fence.gridPos2) 
        print() 
        print()
        print(boardFenceCellsV)

    elif fence.align == 'h': 
        boardFenceCellsH.append(fence.gridPos1)
        boardFenceCellsH.append(fence.gridPos2) 
        print() 
        print()
        print(boardFenceCellsH)


    boardFencel += 1 



def checkAdj(cell1, cell2, allignment):
    ''' check adjacensy and dislpay the color- fucking spellings ''' 

    global selectedColor 
    proceed = False

    if allignment == 'v':
        if (cell1[0] == cell2[0] and cell1[1] == cell2[1] + 1) or (cell1[0] == cell2[0] and cell1[1] == cell2[1] - 1):

            if cell1[1] == cell2[1] + 1:
                gridPos1 = [cell2[0], cell2[1]]
                gridPos2 = [cell1[0], cell1[1]] 
            else:
                gridPos1 = [cell1[0], cell1[1]]
                gridPos2 = [cell2[0], cell2[1]] 
            align = 'v'
 
            if selectedColor == 'red':
                print('Control: red fcount has been deprecated')
                redDog.fcount -= 1 
            else:
                print('Control: blue fcount has been deprecated')
                blueDog.fcount -= 1 

            addOnBoard(gridPos1, gridPos2, align)


            proceed = True
            return proceed       
        else:
            '''invalid''' 
            print('Error: The cells seleceted for the fence are not in sync')
            return proceed 

    elif allignment == 'h':
        if (cell1[1] == cell2[1] and cell1[0] == cell2[0] + 1) or (cell1[1] == cell2[1] and cell1[0] == cell2[0] - 1):
            ''' valid ''' 

            if cell1[0] == cell2[0] + 1:
                gridPos1 = [cell2[0], cell2[1]]
                gridPos2 = [cell1[0], cell1[1]] 
            else:
                gridPos1 = [cell1[0], cell1[1]]
                gridPos2 = [cell2[0], cell2[1]]

            align = 'h'

            if selectedColor == 'red':
                print('Control: red fcount has been deprecated')
                redDog.fcount -= 1 
            else:
                print('Control: blue fcount has been deprecated')
                blueDog.fcount -= 1 

            addOnBoard(gridPos1, gridPos2, align)

            proceed = True 
            return proceed       
        else: 
            ''' invalid ''' 
            print('Error: The cells selected for the fence are not adjascent')
            return proceed 
    else:
        return proceed 


def checkAlign(cell1, cell2, allignment1, allignment2):
    ''' are the alignment of the cells in sync '''

    proceed = False 
    if allignment1 == allignment2:
        proceed = checkAdj(cell1, cell2, allignment1) 
        return proceed 
    else:
        print('Error: The cells are not aligned')
        return proceed 


#drawing the complete game board
def deploy_game_board():

    ''' Function for drawing the 4 major elements of the game board''' 
    DISPLAY.fill(SADDLEBROWN)
    pygame.draw.rect(DISPLAY, GREEN, (60, 159, 10, 172))
    pygame.draw.rect(DISPLAY, GREEN, (875, 159, 10, 172))   

    #square cell grid
    for i in range (7):
        for j in range (7):
            pygame.draw.rect(DISPLAY, BLUE,((185 + i * 91), (35 + j * 91), 81, 81))

    #vertical fence grid
    for i in range (6):
        for j in range (7):
            pygame.draw.rect(DISPLAY, BLACK, ((266 + i * 91), (35 + j * 91) , 10, 81))

    #horizontal fence grid
    for i in range (7):
        for j in range (6):
            pygame.draw.rect(DISPLAY, LESSBLACK, ((185 + i * 91), (116 + j * 91), 81, 10))

    #small squares grid 
    for i in range (6):
        for j in range (6):
            pygame.draw.rect(DISPLAY, SQUAREBLACK, ((266 + i * 91), (116 + j * 91), 10, 10))


def initiate():
    redDog.display(DISPLAY, redDog.cellPos[0], redDog.cellPos[1])
    blueDog.display(DISPLAY, blueDog.cellPos[0], blueDog.cellPos[1]) 
    for i in range(0,boardFencel):
        boardFence[i].display(DISPLAY, boardFence[i].gridPos1[0], boardFence[i].gridPos1[1], boardFence[i].align)
        pygame.display.update()


#=======================CONTROL FUNCTIONS=================================================
def controlDisp():
    print() 
    print() 
    print('We are in control disp function trying to touble shoot the fence problem')
    time.sleep(2) 
    print()
    print('For the red list we have') 
    for i in range(0,redDog.fcount):
        print('Printing red fence' + str(i))
        controlFunc(redFence[i])
        time.sleep(5)
        print() 
    print()
    print('For the blue list we have')
    for i in range(0, blueDog.fcount):
        print('Printing blue fence' + str(i))
        controlFunc(blueFence[i])
        time.sleep(5)
        print()
    print() 
    print('For the on board list we have') 
    for i in range(0, boardFencel):
        print('Printing board fence' + str(i))
        controlFunc(boardFence[i])
        time.sleep(5) 
        print()

def controlFunc(fence):
    print('fence parameters') 
    print(fence.color)
    print(fence.onBoard)
    print(fence.xPos1)
    print(fence.yPos1)
    print(fence.xPos2)
    print(fence.yPos2)
    print(fence.align)
#=========================================================================================


def main():
    
    ''' Actual game play control area''' 
    global selectedColor #indicator for whose chance it is 
    select = False  #indicator for is something selected or not 
    selectD = False #indicator if dog is selected or not
    selectF = False #indicator if fence is selcted or not 
    countF = 0 #control for selecting fences 


    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP: 
                click = pygame.mouse.get_pos() #click is a tupple storing the coordinates of the mouse click
                x = click[0]
                y = click[1]  
                color = tuple(DISPLAY.get_at((x, y))[:3])

                if select == False: 
                    dogClick_xipos = (click[0] - 185) // 91
                    dogClick_yipos = (click[1] - 35) // 91
                    dogClick_ipos = [dogClick_xipos, dogClick_yipos]

                    if dogClick_ipos in dogPositions:
                        ''' select dog''' 
                        selectedDog = selectDog(dogClick_ipos)

                        if selectedDog is None:
                            select = False 
                        elif selectedDog is not None:
                            select = True 
                            selectD = True 
                            selectF = False
                            

                    elif color == GREEN:
                        '''player selected a fence'''
                        selectedFence = selectFence(click[0]) 

                        if selectedFence is False:
                            print('Error: Either you are all out of fences or you chose the fence of the other player')
                            select = False
                        elif selectedFence is True: 
                            print('Instruction: You have selected a fence, now choose two cells on the board for your fencd')
                            selectD = False
                            selectF = True 
                            select = True
                            

                    else:
                        '''or the player selected an invalid position'''
                        print('Error: Either select a dog or a fence') 
 

                elif select == True:
                    '''select is true''' 

                    if selectD == True and selectF == False :
                        '''selected a dog'''
                        dogClick_xfpos = (click[0] - 185) // 91
                        dogClick_yfpos = (click[1] - 35) // 91
                        dogClick_fpos = [dogClick_xfpos, dogClick_yfpos]
                        moveDog(selectedDog, dogClick_fpos, DISPLAY, color)
                        select = False
                        selectD = False

                    if selectF == True and selectD == False:
                        '''selected a fence''' 

                        countF += 1 

                        if countF == 1:
                            ''' one more cell is to be selected '''

                            fenceone_xpos = click[0]
                            fenceone_ypos = click[1]
                            allignment1 = vorh(fenceone_xpos, fenceone_ypos)

                            if allignment1 == 'v':
                                cell1 =  [(fenceone_xpos-266) // 91  , (fenceone_ypos-35) // 91]
                            elif allignment1 == 'h':
                                cell1 =  [(fenceone_xpos-185) // 91  , (fenceone_ypos-116) // 91]
                            else:
                                print('Error: No valid allignment was returned')

                            print('Instruction: One more cell is to be selected')

                        elif countF == 2:
                            ''' both cells have been selected ''' 

                            fencetwo_xpos = click[0]
                            fencetwo_ypos = click[1]
                            allignment2 = vorh(fencetwo_xpos, fencetwo_ypos)

                            if allignment2 == 'v':
                                cell2 =  [(click[0]-266) // 91  , (click[1]-35) // 91]
                            elif allignment2 == 'h':
                                cell2 =  [(fencetwo_xpos-185) // 91  , (fencetwo_ypos-116) // 91]
                            else:
                                print('Error: No valid allignment was returned')

                            print('Instruction: Both cells have been selected')

                            proceed = checkAlign(cell1, cell2, allignment1, allignment2)
                            
                            if proceed == True:
                                ''' the color has been changed and the way has been blocked, release chance '''
                                countF = 0
                                select = False
                                selectF = False 
                                selectD = False 
                                if selectedColor == 'red':
                                    print('selected color has been changed')
                                    selectedColor = 'blue'
                                else: 
                                    selectedColor = 'red' 
                            elif proceed == False: 
                                ''' user is asked to select a valid cell ''' 
                                print('Error: The cells selected were not valid')
                                select = False
                                selectF = False 
                                selectD = False
                        

        deploy_game_board() 
        initiate() 
        

        myfont = pygame.font.Font('sans.ttf', 30) #copied

        stringTurn = selectedColor + "'s turn" #copied
        labelTurn = myfont.render(stringTurn, 1, BLACK) #copied 
        DISPLAY.blit(labelTurn, (20, 620))

        stringFenceRed = 'x 8' #to be softcoded 
        labelFenceRed = myfont.render(stringFenceRed, 1, BLACK) 
        DISPLAY.blit(labelFenceRed, (100, 230))

        stringFenceBlue = 'x 8' #to be softcoded 
        labelFenceBlue = myfont.render(stringFenceBlue, 1, BLACK)
        DISPLAY.blit(labelFenceBlue, (915, 230)) 
        
        
        pygame.display.update()
        clock.tick(20)

main() 