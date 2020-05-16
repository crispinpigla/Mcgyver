"""" Affiche la version pygame du jeu """


import time
import pygame

from pygame.locals import *


class mode_pygame(object):

    """docstring for mode_pygame"""

    def __init__(self, mg0, aiguille0, tube_plastiqe0, ether0, sortie0, gardien0, plateau0):
        self.jeu_pygame(mg0, aiguille0, tube_plastiqe0, ether0, sortie0, gardien0, plateau0 )


    def jeu_pygame(self, mg0, aiguille0, tube_plastiqe0, ether0, sortie0, gardien0, plateau0 ):

        """" Affiche la version pygame du jeu """

        pygame.init()
        fenetre = pygame.display.set_mode((600, 600), RESIZABLE)

        #  Définition du mur
        pygame_wall = []
        fond = pygame.image.load("Mcgyver/fbc1.png").convert()
        fenetre.blit(fond, (0, 0))

    	#  Placement des murs
        for i_0 in plateau0.murs:
            pygame_wall.append(pygame.image.load("Mcgyver/macgyver_ressources/ressource/brique.png").convert())

    	#print( pygame_wall )
        for i_1 in pygame_wall:
            fenetre.blit(i_1, (plateau0.murs[pygame_wall.index(i_1)][0] * 40, plateau0.murs[pygame_wall.index(i_1)][1] * 40))

    	#  Placement de McGyver et du gardien
    	# McGyver
        py_mcgyver = pygame.image.load("Mcgyver/macgyver_ressources/ressource/mcgyver1.png").convert_alpha()
        anneau_mcgyver = pygame.image.load("Mcgyver/macgyver_ressources/ressource/anneaunoir.png").convert_alpha()
        fenetre.blit(py_mcgyver, ((mg0.position[0] * 40) + 7.5, (mg0.position[1] * 40) + 7.5))
        fenetre.blit(anneau_mcgyver, (mg0.position[0] * 40, mg0.position[1] * 40))
    	# Gardien
        py_gardien = pygame.image.load("Mcgyver/macgyver_ressources/ressource/gardien1.png").convert_alpha()

        #  Placement de la sortie et du gardien
        anneau_sortie = pygame.image.load("Mcgyver/macgyver_ressources/ressource/anneaurouge.png").convert_alpha()
        fenetre.blit(py_gardien, ((gardien0.position[0] * 40) + 7.5, (gardien0.position[1] * 40) + 7.5))
        fenetre.blit(anneau_sortie, (gardien0.position[0] * 40, gardien0.position[1] * 40))	

    	# Placement des objets à ramasser
        anneau_objets = pygame.image.load("Mcgyver/macgyver_ressources/ressource/anneauvert.png").convert_alpha()
    	# aiguille
        py_aiguille0 = pygame.image.load("Mcgyver/macgyver_ressources/ressource/aiguille1.png").convert_alpha()
        fenetre.blit(py_aiguille0, ((aiguille0.position[0] * 40) + 7.5, (aiguille0.position[1] * 40) + 7.5))	
        fenetre.blit(anneau_objets, (aiguille0.position[0] * 40, aiguille0.position[1] * 40))	
    	# tube plastique
        py_tube_plastique0 = pygame.image.load("Mcgyver/macgyver_ressources/ressource/tube_plastique1.png").convert()
        fenetre.blit(py_tube_plastique0, ((tube_plastiqe0.position[0] * 40) + 7.5 ,(tube_plastiqe0.position[1] * 40) + 7.5))	
        fenetre.blit(anneau_objets, (tube_plastiqe0.position[0] * 40, tube_plastiqe0.position[1] * 40))	
    	# ether
        py_ether0 = pygame.image.load("Mcgyver/macgyver_ressources/ressource/ether1.png")
        fenetre.blit(py_ether0, (( ether0.position[0] * 40) + 7.5, (ether0.position[1] * 40) + 7.5))	
        fenetre.blit(anneau_objets, (ether0.position[0] * 40, ether0.position[1] * 40))	

        # Affichage des objets placés
        pygame.display.flip()

        # La boucle du jeu
        while mg0.position != gardien0.position:
            for event in pygame.event.get():

                # sortie par fermeture de la fenetre
                if event.type == QUIT:
                    mg0.position = gardien0.position

                # Capture des mouvements
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        direction_input = 'j'
                    elif event.key == K_UP:
                        direction_input = 'i'
                    elif event.key == K_RIGHT:
                        direction_input = 'l'
                    elif event.key == K_DOWN:
                        direction_input = 'k'
                    else:
                        direction_input = 'autre'

                    # Gestion des mouvements
                    if (mg0.pas_mcgyver(direction_input) not in plateau0.murs) and (mg0.pas_mcgyver(direction_input) in plateau0.plateauvide):
                        transit_position_mg = mg0.position
                        mg0.position = mg0.pas_mcgyver(direction_input)

                        # Gestion du rammassage des objets
                        if mg0.position == aiguille0.position:
                            mg0.objet_ramasse.append(aiguille0.nom_objet)
                            aiguille0.ramassage()
                        elif mg0.position == tube_plastiqe0.position:
                            mg0.objet_ramasse.append(tube_plastiqe0.nom_objet)
                            tube_plastiqe0.ramassage()
                        elif mg0.position == ether0.position:
                            mg0.objet_ramasse.append(ether0.nom_objet)
                            ether0.ramassage()

    					##  Déplacement de McGyver

                        # gestion de la fluidité des mouvements de Mcgyver
                        fluidite = 70
                        for i0 in range(fluidite):
                            if event.key == K_LEFT:
                                transit_position_mg = (transit_position_mg[0] - (1 / fluidite), transit_position_mg[1])
                            elif event.key == K_UP:
                                transit_position_mg = (transit_position_mg[0], transit_position_mg[1] - (1 / fluidite ))
                            elif event.key == K_RIGHT:
                                transit_position_mg = (transit_position_mg[0] + (1 / fluidite), transit_position_mg[1])
                            elif event.key == K_DOWN:
                                transit_position_mg = (transit_position_mg[0], transit_position_mg[1] + (1/fluidite))

                            # Les remontaoges
                            fenetre.blit(fond, (0, 0))

                            for i1  in pygame_wall:
                                fenetre.blit(i1, (plateau0.murs[pygame_wall.index(i1)][0] * 40, plateau0.murs[pygame_wall.index(i1)][1] * 40))

                            fenetre.blit(py_aiguille0, ((aiguille0.position[0] * 40) + 7.5, (aiguille0.position[1] * 40) + 7.5))	
                            fenetre.blit(anneau_objets, (aiguille0.position[0] * 40, aiguille0.position[1] * 40))	

                            fenetre.blit(py_tube_plastique0, ((tube_plastiqe0.position[0] * 40) + 7.5, (tube_plastiqe0.position[1] * 40) + 7.5))
                            fenetre.blit(anneau_objets , ( tube_plastiqe0.position[0] * 40, tube_plastiqe0.position[1] * 40))

                            fenetre.blit(py_ether0, (( ether0.position[0] * 40) + 7.5, (ether0.position[1] * 40) + 7.5))	
                            fenetre.blit(anneau_objets, (ether0.position[0] * 40, ether0.position[1] * 40))

                            fenetre.blit(py_mcgyver, ((transit_position_mg[0] * 40) + 7.5 , (transit_position_mg[1] * 40) + 7.5))

                            # Gestion du changement de coloration de l'anneau de Mcgyver
                            if len(mg0.objet_ramasse) == 3:
                                anneau_mcgyver = pygame.image.load("Mcgyver/macgyver_ressources/ressource/anneauvert.png").convert_alpha()

                            fenetre.blit(anneau_mcgyver, (transit_position_mg[0] * 40, transit_position_mg[1] * 40))	

                            # Gestion de la fin du jeu
                            if mg0.position == gardien0.position:
                                if len(mg0.objet_ramasse) == 3:
                                    image_fin = pygame.image.load("Mcgyver/macgyver_ressources/ressource/gagne.png").convert()
                                else:
                                    image_fin = pygame.image.load("Mcgyver/macgyver_ressources/ressource/perdu.png").convert()
                                fenetre.blit(image_fin, (100, 200))

                            # Gestion de la suite du jeu
                            else:
                                # Gestion du changement de coloration de l'anneau de la sortie
                                if len(mg0.objet_ramasse) == 3:
                                    anneau_sortie = pygame.image.load("Mcgyver/macgyver_ressources/ressource/anneauvert.png").convert_alpha()

                                fenetre.blit(py_gardien, ((gardien0.position[0] * 40) + 7.5, (gardien0.position[1] * 40) + 7.5))
                                fenetre.blit(anneau_sortie, (gardien0.position[0] * 40, gardien0.position[1] * 40))

                            # Affichage après mouvement de Mcgyver
                            pygame.display.flip()

                        # Gestion du temps de latence entre la fin du jeu et la fermeture de la fenetre
                        if mg0.position == gardien0.position:
                            time.sleep(5)