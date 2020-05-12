""" Module du plateau """










class Plateau:

    """ Classe du plateau du jeu """

    def __init__(self, taille_plateau):

        self.plateauvide = []

        for i_0 in range(taille_plateau):

            for i_1 in range(taille_plateau):

                self.plateauvide.append((i_1, i_0))


        self.mur = []


"""Renvoie la liste des champs libres du plateau etant donné une liste de mur"""

def mur_to_champs_libres(mur, position_sortie):

    champs_libres = []

    for i_0 in range(15):

        for i_1 in range(15):

            if ((i_1, i_0) not in mur) and (i_1, i_0) != position_sortie:

                champs_libres.append((i_1, i_0))

    return champs_libres











"""Renvoie liste des points dans lesquels point peut se déplacer étant donné un champs libre"""

def move_posible(point, champs_libres):

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
