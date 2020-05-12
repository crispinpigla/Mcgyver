

""" Le main """



import random
import json


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

    with open("Mcgyver/structure.json", "r") as read_file:
        data = json.load(read_file)

	###  Structure
	# déclaration de la structure
    plateau0 = plateau.Plateau(15)
    mg0 = hero.Hero()
    sortie0 = sortie.Sortie()
    gardien0 = gardien.Gardien(15)

	# affectation des données aux attributs de la structure
	# mur du plateau
    for i_0 in data['coordonnees_points_murs']:
        plateau0.mur.append(tuple(i_0))

	# Les positions au debut du jeux
    mg0.position = tuple(data['depart_mcgyver'])
    sortie0.position = tuple(data['sortie_labyrinthe'])
    gardien0.position = tuple(data['sortie_labyrinthe'])

	### Objets à ramasser
    aiguille0 = objet_ramasse.ObjetRamasse('aiguille')
    tube_plastiqe0 = objet_ramasse.ObjetRamasse('tube_plastiqe')
    ether0 = objet_ramasse.ObjetRamasse('ether')

    champs_libres = plateau.mur_to_champs_libres(plateau0.mur, sortie0.position)
    champs_libres0 = list(champs_libres)

	# Remplissage des champs accessibles par Mcgiver
    movables = [mg0.position]
    i_0 = 0
    while i_0 < len(movables):
        for i_1 in plateau.move_posible(movables[i_0], champs_libres0):
            movables.append(i_1)
            champs_libres0.remove(i_1)
        i_0 += 1

	# Suppression des répétitions dans les champs accessibles par Mcgiver
    champs_accessibles = []
    while len(movables) != 0:
        champs_accessibles.append(movables[0])
        for i_2 in range(movables.count(champs_accessibles[-1])):
            movables.remove(champs_accessibles[-1])
    champs_accessibles.remove(mg0.position)

	#  Cas : pas assez d'espace dans le plateau pour insérer 3 objets distinct accessibles par Mcgyver
    if len(champs_accessibles) < 3:
        print('ce tableau ne permet pas de placer 3 objets accessible par McGyver !!')

	#  Cas : assez d'espace dans le plateau pour insérer 3 objets distinct accessibles par Mcgyver
    else:
        random.shuffle(champs_accessibles)
        aiguille0.position = champs_accessibles[0]
        tube_plastiqe0.position = champs_accessibles[1]
        ether0.position = champs_accessibles[2]

		#  Acceuil du jeu
        input_demarrage = input(" Bienvenu dans McGyver Labyrinthe game \n Entrez 'c' pour "
                                "jouer en mode console\n Entrez 'p' pour jouer en mode "
                                "pygame ( recommandé ) \n Entrez 'q' pour quitter\n ")

        while (input_demarrage not in ['c', 'p', 'q']):
            input_demarrage = input(" Bienvenu dans McGyver Labyrinthe game \n Entrez 'c' pour "
                                    "jouer en mode console\n Entrez 'p' pour jouer en mode "
                                    "pygame ( recommandé ) \n Entrez 'q' pour quitter\n ")
        if input_demarrage == 'c':
            mg_console.jeu_console(mg0, aiguille0, tube_plastiqe0, ether0, sortie0, plateau0)
        elif input_demarrage == 'p':
            mg_pygame.jeu_pygame(mg0, aiguille0, tube_plastiqe0,
                                 ether0, sortie0, gardien0, plateau0)
        elif input_demarrage == 'q':
            pass





main()