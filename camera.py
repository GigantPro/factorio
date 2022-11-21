import math
import pygame
from player import Player
import config
from map import Map


class Camera:
    def __init__(self, sc: pygame.Surface, game_class, player: Player, mp: Map) -> None:
        self.sc = sc
        self.core = game_class
        self.player = player
        self.mp = mp

        self.h = self.sc.get_height()
        self.w = self.sc.get_width()
    
    def draw_map(self):
        self.sc.fill((0, 0, 0))

        self.start_pos_x = math.ceil(self.player.x - self.w / 2)
        self.start_pos_y = math.ceil(self.player.y - self.h / 2)
        self.end_pos_x   = math.ceil(self.player.x + self.w / 2)
        self.end_pos_y   = math.ceil(self.player.y + self.h / 2)

        # mp = self.mp.return_generation_chunks_with_coords(
        #     self.start_pos_x // config.chunk_size * config.chunk_size,
        #     self.start_pos_y // config.chunk_size * config.chunk_size,
        #     self.end_pos_x   // config.chunk_size * config.chunk_size,
        #     self.end_pos_y   // config.chunk_size * config.chunk_size,
        #     {
        #         (0, 0.7): 'grass',
        #         (0.7, 0.8): 'iron',
        #         (0.8, 0.85): 'cuprum',
        #         (0.85, 1): 'ground'
        #     }
        # )
        # self._draw_map(mp)

        if self.core.debug:
            self.draw_grid_chunks(self.start_pos_x, self.start_pos_y, self.end_pos_x, self.end_pos_y)
        
        self.draw_player()

        pygame.display.update()

    def draw_grid_chunks(self, start_pos_x, start_pos_y, end_pos_x, end_pos_y):
        for x in range(start_pos_x, end_pos_x + 1):
            if x % (config.chunk_size // self.player.zoom) == 0:
                coord = (abs(x - start_pos_x) * config.zoom)
                pygame.draw.aaline(self.sc, (255, 255, 255), [coord, 0], [coord, self.h])
        for y in range(start_pos_y, end_pos_y + 1):
            if abs(y % (config.chunk_size // self.player.zoom)) == 0:
                coord = (abs(y - end_pos_y) * config.zoom)
                pygame.draw.aaline(self.sc, (255, 255, 255), [0, coord], [self.w, coord])
    
    def draw_player(self):
        pygame.draw.rect(self.sc, (100, 100, 100), (self.w / 2 - 5, self.h / 2 - 10, 25, 50))  
    
    def _draw_map(self, mp):
        for x, y in mp:
            if mp[(x, y)] == 'grass':
                pygame.draw.rect(self.sc, (0, 255, 0), 
                        ((x - self.start_pos_x) * config.zoom, (y - self.start_pos_y) * config.zoom, config.chunk_size, config.chunk_size))
            elif mp[(x, y)] == 'iron':
                pass
            elif mp[(x, y)] == 'cuprum':
                pass
            elif mp[(x, y)] == 'ground':
                pass