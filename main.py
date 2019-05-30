import arcade

# screen proportions
WIDTH = 600
HEIGHT = 600
TITLE = "Connect Four"

# Grid properties
ROW = COL = 5
grid = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]
PORTION = 50
#open the window. Set the window title and dimensions
arcade.open_window(WIDTH, HEIGHT, TITLE)

# set the background color to black
arcade.set_background_color(arcade.color.BLACK)

# Clear screen and start render process
arcade.start_render()


def draw():
    """
    draw connect four
    """
    margin_x = WIDTH // 2 - PORTION*2
    margin_y = HEIGHT//2 - PORTION*2
    for row in range(ROW):
        for column in range(COL):
            arcade.draw_rectangle_filled(margin_x + row * PORTION, margin_y + column * PORTION, PORTION,
                                         PORTION, arcade.color.WHITE)
            if grid[column][row] == 0:
                arcade.draw_circle_filled(margin_x + row * PORTION, margin_y + column *PORTION,  PORTION//2, arcade.color.BLACK)
            elif grid[column][row] == 1:
                arcade.draw_circle_filled(margin_x + row * PORTION, margin_y + column * PORTION, PORTION // 2,
                                          arcade.color.RED)
            else:
                arcade.draw_circle_filled(margin_x + row * PORTION, margin_y + column * PORTION, PORTION // 2,
                                          arcade.color.BLUE)



# draw the grid
draw()
# Finish drawing and display the result
arcade.finish_render()

# Keep the window open until the user hits  the 'close' button
arcade.run()