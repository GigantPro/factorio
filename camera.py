import math
import random
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

        self.player_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

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
            if x % (config.chunk_size * self.player.zoom) == 0:
                coord = (abs(x - start_pos_x) * config.zoom)
                pygame.draw.aaline(self.sc, (255, 255, 255), [coord, 0], [coord, self.h])
        for y in range(start_pos_y, end_pos_y + 1):
            if abs(y % (config.chunk_size * self.player.zoom)) == 0:
                coord = (abs(y - end_pos_y) / config.zoom)
                pygame.draw.aaline(self.sc, (255, 255, 255), [0, coord], [self.w, coord])
    
    def draw_player(self):
        pygame.draw.rect(self.sc, self.player_color, (self.w / 2 - 10 * self.player.zoom, self.h / 2 - 20 * self.player.zoom, 20 * self.player.zoom, 40 * self.player.zoom))  
    
    def _draw_big_chunks(self, mp):
        player_coord = self.player.get_coords()
        monitor_coord_x = player_coord[0] - (self.w / 2) * self.player.zoom
        monitor_coord_y = player_coord[1] - (self.h / 2) * self.player.zoom
        for coord in mp:
            self._draw_small_chunks(mp[coord], (monitor_coord_x, monitor_coord_y))
            
    def _draw_small_chunks(self, big_chank, monitor_coord):
        for x, y in big_chank:
            mon_xy = self._xy_to_monitor_xy(x, y, *monitor_coord)
            if big_chank[(x, y)] == 'cuprum':
                pygame.draw.rect(self.sc, (50, 10, 200), (mon_xy[0], mon_xy[1], config.chunk_size * self.player.zoom, config.chunk_size * self.zoom))  
            elif big_chank[(x, y)] == 'cuprum':
                pass
            elif big_chank[(x, y)] == 'cuprum':
                pass
            elif big_chank[(x, y)] == 'cuprum':
                pass
            elif big_chank[(x, y)] == 'cuprum':
                pass
            elif big_chank[(x, y)] == 'cuprum':
                pass
            else:
                pass

    def _xy_to_monitor_xy(self, x1: int, y1: int, x2: int, y2: int) -> tuple[int, int]:
        return tuple(1, 1)