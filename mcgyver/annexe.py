










class Plateau:

	"""docstring for Plateau"""

	def __init__( self , taille_plateau ):

		self.plateauvide = []
		
		for i0 in range( taille_plateau ):
			
			for i1 in range( taille_plateau ):
				
				self.plateauvide.append( ( i1 , i0 ) )


	# renvoie une liste de mur valide en protegeant les routes des murs 

	def initialisemur( self , taille_plateau , route1 , route2 , route3 , route4 ):

		self.mur = []

		for i0 in range( taille_plateau ):
			
			for i1 in range( taille_plateau ):
				
				if ( ( i1 , i0 ) in route1 ) or ( ( i1 , i0 ) in route2 ) or ( ( i1 , i0 ) in route3 ) or ( ( i1 , i0 ) in route4 ) :

					pass

				else :

					if random.randrange( 2 ) == 0 :

						self.mur.append( ( i1 , i0 ) )

					else :

						pass




class Sortie:

	"""docstring for Sortie"""

	def __init__( self , taille_plateau ):

		self.position = ( random.randrange( taille_plateau - 1 ) , random.randrange( taille_plateau - 1 ) )

		self.route_mg = []

		


class Heros:

	"""docstring for Heros"""

	def __init__( self , taille_plateau ):

		self.position = ( random.randrange( taille_plateau - 1 ) , random.randrange( taille_plateau - 1 ) )

		self.objet_ramasse = [] ;




class Gardien:

	"""docstring for Gardien"""
	
	def __init__( self , taille_plateau ):

		self.position = ( 0 , 0)




class ObjetsRamasses:

	"""docstring for Objets"""

	def __init__( self , taille_plateau , nom_de_lobjet ):


		self.position = ( random.randrange( taille_plateau - 1 ) , random.randrange( taille_plateau - 1 ) )

		self.route_mg = []

		self.nom_objet = nom_de_lobjet
		
	



"""  Fait un pas d'une cible vers le curseur dans un plateau vide ( pour la construction des routes )  """

#      A fonctionner 

class Pas:

	"""docstring for Pas"""

	def __init__( self ):
		
		pass


	def make_pas( self , curseur , cible ):
		
		#curseur_intermediaire = ( curseur[0] + 2 , curseur[1] + 2 )

		

		curseur_intermediaire = curseur

		
		if curseur == cible :
			
			print( 'le curseur est sur la cible' )

		elif curseur[0] == cible[0] :

			if cible[1] > curseur[1] :

				curseur_intermediaire = ( curseur[0] , curseur[1] + 1 )


			elif cible[1] < curseur[1] :

				curseur_intermediaire = ( curseur[0] , curseur[1] - 1 )



		elif curseur[1] == cible[1] :

			if cible[0] > curseur[0] :

				curseur_intermediaire = ( curseur[0] + 1 , curseur[1] )
				 

			elif cible[0] < curseur[0] :

				curseur_intermediaire = ( curseur[0] - 1 , curseur[1] )
				 



		else :


			if random.randrange( 2 ) == 0 :
				
				if cible[0] > curseur[0] :

					curseur_intermediaire = ( curseur[0] + 1 , curseur[1] )
					 

				elif cible[0] < curseur[0] :

					curseur_intermediaire = ( curseur[0] - 1 , curseur[1] )
					 

			else :

				if cible[1] > curseur[1] :

					curseur_intermediaire = ( curseur[0] , curseur[1] + 1 )
					 

				elif cible[1] < curseur[1] :

					curseur_intermediaire = ( curseur[0] , curseur[1] - 1 )
					 

		
		return ( curseur_intermediaire )	



	def make_pas_with_mur( self , curseur , cible  ):
		pass

















def generate_structure():
	
	pas = Pas();

	plateau = Plateau(15)

	position_initialisee = []

	mg = Heros(15)

	position_initialisee.append( mg.position )





	aiguille = ObjetsRamasses( 15 , 'aiguille' )

	# Test si la position de l'aiguille est déjà occupée

	while aiguille.position in position_initialisee :
		
		aiguille = ObjetsRamasses( 15 , 'aiguille' )

	# Ajout de la position de l'aiguille dans la liste des positions occupées

	position_initialisee.append( aiguille.position )

	# Définition de la route que mcgyver emprunte pour atteindre cet objet

	lepas = mg.position

	aiguille.route_mg.append( lepas )

	while lepas != aiguille.position :

		lepas = pas.make_pas( lepas , aiguille.position )

		aiguille.route_mg.append( lepas )

	#print( aiguille.route_mg )





	tube_plastiqe = ObjetsRamasses( 15 , 'tube_plastiqe' )

	# Test si la position du tube en plastiqe est déjà occupée

	while tube_plastiqe.position in position_initialisee :
		
		tube_plastiqe = ObjetsRamasses( 15 , 'tube_plastiqe' )

	# Ajout de la position du tube en plastiqe dans la liste des positions occupées

	position_initialisee.append( tube_plastiqe.position )

	# Définition de la route que mcgyver emprunte pour atteindre cet objet

	lepas = mg.position

	tube_plastiqe.route_mg.append( lepas )

	while lepas != tube_plastiqe.position :

		lepas = pas.make_pas( lepas , tube_plastiqe.position )

		tube_plastiqe.route_mg.append( lepas )

	#print( tube_plastiqe.route_mg )





	ether = ObjetsRamasses( 15 , 'ether' )

	# Test si la position de l'ether est déjà occupée

	while ether.position in position_initialisee :
		
		ether = ObjetsRamasses( 15 , 'ether' )

	# Ajout de la position de l'ether dans la liste des positions occupées

	position_initialisee.append( ether.position )

	# Définition de la route que mcgyver emprunte pour atteindre cet objet

	lepas = mg.position

	ether.route_mg.append( lepas )

	while lepas != ether.position :

		lepas = pas.make_pas( lepas , ether.position )

		ether.route_mg.append( lepas )

	#print( ether.route_mg )





	sortie = Sortie(15)

	# Test si la position de la sortie est déjà occupée

	while ( sortie.position in aiguille.route_mg ) or ( sortie.position in tube_plastiqe.route_mg ) or ( sortie.position in ether.route_mg ) :
		
		sortie = Sortie( 15 )

	# Ajout de la position de la sortie dans la liste des positions occupées

	position_initialisee.append( sortie.position )

	# Définition de la route que mcgyver emprunte pour atteindre la sorite

	lepas = mg.position

	sortie.route_mg.append( lepas )

	while lepas != sortie.position :

		lepas = pas.make_pas( lepas , sortie.position )

		sortie.route_mg.append( lepas )

	#print( 'sortie ' , sortie.route_mg )



	plateau.initialisemur( 15 , aiguille.route_mg , tube_plastiqe.route_mg , ether.route_mg , sortie.route_mg  )




	gardien = Gardien()

	gardien.position = sortie.position


	plateaujson = []

	for i0 in plateau.mur :
		
		plateaujson.append( list( i0 ) )

	#print( 'structure json : ' , plateaujson , list( mg.position ) , list(sortie.position) )

	return( [ plateau , mg , sortie , [ aiguille , tube_plastiqe , ether ] ] )
	
















##       Pygame initial

	    """
        pygame.init()
        fenetre = pygame.display.set_mode((600, 600), RESIZABLE)

        #  Définition du mur
        
        pygame_wall = []
        fond = pygame.image.load("mcgyver/fbc1.png").convert()

        
        fenetre.blit(fond, (0, 0))
        
    	#  Placement des murs
        for i_0 in plateau0.murs:
            pygame_wall.append(pygame.image.load("mcgyver/macgyver_ressources/ressource/brique.png").convert())

    	#print( pygame_wall )
        for i_1 in pygame_wall:
            fenetre.blit(i_1, (plateau0.murs[pygame_wall.index(i_1)][0] * 40, plateau0.murs[pygame_wall.index(i_1)][1] * 40))

    	#  Placement de McGyver et du gardien
    	# McGyver
        py_mcgyver = pygame.image.load("mcgyver/macgyver_ressources/ressource/mcgyver1.png").convert_alpha()
        anneau_mcgyver = pygame.image.load("mcgyver/macgyver_ressources/ressource/anneaunoir.png").convert_alpha()
        fenetre.blit(py_mcgyver, ((mg0.position[0] * 40) + 7.5, (mg0.position[1] * 40) + 7.5))
        fenetre.blit(anneau_mcgyver, (mg0.position[0] * 40, mg0.position[1] * 40))
    	# Gardien
        py_gardien = pygame.image.load("mcgyver/macgyver_ressources/ressource/gardien1.png").convert_alpha()

        #  Placement de la sortie et du gardien
        anneau_sortie = pygame.image.load("mcgyver/macgyver_ressources/ressource/anneaurouge.png").convert_alpha()
        fenetre.blit(py_gardien, ((gardien0.position[0] * 40) + 7.5, (gardien0.position[1] * 40) + 7.5))
        fenetre.blit(anneau_sortie, (gardien0.position[0] * 40, gardien0.position[1] * 40))	

    	# Placement des objets à ramasser
        anneau_objets = pygame.image.load("mcgyver/macgyver_ressources/ressource/anneauvert.png").convert_alpha()
    	# aiguille
        py_aiguille0 = pygame.image.load("mcgyver/macgyver_ressources/ressource/aiguille1.png").convert_alpha()
        fenetre.blit(py_aiguille0, ((aiguille0.position[0] * 40) + 7.5, (aiguille0.position[1] * 40) + 7.5))	
        fenetre.blit(anneau_objets, (aiguille0.position[0] * 40, aiguille0.position[1] * 40))	
    	# tube plastique
        py_tube_plastique0 = pygame.image.load("mcgyver/macgyver_ressources/ressource/tube_plastique1.png").convert()
        fenetre.blit(py_tube_plastique0, ((tube_plastiqe0.position[0] * 40) + 7.5 ,(tube_plastiqe0.position[1] * 40) + 7.5))	
        fenetre.blit(anneau_objets, (tube_plastiqe0.position[0] * 40, tube_plastiqe0.position[1] * 40))	
    	# ether
        py_ether0 = pygame.image.load("mcgyver/macgyver_ressources/ressource/ether1.png")
        fenetre.blit(py_ether0, (( ether0.position[0] * 40) + 7.5, (ether0.position[1] * 40) + 7.5))	
        fenetre.blit(anneau_objets, (ether0.position[0] * 40, ether0.position[1] * 40))	

        # Affichage des objets placés
        pygame.display.flip()

        """

        #fenetre = pygame.display.set_mode((600, 600), RESIZABLE)
        
        #pygame.sprite.Group.draw( )
        #time.sleep(5)







        """

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
                    mg0.pas_mcgyver(direction_input)

					##  Déplacement de McGyver

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

                    fenetre.blit(py_mcgyver, ((mg0.position[0] * 40) + 7.5 , (mg0.position[1] * 40) + 7.5))

                    # Gestion du changement de coloration de l'anneau de Mcgyver
                    if len(mg0.objet_ramasse) == 3:
                        anneau_mcgyver = pygame.image.load("Mcgyver/macgyver_ressources/ressource/anneauvert.png").convert_alpha()

                    fenetre.blit(anneau_mcgyver, (mg0.position[0] * 40, mg0.position[1] * 40))	

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


        """