import numpy
import random
import pygame


class MapGenerator:
    def __init__(self):
        self.ground_image = pygame.image.load('resourses/ground.png').convert()
        self.coal_image = pygame.image.load('resourses/coal.png').convert()
        self.tree_image = pygame.image.load('resourses/tree.png').convert()
        self.iron_image = pygame.image.load('resourses/iron.png').convert()
        # добавить все текстуры

    def generate_arr(self):
        point_arr = numpy.zeros([1000, 1000], numpy.uint16)
        for i in range(1000):
            for x in range(len(point_arr[i])):
                if random.random() <= 0.15:
                    point_arr[i][x] = 1
                elif 0.9 <= random.random() < 0.95:
                    point_arr[i][x] = 2
                elif 0.89 <= random.random() < 0.9:
                    point_arr[i][x] = 3

        return point_arr

    def draw_map(self, screen):
        arr = self.generate_arr()
        color = [self.ground_image,self.tree_image,self.coal_image, self.iron_image]
        for x in range(len(arr)):
            for y in range(len(arr[x])):
                screen.blit(color[arr[x][y]], (x * 32, y * 32, x * 32 + 32, y * 32 + 32))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 1000, 1000
    screen = pygame.display.set_mode(size)
    screen.fill('white')

    running = True
    map = MapGenerator()
    map.draw_map(screen)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
    pygame.quit()