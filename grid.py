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

class Grid:
    def __init__(self, rows: int, columns: int) -> None:
        self.__rows = rows
        self.__columns = columns
        self.__grid = [[0 for _ in range(columns)] for _ in range(rows)]
    
    def print(self) -> None:
        """
        Prints the grid in the terminal
        """
        pass
    
    def set(self, row: int, column: int, state: int) -> None:
        """
        Changes the state of the cell at position (row, column) in the matrix self.__grid to either 0 (dead) or 1 (alive)

        :param int row: row of the cell
        :param int column: column of the cell
        :param int state: state of the cell
        """
        try:
            if not isinstance(state, int):
                raise(TypeError(f"The 'state' parameter must be int, but {type(state).__name__} was given"))
            elif state != 0 and state != 1:
                raise(ValueError(f"The 'state' parameter must be either 0 or 1, but {state} was given"))
            else:
                self.__grid[row][column] = state
        except TypeError:
            int_row = isinstance(row, int)
            int_column = isinstance(column, int)

            if not int_row and not int_column:
                raise(TypeError(f"The 'row' and 'column' parameters must be both int, but {type(row).__name__} (row)" \
                                f" and {type(column).__name__} (column) were given"))
            elif not int_row:
                raise(TypeError(f"The 'row' parameter must be int, but {type(row).__name__} was given"))
            else:
                raise(TypeError(f"The 'column' parameter must be int, but {type(column).__name__} was given"))
    
    def alive_neighbours(self, i: int, j: int) -> int:
        """
        Returns the number of alive neighbours for the cell at position (i,j) in the grid

        :param int i: row of the cell
        :param int j: column of the cell
        :return int: number of alive neighbours
        """
        try:
            self.__grid[i][j]
        except TypeError:
            raise(TypeError("The parameters i and j must be int"))
        else:
            res = 0
            for k in range(-1,2):
                for l in range(-1,2):
                    if 0 <= i + k < self.__rows and 0 <= j + l < self.__columns and (k,l) != (0,0):
                        res += self.__grid[i+k][j+l]
            return res
    
    def apply_rules(self, i: int, j: int, alive_neighbours: int) -> None:
        """
        Modifies a cell according to the rules

        :param int i: row of the cell
        :param int j: column of the cell
        :param int alive_neighbours: number of alive cells in the neighbourhood of the cell
        """
        pass
    
    def new_generation(self):
        """
        New iteration of the rules on the current grid
        """
        pass