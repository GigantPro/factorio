import math
import random
import time
import pygame
from player import Player
import config
from map import Map


class Camera:
    def __init__(self, sc: pygame.Surface, game_class, player: Player, mp: Map, clock, font) -> None:
        self.sc = sc
        self.core = game_class
        self.player = player
        self.mp = mp
        self.clock = clock
        self.font = font

        self.h = self.sc.get_height()
        self.w = self.sc.get_width()

        # self.pers = pygame.image.load('pers_zad.png')

        self.player_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    def print_fps(self, clock: pygame.time.Clock, font: pygame.font.Font):
        text = font.render(str(int(clock.get_fps())), False, (255, 255, 255))
        self.sc.blit(text, (0, 0))

    def draw_map(self):
        self.sc.fill((0, 0, 0))
        
        self._draw_big_chunks(self.mp.get_map())

        # if config.debug:
        #     self.draw_grid_chunks(self.start_pos_x, self.start_pos_y, self.end_pos_x, self.end_pos_y)
        if config.fps_counter:
            self.print_fps(self.clock, self.font)
        
        self.draw_player()

        pygame.display.update()

    def draw_grid_chunks(self, start_pos_x, start_pos_y, end_pos_x, end_pos_y):
        for x in range(int(start_pos_x), int(end_pos_x) + 1):
            if x % (config.chunk_size * self.player.zoom) == 0:
                coord = (abs(x - start_pos_x) * config.max_zoom)
                pygame.draw.aaline(self.sc, (255, 255, 255), [coord, 0], [coord, self.h])
        for y in range(int(start_pos_y), int(end_pos_y) + 1):
            if abs(y % (config.chunk_size * self.player.zoom)) == 0:
                coord = (abs(y - end_pos_y) / config.max_zoom)
                pygame.draw.aaline(self.sc, (255, 255, 255), [0, coord], [self.w, coord])
    
    def draw_player(self):
        x, y = self._xy_to_monitor_xy(*self.player.get_coords())
        x = x - config.cell_size / 2 * self.player.zoom
        y = y - config.cell_size * 2 * self.player.zoom
        pygame.draw.rect(self.sc, self.player_color, (x, y, config.cell_size * self.player.zoom, config.cell_size * 2 * self.player.zoom))  

    def _draw_big_chunks(self, mp):
        x1, y1, x2, y2 = self._get_xy_visible_chunk()
        for coord in mp:
            tmp = tuple(coord.split(', '))
            tmp = (int(tmp[0]), int(tmp[1]))
            if tmp >= (x1, y1) and tmp <= (x2, y2):
                self._draw_small_chunks(mp[coord])
            
    def _draw_small_chunks(self, big_chank):
        for coo in big_chank:
            x, y = tuple(map(int, coo.split(', ')))
            mon_xy = self._xy_to_monitor_xy(x, y)
            if big_chank[f'{x}, {y}'] == '3':
                # self.sc.blit(self.pers, (config.cell_size * self.player.zoom, config.cell_size * self.player.zoom))
                pygame.draw.rect(self.sc, (50, 10, 200), (mon_xy[0], mon_xy[1], config.cell_size * self.player.zoom, config.cell_size * self.player.zoom))  
            elif big_chank[f'{x}, {y}'] == 'cuprum':
                pass
            elif big_chank[f'{x}, {y}'] == 'cuprum':
                pass
            elif big_chank[f'{x}, {y}'] == 'cuprum':
                pass
            elif big_chank[f'{x}, {y}'] == 'cuprum':
                pass
            elif big_chank[f'{x}, {y}'] == 'cuprum':
                pass
            else:
                pass

    def _xy_to_monitor_xy(self, x1: int, y1: int) -> tuple[float, float]:
        return (((self.w / 2) + (x1 - self.player.x) * self.player.zoom), ((self.h / 2) - (y1 - self.player.y) * self.player.zoom))
    
    def _get_xy_visible_chunk(self) -> tuple[int, int, int, int]:
        x1 = self.player.x - (((self.w * self.player.zoom) // config.chunk_size) * config.chunk_size) 
        x2 = self.player.x + (((self.w * self.player.zoom) // config.chunk_size) * config.chunk_size)
        y1 = self.player.y + (((self.h * self.player.zoom) // config.chunk_size) * config.chunk_size)
        y2 = self.player.y - (((self.h * self.player.zoom) // config.chunk_size) * config.chunk_size)
        return x1, y1, x2, y2