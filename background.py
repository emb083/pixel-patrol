import pygame, os

class Background:

    def __init__(self, image:str) -> None:
        self.surf = pygame.image.load(os.path.join('assets/bgs', image))
        self.rect = self.surf.get_rect()
        self.rect.topleft = (0, 0)

    def change_bg(self, new_image:str) -> None:
        self.__init__(self, new_image)