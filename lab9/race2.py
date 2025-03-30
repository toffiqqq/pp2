import pygame
import random
import sys

pygame.init()

# Game constants
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GOLD = (255, 215, 0)
RED = (255, 0, 0)

# Player setup
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Coin setup
coin_radius = 15
coin_x = random.randint(0, WIDTH - coin_radius)
coin_y = random.randint(0, HEIGHT - coin_radius)
coin_weight = random.randint(1, 5)  # Coins have random weights

# Enemy setup
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, WIDTH - enemy_width)
enemy_y = 0
enemy_speed = 2

# Score and speed variables
score = 0
coins_collected = 0
N = 5  # After collecting 5 coins, enemy speed increases

font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

# Functions to draw objects
def draw_player(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, player_width, player_height))

def draw_coin(x, y, weight):
    pygame.draw.circle(screen, GOLD, (x, y), coin_radius)
    # Display the coin's weight on it
    weight_text = font.render(f"W:{weight}", True, BLACK)
    screen.blit(weight_text, (x, y))

def draw_enemy(x, y):
    pygame.draw.rect(screen, RED, (x, y, enemy_width, enemy_height))

def show_score(score):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (WIDTH - 150, 10))

def show_coins_collected(coins_collected):
    coins_text = font.render(f"Coins: {coins_collected}", True, BLACK)
    screen.blit(coins_text, (10, 10))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Player movement
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_height:
        player_y += player_speed

    # Collision detection with coin
    if (player_x < coin_x + coin_radius and player_x + player_width > coin_x and
        player_y < coin_y + coin_radius and player_y + player_height > coin_y):
        score += coin_weight  # Increase score by coin's weight
        coins_collected += 1
        coin_x = random.randint(0, WIDTH - coin_radius)
        coin_y = random.randint(0, HEIGHT - coin_radius)
        coin_weight = random.randint(1, 5)  # New random weight for the next coin

    # Increase enemy speed after collecting N coins
    if coins_collected >= N:
        enemy_speed = 4  # Increase enemy speed

    # Move enemy
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = 0  # Reset enemy to top once it goes off the screen
        enemy_x = random.randint(0, WIDTH - enemy_width)

    # Check for collision with enemy (if the player collides with the enemy, the game ends or resets)
    if (player_x < enemy_x + enemy_width and player_x + player_width > enemy_x and
        player_y < enemy_y + enemy_height and player_y + player_height > enemy_y):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw everything
    draw_player(player_x, player_y)
    draw_coin(coin_x, coin_y, coin_weight)
    draw_enemy(enemy_x, enemy_y)

    # Display the score and number of coins collected
    show_score(score)
    show_coins_collected(coins_collected)

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)