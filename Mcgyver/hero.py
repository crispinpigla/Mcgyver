""" Classe de Mcgyver """












class Hero:

    """ Classe de McGyver """

    def __init__(self, plateau):

        self.position = plateau.depart
        self.objet_ramasse = []



    def pas_mcgyver(self, direction):

        """ Definit la position de Mcgyver apres un pas """

        new_pos = None

        if direction == 'j':
            new_pos = (self.position[0] - 1, self.position[1])
        elif direction == 'l':
            new_pos = (self.position[0] + 1, self.position[1])
        elif direction == 'k':
            new_pos = (self.position[0], self.position[1] + 1)
        elif direction == 'i':
            new_pos = (self.position[0], self.position[1] - 1)
        else:
            new_pos = (self.position[0], self.position[1])

        return new_pos
