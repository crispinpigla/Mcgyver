

"""  Sortie du labyrinthe  """




class Sortie:

    """  Sortie du labyrinthe  """

    def __init__(self, plateau):

        self._position = plateau.arrive

    @property
    def position(self):
    	return self._position
    