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

        self.player_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    def print_fps(self, clock: pygame.time.Clock, font: pygame.font.Font):
        start_time = time.time()
        text = font.render(str(int(clock.get_fps())), False, (255, 255, 255))
        self.sc.blit(text, (0, 0))
        print(time.time() - start_time)

    def draw_map(self):
        self.sc.fill((0, 0, 0))

        # self.start_pos_x = self.player.x - (self.w / 2) / self.player.zoom
        # self.start_pos_y = self.player.y + (self.h / 2) / self.player.zoom
        # self.end_pos_x   = self.player.x + (self.w / 2) / self.player.zoom
        # self.end_pos_y   = self.player.y - (self.h / 2) / self.player.zoom

        self.start_pos_x, self.start_pos_y, self.end_pos_x, self.end_pos_y = self._get_start_pos_monitor()

        self._draw_big_chunks(self.mp.load_map(self.core.name_save))

        if self.core.debug:
            self.draw_grid_chunks(self.start_pos_x, self.start_pos_y, self.end_pos_x, self.end_pos_y)
        
        self.draw_player()

        pygame.display.update()

    def draw_grid_chunks(self, start_pos_x, start_pos_y, end_pos_x, end_pos_y):
        for x in range(int(start_pos_x), int(end_pos_x) + 1):
            if x % (config.chunk_size * self.player.zoom) == 0:
                coord = (abs(x - start_pos_x) * config.zoom)
                pygame.draw.aaline(self.sc, (255, 255, 255), [coord, 0], [coord, self.h])
        for y in range(int(start_pos_y), int(end_pos_y) + 1):
            if abs(y % (config.chunk_size * self.player.zoom)) == 0:
                coord = (abs(y - end_pos_y) / config.zoom)
                pygame.draw.aaline(self.sc, (255, 255, 255), [0, coord], [self.w, coord])
    
    def draw_player(self):
        # pygame.draw.rect(self.sc, self.player_color, (self.w / 2 - 10 * self.player.zoom, self.h / 2 - 20 * self.player.zoom, 20 * self.player.zoom, 40 * self.player.zoom))  
        pygame.draw.rect(self.sc, self.player_color, (*self._xy_to_monitor_xy(*self.player.get_coords()), 20 * self.player.zoom, 40 * self.player.zoom))  
    
    def _draw_big_chunks(self, mp):
        player_coord = self.player.get_coords()
        monitor_coord_x = player_coord[0] - (self.w / 2) / self.player.zoom
        monitor_coord_y = player_coord[1] - (self.h / 2) / self.player.zoom
        for coord in mp:
            self._draw_small_chunks(mp[coord], (monitor_coord_x, monitor_coord_y))
            
    def _draw_small_chunks(self, big_chank, monitor_coord):
        for coo in big_chank:
            x, y = tuple(map(int, coo.split(', ')))
            mon_xy = self._xy_to_monitor_xy(x, y)
            if big_chank[f'{x}, {y}'] == '3':
                pygame.draw.rect(self.sc, (50, 10, 200), (mon_xy[0], mon_xy[1], config.chunk_size * self.player.zoom, config.chunk_size * self.player.zoom))  
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

    def _xy_to_monitor_xy(self, x1: int, y1: int) -> tuple[int, int]:
        x21, y21, x22, y22 = self._get_start_pos_monitor()
        x = y = 0
        if x21 >= 0:   # X >= 0
            x = x21 - abs(x1)
        elif x21 < 0:  # X <  0
            x = abs(x21) - x1

        if y21 >= 0:   # Y >= 0
            y = y21 - abs(y1)
        elif y21 < 0:  # Y <  0
            y = abs(y21) - abs(y1)
        return (x, y)
    
    def _get_start_pos_monitor(self) -> tuple[int, int, int, int]:
        x1 = y1 = x2 = y2 = 0
        if self.player.x >= 0:   # X >= 0
            x1 = self.player.x - (self.w / 2) / self.player.zoom
        elif self.player.x < 0:  # X <  0
            self.player.x + (self.w / 2) / self.player.zoom

        if self.player.y >= 0:   # Y >= 0
            self.player.y + (self.h / 2) / self.player.zoom
        elif self.player.y < 0:  # Y <  0
            self.player.y - (self.h / 2) / self.player.zoom
        return (x1, y1, x2, y2)