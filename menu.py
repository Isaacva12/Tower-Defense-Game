import pygame
import os

class Button:
    def __init__(self,x,y, image, name):
        self.image = image
        self.name = name
        self.x = x
        self.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def click(self, X, Y):
        """
        devuelve si se selecciona la torre del menu o no
        :param X: int
        :param Y: int
        :return: bool
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
            return False

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))


class Menu:
    """
    Menu para seleccionar las torres
    """
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.width = image.get_width()
        self.height = image.get_height()
        self.towers_name = []
        self.towers = 0
        self.buttons = []
        self.background = image
        self.upgrade = 0
        self.image_upgrade = image
        self.towers_cost = []
        self.upgrade_cost = []

    def draw(self, win):
        """
        crea el menu y botones
        :param win: surface
        :return: None
        """
        win.blit(self.background, (self.x, self.y))
        for i in self.buttons:
            i.draw(win)

    def add_buttons_towers(self, image, name):
        """
        añadir los botones de las torres
        :param image: surface
        :param name: str
        :return: None
        """
        self.towers += 1
        dif_y = self.height/self.towers/3
        button_y = self.towers * dif_y - image.get_height()/3
        button_x = self.x + self.width/3 - image.get_width()/3
        self.buttons.append(Button(button_x, button_y, image, name))

    def add_buttons_upgrade(self, image_up, name):
        """
        añadir los botones de las torres
        :param image: surface
        :param name: str
        :return: None
        """
        self.upgrade += 1
        dif_x = self.width/self.upgrade/2
        button_x = self.x + self.upgrade * dif_x - image_up.get_width()
        button_y = self.y + self.height/2 - image_up.get_height()/2
        self.buttons.append(Button(button_x, button_y, image_up, name))

    def selected(self, X, Y):
        """
        devuelve el elemento seleccionado
        :param X: int
        :param Y: int
        :return: str
        """
        for button in self.buttons:
            if button.click(X,Y):
                return button.name
        return None
