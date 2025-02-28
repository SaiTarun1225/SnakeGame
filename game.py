import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock
clock = pygame.time.Clock()

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Snake speed levels
SPEEDS = {
    "Easy": 10,
    "Medium": 20,
    "Hard": 30
}

# Functions
def message(msg, color, x, y):
    msg_text = font_style.render(msg, True, color)
    screen.blit(msg_text, [x, y])

def display_score(score, lives):
    score_text = score_font.render(f"Score: {score}  Lives: {lives}", True, YELLOW)
    screen.blit(score_text, [10, 10])

def game_loop(mode):
    game_over = False
    game_close = False

    # Snake properties
    x1, y1 = WIDTH // 2, HEIGHT // 2
    x1_change, y1_change = 0, 0
    snake_block = 10
    snake_list = []
    length_of_snake = 1

    # Lives and score
    lives = 3
    score = 0

    # Food
    food_x = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            screen.fill(BLACK)
            message("Game Over! Press M for Menu", RED, WIDTH // 6, HEIGHT // 3)
            display_score(score, lives)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_m:
                    main()

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            lives -= 1
            if lives == 0:
                game_close = True
            else:
                x1, y1 = WIDTH // 2, HEIGHT // 2
                x1_change, y1_change = 0, 0

        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)

        pygame.draw.rect(screen, GREEN, [food_x, food_y, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        for segment in snake_list:
            pygame.draw.rect(screen, BLUE, [segment[0], segment[1], snake_block, snake_block])

        display_score(score, lives)
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            score += 10

        clock.tick(SPEEDS[mode])

    pygame.quit()
    quit()

def main():
    run = True
    while run:
        screen.fill(BLACK)
        message("Welcome to Snake Game!", GREEN, WIDTH // 4, HEIGHT // 5)
        message("Select Mode: 1. Easy  2. Medium  3. Hard", WHITE, WIDTH // 6, HEIGHT // 3)
        message("Press Q to Quit", RED, WIDTH // 3, HEIGHT // 2)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_loop("Easy")
                elif event.key == pygame.K_2:
                    game_loop("Medium")
                elif event.key == pygame.K_3:
                    game_loop("Hard")
                elif event.key == pygame.K_q:
                    run = False

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
