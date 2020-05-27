

"""  La classe de la sortie du labyrinthe est créee dans ce fichier """


class Sortie:
    """  Cette classe est la classe de la sortie du labyrinthe gardée par le gardien,
    et que le heros doit rejoindre une fois qu'il a ramassé tous les objets
    """

    def __init__(self, plateau):

        self._position = plateau.arrive

    @property
    def position(self):
        return self._position
