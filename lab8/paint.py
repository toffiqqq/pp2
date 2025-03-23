import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

colors = [BLACK, RED, GREEN, BLUE, YELLOW, ORANGE]
color_names = ['Black', 'Red', 'Green', 'Blue', 'Yellow', 'Orange']

current_color = BLACK
drawing_shape = 'line'

screen.fill(WHITE)

font = pygame.font.SysFont("Arial", 20)

def display_color_name():
    color_text = font.render(f"Current Color: {color_names[colors.index(current_color)]}", True, current_color)
    screen.blit(color_text, (10, HEIGHT - 30))

def draw_shape(start_pos, end_pos, shape_type, color):
    if shape_type == 'rectangle':
        pygame.draw.rect(screen, color, pygame.Rect(start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 2)
    elif shape_type == 'circle':
        radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
        pygame.draw.circle(screen, color, start_pos, radius, 2)
    elif shape_type == 'eraser':
        pygame.draw.rect(screen, WHITE, pygame.Rect(end_pos[0] - 10, end_pos[1] - 10, 20, 20))

def draw_buttons():
    pygame.draw.rect(screen, RED, pygame.Rect(10, 10, 100, 30))
    pygame.draw.rect(screen, GREEN, pygame.Rect(120, 10, 100, 30))
    pygame.draw.rect(screen, BLUE, pygame.Rect(230, 10, 100, 30))
    pygame.draw.rect(screen, YELLOW, pygame.Rect(340, 10, 100, 30))
    pygame.draw.rect(screen, ORANGE, pygame.Rect(450, 10, 100, 30))

    pygame.draw.rect(screen, WHITE, pygame.Rect(560, 10, 100, 30))
    pygame.draw.rect(screen, BLACK, pygame.Rect(670, 10, 100, 30))

    text_font = pygame.font.SysFont("Arial", 20)

    draw_rectangle_text = text_font.render("Rectangle", True, BLACK)
    draw_circle_text = text_font.render("Circle", True, BLACK)
    eraser_text = text_font.render("Eraser", True, BLACK)
    undo_text = text_font.render("Undo", True, BLACK)

    screen.blit(draw_rectangle_text, (20, 15))
    screen.blit(draw_circle_text, (130, 15))
    screen.blit(eraser_text, (240, 15))

    pygame.draw.rect(screen, WHITE, (10, HEIGHT - 60, 150, 50))
    pygame.draw.rect(screen, BLACK, (170, HEIGHT - 60, 150, 50))

    undo_button = pygame.Rect(10, HEIGHT - 60, 150, 50)
    clear_button = pygame.Rect(170, HEIGHT - 60, 150, 50)

    pygame.display.flip()

def reset_screen():
    screen.fill(WHITE)
    draw_buttons()
    display_color_name()

def main():
    global current_color, drawing_shape
    is_drawing = False
    start_pos = None
    history = []

    reset_screen()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    is_drawing = True
                    start_pos = event.pos

                    if pygame.Rect(10, 10, 100, 30).collidepoint(event.pos):
                        current_color = RED
                    elif pygame.Rect(120, 10, 100, 30).collidepoint(event.pos):
                        current_color = GREEN
                    elif pygame.Rect(230, 10, 100, 30).collidepoint(event.pos):
                        current_color = BLUE
                    elif pygame.Rect(340, 10, 100, 30).collidepoint(event.pos):
                        current_color = YELLOW
                    elif pygame.Rect(450, 10, 100, 30).collidepoint(event.pos):
                        current_color = ORANGE
                    elif pygame.Rect(560, 10, 100, 30).collidepoint(event.pos):
                        drawing_shape = 'rectangle'
                    elif pygame.Rect(670, 10, 100, 30).collidepoint(event.pos):
                        drawing_shape = 'circle'
                    elif pygame.Rect(560, HEIGHT - 60, 100, 50).collidepoint(event.pos):
                        drawing_shape = 'eraser'

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if is_drawing:
                        end_pos = event.pos
                        if drawing_shape != 'eraser':
                            history.append((drawing_shape, start_pos, end_pos, current_color))
                        is_drawing = False
                        draw_shape(start_pos, end_pos, drawing_shape, current_color)
                    start_pos = None

            if event.type == pygame.MOUSEMOTION:
                if is_drawing:
                    end_pos = event.pos
                    if drawing_shape == 'eraser':
                        draw_shape(start_pos, end_pos, drawing_shape, WHITE)

        draw_buttons()
        display_color_name()
        pygame.display.update()

if __name__ == "__main__":
    main()