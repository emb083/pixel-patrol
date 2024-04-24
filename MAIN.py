import pygame, os
from alien import Alien
from animations import Animation
from background import Background
from bullet import Bullet
from constants import *
from game import Game
from player import Player
from textbox import Textbox

# Initialize pygame library and display
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pixel Patrol: Alien Onslaught')
icon = pygame.image.load(os.path.join(f"assets/alien", "death-2.png"))
pygame.display.set_icon(icon)

# setup music
pygame.mixer.init()
pygame.mixer.music.load(os.path.join("assets/sounds", 'music.wav'))
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

sprites = pygame.sprite.Group() # Create sprites group
aliens = pygame.sprite.Group() # Create aliens group
bullets = pygame.sprite.Group() # Create bullets

player = Player(sprites) # Create a player object
clock = pygame.time.Clock() # Create clock for framerate
bg = Background("world-1.jpg") # Create background
g = Game() # Create game object to track game variables

# setup player gui elements
guiScore = Textbox(sprites, "PressStart2P-Regular.ttf", 20, f"Score: 0", {"top":15, "centerx":WIDTH/2})
guiLives = Textbox(sprites, "PressStart2P-Regular.ttf", 20, f"Lives: 3", {"bottom":HEIGHT-15,"centerx":WIDTH/2})

RUNNING = True  # A variable to determine whether to get out of the infinite game loop

# gameloop variables:

while (RUNNING):
    tick = clock.tick(FRAMERATE)
    
    # Look through all the events that happened in the last frame to see
    # if the user tried to exit.
    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE):
            RUNNING = False
        elif (event.type == QUIT):
            RUNNING = False
        elif (event.type == KEYDOWN and event.key == K_SPACE) and g.gameover is False:
            # shoot animation
            createBullet = lambda group, position: Bullet(group, position)
            playerShoot = Animation(player, "shoot", [1, 2, 3, 4, 5, "trigger", 6, 2, 1], 4, trigger=lambda group, position: Bullet(group, position), trigger_data=((sprites, bullets), player.getBulletPosition()))
            g.current_animations[f"{player.id}.shoot"] = playerShoot
            
            # play sound
            SOUNDS['shoot'].set_volume(0.3)
            SOUNDS['shoot'].play()

    if len(g.current_animations) > 0:
        # loop through all currently running animations
        for animation_key in g.current_animations.copy():
            animation = g.current_animations[animation_key]
            if animation.animationDelay > animation.framerate:
                # if it's time to go to the next frame, update
                finish = animation.updateAnimation()
                animation.animationDelay = 0
                if finish:
                    # remove animation and reset to original sprite if animation done
                    g.current_animations.pop(animation_key)
                    animation.target.resetSprite()
            else:
                # if too early to switch frames, tick timer
                animation.animationDelay += tick

    # check if time to bring in next enemy
    if g.enemy_delay > ENEMY_DELAY and g.current_enemy is False:
        # if yes, create one and reset timer
        enemy = Alien((sprites, aliens), g.difficulty)
        alienWalk = Animation(enemy, "walk", [1, 2], 256, True)
        g.current_animations[f"{enemy.id}.walk"] = alienWalk
        g.enemy_delay = 0
        g.current_enemy = True
        g.enemies_sent += 1
    else:
        # if not, tick timer
        g.enemy_delay += tick

    # if enemy on screen, reset timer and move enemy downwards
    if g.current_enemy: # if enemy on screen,
        for alien in aliens: # move moving-aliens downward
            missed = alien.move(tick) # check if the alien's gone off-screen
            g.enemy_delay = 0 # and reset timer
            if missed:
                g.lives -= 1 # update counter
                guiLives.updateText(f"Lives: {g.lives}") # update screen
                SOUNDS['lose-life'].play() # play sound
                if g.lives == 0:
                    # game over
                    g.gameover = True
                    sprites.empty() # get rid of all sprites

                    gameover = Textbox(sprites, "PressStart2P-Regular.ttf", 65, "GAME OVER", {"centerx":WIDTH/2, "centery":(HEIGHT/2)-75})
                    finalScore = Textbox(sprites, "PressStart2P-Regular.ttf", 35, f"Final score: {g.score}", {"centerx":WIDTH/2, "centery":(HEIGHT/2)+75})
        if aliens.has(enemy) is False: # if enemy is non-moving
            if f"{enemy.id}.walk" in g.current_animations.keys(): # stop walking animation if it's still running
                g.current_animations.pop(f"{enemy.id}.walk")
                enemy.resetSprite()
        if sprites.has(enemy) is False and g.gameover is False: # if enemy has been .kill()'d and it isn't gameover,
            g.current_enemy = False # then there are no more enemies on screen

    for bullet in bullets:
        hitAnimation = Animation(bullet, 'hit', [1,2,3,4,4,"trigger"], 4, trigger=lambda bullet: bullet.kill(), trigger_data=[bullet])
        hitWall = bullet.goRight(tick) # move all bullets on the screen
        if hitWall: # if the bullet hits the wall,
            bullets.remove(bullet) # remove the bullets from the moving-bullets group
            g.current_animations[f"{bullet.id}.hit"] = hitAnimation # start hit animation
            SOUNDS['hit'].set_volume(0.5)
            SOUNDS['hit'].play() # play sound
        else:
            for alien in aliens: # for any aliens on screen
                if bullet.rect.colliderect(alien.rect): # if it hits the alien
                    g.score += 1 # increase score
                    guiScore.updateText(f"Score: {g.score}")

                    bullets.remove(bullet) # remove the bullets from the moving-bullets group
                    g.current_animations[f"{bullet.id}.hit"] = hitAnimation # start hit animation
                    SOUNDS['hit'].set_volume(0.5)
                    SOUNDS['hit'].play() # play sound

                    aliens.remove(alien) # remove alien from moving-aliens group
                    deathAnimation = Animation(alien, 'death', [1,1,1,2,2,3,4,5,5,"trigger"], 50, trigger=lambda alien: alien.kill(), trigger_data=[alien]) # start alien death animation
                    g.current_animations[f"{alien.id}.death"] = deathAnimation
                    SOUNDS['alien-death'].play() # play sound

    # Collect user input and update
    pressedKeys = pygame.key.get_pressed()
    player.update(pressedKeys, tick)

    # Paste stuff onto screen
    screen.blit(bg.surf, bg.rect)
    for entity in sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()