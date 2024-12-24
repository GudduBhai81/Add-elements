import pygame

# Initialize Pygame
pygame.init()

# Set up the game screen
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("My first game screen")

# Define colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Background color
screen.fill(BLACK)

# Create a rectangle
rectangle_width = 100
rectangle_height = 50
rectangle_x = (window_size[0] - rectangle_width) // 2
rectangle_y = (window_size[1] - rectangle_height) // 2
rectangle = pygame.Rect(rectangle_x, rectangle_y, rectangle_width, rectangle_height)

# Set up text
font = pygame.font.Font(None, 36)
text = font.render("Hello, Pygame!", True, WHITE)
text_rect = text.get_rect(center=(window_size[0] // 2, 50))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the rectangle
    pygame.draw.rect(screen, RED, rectangle)

    # Draw the text
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()