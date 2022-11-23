import pygame
from player import Player
from map import Map
from camera import Camera
from threading import Thread
from datetime import datetime
import config


class Core:
    def __init__(self, W: int=None, H: int=None, debug: bool=config.debug, fps: int=config.fps) -> None:
        self.debug = debug
        self.fps = fps
        
        pygame.init()
        self.display_info = pygame.display.Info()
        if not W or not H:
            self.W = self.display_info.current_w
            self.H = self.display_info.current_h
        else:
            self.W = W
            self.H = H
        self.sc = pygame.display.set_mode((self.W, self.H), pygame.FULLSCREEN)
        self.p_clock = pygame.time.Clock()

        self.player = Player(0, 0, config.speed, config.zoom)
        if config.seed:
            self.map = Map(config.seed)
        else:
            self.map = Map()
        self.camera = Camera(self.sc, self, self.player, self.map)
        
        self.last_frame_delta = 1
    
    def start_game(self):
        self.flag_stop_game_thread = False
        self.game_run_thread = Thread(target=self._game_run).run()
    
    def _game_run(self):
        while not self.flag_stop_game_thread:
            delta_time = self.p_clock.tick(self.fps)

            self.player.keyboard_move(delta_time)
            self.camera.draw_map()
        return
