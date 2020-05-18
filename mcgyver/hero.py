""" Classe de Mcgyver """












class Hero:

    """ Classe de McGyver """

    def __init__(self, plateau):

        self._position = plateau.depart
        self._objet_ramasse = []
        self._routes = plateau.routes


    def pas_mcgyver(self, direction, liste_objets_aramass, gardien):

        """ Definit la position de Mcgyver apres un pas """

        if direction == 'j':
            if (self._position[0] - 1, self._position[1]) in self._routes:
                self._position = (self._position[0] - 1, self._position[1])
                for obj in liste_objets_aramass:
                    if self.position == obj.position:
                        self.objet_ramasse.append(obj.nom_objet)
                        obj.ramassage()
        elif direction == 'l':
            if (self._position[0] + 1, self._position[1]) in self._routes:
                self._position = (self._position[0] + 1, self._position[1])
                for obj in liste_objets_aramass:
                    if self.position == obj.position:
                        self.objet_ramasse.append(obj.nom_objet)
                        obj.ramassage()
        elif direction == 'k':
            if (self._position[0], self._position[1] + 1) in self._routes:
                self._position = (self._position[0], self._position[1] + 1)
                for obj in liste_objets_aramass:
                    if self.position == obj.position:
                        self.objet_ramasse.append(obj.nom_objet)
                        obj.ramassage()
        elif direction == 'i':
            if (self._position[0], self._position[1] - 1) in self._routes:
                self._position = (self._position[0], self._position[1] - 1)
                for obj in liste_objets_aramass:
                    if self.position == obj.position:
                        self.objet_ramasse.append(obj.nom_objet)
                        obj.ramassage()
        else:
            self._position = (self._position[0], self._position[1])


    # getters
    @property
    def position(self):
        return self._position

    @property
    def objet_ramasse(self):
        return self._objet_ramasse
    

    # setters
    @position.setter
    def position(self,valeur):
        self._position = valeur

    @objet_ramasse.setter
    def objet_ramasse(self,valeur):
        self._objet_ramasse = valeur
    
