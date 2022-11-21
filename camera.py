import math
import pygame


pygame.init()

W = 1000
H = 600

sc = pygame.display.set_mode((W, H))
sc.fill((0, 0, 0))
pygame.display.update()

pygame.display.set_caption('camera')
# pygame.display.set_icon(pygame.image.load('ico.bmp'))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

DEBUG_LINES = True

FPS = 60
p_clock = pygame.time.Clock()

mp = {
    'unit_size': 100
} # описание клеток по типу {(x, y): 'color\0(25, 25, 25)'} или еще както. unit_size только настраивать!
player = {
    'x'     : 0,
    'y'     : 0,
    'speed' : 7,
    'zoom'  : 0.75,
    'figure': pygame.draw.rect
}

move_right = False
move_left = False
move_up = False
move_down = False

while True:
    sc.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            elif event.key == pygame.K_LEFT:
                move_left = True
            elif event.key == pygame.K_UP:
                move_up = True
            elif event.key == pygame.K_DOWN:
                move_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            elif event.key == pygame.K_RIGHT:
                move_right = False
            elif event.key == pygame.K_UP:
                move_up = False
            elif event.key == pygame.K_DOWN:
                move_down = False
    
    if move_right:
        player['x'] += player['speed']
    if move_left:
        player['x'] -= player['speed']
    if move_down:
        player['y'] -= player['speed']
    if move_up:
        player['y'] += player['speed']
    
    # print(unit_wh)
    start_pos_x = math.ceil(player['x'] - W / 2 / player['zoom'])
    start_pos_y = math.ceil(player['y'] - H / 2 / player['zoom'])
    end_pos_x   = math.ceil(player['x'] + W / 2 / player['zoom'])
    end_pos_y   = math.ceil(player['y'] + H / 2 / player['zoom'])

    if DEBUG_LINES:
        for x in range(start_pos_x, end_pos_x + 1):
            if abs(x % mp['unit_size']) == 0:
                coord = (abs(x - start_pos_x) * player['zoom'])
                pygame.draw.aaline(sc, WHITE, [coord, 0], [coord, H])
        for y in range(start_pos_y, end_pos_y + 1):
            if abs(y % mp['unit_size']) == 0:
                coord = (abs(y - end_pos_y) * player['zoom'])
                pygame.draw.aaline(sc, WHITE, [0, coord], [W, coord])
    
    player['figure'](sc, BLUE, (W / 2 - 5, H / 2 - 10, 25, 50))
    pygame.display.update()
    p_clock.tick(FPS)