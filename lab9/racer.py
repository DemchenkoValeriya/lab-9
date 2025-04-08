# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initializing
pygame.init()

# FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 3
SCORE = 0
COINS = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 15)
font_small = pygame.font.SysFont("Verdana", 15)
game_over = font.render("Game Over. Press SPACE to Restart or ESC to Quit", True, BLACK)

background = pygame.image.load("C:\\Users\\User\\Desktop\\lab8\\AnimatedStreet.png")

# Create a white screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("Racer")

# Speed upgrade checkpoints
c1, c2, c3, c4, c5 = False, False, False, False, False

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\User\\Desktop\\lab8\\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\User\\Desktop\\lab8\\coin.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))

    def move(self):
        global COINS, SPEED, c1, c2, c3, c4, c5
        # Adding coins depending on height
        if self.rect.bottom < SCREEN_HEIGHT // 3:
            COINS += 3
        elif self.rect.bottom < SCREEN_HEIGHT // 1.5:
            COINS += 2
        else:
            COINS += 1

        # Increase SPEED after collecting coins
        if not c1 and COINS >= 10:
            SPEED += 1
            c1 = True
        if not c2 and COINS >= 20:
            SPEED += 1
            c2 = True
        if not c3 and COINS >= 30:
            SPEED += 1
            c3 = True
        if not c4 and COINS >= 40:
            SPEED += 1
            c4 = True
        if not c5 and COINS >= 50:
            SPEED += 1
            c5 = True

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\User\\Desktop\\lab8\\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if self.rect.top > 0 and pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT and pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coinss = pygame.sprite.Group()
coinss.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

def reset_game():
    global SCORE, COINS, SPEED, c1, c2, c3, c4, c5
    SCORE = 0
    COINS = 0
    SPEED = 3
    c1 = c2 = c3 = c4 = c5 = False
    P1.rect.center = (160, 520)
    for enemy in enemies:
        enemy.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    for coin in coinss:
        coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))

def game_over_screen():
    screen.fill(RED)
    screen.blit(game_over, (10, 250))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:  # Restart
                    reset_game()
                    return
                elif event.key == K_ESCAPE:  # Quit
                    pygame.quit()
                    sys.exit()

background_y = 0  # Initialize background scroll

# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.1
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Scroll the background
    background_y = (background_y + SPEED) % background.get_height()
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y - background.get_height()))

    # Display scores
    scores = font_small.render(str(SCORE), True, BLACK)
    screen.blit(scores, (10, 10))
    coins = font_small.render(str(COINS), True, BLACK)
    screen.blit(coins, (370, 10))

    # Move player
    P1.move()

    # Move and draw all sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    # Move enemies
    for enemy in enemies:
        enemy.move()

    # Move coins (down)
    for coin in coinss:
        coin.rect.y += SPEED
        if coin.rect.top > SCREEN_HEIGHT:
            coin.rect.y = -coin.rect.height
            coin.rect.x = random.randint(40, SCREEN_WIDTH - 40)

    # Check for collision: Player vs Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        game_over_screen()

    # Check for collision: Player vs Coin
    coin_hit_list = pygame.sprite.spritecollide(P1, coinss, True)
    for coin in coin_hit_list:
        coin.move()  # add coins to score
        new_coin = Coin()
        coinss.add(new_coin)
        all_sprites.add(new_coin)

    pygame.display.update()
    FramePerSec.tick(FPS)
