from settings import *
import time

x_chips = [0]*len(grid)

def switchTeam(x):
    global curr
    if curr:
        grid[0][x] = 1
        curr = False
    else:
        grid[0][x] = 2
        curr = True



def win():
    boardHeight = len(grid[0])
    boardWidth = len(grid)
    tile = 2 if curr else 1
    # check horizontal spaces
    for y in range(boardHeight):
        for x in range(boardWidth - 3):
            if tile != 0 and grid[x][y] == tile and grid[x + 1][y] == tile and grid[x + 2][y] == tile and grid[x + 3][
                y] == tile:
                team(curr)
                return True

    # check vertical spaces
    for x in range(boardWidth):
        for y in range(boardHeight - 3):
            if  tile != 0 and grid[x][y] == tile and grid[x][y + 1] == tile and grid[x][y + 2] == tile and grid[x][
                        y + 3] == tile:
                team(curr)
                return True

    # check / diagonal spaces
    for x in range(boardWidth - 3):
        for y in range(3, boardHeight):
            if tile != 0 and grid[x][y] == tile and grid[x + 1][y - 1] == tile and grid[x + 2][y - 2] == tile and grid[x + 3][
                        y - 3] == tile:
                team(curr)
                return True

    # check \ diagonal spaces
    for x in range(boardWidth - 3):
        for y in range(boardHeight - 3):
            tile = grid[x-1][y-1]
            if tile != 0 and grid[x][y] == tile and grid[x + 1][y + 1] == tile and grid[x + 2][y + 2] == tile and grid[x + 3][
                        y + 3] == tile:
                print("Win")
                team(curr)
                return True

def team(won):
    arcade.draw_text(f"{'Red Team' if not won else 'Blue Team'} Won", SCREEN_WIDTH//2 - 200, SCREEN_HEIGHT-100,
                     arcade.color.RED if not won else arcade.color.BLUE
                     , 52, font_name='GARA')


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.shape_list = None
        self.radius = 20


    def update(self, dt):
        """ Move everything """

        # if no team has win

        if not win():
            if not self.draw():
                for i in range(1, len(grid)):
                    for j in range(len(grid[i])):
                        # check if after is empty slot
                        if grid[i-1][j] != 0 and grid[i][j] == 0:
                            # chip falls down
                            grid[i][j] = grid[i-1][j]
                            grid[i - 1][j] = 0
        else:
            time.sleep(1)
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    grid[i][j] = 0




    def on_key_press(self, symbol: int, modifiers: int):
        keys = [49 + i for i in range(len(grid[0]))]
        for i in range(len(keys)):
            if symbol == keys[i] and grid[0][i] == 0:
                switchTeam(i)



    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        global curr
        for i in range(len(x_chips)):

            if x_chips[i] - WIDTH < x < x_chips[i] and \
                    (button == arcade.MOUSE_BUTTON_LEFT or
                     button == arcade.MOUSE_BUTTON_MIDDLE or
                     button == arcade.MOUSE_BUTTON_RIGHT)\
                    and grid[0][i] == 0:
                switchTeam(i)




    def on_draw(self):
        """
        Render the screen.
        """
        if not win():
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

        if win():
            team(curr)



    def draw(self):
        return False not in [j != 0 for i in grid for j in i]


def main():
    window = MyGame()
    arcade.run()


if __name__ == "__main__":

    main()
    print(x_chips)
