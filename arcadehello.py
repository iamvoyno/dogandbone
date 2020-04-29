import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

arcade.open_window(600, 600, "yeah!")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

arcade.draw_circle_filled(300,300,200, arcade.color.YELLOW)
arcade.draw_circle_filled(370,350,20, arcade.color.BLACK)
arcade.draw_circle_filled(230,350,20, arcade.color.BLACK)
arcade.draw_arc_outline(300,280, 120, 100, arcade.color.BLACK, 190, 350, 10)
arcade.finish_render()
arcade.run()
