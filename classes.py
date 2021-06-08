#-*- coding: utf-8 -*- # codage des accents


"""Classes du jeu de Labyrinthe Donkey Kong"""
# -*- coding: cp1252 -*-

import time
import pygame
from pygame.locals import * 
from constantes import *

class Niveau:
	"""Classe permettant de creer un niveau"""
	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = 0
	
	
	def generer(self):
		"""Méthode permettant de générer le niveau en fonction du fichier.
		On crée une liste générale, contenant une liste par ligne à afficher"""	
		#On ouvre le fichier
		with open(self.fichier, "r") as fichier:
			structure_niveau = []
			#On parcourt les lignes du fichier
			for ligne in fichier:
				ligne_niveau = []
				#On parcourt les sprites (lettres) contenus dans le fichier
				for sprite in ligne:
					#On ignore les "\n" de fin de ligne
					if sprite != '\n':
						#On ajoute le sprite à la liste de la ligne
						ligne_niveau.append(sprite)
				#On ajoute la ligne à la liste du niveau
				structure_niveau.append(ligne_niveau)
			#On sauvegarde cette structure
			self.structure = structure_niveau
			
	def degenerer(self):
                #On ouvre le fichier
		with open(self.fichier, "r") as fichier:
			structure_niveau = []
			#On parcourt les lignes du fichier
			for ligne in fichier:
				ligne_niveau = []
				#On parcourt les sprites (lettres) contenus dans le fichier
				for sprite in ligne:
					#On ignore les "\n" de fin de ligne
					if sprite != '\n':
						#On ajoute le sprite à la liste de la ligne
						ligne_niveau.append(0)
				#On ajoute la ligne à la liste du niveau
				structure_niveau.append(ligne_niveau)
			#On sauvegarde cette structure
			self.structure = structure_niveau
                
	
	def afficher(self, fenetre):
		"""Méthode permettant d'afficher le niveau en fonction 
		de la liste de structure renvoyée par generer()"""
		#Chargement des images (seule celle d'arrivée contient de la transparence)
		feuille = pygame.image.load(image_feuille).convert()
		depart = pygame.image.load(image_depart).convert()
		arrivee = pygame.image.load(image_arrivee).convert_alpha()
		planete = pygame.image.load(image_planete).convert_alpha()
		vortex = pygame.image.load(image_vortex).convert()


		
		#On parcourt la liste du niveau
		num_ligne = 0
		for ligne in self.structure:
			#On parcourt les listes de lignes
			num_case = 0
			for sprite in ligne:
				#On calcule la position réelle en pixels
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				if sprite == 'm':		   #m = feuille
					fenetre.blit(feuille,(x,y))
				elif sprite == 'd':		   #d = Départ
					fenetre.blit(depart,(x,y))
				elif sprite == 'a':		   #a = Arrivée
					fenetre.blit(arrivee,(x,y))
				elif sprite == 's':                #s = planete
                                        fenetre.blit(planete,(x,y))
                                elif sprite == 'h':                #h/g/b/d/v = vortex
                                        fenetre.blit(vortex,(x,y))
                                elif sprite == 'g':
                                        fenetre.blit(vortex,(x,y))
                                elif sprite == 'd':
                                        fenetre.blit(vortex,(x,y))
                                elif sprite == 'b':
                                        fenetre.blit(vortex,(x,y))
                                elif sprite == 'v':
                                        fenetre.blit(vortex,(x,y))
                                        
                                num_case += 1
			num_ligne += 1
			
			
class Perso:
	"""Classe permettant de créer un personnage"""
	def __init__(self, droite, gauche, haut, bas, niveau):
		#Sprites du personnage
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()
		#Position du personnage en cases et en pixels
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		#Direction par défaut
		self.direction = self.droite
		#Niveau dans lequel le personnage se trouve 
		self.niveau = niveau
	
	
	def deplacer(self, direction):
		"""Methode permettant de déplacer le personnage"""
                pygame.time.Clock().tick(300000)
                
		#Simulation gravité
		if direction == 'rien':
                    b = True
		    if direction == 'end':
			b= False
		    print "gravite"                   
                    while b:
                            
                        if self.case_y > 23:
                            b = False
                            
                        elif  self.niveau.structure[self.case_y+1][self.case_x] =='v' or self.niveau.structure[self.case_y+1][self.case_x] == 'b':
                            self.case_y += 1
                            self.y = self.case_y * taille_sprite

                        elif self.niveau.structure[self.case_y+1][self.case_x]=='0':
                            self.case_y += 1
                            self.y = self.case_y * taille_sprite
                            
                        else :
                            b = False          
                        self.direction = self.bas

                         
		    

		
		#Déplacement vers la droite
		if direction == 'droite':
			#Pour ne pas dépasser l'écran
			if self.case_x < (nombre_sprite_cote - 1):
				#On vérifie que la case de destination n'est pas un mur ou un asteroide
				if self.niveau.structure[self.case_y][self.case_x+1] != 'm'and self.niveau.structure[self.case_y][self.case_x+1] != 's':
					#Déplacement d'une case
					self.case_x += 1
					#Calcul de la position "réelle" en pixel
					self.x = self.case_x * taille_sprite
			#Image dans la bonne direction
			self.direction = self.droite
		
		#Déplacement vers la gauche
		if direction == 'gauche':
			if self.case_x > 0:
				if self.niveau.structure[self.case_y][self.case_x-1] != 'm'and self.niveau.structure[self.case_y][self.case_x-1] != 's':
					self.case_x -= 1
					self.x = self.case_x * taille_sprite
			self.direction = self.gauche
		
		#Déplacement vers le haut
		if direction == 'haut_droite':
		    if self.case_y > 0 and self.case_x <= nombre_sprite_cote and self.case_x>=0 and self.case_y<=nombre_sprite_haut:
		        if self.niveau.structure[self.case_y-1][self.case_x] != 'm'and self.niveau.structure[self.case_y-1][self.case_x] != 's':
			    self.case_y -=1
			    self.y = self.case_y * taille_sprite
			    self.case_x += 1		
			    self.x = self.case_x * taille_sprite			    			    
		        self.direction = self.haut
			
		if direction == 'haut_gauche':
		    if self.case_y > 0 and self.case_x <= nombre_sprite_cote and self.case_x>=0 and self.case_y<=nombre_sprite_haut:
		        if self.niveau.structure[self.case_y-1][self.case_x] != 'm'and self.niveau.structure[self.case_y-1][self.case_x] != 's':
			    self.case_y -=1
			    self.y = self.case_y * taille_sprite
			    self.case_x -= 1		
			    self.x = self.case_x * taille_sprite			    			    
		        self.direction = self.haut	
			
			
		if direction == 'haut_gauche_eau':
		    if self.case_y > 0 and self.case_x <= nombre_sprite_cote and self.case_x>=0 and self.case_y<=nombre_sprite_haut:
		        if self.niveau.structure[self.case_y-1][self.case_x] != 'm'and self.niveau.structure[self.case_y-1][self.case_x] != 's':
			    self.case_y -=2
			    self.y = self.case_y * taille_sprite
			    self.case_x -= 1		
			    self.x = self.case_x * taille_sprite			    			    
		        self.direction = self.haut			
			
		if direction == 'haut_droite_espace':
		    if self.case_y > 0 and self.case_x <= nombre_sprite_cote and self.case_x>=0 and self.case_y<=nombre_sprite_haut:
		        if self.niveau.structure[self.case_y-1][self.case_x] != 'm'and self.niveau.structure[self.case_y-1][self.case_x] != 's':
			    self.case_y -=1
			    self.y = self.case_y * taille_sprite			    			    			    
		        self.direction = self.haut
			
		if direction == 'haut_droite_eau':
		    if self.case_y > 0 and self.case_x <= nombre_sprite_cote and self.case_x>=0 and self.case_y<=nombre_sprite_haut:
		        if self.niveau.structure[self.case_y-1][self.case_x] != 'm'and self.niveau.structure[self.case_y-1][self.case_x] != 's':
			    self.case_y -=2
			    self.y = self.case_y * taille_sprite
			    self.case_x += 1		
			    self.x = self.case_x * taille_sprite			    			    
		        self.direction = self.haut
			
		if direction == 'bas':
                    if self.case_y < 23:
                        if self.niveau.structure[self.case_y+1][self.case_x] != 'm'and self.niveau.structure[self.case_y+1][self.case_x] != 's':
                                self.case_y += 1
                                self.y = self.case_y * taille_sprite
                        self.direction = self.bas				
			
			
									                                        
			
	def replacer ( self, abcisse, ordonnee ):
                """ Méthode permettant de replacer le personnage au bon endroit"""
                self.case_x = abcisse
		self.case_y = ordonnee
		self.x = self.case_x * taille_sprite
		self.y = self.case_y * taille_sprite
		

                
