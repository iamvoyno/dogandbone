
import arcade 

#---------------------Constants-------------------------------------------------------------#

SW= 730
SH= 702
ST= "Dog and the Bone against Bot"
SPRITE_SCALING_RED_DOG= 0.13
SPRITE_SCALING_BLUE_DOG= 0.15
SPRITE_SCALING_PINK_DOG= 0.07
SPRITE_SCALING_BROWN_DOG= 0.3
RED_DOG = "reddog.jpg"
BLUE_DOG = "bluedog.jpg"
PINK_DOG = "pinkdog.jpg"
BROWN_DOG = "browndog.png"

#---------------------Drawing functions-----------------------------------------------------#

def draw_grid():
    ''' Draw a grid using square cell function '''
    for x in range(65, SW, 100):
        for y in range(51, SH, 100):
            draw_cell(x,y)

def draw_cell(x,y):
    ''' Draws a sqare cell of the grid at (x,y) '''
    arcade.draw_rectangle_outline(x,y,100,100,arcade.color.GREEN)
    #also make wide border and texture and fill color

def draw_dog(dog, scaling, x, y):
    ''' draw a specific player dog at center (x,y) '''
    dog_spirite = arcade.Sprite(dog, scaling)
    dog_spirite.center_x = x
    dog_spirite.center_y = y
    dog_spirite.draw()

def draw_fence(x_left, x_right, y_top, y_down):
    ''' draw a fence at left to right and top to down '''
    arcade.draw_lrtb_rectangle_filled(x_left, x_right, y_top, y_down, arcade.color.DARK_BROWN)
    #make a broad fence


arcade.open_window(SW, SH, ST)
arcade.set_background_color(arcade.color.WHITE)

#render process- done before other drawing games
arcade.start_render()

draw_grid()
draw_dog(RED_DOG, SPRITE_SCALING_RED_DOG, 65, 51)
draw_fence(15, 15, 200, 1)

#finish render process
arcade.finish_render()

#keeping window open until the user hits the close button
arcade.run()





#drawing from the window class

#class DogandBone(arcade.Window):
#    '''Main application class'''
#    def _init__(self, width, height):
#        super().__init__(width, height)

#        arcade.set_background_color(arcade.color.AMAZON)

#    def setup(self):
        #setting up game here
#        pass

#     def on_draw(self):
#         '''Rendering screen here'''
#         arcade.start_render()
         #drawing code goes here

#     def update(self, delta_time): #60 times per second
#         '''logic to move and the game logic'''
#         pass

#def main():
#    game = DogandBone(SW, SH)
#    game.setup()
#    arcade.run()

#if __name__ == "__main__"
#    main()
