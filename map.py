import os
import random
import config
import json


class Map:
    def __init__(self, seed: int= random.randint(10000, 1000000)) -> None:
        self.seed = seed

    def get_resourses_types(self):
        return {
            1: 'iron',
            2: 'cuprum',
            3: 'water',
            4: 'ground',
            5: 'grass'
        }
    
    # def create_first_big_chunk(self):
    #     _map = {}
    #     for x in range(x1, x2 + 1, config.chunk_size):
    #         for y in range(y1, y2 + 1, config.chunk_size):

    def return_generation_chunks_with_coords(self, x1, y1, x2, y2, chanse):
        mp = {}
        rndd = random.Random(self.seed + x1 + x2 + y1 + y2)
        for x in range(x1, x2 + 1, config.chunk_size):
            for y in range(y1, y2 + 1, config.chunk_size):
                rnd = rndd.random()
                for ch in chanse:
                    if ch[0] <= rnd and ch[1] >= rnd:
                        mp[(x, y)] = chanse[ch]
                        break
        # self.save_map(mp)
        return mp
    
    def save_map(self, map):
        dir_path = f"{os.environ['APPDATA']}\\GigantPro"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        with open(f'{dir_path}\\saves\\{self.seed}.json') as f:
            json.dump(f, map)