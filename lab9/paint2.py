import pygame
import sys

pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

colors = [BLACK, RED, GREEN, BLUE, YELLOW, ORANGE]
color_names = ['Black', 'Red', 'Green', 'Blue', 'Yellow', 'Orange']

# Initialize variables
current_color = BLACK
drawing_shape = 'line'
history = []  # To store drawing history for undo

# Setup Pygame font
font = pygame.font.SysFont("Arial", 20)

def display_color_name():
    """Display the name of the current color being used for drawing."""
    color_text = font.render(f"Current Color: {color_names[colors.index(current_color)]}", True, current_color)
    screen.blit(color_text, (10, HEIGHT - 30))

def draw_shape(start_pos, end_pos, shape_type, color):
    """Draw a shape based on the selected shape type."""
    if shape_type == 'rectangle':
        pygame.draw.rect(screen, color, pygame.Rect(start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 2)
    elif shape_type == 'circle':
        radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
        pygame.draw.circle(screen, color, start_pos, radius, 2)
    elif shape_type == 'eraser':
        pygame.draw.rect(screen, WHITE, pygame.Rect(end_pos[0] - 10, end_pos[1] - 10, 20, 20))
    elif shape_type == 'square':
        side_length = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
        pygame.draw.rect(screen, color, pygame.Rect(start_pos[0], start_pos[1], side_length, side_length), 2)
    elif shape_type == 'right_triangle':
        # Create a right triangle using 3 points
        points = [start_pos, (end_pos[0], start_pos[1]), end_pos]
        pygame.draw.polygon(screen, color, points, 2)
    elif shape_type == 'equilateral_triangle':
        # Create an equilateral triangle
        side_length = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
        height = (3 ** 0.5 / 2) * side_length  # Height of an equilateral triangle
        points = [
            start_pos,
            (start_pos[0] + side_length, start_pos[1]),
            (start_pos[0] + side_length / 2, start_pos[1] - height)
        ]
        pygame.draw.polygon(screen, color, points, 2)
    elif shape_type == 'rhombus':
        # Draw a rhombus
        width = abs(end_pos[0] - start_pos[0])
        height = abs(end_pos[1] - start_pos[1])
        points = [
            (start_pos[0] + width / 2, start_pos[1]),
            (start_pos[0] + width, start_pos[1] + height / 2),
            (start_pos[0] + width / 2, start_pos[1] + height),
            (start_pos[0], start_pos[1] + height / 2)
        ]
        pygame.draw.polygon(screen, color, points, 2)

def draw_buttons():
    """Draw the color and shape buttons."""
    # Color buttons
    pygame.draw.rect(screen, RED, pygame.Rect(10, 10, 100, 30))
    pygame.draw.rect(screen, GREEN, pygame.Rect(120, 10, 100, 30))
    pygame.draw.rect(screen, BLUE, pygame.Rect(230, 10, 100, 30))
    pygame.draw.rect(screen, YELLOW, pygame.Rect(340, 10, 100, 30))
    pygame.draw.rect(screen, ORANGE, pygame.Rect(450, 10, 100, 30))

    # Shape buttons
    pygame.draw.rect(screen, WHITE, pygame.Rect(560, 10, 100, 30))
    pygame.draw.rect(screen, BLACK, pygame.Rect(670, 10, 100, 30))

    # Undo and Clear buttons
    pygame.draw.rect(screen, WHITE, (10, HEIGHT - 60, 150, 50))
    pygame.draw.rect(screen, BLACK, (170, HEIGHT - 60, 150, 50))

    # Add text labels to buttons
    text_font = pygame.font.SysFont("Arial", 20)
    draw_rectangle_text = text_font.render("Rectangle", True, BLACK)
    draw_circle_text = text_font.render("Circle", True, BLACK)
    eraser_text = text_font.render("Eraser", True, BLACK)
    undo_text = text_font.render("Undo", True, BLACK)
    clear_text = text_font.render("Clear", True, BLACK)
    draw_square_text = text_font.render("Square", True, BLACK)
    draw_triangle_text = text_font.render("Right Tri", True, BLACK)
    equilateral_text = text_font.render("Equilateral", True, BLACK)
    rhombus_text = text_font.render("Rhombus", True, BLACK)

    screen.blit(draw_rectangle_text, (20, 15))
    screen.blit(draw_circle_text, (130, 15))
    screen.blit(eraser_text, (240, 15))
    screen.blit(undo_text, (20, HEIGHT - 45))
    screen.blit(clear_text, (180, HEIGHT - 45))
    screen.blit(draw_square_text, (350, 15))
    screen.blit(draw_triangle_text, (460, 15))
    screen.blit(equilateral_text, (570, 15))
    screen.blit(rhombus_text, (690, 15))

    pygame.display.flip()

def reset_screen():
    """Reset the screen and redraw the buttons and color name."""
    screen.fill(WHITE)
    draw_buttons()
    display_color_name()

def main():
    """Main game loop."""
    global current_color, drawing_shape, history
    is_drawing = False
    start_pos = None

    reset_screen()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button clicked
                    is_drawing = True
                    start_pos = event.pos

                    # Handle color change on button clicks
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
                    elif pygame.Rect(10, HEIGHT - 60, 150, 50).collidepoint(event.pos):  # Undo
                        if history:
                            history.pop()  # Remove last drawing from history
                            reset_screen()  # Reset the screen
                            for action in history:  # Redraw the rest of the actions
                                draw_shape(action[1], action[2], action[0], action[3])
                    elif pygame.Rect(170, HEIGHT - 60, 150, 50).collidepoint(event.pos):  # Clear
                        history = []  # Clear history
                        reset_screen()
                    elif pygame.Rect(350, 10, 100, 30).collidepoint(event.pos):  # Square
                        drawing_shape = 'square'
                    elif pygame.Rect(460, 10, 100, 30).collidepoint(event.pos):  # Right Triangle
                        drawing_shape = 'right_triangle'
                    elif pygame.Rect(570, 10, 100, 30).collidepoint(event.pos):  # Equilateral Triangle
                        drawing_shape = 'equilateral_triangle'
                    elif pygame.Rect(690, 10, 100, 30).collidepoint(event.pos):  # Rhombus
                        drawing_shape = 'rhombus'

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if is_drawing:
                        end_pos = event.pos
                        if drawing_shape != 'eraser':
                            history.append((drawing_shape, start_pos, end_pos, current_color))  # Store drawing action in history
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