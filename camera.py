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

FPS = 60
p_clock = pygame.time.Clock()

mp = {
    'unit_size': 5
} # описание клеток по типу {(x, y): 'color\0(25, 25, 25)'}
player = {
    'x'     : 0,
    'y'     : 0,
    'speed' : 50,
    'zoom'  : 1,
    'figure': pygame.draw.rect
}

while True:
    sc.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player['x'] += player['speed']
            elif event.key == pygame.K_RIGHT:
                pass
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_RIGHT:
                pass
    
    # print(unit_wh)
    start_pos_x = math.ceil(player['x'] - W / 2 / player['zoom'] * (W / 2))
    start_pos_y = math.ceil(player['y'] - H / 2 / player['zoom'] * (H / 2))
    end_pos_x   = math.ceil(player['x'] + W / 2 / player['zoom'] * (W / 2))
    end_pos_y   = math.ceil(player['y'] + H / 2 / player['zoom'] * (H / 2))
    print(start_pos_x)



    # print(start_pos_x, start_pos_y, end_pos_x, end_pos_y) # -50 -30 50 30

    for x in range(start_pos_x, end_pos_x + 1):
        # print(x, '###########')
        if abs(x % mp['unit_size']) == 0:
            coord = math.ceil(((end_pos_x - start_pos_x) / mp['unit_size']) * ((x / mp['unit_size']) - (start_pos_x / mp['unit_size'])))
            pygame.draw.rect(sc, WHITE, (coord, 0, 1, H))
            print(x, coord)
    
    player['figure'](sc, BLUE, (W / 2 - 5, H / 2 - 10, 25, 50))
    pygame.display.update()
    p_clock.tick(FPS)