from settings import *

x_chips = [0]*len(grid)

def switchTeam(x):
    global curr
    if curr:
        grid[0][x] = 1
        curr = False
    else:
        grid[0][x] = 2
        curr = True


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.shape_list = None
        self.radius = 20


    def update(self, dt):
        """ Move everything """

        for i in range(1, len(grid)):
            if grid[i-1] == 1:
                pass

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.KEY_1:
            grid[0][0] = 1
            switchTeam(0)
            print(curr)
        if symbol == arcade.key.KEY_2:
            grid[0][1] = 1
            switchTeam(1)
        if symbol == arcade.key.KEY_3:
            grid[0][2] = 1
            switchTeam(2)
        if symbol == arcade.key.KEY_4:
            grid[0][3] = 1
            switchTeam(3)
        if symbol == arcade.key.KEY_5:
            grid[0][4] = 1
            switchTeam(4)
        if symbol == arcade.key.KEY_6:
            grid[0][5] = 1
            switchTeam(5)



    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        global curr
        for i in range(len(x_chips)):

            if x_chips[i] - WIDTH < y < x_chips[i] and (button == arcade.MOUSE_BUTTON_LEFT or button == arcade.MOUSE_BUTTON_MIDDLE or button == arcade.MOUSE_BUTTON_RIGHT):
                if curr:
                    grid[i][len(grid[0])-1] = 1
                    curr = False
                else:
                    grid[i][len(grid[0])-1] = 2
                    curr = True




    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        margin_x = SCREEN_WIDTH//2 - WIDTH*2
        margin_y = SCREEN_HEIGHT//2 - WIDTH*2
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                x_chips[j] = (margin_x + j*WIDTH)
                arcade.draw_rectangle_filled( margin_x + i*WIDTH, margin_y*2 + -j *WIDTH,WIDTH, WIDTH, arcade.color.WHITE)
                if grid[j][i] == 0:
                    arcade.draw_circle_filled(margin_x + i*WIDTH, margin_y*2 + -j*WIDTH, WIDTH//2, arcade.color.BLACK)
                if grid[j][i] == 1:
                    arcade.draw_circle_filled(margin_x + i*WIDTH, margin_y*2 +-j*WIDTH, WIDTH//2, arcade.color.RED)
                if grid[j][i] == 2:
                    arcade.draw_circle_filled(margin_x + i*WIDTH, margin_y*2 + -j*WIDTH, WIDTH//2, arcade.color.BLUE)



def main():
    window = MyGame()
    arcade.run()


if __name__ == "__main__":

    main()
    print(x_chips)
