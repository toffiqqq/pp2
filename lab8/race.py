import pygame
import random
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GOLD = (255, 215, 0)

player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

coin_radius = 15
coin_x = random.randint(0, WIDTH - coin_radius)
coin_y = random.randint(0, HEIGHT - coin_radius)

score = 0

font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

def draw_player(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, player_width, player_height))

def draw_coin(x, y):
    pygame.draw.circle(screen, GOLD, (x, y), coin_radius)

def show_score(score):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (SCREEN_WIDTH - 150, 10))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_height:
        player_y += player_speed

    if (player_x < coin_x + coin_radius and player_x + player_width > coin_x and
        player_y < coin_y + coin_radius and player_y + player_height > coin_y):
        score += 1  
        coin_x = random.randint(0, WIDTH - coin_radius)
        coin_y = random.randint(0, HEIGHT - coin_radius)

    screen.fill(WHITE)

    draw_player(player_x, player_y)
    draw_coin(coin_x, coin_y)

    show_score(score)

    pygame.display.update()

    clock.tick(60)