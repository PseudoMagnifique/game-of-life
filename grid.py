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
        self.__loaded = set()
    
    def display(self) -> None:
        """
        Prints the grid in the terminal
        """
        res = "\n".join([" ".join(["x" if cell else "." for cell in row]) for row in self.__grid])
        print(res)
    
    def set(self, row: int, column: int, state: int) -> None:
        """
        Changes the state of the cell at position (row, column) in the matrix self.__grid to either 0 (dead) or 1 (alive)
        and updates the self.__loaded set

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
                if state:  # loads the cell on its neighbours
                    self.load(row, column)
                else:  # unload the cell and its neighbours
                    self.unload(row, column)
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
    
    def load(self, i: int, j: int) -> None:
        """
        Updates the self.__loaded set: the (i,j) cell and its neighbours are loaded

        :param int i: row of the cell
        :param int j: column of the cell
        """
        self.__loaded.add((i,j))
        self.__loaded.update(self.neighbours(i,j))
    
    def unload(self, i: int, j: int) -> None:
        """
        Updates the self.__loaded set: the (i,j) cell and its neighbours are unloaded

        :param int i: row of the cell
        :param int j: column of the cell
        """
        self.__loaded.discard((i,j))
        self.__loaded = self.__loaded - set(self.neighbours(i,j))

    def neighbours(self, i: int, j: int) -> list[tuple[int,int]]:
        """
        Returns the list of the neighbours coordinates for the cell at position (i,j) in the grid

        :param int i: row of the cell
        :param int j: column of the cell
        :return list[tuple[int,int]]: list of the neighbours coordinates
        """
        try:
            self.__grid[i][j]
        except TypeError:
            raise(TypeError("The parameters i and j must be int"))
        else:
            res = []
            for k in range(-1,2):
                for l in range(-1,2):
                    if 0 <= i + k < self.__rows and 0 <= j + l < self.__columns and (k,l) != (0,0):
                        res.append((i+k,j+l))
            return res
    
    def alive_neighbours(self, i: int, j: int) -> int:
        """
        Returns the number of alive neighbours coordinates for the cell at position (i,j) in the grid

        :param int i: row of the cell
        :param int j: column of the cell
        :return int: number of alive neighbours coordinates
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
    
    def apply_rules(self, i: int, j: int, alive_neighbours: int) -> int:
        """
        Outputs the next state of a cell according to the rules

        :param int i: row of the cell
        :param int j: column of the cell
        :param int alive_neighbours: number of alive cells in the neighbourhood of the cell
        :return int: next state of the cell
        """
        if alive_neighbours == 2:
            return self.__grid[i][j]
        elif alive_neighbours == 3:
            return 1
        else:
            return 0
    
    def new_generation(self) -> None:
        """
        New iteration of the rules on the current grid
        """
        next_generation = {}
        for cell in self.__loaded:
            next_generation[cell] = self.apply_rules(*cell, self.alive_neighbours(*cell))
        for cell in next_generation:
            self.set(*cell, next_generation[cell])