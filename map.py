import os
import random
import config
import json
from perlin_noise import PerlinNoise
from pprint import pprint


class Map:
    def __init__(self, seed: int = random.randint(10000, 1000000)) -> None:
        self.seed = seed
        self.resources = {
            '1': (-1, 0),  # ground
            '2': (0, 0.1),  # iron
            '3': (0.1, 0.2),  # copper
            '4': (0, 2, 0.35),  # coal
            '5': (0.35, 1)  # water
        }

    def create_chunk(self, left, top):
        noise1 = PerlinNoise(octaves=3, seed=self.seed)
        noise2 = PerlinNoise(octaves=6, seed=self.seed)
        noise3 = PerlinNoise(octaves=12, seed=self.seed)

        size = config.big_chunk_size
        values = {}
        for i in range(size):
            for j in range(size):
                noise_val = noise1([i / size, j / size])
                noise_val += 0.5 * noise2([i / size, j / size])
                noise_val += 0.25 * noise3([i / size, j / size])

                res_id = -1
                for k, v in self.resources.items():
                    if v[0] < noise_val <= v[1]:
                        res_id = k

                values[(left + i, top - j)] = res_id
        self.save_map(values)
        # pprint(values)

    #
    # def return_generation_chunks_with_coords(self, x1, y1, x2, y2, chanse):
    #     mp = {}
    #     rndd = random.Random(self.seed + x1 + x2 + y1 + y2)
    #     for x in range(x1, x2 + 1, config.chunk_size):
    #         for y in range(y1, y2 + 1, config.chunk_size):
    #             rnd = rndd.random()
    #             for ch in chanse:
    #                 if ch[0] <= rnd and ch[1] >= rnd:
    #                     mp[(x, y)] = chanse[ch]
    #                     break
    #     # self.save_map(mp)
    #     return mp

    def save_map(self, map):
        # dir_path = f"/maps"
        # if not os.path.exists(dir_path):
        #     os.makedirs(dir_path)

        with open(f'{self.seed}.txt', 'w') as f:
            f.write(str(map))


nm = Map()
nm.create_chunk(0, 0)
