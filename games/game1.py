import pygame
from pygame.locals import *
import os
import sys
from enemies.enemy1 import Enemy1
from enemies.enemy2 import Enemy2
from enemies.enemy3 import Enemy3
from towers.tower1 import Tower1
from towers.tower2 import Tower2
from towers.tower3 import Tower3
from menus.in_game_menu import BuyMenu
import time
import random

pygame.init()
lifes_image = pygame.transform.scale(pygame.image.load(os.path.join("buttons_symbols", "heart-icon2.png")), (40,40))
gems_image = pygame.transform.scale(pygame.image.load(os.path.join("buttons_symbols", "gemas.png")), (40,40))
background_menu = pygame.transform.scale(pygame.image.load(os.path.join("buttons_symbols", "wood_menu.png")), (150, 250))
buy_tower1 = pygame.transform.scale(pygame.image.load(os.path.join("towers/1/shoot_002.png")), (70, 70))
buy_tower2 = pygame.transform.scale(pygame.image.load(os.path.join("towers/2/fire_002.png")), (70, 70))
buy_tower3 = pygame.transform.scale(pygame.image.load(os.path.join("towers/3/stone_002.png")), (70, 70))


class Juego:
    def __init__(self):
        self.width = 1200
        self.height = 650
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = [Enemy3()]
        self.towers = [Tower1(250,300), Tower2(500,250), Tower3(850, 500)]
        self.lifes = 50
        self.gems = 800
        self.background = pygame.image.load(os.path.join("maps/mapa1.jpg"))
        self.menu = BuyMenu(1050, 0, background_menu)
        self.menu.add_buttons_towers(buy_tower1, "buy_tower1", 500)
        self.menu.add_buttons_towers(buy_tower2, "buy_tower2", 600)
        self.menu.add_buttons_towers(buy_tower3, "buy_tower3", 800)
        self.timer = time.time()
        self.text = pygame.font.Font("freesansbold.ttf", 32)
        self.selected_tower = None

        #self.clicks = [] #se puede borrar, era para crear el camino de los enemmigos

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            if time.time() - self.timer >= random.randrange(1,5)/2:
                self.timer = time.time()
                self.enemies.append(random.choice([Enemy1(), Enemy2(), Enemy3()]))
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_clicked = None
                    if self.selected_tower:
                        button_clicked = self.selected_tower.menu.selected(pos[0], pos[1])
                        if button_clicked:
                            if button_clicked == "Upgrade":
                                cost = self.selected_tower.get_upgrade_cost()
                                if self.gems >= cost:
                                    self.gems -= cost
                                    self.selected_tower.upgrade()
                    if not(button_clicked):
                        for tower in self.towers:
                            if tower.click(pos[0], pos[1]):
                                tower.selected = True
                                self.selected_tower = tower
                            else:
                                tower.selected = False
                 #   self.clicks.append(pos)
                  #  print(self.clicks)  #se puuede borrar es para crear camino enemigos

            #terminar loop y eliminar enemigos y vidas
            to_del = []
            for enemy in self.enemies:
                if enemy.y < -15:
                    to_del.append(enemy)
            for d in to_del:
                self.lifes -= 1
                self.enemies.remove(d)

            #terminar loop torres
            for tower in self.towers:
                self.gems += tower.attack(self.enemies)

            #si se pierde
            if self.lifes <= 0:
                print("GAME OVER")
                run = False

            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.background, (0,0))
        #for p in self.clicks:
         #   pygame.draw.circle(self.win, (255,0,0), (p[0], p[1]), 5, 0) #se puede borrar era para crear camino enemigos

       #dibujar torres
        for tower in self.towers:
            tower.draw(self.win)

        #dibujar enemigos
        for enemy in self.enemies:
            enemy.draw(self.win)

        #dibujar vidas
        life = lifes_image
        self.win.blit(life, (20, 10))
        value_life = self.text.render(str(self.lifes), 1, (255,255,255))
        self.win.blit(value_life, (65,18))

        #dibujar gemas
        gems = gems_image
        self.win.blit(gems, (120, 10))
        value_gems = self.text.render(str(self.gems), 1, (255, 255, 255))
        self.win.blit(value_gems, (170, 18))

        #dibujar menu
        self.menu.draw(self.win)

        pygame.display.update()

    def towers_menu(self):
        pass



#j = Juego()
#j.run()
