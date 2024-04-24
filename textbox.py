import pygame, os
from constants import COLORS

class Textbox(pygame.sprite.Sprite):

    def __init__(self, group, font:str, fontsize:int, text:str, position:dict, color:list=COLORS['white']):
        pygame.sprite.Sprite.__init__(self, group)
        self.font = pygame.font.Font(os.path.join(f"assets/fonts/{font}"), fontsize)
        self.color = color
        self.surf = self.font.render(text, True, self.color)
        self.rect = self.surf.get_rect()
        for p in position:
            direction = f"self.rect.{p} = {position[p]}"
            exec(direction)

    def updateText(self, text:str):
        self.surf = self.font.render(text, True, self.color)
        coords = self.rect.center
        self.rect = self.surf.get_rect(center=coords)