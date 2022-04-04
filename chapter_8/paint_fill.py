# python3
# paint_fill.py - Fills all surrounding pixels of a selected pixel with the new color.


class Pixel:
    """
    Class that represents an individual pixel on a screen.
    """

    def __init__(self, color, pos):
        self.color = color 

        # Position on the screen
        self.pos = pos

        # Adjacent pixels:
        self.right = None
        self.top_right = None
        self.top = None
        self.top_left = None
        self.left = None
        self.bottom_left = None
        self.bottom = None
        self.bottom_right = None

        # Create a list of potential options for all pixels
        self.possible_options = self._check_possible_options()
        self.opposites = {}


    def _check_possible_options(self):
        possible_options = []
        check_options = [
            self.right, 
            self.top_right, 
            self.top, 
            self.top_left, 
            self.left, 
            self.bottom_left, 
            self.bottom, 
            self.bottom_right, 
        ]
        for option in check_options:
            if option !=None:
                possible_options.append(option)

        return possible_options


class Screen:
    """
    2 dimensional representation of a screen using an array (list) of arrays (lists)
    """
    
    def __init__(self):
        self.position_dict = {}
        self.screen = self._create_screen()

    
    def _create_grid(self):
        N = 10
        grid = []
        for y in range(N):
            row = []
            y = y * N
            for x in range(N):
                pos = y + x
                pixel = Pixel('White', pos)
                row.append(pixel)
            grid.append(row)

        return grid

    def _create_screen(self):
        """
        Creates a standard Othello board.
        """
        grid = self._create_grid()
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                pixel = grid[y][x]
                
                if y == 0:
                    pixel.bottom = grid[y + 1][x]
                    if x == 0:
                        pixel.bottom_right = grid[y + 1][x + 1]
                        pixel.right = grid[y][x + 1]
                    elif x == len(grid[0]) - 1:
                        pixel.bottom_left = grid[y + 1][x - 1]
                        pixel.left = grid[y][x - 1]
                    else:
                        pixel.right = grid[y][x + 1]
                        pixel.bottom_right = grid[y + 1][x + 1]
                        pixel.bottom_left = grid[y + 1][x - 1]
                        pixel.left = grid[y][x - 1]
                
                elif y == len(grid) -1:
                    pixel.top = grid[y - 1][x]
                    if x == 0:
                        pixel.top_right = grid[y - 1][x + 1]
                        pixel.right = grid[y][x + 1]
                    elif x == len(grid[0]) - 1:
                        pixel.top_left = grid[y - 1][x - 1]
                        pixel.left = grid[y][x - 1]
                    else:
                        pixel.right = grid[y][x + 1]
                        pixel.top_right = grid[y - 1][x + 1]
                        pixel.top_left = grid[y - 1][x - 1]
                        pixel.left = grid[y][x - 1]
                
                elif x == 0:
                    pixel.right = grid[y][x + 1]
                    pixel.top_right = grid[y - 1][x + 1]
                    pixel.top = grid[y - 1][x]
                    pixel.bottom = grid[y + 1][x]
                    pixel.bottom_right = grid[y + 1][x + 1]

                elif x == len(grid[0]) - 1:
                    pixel.left = grid[y][x - 1]
                    pixel.bottom_left = grid[y + 1][x - 1]
                    pixel.bottom = grid[y + 1][x]
                    pixel.top = grid[y - 1][x]
                    pixel.top_left = grid[y - 1][x - 1]

                else:
                    pixel.right = grid[y][x + 1]
                    pixel.top_right = grid[y - 1][x + 1]
                    pixel.top = grid[y - 1][x]
                    pixel.top_left = grid[y - 1][x - 1]
                    pixel.left = grid[y][x - 1]
                    pixel.bottom_left = grid[y + 1][x - 1]
                    pixel.bottom = grid[y + 1][x]
                    pixel.bottom_right = grid[y + 1][x + 1]
                
                pixel.possible_options = pixel._check_possible_options()
                self.position_dict[pixel.pos] = pixel

        return grid

    def fill_in_paint(self, pixel, new_color):

        old_color = pixel.color
        pixel.color = new_color

        for option in pixel.possible_options:
            if option.color == old_color:
                self.fill_in_paint(option, new_color)

    def paint_fill(self, pixel_position, new_color):
        """
        Fills all surrounding pixels of a selected pixel with the new color.
        """
        pixel = self.position_dict[pixel_position]

        self.fill_in_paint(pixel, new_color)

    def paint_single_pixel(self, pixel_position, new_color):

        pixel = self.position_dict[pixel_position]
        pixel.color = new_color

        return pixel.color
        

    def print_screen(self):
        """
        Prints the current state of the screen
        """
        screen = self.screen

        for y in range(len(screen)):
            for x in range(len(screen[0])):
                pixel = screen[y][x]

                print(f" {pixel.color} ", end='')
            print()
        print("\n")


def example():

    screen = Screen()
    screen.print_screen()

    for pos in range(0, 20):
        screen.paint_single_pixel(pos, 'Blue')
    screen.print_screen()
    
    for pos in range(80, 100):
        screen.paint_single_pixel(pos, 'Yellow')

    for pos in range(40, 52):
        screen.paint_single_pixel(pos, 'Black')

    screen.print_screen()
    screen.paint_fill(52, 'Red')
    screen.print_screen()
                 

if __name__ == "__main__":
    example()