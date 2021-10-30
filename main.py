#importations 
import pygame as p
from pygame.locals import *
import random as r
import sys as s
import time as t

#definition des variables
hauteurjeu= 800
largeurjeu = 800
x_serp = hauteurjeu//2
y_serp = largeurjeu//2
dimension_serp = 10
mort = False

x=x_serp
y = y_serp
x_change = 0
y_change = 5
couleur = (223,190,131)
#logique de jeu
def jeu():
    looping = True
    p.init()
    font = p.font.SysFont(None,25)
    fen = p.display.set_mode((largeurjeu,hauteurjeu))
    p.display.set_caption('Jeu du python')
    fps = 30
    clock = p.time.Clock()
    serpent = Serpent(fen,x_serp,y_serp,largeurjeu,hauteurjeu,couleur)
    point = Points(r.randrange(0,largeurjeu-dimension_serp,10),r.randrange(0,hauteurjeu-dimension_serp,10),largeurjeu,hauteurjeu)
    serpent.placer_serp
    while looping:
            for event in p.event.get():
                    if event.type == p.QUIT:
                        looping = False
                        p.quit()
                        quit()
                    elif event.type == p.KEYDOWN:
                        if event.key == p.K_LEFT:
                            x_change = -5
                            y_change = 0
                        if event.key == p.K_RIGHT:
                            x_change = 5
                            y_change = 0
                        if event.key == p.K_UP:
                            y_change = -5
                            x_change = 0
                        if event.key == p.K_DOWN:
                            y_change = 5
                            x_change = 0
            serpent.mouvement(x,y,largeurjeu,hauteurjeu)                
            if x < 0 or x+dimension_serp/2  >= largeurjeu or y < 0 or y +dimension_serp/2  >= hauteurjeu:
                mort = True
                serpent.jeu_perdu()
                p.display.update()
                looping = False
                while mort:
                    for event in p.event.get():
                        if event.type == p.KEYDOWN:
                            if event.key == p.K_ESCAPE:
                                p.quit()
                                quit()
                            elif event.key == p.K_r:
                                mort = False
                                fen.fill((0,0,0))   
                                serpent.placer_serp(x_serp,y_serp,dimension_serp,dimension_serp)
                            
    
#objets
class Serpent():
    def __init__(self,fen,x_dep,y_dep,largeur,hauteur,couleur):
        self.fen = fen
        self.x_dep = x_dep
        self.y_dep = y_dep
        self.hauteur = hauteur
        self.largeur = largeur
        self.couleur = couleur
        
    def placer_serp(self,x_dep,y_dep,largeur,hauteur):
        p.draw.rect(self.fen,self.couleur,[self.x_dep,self.y_dep,self.largeur,self.hauteur])
        p.display.update()
        serpent.mouvement(self,self.x_dep,self.y_dep,self.largeur,self.hauteur)
                
    def mouvement(self,x,y,largeurbis,hauteurbis):
        self.fen.fill((0,0,0))     
        self.x = x
        self.y = y
        x += x_change
        y += y_change
        print(x," x")
        print("y ",y)    
        p.draw.rect(self.fen,self.couleur,[x,y,largeurbis,hauteurbis])
        p.display.update()
        clock.tick(fps)
            
    def jeu_perdu(self):
        txt = font.render("C'est Perdu!, Appuyer sur 'ESC' pour quitter et 'R' pour recommencer!",True,(220,122,139))
        self.fen.blit(txt,[x_serp,y_serp])
        
class Points():
    def __init__(self,pointx,pointy,largeur,hauteur):
        self.pointx = pointx
        self.pointy = pointy
        self.largeur = largeur
        self.hauteur = hauteur
        self.fen = p.display.set_mode((largeur,hauteur))
        
    def placer_point(self,largeur,hauteur):
        p.draw.rect(self.fen,(200,0,0),[self.pointx,self.pointy,largeur,hauteur])


jeu()


