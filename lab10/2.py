import psycopg2
import pygame
import sys
import random

def connect_db():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="050307",
        host="localhost",
        port="5432"
    )

def create_tables():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE NOT NULL
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_scores (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id), 
            score INTEGER,
            level INTEGER,
            saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()
    cur.close()
    conn.close()

def get_user_id(username):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    result = cur.fetchone()
    if result:
        user_id = result[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return user_id
    
def get_last_score(user_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT score, level FROM user_scores WHERE user_id = %s ORDER BY saved_at DESC LIMIT 1", (user_id,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result if result else (0, 1)


def save_score(user_id, score, level):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
    conn.commit()
    cur.close()
    conn.close()

#enter name
create_tables()
username = input("Enter your username: ").strip()
user_id = get_user_id(username)
score, level = get_last_score(user_id)

print(f"Welcome, {username}. Starting from level {level}, score {score}.")

#snake game code
pygame.init()
cell_size = 10
screen_size = 500
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("Snake")

black = (0, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

snake_pos = [100, 100]
snake_body = [[100, 100], [90, 100], [80, 100]]
direction = 'RIGHT'
change_to = direction

speed = 10 
clock = pygame.time.Clock()
paused = False
running = True

class Food:
    def __init__(self, pos):
        self.pos = pos
        self.weight = random.choice([1, 2, 3])
        self.timer = 100

def generate_food(count):
    food_items = []
    while len(food_items) < count:
        x = random.randint(0, (screen_size // cell_size) - 1) * cell_size
        y = random.randint(0, (screen_size // cell_size) - 1) * cell_size
        pos = [x, y]
        if pos not in snake_body and all(f.pos != pos for f in food_items):
            food_items.append(Food(pos))
    return food_items

food_positions = generate_food(1)
food_spawn_interval = 5000  
last_food_spawn_time = pygame.time.get_ticks()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_score(user_id, score, level)
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
            elif event.key == pygame.K_p:
                paused = not paused
            elif event.key == pygame.K_s:
                save_score(user_id, score, level)
                print("Game state saved!")

    if paused:
        font = pygame.font.SysFont("Arial", 40)
        pause_text = font.render("Paused", True, white)
        screen.blit(pause_text, [screen_size // 2 - 60, screen_size // 2])
        pygame.display.flip()
        continue

    direction = change_to
    
    if direction == 'UP':
        snake_pos[1] -= cell_size
    elif direction == 'DOWN':
        snake_pos[1] += cell_size
    elif direction == 'LEFT':
        snake_pos[0] -= cell_size
    elif direction == 'RIGHT':
        snake_pos[0] += cell_size

    if snake_pos[0]<0:
        snake_pos[0]=500-cell_size
    elif snake_pos[0]>=500:
        snake_pos[0]=0
    elif snake_pos[1]<0:
        snake_pos[1]=500-cell_size
    elif snake_pos[1]>=500:
        snake_pos[1]=0

    snake_body.insert(0, list(snake_pos))
    current_time = pygame.time.get_ticks()
    if current_time - last_food_spawn_time >= food_spawn_interval:
        new_food = generate_food(1)
        food_positions.extend(new_food)
        last_food_spawn_time = current_time
    
    for food in food_positions:
        if snake_pos == food.pos:
            score += food.weight
            food_positions.remove(food)
            if not food_positions:
                level += 1
                speed += 2
                food_positions = generate_food(min(1 + level // 2, 5))
            break
    else:
        snake_body.pop()

    if snake_pos in snake_body[1:]:
        save_score(user_id, score, level)
        running = False

    for food in food_positions[:]:
        food.timer -= 1
        if food.timer <= 0:
            food_positions.remove(food)

    screen.fill(black)
    
    for block in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], cell_size, cell_size))
    
    for food in food_positions:
        if food.weight == 1:
            color = (255,0,0)
        elif food.weight == 2:
            color = (255, 165, 0)  
        else:
            color = (255, 255, 0) 
        pygame.draw.rect(screen, color, pygame.Rect(food.pos[0], food.pos[1], cell_size, cell_size))

    font = pygame.font.SysFont("Arial", 20)
    score_text = font.render(f"Score: {score}  Level: {level}", True, white)
    screen.blit(score_text, [10, 10])

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
sys.exit()