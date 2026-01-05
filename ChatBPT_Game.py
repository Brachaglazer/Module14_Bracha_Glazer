"""
Reflection:
It was definitely not as fun as making it myself! I don't feel like I did anything at all!
It's much funner to come up with the game and the algorithm and enjoy the satisfaction when
it runs properly! Thank You!
"""

import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Apples")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Player setup
player_width, player_height = 80, 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 7

# Apple setup
apple_width, apple_height = 30, 30
apple_x = random.randint(0, WIDTH - apple_width)
apple_y = -apple_height
apple_speed = 5
apple_color = random.choice([RED, GREEN])  # initial apple color

# Score
score = 0

# Font
font = pygame.font.SysFont(None, 36)

# Instructions flag
show_instructions = True
instruction_time = 3000  # milliseconds

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    # Move apple
    apple_y += apple_speed
    if apple_y > HEIGHT:
        apple_y = -apple_height
        apple_x = random.randint(0, WIDTH - apple_width)
        apple_color = random.choice([RED, GREEN])

    # Draw apple
    pygame.draw.rect(screen, apple_color, (apple_x, apple_y, apple_width, apple_height))

    # Collision detection
    if (player_y < apple_y + apple_height and
            player_y + player_height > apple_y and
            player_x < apple_x + apple_width and
            player_x + player_width > apple_x):
        if apple_color == GREEN:
            score += 1
        else:
            score -= 1  # hidden rule, discovered by player
        apple_y = -apple_height
        apple_x = random.randint(0, WIDTH - apple_width)
        apple_color = random.choice([RED, GREEN])

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Display vague instructions at start
    if show_instructions:
        screen.fill(WHITE)
        lines = [
            "Move the blue basket with the arrow keys.",
            "Catch the falling apples to see what happens.",
            "Can you figure out the best strategy?"
        ]
        for i, line in enumerate(lines):
            text_surface = font.render(line, True, BLACK)
            screen.blit(text_surface, (50, 100 + i * 40))
        pygame.display.flip()
        pygame.time.delay(instruction_time)
        show_instructions = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()