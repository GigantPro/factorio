import pygame
from player import Player
from map import Map
from camera import Camera
from threading import Thread
import config


class Core:
    def __init__(self, W: int=None, H: int=None, debug: bool=config.debug, fps: int=config.max_fps) -> None:
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

        self.player = Player(0, 0, config.speed, 1)
        if config.seed:
            self.map = Map(config.seed)
        else:
            self.map = Map()

        self.font = pygame.font.SysFont('Ariel', 25)
        self.camera = Camera(self.sc, self, self.player, self.map, self.p_clock, self.font)

        self._map_init()
        self.map.load_map(self.name_save)
        
        self.last_frame_delta = 1
    
    def start_game(self):
        self.flag_stop_game_thread = False
        self.game_run_thread = Thread(target=self._game_run).run()
    
    def _game_run(self):

        while not self.flag_stop_game_thread:
            thread = Thread(target=self.map.generate_visible_chunks,
                            args=([self.player.chunk_x, self.player.chunk_y],))
            delta_time = self.p_clock.tick(self.fps) / 1000

            if self.player.chunk_changed_flag:

                # self.map.generate_visible_chunks([self.player.chunk_x, self.player.chunk_y])
                thread.start()
                self.player.chunk_changed_flag = False

            self.player.keyboard_move(delta_time)
            self.camera.draw_map()

        return
    
    def _map_init(self):
        self.map.set_camera(self.camera)
        self.map.create_new_map()
        self.name_save = self.map.save_map()