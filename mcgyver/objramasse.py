""" La classe des objets à ramasser est créee dans ce fichier """

import random


class ObjetRamasse:
    """ Cette classe est celle des objets que le heros doit ramasser pour endormir le gardien """

    def __init__(self, plateau, nom_de_lobjet):

        random.shuffle(plateau.place_potenti_objet_ramass)
        self._position = plateau.place_potenti_objet_ramass[-1]
        plateau.place_potenti_objet_ramass.pop()
        self._nom_objet = nom_de_lobjet

    def ramassage(self):
        """ Enlève l'objet ramassé du plateau """

        self._position = (-1, -1)

    # setters

    @property
    def position(self):
        return self._position

    @property
    def nom_objet(self):
        return self._nom_objet

    # getters

    @position.setter
    def position(self, valeur):
        self._position = valeur

    @nom_objet.setter
    def nom_objet(self, valeur):
        self._nom_objet = valeur
