

""" Le main """

import random


###    Mes modules
# Modules de logique
import hero
import plateau
import sortie
import gardien
import objramasse

# Modules d'affichage
import mgconsole
import mgpygame



def main():

    """ Le main """

    ### déclaration du plateau
    plateau0 = plateau.Plateau()

    ### Objets à ramasser
    aiguille0 = objramasse.ObjetRamasse(plateau0, 'aiguille')
    tube_plastiqe0 = objramasse.ObjetRamasse(plateau0, 'tube_plastiqe')
    ether0 = objramasse.ObjetRamasse(plateau0, 'ether')

    ### déclaration du reste de la structure
    mg0 = hero.Hero(plateau0)
    sortie0 = sortie.Sortie(plateau0)
    gardien0 = gardien.Gardien(plateau0)

    mode_console = mgconsole.ModeConsole()
    mode_pygame = mgpygame.ModePygame()

    #  Acceuil du jeu
    input_demarrage = input(" Bienvenu dans McGyver Labyrinthe game \n Entrez 'c' pour "
                            "jouer en mode console\n Entrez 'p' pour jouer en mode "
                            "pygame ( recommandé ) \n Entrez 'q' pour quitter\n ")

    while (input_demarrage not in ['c', 'p', 'q']):
        input_demarrage = input(" Bienvenu dans McGyver Labyrinthe game \n Entrez 'c' pour "
                                "jouer en mode console\n Entrez 'p' pour jouer en mode "
                                "pygame ( recommandé ) \n Entrez 'q' pour quitter\n ")
    if input_demarrage == 'c':
        mode_console.start(mg0, aiguille0, tube_plastiqe0, ether0, gardien0, sortie0, plateau0)
    elif input_demarrage == 'p':
        mode_pygame.start(mg0, [aiguille0, tube_plastiqe0, ether0], gardien0, plateau0)
    elif input_demarrage == 'q':
        pass




main()