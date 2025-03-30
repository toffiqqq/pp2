import pygame
import random
import sys
import time

pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Snake parameters
snake_block = 20
snake_speed = 15  # Initial snake speed
snake_color = GREEN

# Initial snake position
snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'
change_to = snake_direction

# Variables for food
food_pos = [random.randrange(1, (WIDTH // snake_block)) * snake_block,
            random.randrange(1, (HEIGHT // snake_block)) * snake_block]
food_spawn = True
food_weight = random.randint(1, 5)  # Random food weight (from 1 to 5 points)
food_timer = time.time()  # Timer for food

# Score and level
score = 0
level = 1

# Fonts for text display
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Clock
clock = pygame.time.Clock()

# Function to display the score and level
def display_score(score, level):
    value = score_font.render("Score: " + str(score), True, BLACK)
    screen.blit(value, [0, 0])
    level_text = font_style.render("Level: " + str(level), True, BLACK)
    screen.blit(level_text, [WIDTH - 120, 0])

# Function to draw the snake
def draw_snake(snake_block, snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, snake_color, pygame.Rect(block[0], block[1], snake_block, snake_block))

# Function to draw the food
def draw_food(food_pos, food_weight):
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], snake_block, snake_block))
    # Display the food's weight
    weight_text = font_style.render(f"W:{food_weight}", True, BLACK)
    screen.blit(weight_text, [food_pos[0], food_pos[1]])

# Function to end the game
def game_over():
    game_over_message = font_style.render("Game Over! Press Q to Quit or C to Play Again", True, RED)
    screen.blit(game_over_message, [WIDTH // 6, HEIGHT // 3])

# Main game loop
def gameLoop():
    global score, level, snake_speed, snake_pos, snake_direction, food_pos, food_spawn, change_to, food_weight, food_timer

    snake_pos = [[100, 50], [90, 50], [80, 50]]  # Initial snake position
    snake_direction = 'RIGHT'
    change_to = snake_direction
    food_pos = [random.randrange(1, (WIDTH // snake_block)) * snake_block,
                random.randrange(1, (HEIGHT // snake_block)) * snake_block]
    food_spawn = True
    food_weight = random.randint(1, 5)  # Random food weight
    food_timer = time.time()  # Start the food timer

    score = 0
    level = 1
    snake_speed = 15

    game_over_flag = False

    while not game_over_flag:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != 'DOWN':
                    change_to = 'UP'
                if event.key == pygame.K_DOWN and snake_direction != 'UP':
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                    change_to = 'RIGHT'

        # Check if the snake hits the screen boundaries
        if snake_pos[0][0] >= WIDTH or snake_pos[0][0] < 0 or snake_pos[0][1] >= HEIGHT or snake_pos[0][1] < 0:
            game_over_flag = True
            game_over()

        snake_direction = change_to

        # Update the snake's head position
        if snake_direction == 'UP':
            new_head = [snake_pos[0][0], snake_pos[0][1] - snake_block]
        if snake_direction == 'DOWN':
            new_head = [snake_pos[0][0], snake_pos[0][1] + snake_block]
        if snake_direction == 'LEFT':
            new_head = [snake_pos[0][0] - snake_block, snake_pos[0][1]]
        if snake_direction == 'RIGHT':
            new_head = [snake_pos[0][0] + snake_block, snake_pos[0][1]]

        snake_pos.insert(0, new_head)

        # Check if the snake eats the food
        if snake_pos[0] == food_pos:
            score += food_weight  # Add food weight to the score
            if score % 4 == 0:  # Increase level every 4 points
                level += 1
                snake_speed += 2  # Increase snake speed
            food_spawn = False
        else:
            snake_pos.pop()

        # Generate new food if it was eaten
        if not food_spawn:
            food_pos = [random.randrange(1, (WIDTH // snake_block)) * snake_block,
                        random.randrange(1, (HEIGHT // snake_block)) * snake_block]
            food_weight = random.randint(1, 5)  # New random food weight
            food_timer = time.time()  # Reset the food timer
            food_spawn = True

        # Check if the food has been on the screen for too long (5 seconds)
        if time.time() - food_timer > 5:  # If more than 5 seconds passed
            food_spawn = False  # Remove the food
            food_pos = [-100, -100]  # Move the food off-screen

        screen.fill(WHITE)

        # Draw all elements
        draw_snake(snake_block, snake_pos)
        draw_food(food_pos, food_weight)

        # Display the score and level
        display_score(score, level)

        # Check if the snake collides with itself
        if snake_pos[0] in snake_pos[1:]:
            game_over_flag = True
            game_over()

        pygame.display.update()

        # Set the game speed
        clock.tick(snake_speed)

gameLoop()