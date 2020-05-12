""" Classe de Mcgyver """












class Hero:

    """ Classe de McGyver """

    def __init__(self):

        self.new_pos = None

        self.position = (-1, -1)

        self.objet_ramasse = []



	# retourne la position de Mcgyver après un pas suivant une commande

    def pas_mcgyver(self, direction):

        """ Definit la position de Mcgyver apres un pas """

        if direction == 'j':

            self.new_pos = (self.position[0] - 1, self.position[1])

        elif direction == 'l':

            self.new_pos = (self.position[0] + 1, self.position[1])

        elif direction == 'k':

            self.new_pos = (self.position[0], self.position[1] + 1)

        elif direction == 'i':

            self.new_pos = (self.position[0], self.position[1] - 1)

        else:

            self.new_pos = (self.position[0], self.position[1])


        return self.new_pos
