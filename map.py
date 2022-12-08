import os
import random
import config
import json

from perlin_noise import PerlinNoise


class Map:
    # в ините можно загрузить мапу
    def __init__(self, seed: int = random.randint(10000, 1000000)) -> None:
        self.seed = seed
        self.camera = None
        self.player = None
        self.map = {}
        self.resources = {
            '1': (-1, 0),  # ground
            '2': (0, 0.1),  # iron
            '3': (0.1, 0.2),  # copper
            '4': (0.2, 0.35),  # coal
            '5': (0.35, 1)  # water
        }

    def load_map(self, file_name: str) -> None:
        with open(file_name, 'r', encoding='utf-8') as f:
            self.map = json.load(f)
            self.seed = int(file_name.rstrip('.json').split('/')[-1])

    def get_map(self):
        return self.map

    def create_new_map(self) -> None:
        self.generate_visible_chunks([0, 0])

    def set_camera(self, camera) -> None:
        self.camera = camera
        self.player = self.camera.player

    def save_map(self) -> str:
        dir_path = f"maps"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        with open(f'{dir_path}/{self.seed}.json', 'w', encoding='utf-8') as f:
            json.dump(self.map, f, indent=2)
        return f'{dir_path}/{self.seed}.json'

    def generate_visible_chunks(self, player_chunk: list[int, int]):
        count_chunk_col = int(self.camera.w / config.min_zoom // config.cell_size // config.chunk_size + 2)
        count_chunk_row = int(self.camera.h / config.min_zoom // config.cell_size // config.chunk_size + 4)
        # count_chunk_col = int(1920 / config.min_zoom // config.cell_size // config.chunk_size + 2)
        # count_chunk_row = int(1280 / config.min_zoom // config.cell_size // config.chunk_size + 4)


        left = player_chunk[0] - count_chunk_col // 2
        top = player_chunk[1] + count_chunk_row // 2

        for x in range(count_chunk_col):
            for y in range(count_chunk_col):
                self.map[f'{left + x}, {top - y}'] = self.map.get(f'{left + x}, {top - y}',
                                                                  self._create_chunk(left + x, top - y))
        self.save_map()

    def return_visible_chunks_cords(self) -> list:
        player_chunk = self._get_player_chunk()
        count_chunk_col = int(self.camera.w / config.min_zoom // config.cell_size // config.chunk_size + 2)
        count_chunk_row = int(self.camera.h / config.min_zoom // config.cell_size // config.chunk_size + 4)

        left = player_chunk[0] - count_chunk_col // 2
        top = player_chunk[1] + count_chunk_row // 2

        cords = []

        for x in range(count_chunk_col):
            for y in range(count_chunk_col):
                if f'{left + x}, {top - y}' in self.map.keys():
                    cords.append(f'{left + x}, {top - y}')

        return cords

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

    def _get_player_chunk(self):
        left = int(self.player.x // config.cell_size // config.chunk_size)
        top = int(self.player.y // config.cell_size // config.chunk_size)
        return left, top


# m = Map()
# m.create_new_map()
# print(m.get_map().keys())