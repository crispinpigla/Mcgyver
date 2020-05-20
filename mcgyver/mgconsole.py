""" Affiche le jeux en mode console """





class ModeConsole:

    """Classe du mode console"""

    def __init__(self):
        
        pass
        

    def start(self, mg0, aiguille0, tube_plastiqe0, ether0, gardien0, sortie0, plateau0):

        """ Gère les mouvements de Mcgyver en mode console """

        while mg0.position != sortie0.position:
            self.draw_console(mg0.position, [aiguille0, tube_plastiqe0, ether0], sortie0.position, plateau0)
            direction_input = input("Déplacer McGyver !! \n\n j : vers la gauche\n l : vers la droite\n k : vers le bas\n i : vers le haut\n\n ")
            # Modification de la position de Mcgyver
            mg0.pas_mcgyver(direction_input, [aiguille0, tube_plastiqe0, ether0], gardien0)
        self.draw_console(mg0.position, [aiguille0, tube_plastiqe0, ether0], sortie0.position, plateau0)

        #Gestion de la fin du jeu
        if len(mg0.objet_ramasse) == 3:
            print('\n\n Gagné ')
        else:
            print('\n\n Perdu ')


    def draw_console(self, hero, liste_objets, sortie, plateau):

        """ Affiche le jeux en mode console """

        liste_positions_objets = []
        for i_0 in liste_objets:
            liste_positions_objets.append(i_0.position)

        # Remplissage de l'écran
        screen = ''
        for y in range(len(plateau.for_affichage)):
            for x in range(len(plateau.for_affichage[y])):
                if hero == (x, y):
                    screen += ' M '
                elif (x, y) in liste_positions_objets:
                    if liste_objets[liste_positions_objets.index((x, y))].nom_objet == 'aiguille':
                        screen += ' I '
                    elif liste_objets[liste_positions_objets.index((x, y))].nom_objet == 'tube_plastiqe':
                        screen += ' T '
                    elif liste_objets[liste_positions_objets.index((x, y))].nom_objet == 'ether':
                        screen += ' E '
                elif sortie == (x, y):
                    screen += ' S '
                elif (x, y) in plateau.murs:
                    screen += ' X '
                else:
                    screen += '   '
            screen += '\n'

        # affichage de l'écran
        print(screen)