class Game:

    def __init__(self) -> None:
        self.difficulty = 0
        self.score = 0
        self.lives = 3
        self.current_animations = {}
        self.enemy_delay = 0
        self.current_enemy = False
        self.enemies_sent = 0
        self.gameover = False

    # getters and setters
    @property
    def lives(self) -> int:
        return self._lives
    
    @lives.setter
    def lives(self, new_lives:int) -> None:
        if new_lives > 0:
            self._lives = new_lives
        else:
            self._lives = 0 # no negatives
            self.current_animations.clear() # stop all running animations
            self.current_enemy = True # make sure no new enemies spawn

    @property
    def enemies_sent(self) -> int:
        return self._enemies_sent
    
    @enemies_sent.setter
    def enemies_sent(self, new_enemies_sent:int) -> None:
        self._enemies_sent = new_enemies_sent
        if new_enemies_sent%5 == 0 and new_enemies_sent!=0:
            self.difficulty += 1