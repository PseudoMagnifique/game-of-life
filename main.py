"""
    Game of life Python implementation
    Copyright (C) 2024  pseudomagnifique

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

LICENSE = """
Game of life Python implementation Copyright (C) 2024  pseudomagnifique
This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
This is free software, and you are welcome to redistribute it
under certain conditions; type `show c' for details.
"""

import argparse
import keyboard
from grid import Grid

parser = argparse.ArgumentParser()
parser.add_argument("--rows", help="number of rows in the grid", type=int, default=20)
parser.add_argument("--columns", help="number of columns in the grid", type=int, default=20)

args = parser.parse_args()

grid = Grid(args.rows,args.columns)

# allow the user to configure initial configuration

print("""
      Commands:
      - Choose a cell to modify with the arrow keys
      - Press 'x' to modify the state of the cell (alive: 1, dead: 0)
      - Press '<Enter>' to start the game
      """
)

start = False
pos_i = 0
pos_j = 0

while not start:
    key = keyboard.read_key()

    if key == "right" and pos_j + 1 < args.columns:
        pos_j += 1
    elif key == "left" and pos_j - 1 >= 0:
        pos_j -= 1
    elif key == "up" and pos_i - 1 >= 0:
        pos_i -= 1
    elif key == "down" and pos_i + 1 < args.columns:
        pos_i += 1
    elif key == "x":
        grid.set(pos_i, pos_j, int(not grid[pos_i][pos_j]))
    elif key == "enter":
        start = True
    
    if not start:
        grid.select(pos_i, pos_j)


# GAME