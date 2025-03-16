import pygame
import time
import math
pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mickey Mouse Watch')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

hand_image = pygame.image.load('mickeyclock.jpeg')
center_x, center_y = WIDTH // 2, HEIGHT // 2

def draw_clock():
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, (center_x, center_y), 200, 5)  

    for i in range(60):
        angle = math.radians(i * 6)
        x1 = center_x + 180 * math.cos(angle)
        y1 = center_y + 180 * math.sin(angle)
        x2 = center_x + 190 * math.cos(angle)
        y2 = center_y + 190 * math.sin(angle)
        pygame.draw.line(screen, BLACK, (x1, y1), (x2, y2), 2)

def draw_hands(minutes, seconds):
    minute_angle = 90 - (minutes * 6)  
    rotated_hand = pygame.transform.rotate(hand_image, minute_angle)
    hand_rect = rotated_hand.get_rect(center=(center_x, center_y))
    screen.blit(rotated_hand, hand_rect.topleft)
    
    second_angle = 90 - (seconds * 6)  
    rotated_hand_seconds = pygame.transform.rotate(hand_image, second_angle)
    hand_rect_seconds = rotated_hand_seconds.get_rect(center=(center_x, center_y))
    screen.blit(rotated_hand_seconds, hand_rect_seconds.topleft)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    draw_clock()
    draw_hands(minutes, seconds)

    pygame.display.flip()

    pygame.time.delay(1000)

pygame.quit()