from agent import Agent
import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 400
BLOCK = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Snake Game")

BLACK = (20, 20, 20)
GREEN = (0, 255, 100)
HEAD_COLOR = (0, 200, 255)
RED = (255, 60, 60)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 25)

agent = Agent()

high_score = 0


def draw_snake(snake):
    for i, block in enumerate(snake):
        if i == len(snake) - 1:
            pygame.draw.rect(screen, HEAD_COLOR, [block[0], block[1], BLOCK, BLOCK])
        else:
            pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK, BLOCK])


def draw_score(score):
    value = font.render("Score: " + str(score), True, WHITE)
    screen.blit(value, [10, 10])


def draw_high_score(score):
    value = font.render("High Score: " + str(score), True, WHITE)
    screen.blit(value, [400, 10])


def draw_grid():
    for x in range(0, WIDTH, BLOCK):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, BLOCK):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (WIDTH, y))


def game_over_screen(score):
    global high_score

    if score > high_score:
        high_score = score

    while True:
        screen.fill(BLACK)

        text1 = font.render("GAME OVER!", True, RED)
        text2 = font.render("Score: " + str(score), True, WHITE)
        text3 = font.render("Press R to Restart", True, WHITE)

        screen.blit(text1, [WIDTH // 3, HEIGHT // 3])
        screen.blit(text2, [WIDTH // 3, HEIGHT // 2])
        screen.blit(text3, [WIDTH // 4, HEIGHT // 1.5])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game()


def game():
    x = WIDTH // 2
    y = HEIGHT // 2

    snake = []
    length = 1

    food_x = random.randrange(0, WIDTH, BLOCK)
    food_y = random.randrange(0, HEIGHT, BLOCK)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # 🤖 AI Move
        move = agent.get_action(x, y, food_x, food_y, WIDTH, HEIGHT, BLOCK, snake)

        if move == "RIGHT":
            x += BLOCK
        elif move == "LEFT":
            x -= BLOCK
        elif move == "UP":
            y -= BLOCK
        elif move == "DOWN":
            y += BLOCK

        # Collision with wall
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_over_screen(length - 1)

        snake_head = [x, y]
        snake.append(snake_head)

        if len(snake) > length:
            del snake[0]

        # Self collision
        for block in snake[:-1]:
            if block == snake_head:
                game_over_screen(length - 1)

        # Eat food
        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH, BLOCK)
            food_y = random.randrange(0, HEIGHT, BLOCK)
            length += 1

        screen.fill(BLACK)

        draw_grid()

        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK, BLOCK])

        draw_snake(snake)
        draw_score(length - 1)
        draw_high_score(high_score)

        pygame.display.update()

        # Speed increase
        speed = 8 + (length // 5)
        clock.tick(speed)


game()