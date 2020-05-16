""" Module du plateau """










class Plateau:

    """ Classe du plateau du jeu """

    def __init__(self):

        self._plateauvide = []
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

        with open("Mcgyver/structure.txt") as lignes:

            ligne0 = []

            for y, ligne in enumerate(lignes):
                for x, char in enumerate(ligne):
                    self.plateauvide.append((x, y))
                    ligne0.append((x, y))
                    if char == ".":
                        self.routes.append((x, y))

                    elif char == "D":
                        self.depart.append((x, y))

                    elif char == "A":
                        self.arrive.append((x, y))

                    else:
                        self.murs.append((x, y))
                self.for_affichage.append(ligne0)
                ligne0 = []

        if len( self.depart ) == 1  :
            self.depart = self.depart[0]
        else:
            raise ValueError("Le tableau doit posseder un départ ")

        if len( self.arrive ) == 1  :
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
                champs_libres0.remove(i_1)
            i_0 += 1

        # Suppression des répétitions dans les champs accessibles par Mcgiver
        champs_accessibles = []
        while len(movables) != 0:
            champs_accessibles.append(movables[0])
            for i_2 in range(movables.count(champs_accessibles[-1])):
                movables.remove(champs_accessibles[-1])
        champs_accessibles.remove(self.depart)

        self.accessible = champs_accessibles

        #  Cas : pas assez d'espace dans le plateau pour insérer 3 objets distinct accessibles par Mcgyver
        if len(self.accessible) < 3:
            raise ValueError("Ce tableau ne permet pas de placer 3 objets accessible par McGyver !!")
        #  Cas : La sortie n'est pas accessible par Mcgyver
        elif len(self.move_posible( self.arrive, self.accessible)) == 0:
            raise ValueError("Arrivée inaccessible par Mcgyver")
        #  Cas : assez d'espace dans le plateau pour insérer 3 objets distinct accessibles par Mcgyver et sortie accessible
        else:
            self._place_potenti_objet_ramass = self.accessible


    def move_posible(self, point, champs_libres):

        """Renvoie liste des points dans lesquels point peut se déplacer étant donné un champs libre"""

        mov_posible = []

        #   Les coins
        if point in [(0, 0), (0, 15 - 1), (15 - 1, 0), (15 - 1, 15 - 1)]:

            #  coin bas gauche
            if point == (0, 0):
                if (1, 0) in champs_libres:
                    mov_posible.append((1, 0))
                if (0, 1) in champs_libres:
                    mov_posible.append((0, 1))

            # coin haut gauche
            elif point == (0, 15 - 1):
                if (0, (15 - 1) - 1) in champs_libres:
                    mov_posible.append((0, (15 - 1) - 1))
                if (1, 15 - 1) in champs_libres:
                    mov_posible.append((1, 15 - 1))

            # coin bas droit
            elif point == (15 - 1, 0):
                if ((15 - 1) - 1, 0) in champs_libres:
                    mov_posible.append(((15 - 1) - 1, 0))
                if (15 - 1, 1) in champs_libres:
                    mov_posible.append((15 - 1, 1))

            # coin haut droit
            elif point == (15 - 1, 15 - 1):
                if ((15 - 1) - 1, 15 - 1) in champs_libres:
                    mov_posible.append(((15 - 1) - 1, 15 - 1))
                if (15 - 1, (15 - 1) - 1) in champs_libres:
                    mov_posible.append((15 - 1, (15 - 1) - 1))

        # Les extrémités
        elif (point[0] == 0) or (point[0] == 15 - 1) or (point[1] == 0) or (point[1] == 15 - 1):

            #extrémités gauches
            if  point[0] == 0:
                if (0, point[1] + 1) in champs_libres:
                    mov_posible.append((0, point[1] + 1))
                if (1, point[1]) in champs_libres:
                    mov_posible.append((1, point[1]))
                if (0, point[1] - 1) in champs_libres:
                    mov_posible.append((0, point[1] - 1))

            #extrémités droits
            elif point[0] == 15 - 1:
                if (point[0] - 1, point[1]) in champs_libres:
                    mov_posible.append((point[0] - 1, point[1]))
                if (point[0], point[1] - 1) in champs_libres:
                    mov_posible.append((point[0], point[1] - 1))
                if (point[0], point[1] + 1) in champs_libres:
                    mov_posible.append((point[0], point[1] + 1))

            #extrémités bas
            elif point[1] == 0:
                if (point[0] - 1, point[1]) in champs_libres:
                    mov_posible.append((point[0] - 1, point[1]))
                if (point[0] + 1, point[1]) in champs_libres:
                    mov_posible.append((point[0] + 1, point[1]))
                if (point[0], point[1] + 1) in champs_libres:
                    mov_posible.append((point[0], point[1] + 1))

            #extrémités hauts
            elif point[1] == 15 - 1:
                if (point[0] - 1, point[1]) in champs_libres:
                    mov_posible.append((point[0] - 1, point[1]))
                if (point[0] + 1, point[1]) in champs_libres:
                    mov_posible.append((point[0] + 1, point[1]))
                if (point[0], point[1] - 1) in champs_libres:
                    mov_posible.append((point[0], point[1] - 1))


        # le reste
        else:
            if (point[0] - 1, point[1]) in champs_libres:
                mov_posible.append((point[0] - 1, point[1]))
            if (point[0] + 1, point[1]) in champs_libres:
                mov_posible.append((point[0] + 1, point[1]))
            if (point[0], point[1] - 1) in champs_libres:
                mov_posible.append((point[0], point[1] - 1))
            if (point[0], point[1] + 1) in champs_libres:
                mov_posible.append((point[0], point[1] + 1))

        return mov_posible




    # Les getters

    @property
    def plateauvide( self ):
        return self._plateauvide

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

    @plateauvide.setter
    def plateauvide(self, valeur ):
        self._plateauvide = valeur

    @routes.setter
    def routes(self, valeur ):
        self._routes = valeur

    @murs.setter
    def murs(self, valeur ):
        self._murs = valeur

    @depart.setter
    def depart(self, valeur ):
        self._depart = valeur

    @arrive.setter
    def arrive(self, valeur ):
        self._arrive = valeur

    @accessible.setter
    def accessible(self, valeur):
        self._accessible = valeur

    @place_potenti_objet_ramass.setter
    def place_potenti_objet_ramass(self, valeur):
        self._place_potenti_objet_ramass = valeur

    @for_affichage.setter
    def for_affichage(self, valeur):
        self._for_affichage = valeur