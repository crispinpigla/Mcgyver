

""" Le main """



import random


###    Mes modules
# Modules de logique
import hero
import plateau
import sortie
import gardien
import objet_ramasse

# Modules d'affichage
import mg_console
import mg_pygame






def main():

    """ Le main """


    ### déclaration de la structure

    plateau0 = plateau.Plateau()

    mg0 = hero.Hero(plateau0)
    sortie0 = sortie.Sortie(plateau0)
    gardien0 = gardien.Gardien(plateau0)


    ### Objets à ramasser

    aiguille0 = objet_ramasse.ObjetRamasse(plateau0, 'aiguille')
    tube_plastiqe0 = objet_ramasse.ObjetRamasse(plateau0, 'tube_plastiqe')
    ether0 = objet_ramasse.ObjetRamasse(plateau0, 'ether')


    #  Acceuil du jeu
    input_demarrage = input(" Bienvenu dans McGyver Labyrinthe game \n Entrez 'c' pour "
                            "jouer en mode console\n Entrez 'p' pour jouer en mode "
                            "pygame ( recommandé ) \n Entrez 'q' pour quitter\n ")

    while (input_demarrage not in ['c', 'p', 'q']):
        input_demarrage = input(" Bienvenu dans McGyver Labyrinthe game \n Entrez 'c' pour "
                                "jouer en mode console\n Entrez 'p' pour jouer en mode "
                                "pygame ( recommandé ) \n Entrez 'q' pour quitter\n ")
    if input_demarrage == 'c':
        mode_console = mg_console.mode_console(mg0, aiguille0, tube_plastiqe0, ether0, sortie0, plateau0)

    elif input_demarrage == 'p':
        mode_pygame = mg_pygame.mode_pygame(mg0, aiguille0, tube_plastiqe0, ether0, sortie0, gardien0, plateau0)

    elif input_demarrage == 'q':
        pass




main()