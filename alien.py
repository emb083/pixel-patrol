import pygame
from random import randint, choice
from constants import WIDTH, HEIGHT
from entity import Entity

class Alien(pygame.sprite.Sprite, Entity):

    def __init__(self, group, difficulty:int) -> None:
        if difficulty == 0:
            mvmt_speed = 0.05
        else:
            mvmt_speed = (difficulty*0.05)+0.1
        pygame.sprite.Sprite.__init__(self, group)
        Entity.__init__(self, "alien", "walk-1.png", 0.625, mvmt_speed)
        self.rect.right = randint(600, WIDTH-25)
        self.direction = choice(['up', 'down'])
        match self.direction:
            case "up": self.rect.top = HEIGHT
            case "down": self.rect.bottom = 0

    def goDown(self, tick:int):
        self.rect.y += self.mvmt_speed*tick
        if self.rect.top >= HEIGHT:
            self.kill()
            return True
        return False
    
    def goUp(self, tick:int):
        self.rect.y -= self.mvmt_speed*tick
        if self.rect.bottom <= 0:
            self.kill()
            return True
        return False
    
    def move(self, tick:int):
        if self.direction == "up":
            hitwall = self.goUp(tick)
        elif self.direction == "down":
            hitwall = self.goDown(tick)
        return hitwall