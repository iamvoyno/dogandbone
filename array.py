import numpy as np

SCREEN_WIDTH = 16
SCREEN_HEIGHT = 10

STATUSARRAY = np.arange(SCREEN_WIDTH * SCREEN_HEIGHT).reshape(SCREEN_HEIGHT, SCREEN_WIDTH)

#initialize array
for i in range (0, SCREEN_WIDTH ):
    for j in range (0, SCREEN_HEIGHT ):
        STATUSARRAY[j][i] = 0
print(STATUSARRAY)

#black box
SCREEN_WIDTH_OFFSET = 4  #the black box starts with this pixel
SCREEN_HEIGHT_OFFSET = 1   #the black box start with this pixel
for i in range (SCREEN_WIDTH_OFFSET, SCREEN_WIDTH - SCREEN_WIDTH_OFFSET):
    for j in range (SCREEN_HEIGHT_OFFSET, SCREEN_HEIGHT - SCREEN_HEIGHT_OFFSET):
        STATUSARRAY[j][i] = -2
print(STATUSARRAY)

#blue box grid
for x_pos_box in range (0, 3):
    for y_pos_box in range (0, 3):
        x_coor = SCREEN_WIDTH_OFFSET + x_pos_box * 3
        y_coor = SCREEN_HEIGHT_OFFSET + y_pos_box * 3
        for i in range (x_coor, x_coor + 2):
            for j in range (y_coor, y_coor +2):
                STATUSARRAY[j][i] = -1
print(STATUSARRAY)
