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

import argparse
from grid import Grid

parser = argparse.ArgumentParser()
parser.add_argument("--rows", help="number of rows in the grid", type=int, default=20)
parser.add_argument("--columns", help="number of columns in the grid", type=int, default=20)

args = parser.parse_args()

grid = Grid(args.rows,args.columns)

# print LICENSE
# allow the user to configure initial configuration
# GAME
# new_generation:
#   apply the rules to every cell of the grid
#   modifies a copy of the grid
#   the copy becomes the grid

# to make the "apply the rules" part faster, "unload" useless cells