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
import time
from grid import Grid

class Game:
    def __init__(self, args: argparse.Namespace) -> None:
        self.__args = args
        self.__rows = self.__args.rows
        self.__columns = self.__args.columns
        self.__grid = Grid(self.__rows, self.__columns)
        self.__moves = {"up": (-1,0), "left": (0,-1), "down": (1,0), "right": (0,1)}

        if self.__args.zqsd:
            self.__keys = "zqsd"
            self.__key_to_move = {"z": "up", "q": "left", "s": "down", "d": "right"}
        else:
            self.__keys = "wasd"
            self.__key_to_move = {"w": "up", "a": "left", "s": "down", "d": "right"}
    
    def license(self) -> None:
        """
        Prints the license in the terminal
        """
        print("Game of life Python implementation Copyright (C) 2024  pseudomagnifique")
        print("This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.")
        print("This is free software, and you are welcome to redistribute it")
        print("under certain conditions; type `show c' for details.")
        print()
    
    def commands(self) -> None:
        """
        Prints the commands in the terminal
        """
        print("Commands:")
        items = self.__key_to_move.items()
        for item in items:
            print(f"- Press '{item[0]}' for going {item[1]}")
        print("- Press 'x' to modify the state of the cell (alive: 1, dead: 0)")
        print("- Press '<Enter>' to start the game")
        print()
    
    def config(self):
        """
        Lets the user choose the initial configuration
        """
        start = False
        pos_i = 0
        pos_j = 0

        self.__grid.select(pos_i, pos_j)

        while not start:
            key = input(f"Move ({self.__keys}): ")

            if key not in self.__keys:  # the key is neither a move key or enter
                if key == "x":  # changes the state of the selected cell
                    self.__grid.set(pos_i, pos_j, int(not self.__grid[pos_i][pos_j]))
                    self.__grid.select(pos_i, pos_j)
                else:  # the key is not valid
                    self.__grid.select(pos_i, pos_j)
                    print(f"Invalid key, please choose between '{self.__keys}' for movement, 'x' for state change or '<Enter>' for starting the game")
            else:  # the key is either a move key or enter
                if key == "":  # the key is enter, starts the game
                    start = True
                else:  # the key is a move key
                    move = self.__moves[self.__key_to_move[key]]
                    if 0<= pos_i + move[0] < self.__rows and 0 <= pos_j + move[1] < self.__columns:
                        pos_i += move[0]
                        pos_j += move[1]
                    self.__grid.select(pos_i, pos_j)
    
    def start(self) -> None:
        next = True
        print(self.__grid, end="\n\n\n")

        while next:
            self.__grid.new_generation()
            print(self.__grid, end="\n\n\n")
            time.sleep(0.5)