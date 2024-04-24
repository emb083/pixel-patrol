import pygame, os, uuid
from constants import WIDTH, HEIGHT

class Entity:
    
    def __init__(self, type:str, sprite:str, sprite_scale:float=1, mvmt_speed:float=0.2):
        self.id = uuid.uuid4()
        self.type = type
        self.sprite_scale = sprite_scale
        self.base_sprite = sprite
        self.current_sprite = sprite
        self.mvmt_speed = mvmt_speed

        self.surf = pygame.image.load(os.path.join(f"assets/{self.type}", sprite))
        self.surf = pygame.transform.scale_by(self.surf, self.sprite_scale)
        self.rect = self.surf.get_rect()
    
    # getters and setters

    @property
    def type(self) -> str:
        return self._type
    
    @type.setter
    def type(self, new_type:str) -> None:
        if new_type in ['player', 'alien', 'bullet']:
            self._type = new_type
        else:
            self._type = 'alien'

    @property                                               # mvmt_speed
    def mvmt_speed(self) -> float:
        return self._mvmt_speed
    
    @mvmt_speed.setter
    def mvmt_speed(self, new_mvmt_speed:float) -> None:
        if new_mvmt_speed > 0:
            self._mvmt_speed = new_mvmt_speed
        else:
            self._mvmt_speed = 0.2
    
# other methods
            
    def goLeft(self, tick:int):
        self.rect.x -= self.mvmt_speed*tick
        if self.rect.left < 0:
            self.rect.left = 0

    def goRight(self, tick:int):
        self.rect.x += self.mvmt_speed*tick
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def goUp(self, tick:int):
        self.rect.y -= self.mvmt_speed*tick
        if self.rect.top < 0:
            self.rect.top = 0

    def goDown(self, tick:int):
        self.rect.y += self.mvmt_speed*tick
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def updateSprite(self, sprite:str):
        self.surf = pygame.image.load(os.path.join(f"assets/{self.type}", sprite))
        self.surf = pygame.transform.scale_by(self.surf, self.sprite_scale)
        coords = self.rect.center
        self.rect = self.surf.get_rect(center=coords)
        self.current_sprite = sprite

    def resetSprite(self):
        self.updateSprite(self.base_sprite)