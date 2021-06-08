#-*- coding: utf-8 -*- # codage des accents
from __future__ import division # division flottante par défaut


# LES IMPORTATIONS DE MODULES EXTERNES

import time
import math
import random

from visual import *
from visual.graph import *

###Simulation d'un mouvement dans un champ de gravité uniforme
###Doit retourner un tableau contenant les positions
### A la fin, la classe doit reperer les coordonées entieres pour les attribuer au personage
### on se limite à un saut de 2 Sprites de longueurs et 2 sprites de hauteur max
### Bien sur il ne faut pas que le personnnage traverse les briques lors d'un saut
### de ce fait, les niveaux seront donc limités


	
def main():
	
	
#Données
	#d=input("Durée voulue de la simulation en s :")
	#delta_t=input("Pas temporel de la simulation :")	#pas temporel de la simulation
	t=0.0	#Temps lié à la simulation en s
	delta_t=0.01
	

	m=15.0		#masse en kilogramme
	alpha=45	#Angle en degres
	
	
	alpha=alpha*2*pi
	alpha=alpha/360				#Angle en radians
	g=9.81			# G en m/s²
	k=1.6		# A en kg/s
	Vo=9          #("Norme vitesse initiale en m/s :")
	
#Position initiale
	y0=self.case_y
	x0=self.case_x
	x=self.x
	y=self.y
	a=True
	
	
	dx=0.01  #Pas spatial de la simulation
	
#Vitesse initiale

	vx0=Vo*cos(alpha)
	vy0=Vo*sin(alpha)
	
#Fin des paramètres de la simulation


	numPoint=0
	## Monitoring lié au tracé du graph
	
	
	#c00=gcurve(color=color.white)		#Courbe y(x) sans frottements
	c22=gcurve(color=color.blue)		#Courbe y(x) avec frottements
	pos_y22=array([x,y22])				#Tableau contenant les positions

######## Début simulation

	while a:		
			
		numPoint=numPoint +1			
		t=t+delta_t
		x=x+dx
		
		#Equation sans frottements y(x)
		#y00=-((g)/(2*vx0**2))*x*x +tan(alpha)*x+y0
		
		#Equation y(x) avec frottements
		if  (x*k)/(vx0*m) >1:
			y22=0
		elif 1- (x*k)/(vx0*m) >0:
				
			y22=(m/k)**2 * g *log(1- (x*k)/(vx0*m)) +( (m/k)**2 * g +(m*vy0/k) )*( (x*k)/(vx0*m))

		#Affichage des points de la courbes pour les différents cas
				
		#pos_y00=array([x,y00])
		pos_y22=array([x,y22])

		
		### Tracé des graphs
		#1- graphs liés à la position ne gardant que les coordonnées positives
		
		if y22>=0:						
			c22.plot(pos=(x,y22))				
		
		#if y00>=0:				
			#c00.plot(pos=(x,y00))
			
		#2- graphs liés au temps			

		
		print "Positions en mètres :"
		print "Cas sans frottements fluides :" , pos_y00
		print "Cas avec frottements fluides :" , pos_y22
		#print "---------------------------"
		print "Hauteur en fonction du temps :"
		#print "Cas sans frottements fluides :" , pos_y11
		#print "Cas avec frottements fluides :" , pos_y12	
		print "point numéro ",numPoint	
		print "---------------------------"
		print "---------------------------"	      
		
		if y00 <=0 :
			a=False
			
		#if y11 <= 0 and y12<=0:
			a=False
		
        
        # préparation de l'itération suivante       
        x0,y0 = x,y    
        
        
	#Fin de la boucle de simulation
	
	print "FIN DU CALCUL"
	print "Nombre de points calculés :" , numPoint
		
main()
