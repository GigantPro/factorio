import os
import random
import time
import config
import json
from threading import Thread

from perlin_noise import PerlinNoise


class Map:
    # в ините можно загрузить мапу
    def __init__(self, seed: int = random.randint(10000, 1000000)) -> None:
        self.seed = seed
        self.camera = None
        self.player = None
        self.map = {}
        self.new_map = {}
        self.resources = {
            '1': (-1, 0),  # ground
            '2': (0, 0.1),  # iron
            '3': (0.1, 0.2),  # copper
            '4': (0.2, 0.35),  # coal
            '5': (0.35, 1)  # water
        }

        self.stop_save_thread       = False
        self.save_thread            = Thread(target=self._save_map_time)
        self.save_thread.start()

        self.stop_updating_map      = False
        self.updating_map_thread    = Thread(target=self._update_map)
        self.updating_map_thread.start()


    def load_map(self, file_name: str) -> dict:
        with open(file_name, 'r', encoding='utf-8') as f:
            self.map = json.load(f)
            self.seed = int(file_name.rstrip('.json').split('/')[-1])
        return self.get_map()

    def get_map(self) -> dict:
        return self.map

    def create_new_map(self):
        self.generate_visible_chunks([0, 0])

    def set_camera(self, camera):
        self.camera = camera
        self.player = self.camera.player

    def save_map(self) -> str:
        dir_path = f"maps"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        with open(f'{dir_path}/{self.seed}.json', 'w', encoding='utf-8') as f:
            json.dump(self.map, f, indent=2)
        return f'{dir_path}/{self.seed}.json'

    def generate_visible_chunks(self, player_chunk: list[int, int] = None, new = True):
        if not player_chunk:
            x1 = int(self.player.x // config.cell_size // config.chunk_size)
            y1 = int(self.player.y // config.cell_size // config.chunk_size)
            player_chunk = (x1, y1)
        # print(player_chunk)
        count_chunk_col = int(self.camera.w / config.min_zoom // config.cell_size // config.chunk_size + 2)
        count_chunk_row = int(self.camera.h / config.min_zoom // config.cell_size // config.chunk_size + 2)

        left = player_chunk[0] - count_chunk_col // 2
        top = player_chunk[1] + count_chunk_row // 2
        if not new:
            for x in range(count_chunk_col):
                for y in range(count_chunk_col):
                    self.map[f'{left + x}, {top - y}'] = self.map.get(f'{left + x}, {top - y}',
                                                                    self._create_chunk(left + x, top - y))
        else:
            for y in range(count_chunk_col):
                self.new_map[f'{left + x}, {top - y}'] = self.map.get(f'{left + x}, {top - y}',
                                                                self._create_chunk(left + x, top - y))
        # self.save_thread.start()
        
    def _create_chunk(self, left, top):
        noise1 = PerlinNoise(octaves=3, seed=self.seed + left + top + left * top + random.randint(1, 100))
        noise2 = PerlinNoise(octaves=6, seed=self.seed + left + top + left * top + random.randint(1, 100))
        noise3 = PerlinNoise(octaves=12, seed=self.seed + left + top + left * top + random.randint(1, 100))

        size = config.chunk_size
        chunk = {}
        for i in range(size):
            for j in range(size):

                noise_val = noise1([i / size, j / size])
                noise_val += 0.5 * noise2([i / size, j / size])
                noise_val += 0.25 * noise3([i / size, j / size])

                res_id = -1
                for k, v in self.resources.items():
                    if v[0] < noise_val <= v[1]:
                        res_id = k

                chunk[
                    f'{(left * config.chunk_size + i) * config.cell_size}, {(top * config.chunk_size - j) * config.cell_size}'] = res_id
        return chunk

    def _get_player_coords(self):
        return self.player.x, self.player.y

    def _get_player_chunk(self):
        left = self.player.x // config.cell_size // config.chunk_size
        top = self.player.y // config.cell_size // config.chunk_size
        return left, top

    def _save_map_time(self):
        while not self.stop_save_thread:
            time.sleep(300)
            self.save_map()

    def _update_map(self):
        while not self.stop_save_thread:
            time.sleep(1)
            self.generate_visible_chunks(new = True)
