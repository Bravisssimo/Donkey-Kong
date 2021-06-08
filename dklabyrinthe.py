#-*- coding: utf-8 -*- # codage des accents

""" Jeu DonkeyKongLaby
Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images
"""

import pygame
from pygame.locals import *
from classes import *
from constantes import *


pygame.init()
fenetre = pygame.display.set_mode((cote_fenetre, hauteur_fenetre))
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
pygame.display.set_caption(titre_fenetre)
delay_en_ms=10			# Temps au bout duquel la commande sera répétée la premiere fois
intervalle= 100

continuer = 1
pygame.key.set_repeat(delay_en_ms, intervalle)
while continuer:
    accueil = pygame.image.load(image_accueil).convert()
    fenetre.blit(accueil, (0,0))

    pygame.display.flip()

    continuer_jeu = True
    continuer_accueil = True

    while continuer_accueil:
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_accueil = 0
                continuer_jeu = 0
                continuer = 0
                choix = 0

            elif event.type == KEYDOWN:

                if event.key == K_F1:
                    continuer_accueil = False
                    choix = 'n1'

    if choix != 0:

        fond = pygame.image.load(image_fond_centre).convert()

        niveau=Niveau(choix)
        niveau.generer()
        niveau.afficher(fenetre)

        dk = Perso("images/dk_droite.png", "images/dk_gauche.png","images/dk_haut.png","images/dk_bas.png", niveau)

    while continuer_jeu:
        print choix
	

        pygame.time.Clock().tick(30)
	
        if choix == 'n1':      
	   
	    for event in pygame.event.get():

		if event.type == QUIT:
		    continuer_jeu = 0
		    continuer = 0              
		    
		elif event.type == KEYDOWN :		

		    if event.key == K_ESCAPE:
			continuer_jeu = 0

		    #restart personnage     
		    if event.key == K_r:
			dk.x = 0
			dk.y = 0
			dk.case_x = 0
			dk.case_y = 0
			
		    if event.key == K_RIGHT:
			dk.deplacer('rien')
			dk.deplacer('droite')
		    if event.key == K_LEFT:
			dk.deplacer('rien')
			dk.deplacer('gauche')
		    if event.key == K_UP:		    		    		    
			dk.deplacer('end')
			print "saut en haut a droite"		    
			dk.deplacer('haut_droite')
		    if event.key == K_DOWN:
			print "saut en haut à gauche"		    
			dk.deplacer('rien')
			dk.deplacer('haut_gauche')
		
		else:
		    dk.deplacer('rien')

	    fenetre.blit(fond, (0,0))
	    dk.niveau.afficher(fenetre)
	    fenetre.blit(dk.direction, (dk.x, dk.y))
	    pygame.display.flip()
	    
	    
	elif choix == 'n2' :      #dk dans l'espace sans gravité
	   
	    for event in pygame.event.get():

		if event.type == QUIT:
		    continuer_jeu = 0
		    continuer = 0              
		    
		elif event.type == KEYDOWN :		

		    if event.key == K_ESCAPE:
			continuer_jeu = 0

		    #restart personnage     
		    if event.key == K_r:
			dk.x = 0
			dk.y = 0
			dk.case_x = 0
			dk.case_y = 0
			
		    if event.key == K_RIGHT:
			#dk.deplacer('rien')
			dk.deplacer('droite')
		    if event.key == K_LEFT:
			#dk.deplacer('rien')
			dk.deplacer('gauche')
		    if event.key == K_UP:		    		    		    
			dk.deplacer('end')
			print "saut en haut a droite"		    
			dk.deplacer('haut_droite_espace')
		    if event.key == K_DOWN:
			print "vers le bas"		    
			#dk.deplacer('rien')
			dk.deplacer('bas')
		    
		
		#else:
		    #dk.deplacer('rien')

	    fenetre.blit(fond, (0,0))
	    dk.niveau.afficher(fenetre)
	    fenetre.blit(dk.direction, (dk.x, dk.y))
	    pygame.display.flip()
	    
	elif choix == 'n3':      #dk dans l'eau lors d'un saut le personnage est freiné par l'eau
	   
	    for event in pygame.event.get():

		if event.type == QUIT:
		    continuer_jeu = 0
		    continuer = 0              
		    
		elif event.type == KEYDOWN :		

		    if event.key == K_ESCAPE:
			continuer_jeu = 0

		    #restart personnage     
		    if event.key == K_r:
			dk.x = 0
			dk.y = 0
			dk.case_x = 0
			dk.case_y = 0
			
		    if event.key == K_RIGHT:
			dk.deplacer('rien')
			dk.deplacer('droite')
		    if event.key == K_LEFT:
			dk.deplacer('rien')
			dk.deplacer('gauche')
		    if event.key == K_UP:		    		    		    
			dk.deplacer('end')
			print "saut en haut a droite"		    
			dk.deplacer('haut_droite_eau')
		    if event.key == K_DOWN:
			print "saut en haut à gauche"		    
			dk.deplacer('rien')
			dk.deplacer('haut_gauche_eau')
		
		else:
		    dk.deplacer('rien')

	    fenetre.blit(fond, (0,0))
	    dk.niveau.afficher(fenetre)
	    fenetre.blit(dk.direction, (dk.x, dk.y))
	    pygame.display.flip()	    	    

        if niveau.structure[dk.case_y][dk.case_x] == 'h':
	    choix= 'n2'
            fond = pygame.image.load(image_fond_haut)
            dk.niveau.degenerer()
            dk.niveau=Niveau('n2')
            dk.niveau.generer()
            dk.niveau.afficher(fenetre)
            dk.x=42*taille_sprite
            dk.y=24*taille_sprite
            dk.case_x = 39
            dk.case_y = 24

        if dk.niveau.structure[dk.case_y][dk.case_x] == 'b':
	    choix ='n3'
            fond = pygame.image.load(image_fond_bas)
            dk.niveau.degenerer()
            dk.niveau=Niveau('n3')
            dk.niveau.generer()
            dk.niveau.afficher(fenetre)
            dk.x=26*taille_sprite
            dk.y=0
            dk.case_x = 26
            dk.case_y = 0
