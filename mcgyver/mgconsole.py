""" Affiche le jeux en mode console """


import config




class ModeConsole:

    """Classe du mode console"""

    def __init__(self):
        
        pass
        

    def start(self, mg0, liste_objets_aramass, gardien0, sortie0, plateau0):

        """ Gère les mouvements de Mcgyver en mode console """

        while mg0.position != sortie0.position:
            self.draw_console(mg0.position, liste_objets_aramass, sortie0.position, plateau0)
            direction_input = input("Déplacer McGyver !! \n\n " + config.MOUVEMENT_GAUCHE + " : vers la gauche\n " + config.MOUVEMENT_DROITE + " : vers la droite\n " + config.MOUVEMENT_BAS + " : vers le bas\n " + config.MOUVEMENT_HAUT + " : vers le haut\n\n ")
            # Modification de la position de Mcgyver
            mg0.pas_mcgyver(direction_input, liste_objets_aramass, gardien0)
        self.draw_console(mg0.position, liste_objets_aramass, sortie0.position, plateau0)

        #Gestion de la fin du jeu
        if len(mg0.objet_ramasse) == len(config.OBJETS_ARAMASSER):
            print('\n Gagné \n')
        else:
            print('\n Perdu \n')


    def draw_console(self, hero, liste_objets, sortie, plateau):

        """ Affiche le jeux en mode console """

        liste_positions_objets = []
        for i_0 in liste_objets:
            liste_positions_objets.append(i_0.position)

        # Remplissage de l'écran
        screen = ''
        for y in range(config.HAUTEUR_PLATEAU):
            for x in range(config.LARGEUR_PLATEAU):
                if hero == (x, y):
                    screen += ' M '
                elif (x, y) in liste_positions_objets:
                    for obj in config.OBJETS_ARAMASSER:
                        if obj['nom'] == liste_objets[liste_positions_objets.index((x, y))].nom_objet :
                            screen +=  obj['icone_console']
                elif sortie == (x, y):
                    screen += ' S '
                elif (x, y) in plateau.murs:
                    screen += ' X '
                elif (x, y) in plateau.routes :
                    screen += '   '
            screen += '\n'

        # affichage de l'écran
        print(screen)