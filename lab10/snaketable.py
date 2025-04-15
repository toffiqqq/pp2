import pygame
import random
import sys
import psycopg2

pygame.init()

# PostgreSQL database connection details
def connect_db():
    return psycopg2.connect(
        dbname="snake_table", user="postgres", password="32689263", host="localhost"
    )

# Create tables if they don't exist
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS "snake_user" (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL
        );
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES "snake_user"(id),
            score INTEGER NOT NULL DEFAULT 0,
            level INTEGER NOT NULL DEFAULT 1,
            last_saved TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    conn.commit()
    cursor.close()
    conn.close()

# Check if user exists
def user_exists(username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM \"snake_user\" WHERE username = %s", (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

# Insert new user into the database
def insert_user(username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO \"snake_user\" (username) VALUES (%s) RETURNING id", (username,))
    user_id = cursor.fetchone()[0]
    cursor.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, 0, 1))
    conn.commit()
    cursor.close()
    conn.close()

# Get user score and level
def get_user_score(username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT u.username, s.score, s.level
        FROM "snake_user" u
        JOIN user_score s ON u.id = s.user_id
        WHERE u.username = %s
    """, (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

# Update user score and level
def update_user_score(username, score, level):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE user_score 
        SET score = %s, level = %s, last_saved = CURRENT_TIMESTAMP
        FROM "snake_user"
        WHERE "snake_user".username = %s AND "snake_user".id = user_score.user_id
    """, (score, level, username))
    conn.commit()
    cursor.close()
    conn.close()

# Initialize game settings
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

snake_block = 20
snake_speed = 15
snake_color = GREEN

snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'
change_to = snake_direction

food_pos = [random.randrange(1, (WIDTH // snake_block)) * snake_block,
            random.randrange(1, (HEIGHT // snake_block)) * snake_block]
food_spawn = True

score = 0
level = 1

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

clock = pygame.time.Clock()

# Display score and level
def display_score(score, level):
    value = score_font.render("Score: " + str(score), True, BLACK)
    screen.blit(value, [0, 0])
    level_text = font_style.render("Level: " + str(level), True, BLACK)
    screen.blit(level_text, [WIDTH - 120, 0])

# Draw the snake
def draw_snake(snake_block, snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, snake_color, pygame.Rect(block[0], block[1], snake_block, snake_block))

# Draw the food
def draw_food(food_pos):
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], snake_block, snake_block))

# Handle game over
def game_over():
    game_over_message = font_style.render("Game Over! Press Q to Quit or C to Play Again", True, RED)
    screen.blit(game_over_message, [WIDTH // 6, HEIGHT // 3])

# Main game loop
def gameLoop(username):
    global score, level, snake_speed, snake_pos, snake_direction, food_pos, food_spawn, change_to

    snake_pos = [[100, 50], [90, 50], [80, 50]]
    snake_direction = 'RIGHT'
    change_to = snake_direction
    food_pos = [random.randrange(1, (WIDTH // snake_block)) * snake_block,
                random.randrange(1, (HEIGHT // snake_block)) * snake_block]
    food_spawn = True
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
                if event.key == pygame.K_p:  # Pause and save
                    update_user_score(username, score, level)
                    print(f"Game Paused. Score saved: {score}, Level: {level}")
                    return

        if snake_pos[0][0] >= WIDTH or snake_pos[0][0] < 0 or snake_pos[0][1] >= HEIGHT or snake_pos[0][1] < 0:
            game_over_flag = True
            game_over()

        snake_direction = change_to
        if snake_direction == 'UP':
            new_head = [snake_pos[0][0], snake_pos[0][1] - snake_block]
        if snake_direction == 'DOWN':
            new_head = [snake_pos[0][0], snake_pos[0][1] + snake_block]
        if snake_direction == 'LEFT':
            new_head = [snake_pos[0][0] - snake_block, snake_pos[0][1]]
        if snake_direction == 'RIGHT':
            new_head = [snake_pos[0][0] + snake_block, snake_pos[0][1]]

        snake_pos.insert(0, new_head)

        if snake_pos[0] == food_pos:
            score += 1
            if score % 4 == 0:
                level += 1
                snake_speed += 2
            food_spawn = False
        else:
            snake_pos.pop()

        if not food_spawn:
            food_pos = [random.randrange(1, (WIDTH // snake_block)) * snake_block,
                        random.randrange(1, (HEIGHT // snake_block)) * snake_block]

            while food_pos in snake_pos:
                food_pos = [random.randrange(1, (WIDTH // snake_block)) * snake_block,
                            random.randrange(1, (HEIGHT // snake_block)) * snake_block]

            food_spawn = True

        screen.fill(WHITE)

        draw_snake(snake_block, snake_pos)
        draw_food(food_pos)

        display_score(score, level)

        if snake_pos[0] in snake_pos[1:]:
            game_over_flag = True
            game_over()

        pygame.display.update()

        clock.tick(snake_speed)

# Main program flow
def main():
    create_tables()

    username = input("Enter your username: ")

    if user_exists(username):
        print(f"Welcome back, {username}!")
        user_data = get_user_score(username)
        print(f"Current Level: {user_data[2]} - Current Score: {user_data[1]}")
    else:
        print(f"New user {username}!")
        insert_user(username)

    gameLoop(username)

if __name__ == "__main__":
    main()