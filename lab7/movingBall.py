import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Движущийся мяч')

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_radius = 25  

move_distance = 20

running = True
while running:
    screen.fill(WHITE)  

    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and ball_y - ball_radius > 0:
        ball_y -= move_distance  
    if keys[pygame.K_DOWN] and ball_y + ball_radius < HEIGHT:
        ball_y += move_distance  
    if keys[pygame.K_LEFT] and ball_x - ball_radius > 0:
        ball_x -= move_distance  
    if keys[pygame.K_RIGHT] and ball_x + ball_radius < WIDTH:
        ball_x += move_distance  

    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()