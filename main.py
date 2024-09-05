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
from game import Game

parser = argparse.ArgumentParser()
parser.add_argument("--rows", help="number of rows in the grid", type=int, default=20)
parser.add_argument("--columns", help="number of columns in the grid", type=int, default=20)
parser.add_argument("--zqsd", help="use the zqsd keys to move in the grid", action="store_true")

args = parser.parse_args()

game = Game(args)

game.license()
game.commands()

choice = input("Press '<Enter>' to start ")

if choice == "show w":
    pass
elif choice == "show c":
    pass

game.config()
game.start()