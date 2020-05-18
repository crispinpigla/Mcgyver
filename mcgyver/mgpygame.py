"""" Affiche la version pygame du jeu """


import time
import pygame

from pygame.locals import *





######################################################




class FondSprite( pygame.sprite.Sprite ):

    """ Sprite du fond """

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        fond = pygame.image.load("mcgyver/fbc1.png").convert()
        self._image = fond.subsurface(pygame.Rect(0, 0, 600, 600))
        self._rect = pygame.Rect(0, 0, 600, 600)


    # getters
    @property
    def image(self):
        return self._image

    @property
    def rect(self):
        return self._rect
    



class MurSprite( pygame.sprite.Sprite ):

    """ Sprite de mur """

    def __init__(self, tuple_mur ):
        
        pygame.sprite.Sprite.__init__(self)
        fond = pygame.image.load("mcgyver/macgyver_ressources/ressource/brique.png").convert()        
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
        fond = pygame.image.load("mcgyver/macgyver_ressources/ressource/mcgyver0.png").convert()        
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
        
        pygame.sprite.Sprite.__init__(self)
        if objet_aramass.nom_objet == 'aiguille' :
            fond = pygame.image.load("mcgyver/macgyver_ressources/ressource/aiguille0.png").convert_alpha()   
        elif objet_aramass.nom_objet == 'tube_plastiqe' :
            fond = pygame.image.load("mcgyver/macgyver_ressources/ressource/tube_plastique0.png").convert_alpha()   
        elif objet_aramass.nom_objet == 'ether' :
            fond = pygame.image.load("mcgyver/macgyver_ressources/ressource/ether0.png").convert_alpha()
        self._image = fond.subsurface(pygame.Rect(0, 0, 40, 40))
        self._rect = pygame.Rect(objet_aramass.position[0]*40, objet_aramass.position[1]*40 ,40 ,40 )


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
        fond = pygame.image.load("mcgyver/macgyver_ressources/ressource/gardien0.png").convert()        
        self._image = fond.subsurface(pygame.Rect(0, 0, 40, 40))
        self._rect = pygame.Rect(gardien.position[0]*40, gardien.position[1]*40 ,40 ,40 )


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
        if len(hero.objet_ramasse) == 3 :
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
        group0 = pygame.sprite.Group()
        fond_sprit = FondSprite()
        group0.add(fond_sprit)
        for mur in plateau0.murs:
            group0.add(MurSprite(mur))
        group0.draw(self.fenetre)
        pygame.display.flip()


    def build_hero_objet_gardien(self, mg0, liste_objet, gardien0):
        
        """ Construction du groupe des objets , mcgyver et gardien """

        group1 = pygame.sprite.Group()
        gardien_sprit = GardienSprite(gardien0)
        hero_sprit = HeroSprite(mg0)
        group1.add( gardien_sprit )
        group1.add( hero_sprit )
        for obj in liste_objet:
            group1.add(ObjetsSprite(obj))
        group1.draw(self.fenetre)
        pygame.display.flip()


    def build_fin_jeu(self, hero, gardien):

        # Gestion de la fin du jeu

        if hero.position == gardien.position:
            finjeu_sprit = SpriteFinJeu(hero)
            group2 = pygame.sprite.Group()
            group2.add(finjeu_sprit)
            group2.draw(self.fenetre)
            pygame.display.flip()
            time.sleep(5)


    def start(self, mg0, liste_objet, gardien0, plateau0):

        """" Affiche la version pygame du jeu """

        pygame.init()

        self.fenetre = pygame.display.set_mode((600, 600), RESIZABLE)
        self.build_fond_mur(plateau0)
        self.build_hero_objet_gardien(mg0, liste_objet, gardien0)

        # La boucle du jeu
        while mg0.position != gardien0.position :
            for event in pygame.event.get():

                # sortie par fermeture de la fenetre
                if event.type == QUIT:
                    gardien0.catch()

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
                    mg0.pas_mcgyver(direction_input, liste_objet, gardien0)

                    self.build_fond_mur(plateau0)
                    self.build_hero_objet_gardien(mg0, liste_objet, gardien0)
                    self.build_fin_jeu(mg0, gardien0)