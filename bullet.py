import pygame
from constants import WIDTH, SOUNDS
from entity import Entity

class Bullet(pygame.sprite.Sprite, Entity):

    def __init__(self, group, position:tuple) -> None:
        pygame.sprite.Sprite.__init__(self, group)
        Entity.__init__(self, "bullet", "bullet.png", 2.2, .625)
        self.rect.left = position[0]
        self.rect.centery = position[1]

    def goRight(self, tick:int):
        self.rect.x += self.mvmt_speed*tick
        # return if hit wall
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
            return True
        return False