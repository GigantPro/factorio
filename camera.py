import math
import pygame
from player import Player
import config
# import game_core


class Camera:
    def __init__(self, sc: pygame.Surface, game_class, player: Player) -> None:
        self.sc = sc
        self.core = game_class
        self.player = player

        self.h = self.sc.get_height()
        self.w = self.sc.get_width()
    
    def draw_map(self):
        self.sc.fill((0, 0, 0))

        start_pos_x = math.ceil(self.player.x - self.w / 2 / self.player.zoom)
        start_pos_y = math.ceil(self.player.y - self.h / 2 / self.player.zoom)
        end_pos_x   = math.ceil(self.player.x + self.w / 2 / self.player.zoom)
        end_pos_y   = math.ceil(self.player.y + self.h / 2 / self.player.zoom)

        if self.core.debug:
            self.draw_grid_chunks(start_pos_x, start_pos_y, end_pos_x, end_pos_y)
        
        self.draw_player()

        pygame.display.update()

    def draw_grid_chunks(self, start_pos_x, start_pos_y, end_pos_x, end_pos_y):
        for x in range(start_pos_x, end_pos_x + 1):
            if abs(x % config.chunk_size) == 0:
                coord = (abs(x - start_pos_x) * config.zoom)
                pygame.draw.aaline(self.sc, (255, 255, 255), [coord, 0], [coord, self.h])
        for y in range(start_pos_y, end_pos_y + 1):
            if abs(y % config.chunk_size) == 0:
                coord = (abs(y - end_pos_y) * config.zoom)
                pygame.draw.aaline(self.sc, (255, 255, 255), [0, coord], [self.w, coord])
    
    def draw_player(self):
        pygame.draw.rect(self.sc, (0, 255, 0), (self.w / 2 - 5, self.h / 2 - 10, 25, 50))  