#importations 
import pygame as p
from pygame.locals import *
import random as r
import time as t
p.init()

#definition des variables
hauteurjeu= 800
largeurjeu = 800
x_serp = hauteurjeu//2
y_serp = largeurjeu//2
dimension_serp = 10
font = p.font.SysFont(None,25)
score=0
mort = False
pointrandx = r.randrange(0,largeurjeu-dimension_serp,10)
pointrandy = r.randrange(0,hauteurjeu-dimension_serp,10)
liste_serp = []
longeur_serp = 1
#objets
class Serpent():
    def __init__(self,largeur,hauteur):
        self.hauteur = hauteur
        self.largeur = largeur
        self.fen = p.display.set_mode((largeur,hauteur))
        self.couleur = (92,160,101)
        p.display.set_caption('Jeu du python')
    def corps(self,largeurbis,hauteurbis,liste_serp):
        for elt in liste_serp:
            p.draw.rect(self.fen,self.couleur,[elt[0],elt[1],largeurbis,hauteurbis])
        
        
    def placer_serp(self,x_dep,y_dep,largeur,hauteur):
        p.draw.rect(self.fen,self.couleur,[x_dep,y_dep,largeur,hauteur])
        p.display.update()
        serpent.mouvement(x_dep,y_dep,largeur,hauteur)
                
    def mouvement(self,x,y,largeurbis,hauteurbis):
        global pointrandx,pointrandy,score,liste_serp,longeur_serp,mort
        x_change = 0
        y_change = 10
        looping = True
        print('1')
        fps = 10
        clock = p.time.Clock()
        self.x = x
        self.y = y
        while looping:
            for event in p.event.get():
                    if event.type == p.QUIT:
                        looping = False
                        p.quit()
                        quit()
                    elif event.type == p.KEYDOWN:
                        if event.key == p.K_LEFT:
                            x_change = -10
                            y_change = 0
                        if event.key == p.K_RIGHT:
                            x_change = 10
                            y_change = 0
                        if event.key == p.K_UP:
                            y_change = -10
                            x_change = 0
                        if event.key == p.K_DOWN:
                            y_change = 10
                            x_change = 0
            x += x_change
            y += y_change
            if x < 0 or x+dimension_serp/2  >= largeurjeu or y < 0 or y +dimension_serp/2  >= hauteurjeu:
                mort = True
                serpent.jeu_perdu()
                p.display.update()
            while mort:
                
                for event in p.event.get():
                    if event.type == p.KEYDOWN:
                        if event.key == p.K_ESCAPE:
                            p.quit()
                            quit()
                        elif event.key == p.K_r:
                            mort = False
                            self.fen.fill((0,0,0))
                            score=0
                            serp_initial = []
                            liste_serp =[]
                            longeur_serp =1
                            pointrandx = r.randrange(0,largeurjeu-dimension_serp,10)
                            pointrandy = r.randrange(0,hauteurjeu-dimension_serp,10)
                            point.placer_point(pointrandy,pointrandx,dimension_serp,dimension_serp)
                            serpent.placer_serp(x_serp,y_serp,dimension_serp,dimension_serp)
                    
            print(x," x")
            print("y ",y)
            print(pointrandx,"x point")
            print(pointrandy,"y point")
            if x == pointrandx and y == pointrandy:
                score+=1
                pointrandx = r.randrange(0,largeurjeu-dimension_serp,10)
                pointrandy = r.randrange(0,hauteurjeu-dimension_serp,10)
                longeur_serp += 1
                
            if score>5:
                 fps = 20
            self.fen.fill((39,41,54))
            serpent.score_handler()
            point.placer_point(pointrandy,pointrandx,dimension_serp,dimension_serp)
            
            serp_initial = []
            serp_initial.append(x)
            serp_initial.append(y)
            liste_serp.append(serp_initial)
            print(liste_serp,serp_initial)
            if len(liste_serp) > longeur_serp:
                del liste_serp[0]
            for corps in liste_serp[:-1]:
                if corps == serp_initial:
                    mort = True
                    serpent.jeu_perdu()
                    p.display.update()
            serpent.corps(largeurbis,hauteurbis,liste_serp)
            p.display.update()
            clock.tick(fps)
            
    def jeu_perdu(self):
        txt = font.render("C'est Perdu! Appuyer sur 'ESC' pour quitter et 'R' pour recommencer!",True,(220,122,139))
        self.fen.blit(txt,[x_serp/3,y_serp/3])
        
    def score_handler(self):
        txt2 = font.render("Score: " +str(score),True,(255,255,255))
        self.fen.blit(txt2,[10,10])
        
        
class Points():
    def __init__(self,largeur,hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.fen = p.display.set_mode((largeur,hauteur))
        
    def placer_point(self,pointy,pointx,largeur,hauteur):
        self.pointy = pointy
        self.pointx = pointx
        p.draw.rect(self.fen,(138,152,191),[self.pointx,self.pointy,largeur,hauteur])

serpent = Serpent(largeurjeu,hauteurjeu)
point = Points(largeurjeu,hauteurjeu)
serpent.placer_serp(x_serp,y_serp,dimension_serp,dimension_serp)
