import pygame
from player import Player
from enemy import Enemy
from bullet import PlayerBullet, EnemyBullet
import random

FPS = 30

# initialize
pygame.init()
screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)
background = pygame.image.load("assets/background.png")

# player sprite
player = Player("assets/ship.png", (400, 650))

# enemy sprite
enemy_x = list(range(250, 501, 50))
enemy_y = list(range(70, 171, 50))
enemy_list = []
for x in enemy_x:
    for y in enemy_y:
        enemy_list.append(Enemy("assets/enemy.png", (x, y)))

# grouping
all_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
p_bullet_group = pygame.sprite.Group()
e_bullet_group = pygame.sprite.Group()

all_group.add(player)
player_group.add(player)

for en in enemy_list:
    all_group.add(en)
    enemy_group.add(en)

# main loop
clock = pygame.time.Clock()
cnt = 0
running = True
while running:
    dt = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # receive key event
    pressed_key = pygame.key.get_pressed()

    # set background
    screen.blit(background, (0, 0))

    # set all object
    all_group.draw(screen)
    all_group.update(dt)

    # get current time tick
    now = pygame.time.get_ticks()

    # player shooting
    if pressed_key[pygame.K_SPACE]:
        if now - player.last_shoot > player.shoot_delay:
            player.last_shoot = now
            p_bullet = PlayerBullet("assets/player_bullet.png", player.rect.center)
            all_group.add(p_bullet)
            p_bullet_group.add(p_bullet)

    # enemy shooting
    if now % 10 == 0:
        cnt += 1
        if cnt % 5 == 0:
            cnt = 0
            random_enemy = random.choice(enemy_group.sprites())
            if now - random_enemy.last_shoot > random_enemy.shoot_delay:
                random_enemy.last_shoot = now
                e_bullet = EnemyBullet("assets/enemy_bullet.png", random_enemy.rect.center)
                all_group.add(e_bullet)
                e_bullet_group.add(e_bullet)

    # bullet collision
    pygame.sprite.groupcollide(enemy_group, p_bullet_group, True, True)
    is_game_over = pygame.sprite.groupcollide(player_group, e_bullet_group, True, True)
    if is_game_over:
        running = False

    pygame.display.flip()

pygame.quit()