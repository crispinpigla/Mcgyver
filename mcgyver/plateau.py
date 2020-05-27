""" Module du plateau """


import config


class Plateau:
    """ Cette classe est celle du plateau qui contient tous les éléments du jeu heros,
    murs, sortie et gardien
    """

    def __init__(self):

        self._routes = []
        self._murs = []

        self._depart = []
        self._arrive = []
        self._for_affichage = []
        self._accessible = []
        self._place_potenti_objet_ramass = []

        self.charger_structure()
        self.set_accessible()

    def charger_structure(self):
        """ Charge la structure """

        with open("mcgyver/structure.txt") as lignes:
            ligne0 = []
            for y, ligne in enumerate(lignes):
                for x, char in enumerate(ligne):
                    ligne0.append((x, y))
                    if char == ".":
                        self.routes.append((x, y))
                    elif char == "D":
                        self.depart.append((x, y))
                        self.routes.append((x, y))
                    elif char == "A":
                        self.arrive.append((x, y))
                        self.routes.append((x, y))
                    else:
                        self.murs.append((x, y))
                self.for_affichage.append(ligne0)
                ligne0 = []
        if len(self.depart) == 1:
            self.depart = self.depart[0]
        else:
            raise ValueError("Le tableau doit posseder un départ ")
        if len(self.arrive) == 1:
            self.arrive = self.arrive[0]
        else:
            raise ValueError("Le tableau doit posseder une arrivée ")

    def set_accessible(self):
        """ Définit les champs accessibles """

        # Remplissage des champs accessibles par Mcgiver
        champs_libres0 = list(self.routes)
        movables = [self.depart]
        i_0 = 0
        while i_0 < len(movables):
            for i_1 in self.move_posible(movables[i_0], champs_libres0):
                movables.append(i_1)
                if i_1 in champs_libres0:
                    champs_libres0.remove(i_1)
            i_0 += 1

        # Suppression des répétitions dans les champs accessibles par Mcgiver
        champs_accessibles = []
        while len(movables) != 0:
            champs_accessibles.append(movables[0])
            for i_2 in range(movables.count(champs_accessibles[-1])):
                movables.remove(champs_accessibles[-1])
        champs_accessibles.remove(self.depart)
        champs_accessibles.remove(self.arrive)
        if self.depart in champs_accessibles:
            champs_accessibles.remove(self.depart)
        if self.arrive in champs_accessibles:
            champs_accessibles.remove(self.arrive)

        self.accessible = champs_accessibles

        #  Cas : pas assez d'espace dans le plateau pour insérer 3 objets distinct accessibles par Mcgyver
        if len(self.accessible) < 3:
            raise ValueError(
                "Ce tableau ne permet pas de placer 3 objets accessible par McGyver !!")
        #  Cas : La sortie n'est pas accessible par Mcgyver
        elif len(self.move_posible(self.arrive, self.accessible)) == 0:
            raise ValueError("Arrivée inaccessible par Mcgyver")
        #  Cas : assez d'espace dans le plateau pour insérer 3 objets distinct accessibles par Mcgyver et sortie accessible
        else:
            self._place_potenti_objet_ramass = self.accessible

    def check_move_posible(self, point, champs_libres, direction_check, mov_posible):
        """  Vérifie si un champs est accessible dans une direction  """

        #access = None
        if direction_check == 'left':
            if (point[0] - 1, point[1]) in champs_libres:
                mov_posible.append((point[0] - 1, point[1]))
        elif direction_check == 'right':
            if (point[0] + 1, point[1]) in champs_libres:
                mov_posible.append((point[0] + 1, point[1]))
        elif direction_check == 'up':
            if (point[0], point[1] + 1) in champs_libres:
                mov_posible.append((point[0], point[1] + 1))
        elif direction_check == 'down':
            if (point[0], point[1] - 1) in champs_libres:
                mov_posible.append((point[0], point[1] - 1))
        # return access

    def move_posible(self, point, champs_libres):
        """Renvoie liste des points dans lesquels point peut se déplacer étant donné un champs libre"""

        mov_posible = []

        #   Les coins
        if point in [(0, 0), (0, 15 - 1), (15 - 1, 0), (15 - 1, 15 - 1)]:
            #  coin bas gauche
            if point == (0, 0):
                self.check_move_posible(
                    point, champs_libres, 'right', mov_posible)
                self.check_move_posible(
                    point, champs_libres, 'up', mov_posible)
            # coin haut gauche
            elif point == (0, 15 - 1):
                self.check_move_posible(
                    point, champs_libres, 'down', mov_posible)
                self.check_move_posible(
                    point, champs_libres, 'right', mov_posible)
            # coin bas droit
            elif point == (15 - 1, 0):
                self.check_move_posible(
                    point, champs_libres, 'left', mov_posible)
                self.check_move_posible(
                    point, champs_libres, 'up', mov_posible)
            # coin haut droit
            elif point == (15 - 1, 15 - 1):
                self.check_move_posible(
                    point, champs_libres, 'left', mov_posible)
                self.check_move_posible(
                    point, champs_libres, 'down', mov_posible)
        # Les extrémités
        elif (point[0] == 0) or (point[0] == 15 - 1) or (point[1] == 0) or (point[1] == 15 - 1):
            # extrémités gauches
            if point[0] == 0:
                self.check_move_posible(
                    point, champs_libres, 'up', mov_posible)
                self.check_move_posible(
                    point, champs_libres, 'down', mov_posible)
                self.check_move_posible(
                    point, champs_libres, 'right', mov_posible)
            # extrémités droits
            elif point[0] == 15 - 1:
                self.check_move_posible(
                    point, champs_libres, 'up', mov_posible)
                self.check_move_posible(
                    point, champs_libres, 'down', mov_posible)
                self.check_move_posible(
                    point, champs_libres, 'left', mov_posible)
            # extrémités bas
            elif point[1] == 0:
                self.check_move_posible(
                    point, champs_libres, 'left', mov_posible)
                self.check_move_posible(
                    point, champs_libres, 'right', mov_posible)
                self.check_move_posible(
                    point, champs_libres, 'up', mov_posible)
            # extrémités hauts
            elif point[1] == 15 - 1:
                self.check_move_posible(
                    point, champs_libres, 'left', mov_posible)
                self.check_move_posible(
                    point, champs_libres, 'right', mov_posible)
                self.check_move_posible(
                    point, champs_libres, 'down', mov_posible)
        # le reste
        else:
            self.check_move_posible(point, champs_libres, 'left', mov_posible)
            self.check_move_posible(point, champs_libres, 'right', mov_posible)
            self.check_move_posible(point, champs_libres, 'up', mov_posible)
            self.check_move_posible(point, champs_libres, 'down', mov_posible)

        return mov_posible

    # Les getters

    @property
    def routes(self):
        return self._routes

    @property
    def murs(self):
        return self._murs

    @property
    def depart(self):
        return self._depart

    @property
    def arrive(self):
        return self._arrive

    @property
    def accessible(self):
        return self._accessible

    @property
    def place_potenti_objet_ramass(self):
        return self._place_potenti_objet_ramass

    @property
    def for_affichage(self):
        return self._for_affichage

    # Les setters

    @depart.setter
    def depart(self, valeur):
        self._depart = valeur

    @arrive.setter
    def arrive(self, valeur):
        self._arrive = valeur

    @accessible.setter
    def accessible(self, valeur):
        self._accessible = valeur
