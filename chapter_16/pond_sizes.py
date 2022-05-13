# python3
# pond_sizes.py - Calculates the number and size of ponds given a grid of elevations represented by integers.

from random import randint

class Tile:

    def __init__(self, x, y, pos, elevation):
        self.elevation = elevation
        self.checked = False

        # Position of tile on the map
        self.x = x
        self.y = y
        self.pos = pos

        # Adjacent tiles:
        self.right = None
        self.top_right = None
        self.top = None
        self.top_left = None
        self.left = None
        self.bottom_left = None
        self.bottom = None
        self.bottom_right = None

        # Create a list of potential options for all tiles
        self.possible_options = self._check_possible_options()


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


class Landscape:

    def __init__(self, N):
        self.N = N
        
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.position_dict = {}
        self.water_tiles = []
        self.map = self._create_landscape(N)

    def _create_grid(self, N):
        grid = []
        letters = self.letters
        for y in range(N):
            row = []
            for x in range(N):
                # Create
                tile_type = randint(0, 3)
                if tile_type == 0:
                    # Sea level (lakes, ponds, and rivers)
                    elev = 0
                elif tile_type > 0 and tile_type < 3:
                    # Regular land (hills and other features)
                    elev = randint(1, 4)
                else:
                    # Mountain tiles
                    elev = randint(5, 7)
                pos = f'{letters[y]}{x}'
                tile = Tile(x, y, pos, elev)
                # Append the water tile into this list for quicker reference:
                if tile.elevation == 0:
                    self.water_tiles.append(tile)
                row.append(tile)
            grid.append(row)

        return grid

    def _create_landscape(self, N):
        """
        Creates the landscape map within the grid.
        """
        grid = self._create_grid(N)

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                tile = grid[y][x]
                
                if y == 0:
                    tile.bottom = grid[y + 1][x]
                    if x == 0:
                        tile.bottom_right = grid[y + 1][x + 1]
                        tile.right = grid[y][x + 1]
                    elif x == len(grid[0]) - 1:
                        tile.bottom_left = grid[y + 1][x - 1]
                        tile.left = grid[y][x - 1]
                    else:
                        tile.right = grid[y][x + 1]
                        tile.bottom_right = grid[y + 1][x + 1]
                        tile.bottom_left = grid[y + 1][x - 1]
                        tile.left = grid[y][x - 1]
                
                elif y == len(grid) -1:
                    tile.top = grid[y - 1][x]
                    if x == 0:
                        tile.top_right = grid[y - 1][x + 1]
                        tile.right = grid[y][x + 1]
                    elif x == len(grid[0]) - 1:
                        tile.top_left = grid[y - 1][x - 1]
                        tile.left = grid[y][x - 1]
                    else:
                        tile.right = grid[y][x + 1]
                        tile.top_right = grid[y - 1][x + 1]
                        tile.top_left = grid[y - 1][x - 1]
                        tile.left = grid[y][x - 1]
                
                elif x == 0:
                    tile.right = grid[y][x + 1]
                    tile.top_right = grid[y - 1][x + 1]
                    tile.top = grid[y - 1][x]
                    tile.bottom = grid[y + 1][x]
                    tile.bottom_right = grid[y + 1][x + 1]

                elif x == len(grid[0]) - 1:
                    tile.left = grid[y][x - 1]
                    tile.bottom_left = grid[y + 1][x - 1]
                    tile.bottom = grid[y + 1][x]
                    tile.top = grid[y - 1][x]
                    tile.top_left = grid[y - 1][x - 1]

                else:

                    tile.right = grid[y][x + 1]
                    tile.top_right = grid[y - 1][x + 1]
                    tile.top = grid[y - 1][x]
                    tile.top_left = grid[y - 1][x - 1]
                    tile.left = grid[y][x - 1]
                    tile.bottom_left = grid[y + 1][x - 1]
                    tile.bottom = grid[y + 1][x]
                    tile.bottom_right = grid[y + 1][x + 1]
                
                tile.possible_options = tile._check_possible_options()
                self.position_dict[tile.pos] = tile

        return grid

    def print_map(self):
        """
        Prints the current state of the map
        """
        map = self.map
        letters = self.letters
        space = '  '
        numbers_on_top = f' {space}'
        for x in range(len(map[0])):
            numbers_on_top += f"{space}{letters[x]} "
        horizontal_line_segment = '____'
        horizontal_line = horizontal_line_segment * self.N
        print()
        print(numbers_on_top)
        print(f"{space} {horizontal_line}")
        for y in range(len(map)):
            for x in range(len(map[0])):
                tile = map[x][y]
                if x == 0:
                    if y < 10:
                        print(f"{y}  | {tile.elevation} |",end='')
                    else:
                        print(f"{y} | {tile.elevation} |",end='')
                else:
                    print(f" {tile.elevation} |", end='')
            print(f'\n   {horizontal_line}')


    def search_adj_tiles(self, tile, pond_size):
        """
        Searches adjacent tiles to see if those tiles are water tiles
        """
        pond_size += 1
        tile.checked = True
        for adj_tile in tile.possible_options:
            if adj_tile != None:
                if adj_tile.checked != True and adj_tile.elevation == 0:
                    pond_size = self.search_adj_tiles(adj_tile, pond_size)

        return pond_size

    def calc_ponds(self):
        """
        Calculates all the ponds (adjacent water tiles) on the map
        And the size of those ponds
        """
        all_ponds = {}
        pond_size = 0
        # Go through all the water tiles on the map
        for water_tile in self.water_tiles:
            if water_tile.checked != True:
                pond_size += 1
                water_tile.checked = True
                starting_tile = water_tile
                # Go through all the adjacent tiles to see if the 
                # pond is bigger than one tile.
                for adj_tile in water_tile.possible_options:
                    if adj_tile != None:
                        if adj_tile.checked != True and adj_tile.elevation == 0:
                            pond_size = self.search_adj_tiles(adj_tile, pond_size)

                all_ponds[starting_tile.pos] = pond_size
            pond_size = 0

        return all_ponds



def example():

    world_map = Landscape(8)
    world_map.print_map()
    ponds = world_map.calc_ponds()
    for starting_tile, pond_size in ponds.items():
        print(f"Starting tile: {starting_tile}, Pond size: {pond_size}")


if __name__ == "__main__":
    example()
