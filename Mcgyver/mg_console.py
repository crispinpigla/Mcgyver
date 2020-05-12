""" Affiche le jeux en mode console """




def draw_console(hero, liste_objets, sortie, mur):

    """ Affiche le jeux en mode console """

    liste_positions_objets = []

    for i_0 in liste_objets:

        liste_positions_objets.append(i_0.position)


    screen = ''

    for i_0 in range(15):

        for i_1 in range(15):


            if hero == (i_1, i_0):

                screen += ' M '

            elif (i_1, i_0) in liste_positions_objets:


                if liste_objets[liste_positions_objets.index((i_1, i_0))].nom_objet == 'aiguille':

                    screen += ' I '

                elif liste_objets[liste_positions_objets.index((i_1, i_0))].nom_objet == 'tube_plastiqe':

                    screen += ' T '

                elif liste_objets[liste_positions_objets.index((i_1, i_0))].nom_objet == 'ether':

                    screen += ' E '


            elif sortie == (i_1, i_0):

                screen += ' S '

            elif (i_1, i_0) in mur:

                screen += ' X '

            else:

                screen += '   '


        screen += '\n'



    print(screen)


















def jeu_console(mg0, aiguille0, tube_plastiqe0, ether0, sortie0, plateau0):

    """ Gère les mouvements de Mcgyver en mode console """


    while mg0.position != sortie0.position:


        draw_console(mg0.position, [aiguille0, tube_plastiqe0, ether0], sortie0.position, plateau0.mur)


        direction_input = input("Déplacer McGyver !! \n\n j : vers la gauche\n l : vers la droite\n k : vers le bas\n i : vers le haut\n\n ")

        if (mg0.pas_mcgyver(direction_input) not in plateau0.mur) and (mg0.pas_mcgyver(direction_input) in plateau0.plateauvide):

            mg0.position = mg0.pas_mcgyver(direction_input)

            if mg0.position == aiguille0.position:

                mg0.objet_ramasse.append(aiguille0.nom_objet)

                aiguille0.ramassage()

            elif mg0.position == tube_plastiqe0.position:

                mg0.objet_ramasse.append(tube_plastiqe0.nom_objet)

                tube_plastiqe0.ramassage()

            elif mg0.position == ether0.position:

                mg0.objet_ramasse.append(ether0.nom_objet)

                ether0.ramassage()


    draw_console(mg0.position, [aiguille0, tube_plastiqe0, ether0], sortie0.position, plateau0.mur)

    if len(mg0.objet_ramasse) == 3:

        print('\n\n Gagné ')

    else:

        print('\n\n Perdu ')
