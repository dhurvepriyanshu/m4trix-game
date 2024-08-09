import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
BLOCK_SIZE = 50
BLOCK_FALL_SPEED = 5
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dodge the Falling Blocks')

# Set up the clock for frame rate
clock = pygame.time.Clock()

# Function to draw the player
def draw_player(screen, x, y):
    pygame.draw.rect(screen, BLUE, (x, y, PLAYER_SIZE, PLAYER_SIZE))

# Function to draw a falling block
def draw_block(screen, x, y):
    pygame.draw.rect(screen, RED, (x, y, BLOCK_SIZE, BLOCK_SIZE))

# Main game loop
def game_loop():
    player_x = WIDTH // 2 - PLAYER_SIZE // 2
    player_y = HEIGHT - PLAYER_SIZE
    block_x = random.randint(0, WIDTH - BLOCK_SIZE)
    block_y = -BLOCK_SIZE
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= 10
        if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
            player_x += 10

        # Update block position
        block_y += BLOCK_FALL_SPEED
        if block_y > HEIGHT:
            block_y = -BLOCK_SIZE
            block_x = random.randint(0, WIDTH - BLOCK_SIZE)
            score += 1

        # Check for collisions
        if (block_x < player_x + PLAYER_SIZE and
            block_x + BLOCK_SIZE > player_x and
            block_y < player_y + PLAYER_SIZE and
            block_y + BLOCK_SIZE > player_y):
            print(f"Game Over! Your score: {score}")
            pygame.quit()
            sys.exit()

        # Draw everything
        screen.fill(WHITE)
        draw_player(screen, player_x, player_y)
        draw_block(screen, block_x, block_y)

        # Update the display
        pygame.display.flip()

        # Frame rate
        clock.tick(30)

# Start the game
if __name__ == "__main__":
    game_loop()
