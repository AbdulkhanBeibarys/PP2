import pygame
import sys
import random
import time

pygame.init()

width, height = 500, 500
cell_size = 10

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Snake')

black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)

snake_pos = [100, 100]
snake_body = [[100, 100], [80, 100], [60, 100]]
walls = [[100, 110], [100, 120], [100, 130], [100, 140], [400, 310], [400, 320], [400, 330], [400, 340]]
direction = 'RIGHT'
change_to = direction

# score, level, and speed
score = 0
level = 1
speed = 10

# walls 
for x in range(0, width, cell_size):
    walls.append([x, 0]) 
    walls.append([x, height - cell_size]) 
for y in range(0, height, cell_size):
    walls.append([0, y]) 
    walls.append([width - cell_size, y]) 

food_weight = 1
food_time = 0
food_duration = 0

# generate food 
def generate_food():
    global food_weight, food_time, food_duration
    while True:
        x = random.randrange(0, width, cell_size)
        y = random.randrange(0, height, cell_size)
        if [x, y] not in snake_body and [x, y] not in walls:
            food_weight = random.choice([1, 2, 3])
            food_time = time.time()
            food_duration = random.randint(5, 10)
            return [x, y]

food_pos = generate_food()
clock = pygame.time.Clock()

# Main game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'

    direction = change_to

    # Move snake head
    if direction == 'UP':
        snake_pos[1] -= cell_size
    elif direction == 'DOWN':
        snake_pos[1] += cell_size
    elif direction == 'LEFT':
        snake_pos[0] -= cell_size
    elif direction == 'RIGHT':
        snake_pos[0] += cell_size

    # collision with screen border
    if snake_pos[0] < 0:
        running = False
    elif snake_pos[0] >= width:
        running = False 
    elif snake_pos[1] < 0:
        running = False
    elif snake_pos[1] >= height:
        running = False

    # Insert new head position
    snake_body.insert(0, list(snake_pos))

    # food eaten
    if snake_pos == food_pos:
        score += food_weight
        food_pos = generate_food()
        if score % 5 == 0:
            level += 1
            speed += 2
    else:
        snake_body.pop()

    if time.time() - food_time > food_duration:
        food_pos = generate_food()

    screen.fill(black)

    #snake head
    head = snake_body[0]
    pygame.draw.rect(screen, (0, 155, 0), pygame.Rect(head[0], head[1], cell_size, cell_size))
    
    #snake body
    for block in snake_body[1:]:
        pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], cell_size, cell_size))
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], cell_size, cell_size))

    for wall in walls:
        pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(wall[0], wall[1], cell_size, cell_size))
    
    # colision
    if snake_pos in walls:
        running = False

    if snake_pos in snake_body[1:]:
        running = False

    # display score and level
    font = pygame.font.SysFont('Arial', 20)
    score_text = font.render(f'Score: {score}, Level: {level}', True, (white))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
sys.exit()