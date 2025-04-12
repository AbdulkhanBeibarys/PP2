import pygame
import sys

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Paint')

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)

screen.fill(white)

class Button:
    def __init__(self, x, y, width, height, text, color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 24)
        text_surface = font.render(self.text, True, white)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_action(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()

drawing = False
brush_color = black
mode = 'line'
start_pos = None

def set_black():  
    global brush_color
    brush_color = black
def set_green():  
    global brush_color
    brush_color = green
def set_red(): 
    global brush_color
    brush_color = red
def set_blue():  
    global brush_color
    brush_color = blue
def set_eraser(): 
    global brush_color, mode
    brush_color = white
    mode = 'line'
def set_mode_line():           
    global mode
    mode = 'line'
def set_mode_rect():        
    global mode
    mode = 'rect'
def set_mode_circle():        
    global mode
    mode = 'circle'
def set_mode_eq_triangle():   
    global mode
    mode = 'eq_triangle'
def set_mode_rhombus():       
    global mode
    mode = 'rhombus'
def set_mode_right_triangle():
    global mode
    mode = 'right_triangle'
def clear_screen(): 
    screen.fill(white)
def exit_app(): 
    pygame.quit()
    sys.exit()

buttons = [
    Button(10, 10, 60, 30, 'Black', black, set_black),
    Button(80, 10, 60, 30, 'Green', green, set_green),
    Button(150, 10, 60, 30, 'Red', red, set_red),
    Button(220, 10, 60, 30, 'Blue', blue, set_blue),
    Button(290, 10, 60, 30, 'Er', gray, set_eraser),
    Button(360, 10, 60, 30, 'Line', gray, set_mode_line),
    Button(430, 10, 60, 30, 'Rect', gray, set_mode_rect),
    Button(500, 10, 60, 30, 'Cir', gray, set_mode_circle),
    Button(570, 10, 60, 30, 'Eq-Tri', gray, set_mode_eq_triangle),
    Button(640, 10, 60, 30, 'Rhom', gray, set_mode_rhombus),
    Button(710, 10, 60, 30, 'R-Tri', gray, set_mode_right_triangle),
    Button(10, 50, 60, 30, 'Clear', gray, clear_screen),
    Button(80, 50, 60, 30, 'Exit', gray, exit_app),
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_app()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True
            start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and drawing:
            end_pos = event.pos
            if start_pos[1] > 80 and end_pos[1] > 80:
                if mode == 'line':
                    pygame.draw.line(screen, brush_color, start_pos, end_pos, 5)
                elif mode == 'rect':
                    rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    pygame.draw.rect(screen, brush_color, rect, 2)
                elif mode == 'circle':
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, brush_color, start_pos, radius, 2)
                elif mode == 'eq_triangle':
                    top = start_pos
                    left_base = (start_pos[0] - (end_pos[0] - start_pos[0]), end_pos[1])
                    right_base = (end_pos[0], end_pos[1])
                    pygame.draw.polygon(screen, brush_color, [top, left_base, right_base], 2)
                elif mode == 'rhombus':
                    mid_x = (start_pos[0] + end_pos[0]) // 2
                    mid_y = (start_pos[1] + end_pos[1]) // 2
                    points = [(mid_x, start_pos[1]), (end_pos[0], mid_y), (mid_x, end_pos[1]), (start_pos[0], mid_y)]
                    pygame.draw.polygon(screen, brush_color, points, 2)
                elif mode == 'right_triangle':
                    pygame.draw.polygon(screen, brush_color, [start_pos, (start_pos[0], end_pos[1]), end_pos], 2)
            drawing = False
            start_pos = None

        for button in buttons:
            button.check_action(event)

    if drawing and mode == 'line':
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_y > 80:
            pygame.draw.circle(screen, brush_color, (mouse_x, mouse_y), 5)

    pygame.draw.rect(screen, gray, (0, 0, width, 80))
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()
