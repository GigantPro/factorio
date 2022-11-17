import pygame


pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H))

pygame.display.set_caption('Заголовок окна')
# pygame.display.set_icon(pygame.image.load('ico.bmp'))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

FPS = 60
p_clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_RIGHT:
                pass
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_RIGHT:
                pass
    p_clock.tick(FPS)