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