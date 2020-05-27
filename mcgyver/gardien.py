""" La classe du gardien est crée dans ce fichier """


class Gardien:
    """  Cette classe est celle du gardien de la sortie du labyrinthe  """

    def __init__(self, plateau):
        self._position = plateau.arrive

    # le getter

    @property
    def position(self):
        return self._position
