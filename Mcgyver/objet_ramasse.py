""" Classe des objets à ramasser """








class ObjetRamasse:

    """ Classe des objets à ramasser """

    def __init__(self, nom_de_lobjet):

        self.position = None

        self.nom_objet = nom_de_lobjet



    def ramassage(self):

        """ Enlève l'objet ramassé du plateau """

        self.position = (-1, -1)
	