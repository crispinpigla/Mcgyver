""" Classe des objets à ramasser """

import random






class ObjetRamasse:

    """ Classe des objets à ramasser """

    def __init__(self, plateau, nom_de_lobjet):

        random.shuffle(plateau.place_potenti_objet_ramass)

        self.position = plateau.place_potenti_objet_ramass[-1]
        plateau.place_potenti_objet_ramass.pop()

        self.nom_objet = nom_de_lobjet



    def ramassage(self):

        """ Enlève l'objet ramassé du plateau """

        self.position = (-1, -1)
	