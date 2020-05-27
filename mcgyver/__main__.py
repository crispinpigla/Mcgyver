

""" Le main : fichier de démarrage du jeu """


# Mes modules
# Modules de logique
import hero
import plateau
import sortie
import gardien
import objramasse
# Modules d'affichage
import mgconsole
import mgpygame
# Configuration
import config


def main():
    """ Le main """

    # déclaration du plateau
    plateau0 = plateau.Plateau()

    # Objets à ramasser
    liste_objets_aramass = []
    for elt_dict in config.OBJETS_ARAMASSER:
        liste_objets_aramass.append(
            objramasse.ObjetRamasse(plateau0, elt_dict['nom']))

    # déclaration du reste de la structure
    hero0 = hero.Hero(plateau0)
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
        mode_console.start(hero0, liste_objets_aramass,
                           gardien0, sortie0, plateau0)
    elif input_demarrage == 'p':
        mode_pygame.start(hero0, liste_objets_aramass, gardien0, plateau0)
    elif input_demarrage == 'q':
        pass


main()
