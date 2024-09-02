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

class Cell:
    def __init__(self, i: int, j: int, alive: bool, selected: bool = False):
        """
        Représente une cellule dans la grille

        :param int i: ligne de la cellule
        :param int j: colonne de la cellule
        :param bool alive: indique si la cellule est vivante ou non
        :param bool selected: indique si la case est sélectionnée (pour l'initialisation du jeu), defaults to False
        """
        self.i = i
        self.j = j
        self.alive = alive
        self.selected = selected

    def neighbours(self, m: int, n: int):
        """Retourne les coordonnées des cellules voisines

        :param int m: hauteur de la grille
        :param int n: longueur de la grille
        :return list[tuple(int,int)]: coordonnées des cellules voisines
        """
        res = []
        for k in range(-1,2):
            for l in range(-1,2):
                if 0 <= self.i + k < m and 0 <= self.j + l < n and (k,l) != (0,0):
                    res.append((self.i+k, self.j+l))
        return res