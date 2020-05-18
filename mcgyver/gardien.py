""" Classe du gardien """








class Gardien:

    """  Classe du gardien  """

    def __init__(self, plateau):

        self._position = plateau.arrive


    # le getter
    @property
    def position(self):
    	return self._position

