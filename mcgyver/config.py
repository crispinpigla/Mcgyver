""" Fichier de configuration du jeu """


OBJETS_ARAMASSER = [ { 'nom': 'aiguille',
                       'icone_console': ' I ',
                       'image_ressource': "mcgyver/macgyver_ressources/ressource/aiguille0.png", 
                       'image_ressource_compteur': "mcgyver/macgyver_ressources/ressource/aiguille1.png"
                     },

                     { 'nom': 'tube_plastiqe', 
                       'icone_console': ' T ',
                       'image_ressource': "mcgyver/macgyver_ressources/ressource/tube_plastique0.png",
                       'image_ressource_compteur':  "mcgyver/macgyver_ressources/ressource/tube_plastique1.png" 
                     },

                     { 'nom': 'ether', 
                       'icone_console': ' E ',
                       'image_ressource': "mcgyver/macgyver_ressources/ressource/ether0.png",
                       'image_ressource_compteur': "mcgyver/macgyver_ressources/ressource/ether1.png"
                     }
                   ]

#image des ressources
IMAGE_HERO = "mcgyver/macgyver_ressources/ressource/mcgyver0.png"

IMAGE_MUR = [
             "mcgyver/macgyver_ressources/ressource/murs/mur0.png",
             "mcgyver/macgyver_ressources/ressource/murs/mur1.png",
             "mcgyver/macgyver_ressources/ressource/murs/mur2.png",
             "mcgyver/macgyver_ressources/ressource/murs/mur3.png",
             "mcgyver/macgyver_ressources/ressource/murs/mur4.png",
             "mcgyver/macgyver_ressources/ressource/murs/mur5.png",
             "mcgyver/macgyver_ressources/ressource/murs/mur6.png",
             "mcgyver/macgyver_ressources/ressource/murs/mur7.png",
             "mcgyver/macgyver_ressources/ressource/murs/mur8.png",
             "mcgyver/macgyver_ressources/ressource/murs/mur9.png"
            ]

IMAGE_FOND = "mcgyver/fbc1.png"
IMAGE_GARDIEN = "mcgyver/macgyver_ressources/ressource/gardien0.png"

# Déplacement mode console
MOUVEMENT_GAUCHE = 'j'
MOUVEMENT_DROITE = 'l'
MOUVEMENT_HAUT = 'i'
MOUVEMENT_BAS = 'k'

LARGEUR_PLATEAU = 15
HAUTEUR_PLATEAU = 15