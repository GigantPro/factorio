import math
import random
from threading import Thread
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
        text = font.render(str(int(clock.get_fps())), False, (255, 255, 255))
        self.sc.blit(text, (0, 0))

    def draw_map(self):
        self.sc.fill((0, 0, 0))
        
        # self._draw_big_chunks(self.mp.get_map())
        self.start_rendering = True
        self.visible_chunks = self.mp.return_visible_chunks_cords()
        self._draw_big_chunks(self.visible_chunks)
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
 
    def _draw_big_chunks(self, cords):
        chunks_threads = []
        for cord in cords:
            temp = Thread(target=self._draw_small_chunks(self.mp.get_map()[cord]))
            temp.start()
            chunks_threads.append(temp)
        [i.join() for i in chunks_threads]

    def _draw_small_chunks(self, big_chank):
        for coo in big_chank:
            x, y = tuple(map(int, coo.split(', ')))
            mon_xy = self._xy_to_monitor_xy(x, y)
            if big_chank[f'{x}, {y}'] == '3':
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
        return ((self.w / 2) + (x1 - self.player.x) * self.player.zoom), ((self.h / 2) - (y1 - self.player.y) * self.player.zoom)
    
    def start_threads(self, threads_count: int=4) -> None:
        self.threads_rendering = []
        for i in  range(threads_count):
            self.threads_rendering.append(Thread(target=self._rendering_zone, args=(i,)))
            self.threads_rendering[-1].start()
    
    def _rendering_zone(self, index):
        start_monitor_pos = (self.w // index, self.h // index)
        while True:
            if self.start_rendering:
                for i in self.visible_chunks:
                    x, y = tuple(map(int, i.split(', ')))
                    x, y = self._xy_to_monitor_xy(x, y)
                    if x < start_monitor_pos[0] and y < start_monitor_pos[1]:
                        for big_chank in i:
                            if big_chank[f'{x}, {y}'] == '3':
                                pygame.draw.rect(self.sc, (50, 10, 200), (x, y, config.cell_size * self.player.zoom, config.cell_size * self.player.zoom))  
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

            else:
                pass