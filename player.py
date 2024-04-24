import pygame
from constants import HEIGHT, K_UP, K_DOWN, K_SPACE
from entity import Entity

class Player(pygame.sprite.Sprite, Entity):
    
    def __init__(self, group) -> None:
        pygame.sprite.Sprite.__init__(self, group)
        Entity.__init__(self, "player", "stand.png", mvmt_speed=0.4)
        self.rect.left = 25
        self.rect.centery = HEIGHT/2

    def update(self, pressed:dict, fps:int) -> None:
        global SPACE_PRESSABLE
        if pressed[K_UP]:
            self.goUp(fps)
        if pressed[K_DOWN]:
            self.goDown(fps)
        if pressed[K_SPACE]:
            if SPACE_PRESSABLE:
                SPACE_PRESSABLE = False
        else:
            SPACE_PRESSABLE = True

    def getBulletPosition(self) -> tuple:
        # return beginning position for bullet, accounting for sprite line-up
        return (self.rect.right, self.rect.centery-13)