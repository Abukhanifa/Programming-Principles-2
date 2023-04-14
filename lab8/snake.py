import pygame
import time
import random

snake_speed = 15

WIDTH = 720
HEIGHT = 480

#COLORS
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()

#caption and screen
pygame.display.set_caption('Snakes')
screen = pygame.display.set_mode((WIDTH, HEIGHT))

fps = pygame.time.Clock()

#snake position and body
snake_position = [100, 50]

snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

#RANDOM SPAWN FOR THE FOOD
food_position = [random.randrange(1, (WIDTH // 10)) * 10,
                  random.randrange(1, (HEIGHT // 10)) * 10]

food_spawn = True

#DIRECTION
direction = 'RIGHT'
change_to = direction

#SCORE, LEVEL and LEVELSCORE
score = 0
levelscore = 0
level = 1

#SHOWING THE SCORE
def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)

#SHOWING THE LEVEL
def show_level(color, font, size):
    level_font = pygame.font.SysFont(font, size)
    level_surface = level_font.render('Level : ' + str(level), True, color)
    level_rect = level_surface.get_rect()
    level_rect.midtop = (WIDTH - 50, 0)
    screen.blit(level_surface, level_rect)

#SHOWING THE GAME OVER SCREEN
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WIDTH / 2, HEIGHT / 4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()



#MOVEMENT and DIRECTION
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
        if event.type == pygame.QUIT:
            pygame.quit()
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

#COLLISION SNAKE and FOOD
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 10
        levelscore += 10
        food_spawn = False
    else:
        snake_body.pop()
    if levelscore == 40:
        level += 1
        snake_speed += 4
        levelscore = 0
    if not food_spawn:
        food_position = [random.randrange(1, (WIDTH // 10)) * 10,
                          random.randrange(1, (HEIGHT // 10)) * 10]

    food_spawn = True
    screen.fill(black)

    for pos in snake_body:
        pygame.draw.rect(screen, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, white, pygame.Rect(
        food_position[0], food_position[1], 10, 10))

#COLLISION SNAKE AND WALL
    if snake_position[0] < 0 or snake_position[0] > WIDTH - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > HEIGHT - 10:
        game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
            
#SHOWING THE SCORE AND LEVEL
    show_score(white, 'times new roman', 20)
    show_level(white, 'times new roman', 20)

    pygame.display.update()

    fps.tick(snake_speed)

