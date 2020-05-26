""" Fichier de configuration du jeu """


OBJETS_ARAMASSER = [ { 'nom': 'aiguille', 
                       'image_ressource': "mcgyver/macgyver_ressources/ressource/aiguille0.png", 
                       'image_ressource_compteur': "mcgyver/macgyver_ressources/ressource/aiguille1.png"
                     },

                     { 'nom': 'tube_plastiqe', 
                       'image_ressource': "mcgyver/macgyver_ressources/ressource/tube_plastique0.png",
                       'image_ressource_compteur':  "mcgyver/macgyver_ressources/ressource/tube_plastique1.png" 
                     },

                     { 'nom': 'ether', 
                       'image_ressource': "mcgyver/macgyver_ressources/ressource/ether0.png",
                       'image_ressource_compteur': "mcgyver/macgyver_ressources/ressource/ether1.png" 
                     }
                   ]

#image des ressources
IMAGE_HERO = "mcgyver/macgyver_ressources/ressource/mcgyver0.png"
IMAGE_MUR = "mcgyver/macgyver_ressources/ressource/brique.png"
IMAGE_FOND = "mcgyver/fbc1.png"
IMAGE_GARDIEN = "mcgyver/macgyver_ressources/ressource/gardien0.png"

# Déplacement mode console
MOUVEMENT_GAUCHE = 'j'
MOUVEMENT_DROITE = 'l'
MOUVEMENT_HAUT = 'i'
MOUVEMENT_BAS = 'k'

LARGEUR_PLATEAU = 15
HAUTEUR_PLATEAU = 15