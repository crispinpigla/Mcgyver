"""" Affiche la version pygame du jeu """


import time
import pygame

from pygame.locals import *

import config



######################################################




class FondSprite( pygame.sprite.Sprite ):
    """ Sprite du fond """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        fond = pygame.image.load(config.IMAGE_FOND).convert()
        self._image = fond.subsurface(pygame.Rect(0, 0, 600, 600))
        self._rect = pygame.Rect(0, 0, 600, 600)


    # getters
    @property
    def image(self):
        return self._image

    @property
    def rect(self):
        return self._rect
    



class MurSprite(pygame.sprite.Sprite):
    """ Sprite de mur """

    def __init__(self, tuple_mur ):
        pygame.sprite.Sprite.__init__(self)
        fond = pygame.image.load(config.IMAGE_MUR[1]).convert()
        self._image = fond.subsurface(pygame.Rect(0, 0, 40, 40))
        self._rect = pygame.Rect(tuple_mur[0]*40, tuple_mur[1]*40 ,40 ,40 )


    #getters
    @property
    def image(self):
        return self._image

    @property
    def rect(self):
        return self._rect
    



class HeroSprite( pygame.sprite.Sprite ):
    """ Sprite de hero """

    def __init__(self, hero):
        pygame.sprite.Sprite.__init__(self)
        fond = pygame.image.load(config.IMAGE_HERO).convert()
        self._image = fond.subsurface(pygame.Rect(0, 0, 40, 40))
        self._rect = pygame.Rect(hero.position[0]*40, hero.position[1]*40 ,40 ,40 )


    #getters
    @property
    def image(self):
        return self._image

    @property
    def rect(self):
        return self._rect



class ObjetsSprite( pygame.sprite.Sprite ):
    """ Sprite des objets """

    def __init__(self, objet_aramass):
        
        super().__init__()

        index_objet_config = 0
        while config.OBJETS_ARAMASSER[index_objet_config]['nom'] != objet_aramass.nom_objet :
            index_objet_config += 1
        fond = pygame.image.load(config.OBJETS_ARAMASSER[index_objet_config]['image_ressource']).convert_alpha()
        self._image = fond.subsurface(pygame.Rect(0, 0, 40, 40))
        self._rect = pygame.Rect(objet_aramass.position[0]*40, objet_aramass.position[1]*40 ,40 ,40 )


    #getters
    @property
    def image(self):
        return self._image

    @property
    def rect(self):
        return self._rect




class ObjetsCompteurSprite( pygame.sprite.Sprite ):
    """ Sprite des objets """

    def __init__(self, objet_aramass, index_objet):
        
        super().__init__()

        index_objet_config = 0
        while config.OBJETS_ARAMASSER[index_objet_config]['nom'] != objet_aramass.nom_objet :
            index_objet_config += 1
        fond = pygame.image.load(config.OBJETS_ARAMASSER[index_objet_config]['image_ressource_compteur']).convert_alpha()
        self._image = fond.subsurface(pygame.Rect(0, 0, 25, 25))
        self._rect = pygame.Rect(300+(index_objet*40), 600+12.5 ,25 ,25 )


    #getters
    @property
    def image(self):
        return self._image

    @property
    def rect(self):
        return self._rect




class GardienSprite( pygame.sprite.Sprite ):
    """ Sprite du gardien """

    def __init__(self, gardien):
        
        pygame.sprite.Sprite.__init__(self)
        fond = pygame.image.load(config.IMAGE_GARDIEN).convert()
        self._image = fond.subsurface(pygame.Rect(0, 0, 40, 40))
        self._rect = pygame.Rect(gardien.position[0]*40, gardien.position[1]*40 ,40 ,40 )


    #getters
    @property
    def image(self):
        return self._image

    @property
    def rect(self):
        return self._rect



class CompteurSprite( pygame.sprite.Sprite ):
    """ Sprite du compteur """

    def __init__(self, mcgyver):

        pygame.sprite.Sprite.__init__(self)
        fond = fond = pygame.image.load("mcgyver/macgyver_ressources/ressource/compteurobjram.png").convert()
        self._image = fond.subsurface(pygame.Rect(0, 0, 600, 50))
        self._rect = pygame.Rect(0, 600 ,600 ,50)

    #getters
    @property
    def image(self):
        return self._image

    @property
    def rect(self):
        return self._rect





class SpriteFinJeu( pygame.sprite.Sprite ):

    """ Sprite de fin du jeu """

    def __init__(self, hero):

        pygame.sprite.Sprite.__init__(self)
        if len(hero.objet_ramasse) == len(config.OBJETS_ARAMASSER) :
            fond = pygame.image.load("mcgyver/macgyver_ressources/ressource/gagne.png").convert()
        else:
            fond = pygame.image.load("mcgyver/macgyver_ressources/ressource/perdu.png").convert()
        self._image = fond.subsurface(pygame.Rect(0, 0, 400, 200))
        self._rect = pygame.Rect(100, 200 ,400 ,200 )


    #getters
    @property
    def image(self):
        return self._image

    @property
    def rect(self):
        return self._rect






########################################################


class ModePygame:

    """docstring for mode_pygame"""

    def __init__(self):
        
        pass


    def build_fond_mur(self, plateau0):
        """ Constuit le fond et les murs du jeu """

        # définition, remplisage et affichage du groupe des fonds et murs
        group = pygame.sprite.Group()
        fond_sprit = FondSprite()
        group.add(fond_sprit)
        for mur in plateau0.murs:
            group.add(MurSprite(mur))
        group.draw(self.fenetre)
        pygame.display.flip()


    def build_hero_objet_gardien(self, mg0, liste_objet, gardien0):
        """ Construction du groupe des objets , mcgyver et gardien """

        group = pygame.sprite.Group()
        gardien_sprit = GardienSprite(gardien0)
        hero_sprit = HeroSprite(mg0)
        group.add( gardien_sprit )
        group.add( hero_sprit )
        for obj in liste_objet:
            group.add(ObjetsSprite(obj))
        group.draw(self.fenetre)
        pygame.display.flip()


    def build_object_counter(self, hero):
        """ Construction du groupe du compteur """

        group = pygame.sprite.Group()
        compteur_sprite = CompteurSprite(hero)
        group.add(compteur_sprite)
        for objet in hero.objet_ramasse :
            group.add(ObjetsCompteurSprite(objet, hero.objet_ramasse.index(objet)))
        group.draw(self.fenetre)
        pygame.display.flip()



    def build_fin_jeu(self, hero, gardien):
        # Gestion de la fin du jeu

        if hero.position == gardien.position:
            finjeu_sprit = SpriteFinJeu(hero)
            group = pygame.sprite.Group()
            group.add(finjeu_sprit)
            group.draw(self.fenetre)
            pygame.display.flip()
            time.sleep(5)


    def start(self, mg0, liste_objet, gardien0, plateau0):

        """" Affiche la version pygame du jeu """

        pygame.init()

        self.fenetre = pygame.display.set_mode((600, 650), RESIZABLE)
        self.build_fond_mur(plateau0)
        self.build_hero_objet_gardien(mg0, liste_objet, gardien0)
        self.build_object_counter(mg0)

        # La boucle du jeu
        while mg0.position != gardien0.position :
            for event in pygame.event.get():

                # sortie par fermeture de la fenetre
                if event.type == QUIT:
                    gardien0.catch()

                # Capture des mouvements
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        direction_input = config.MOUVEMENT_GAUCHE
                    elif event.key == K_UP:
                        direction_input = config.MOUVEMENT_HAUT
                    elif event.key == K_RIGHT:
                        direction_input = config.MOUVEMENT_DROITE
                    elif event.key == K_DOWN:
                        direction_input = config.MOUVEMENT_BAS
                    else:
                        direction_input = 'autre'

                    # Gestion des mouvements
                    mg0.pas_mcgyver(direction_input, liste_objet, gardien0)

                    self.build_fond_mur(plateau0)
                    self.build_hero_objet_gardien(mg0, liste_objet, gardien0)
                    self.build_fin_jeu(mg0, gardien0)
                    self.build_object_counter(mg0)