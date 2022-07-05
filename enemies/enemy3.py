import pygame
import os
from .enemies import Enemies

images = []

# recorre las imagenes del enemigo para dar mobilidad
for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    images.append(pygame.transform.scale(
        pygame.image.load(os.path.join("enemies/3", "10_enemies_1_run_0" + add_str + ".png")), (90, 90)))

class Enemy3(Enemies):
    def __init__(self):
        super().__init__()
        self.gems = 20
        self.images = images[:]
        self.max_health = 9
        self.health = self.max_health

