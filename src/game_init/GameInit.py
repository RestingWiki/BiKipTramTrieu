import threading

from nguyenpanda.swan import Color

from src.load_data import LoadData
from src.pokemon.Pokemon import Pokemon

MAX_POKEMON_ID: int = 1025


class GameInit:

    def __init__(self, team_1=3, team_2=3):
        LoadData()
        self._team_1 = team_1
        self._team_2 = team_2
        self._pokemons = []
        self._load_Image()

    def pokemons(self):
        return self._pokemons

    def get_pokemons(self, _id: int):
        return self._pokemons[_id - 1]

    @staticmethod
    def get_pokemon_dict_data():
        return LoadData()

    def _load_Image(self):
        start_id = 1
        end_id = 1026  # Range is [start_id, end_id)
        num_threads = 10
        threads = []
        ids_per_thread = (end_id - start_id) // num_threads
        for i in range(num_threads + 1):
            thread_start_id = start_id + i * ids_per_thread
            thread_end_id = start_id + (i + 1) * ids_per_thread
            if thread_start_id == start_id + num_threads * ids_per_thread:
                thread_end_id = 1026
            thread = threading.Thread(target=self._load_image_from_file, args=(thread_start_id, thread_end_id))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    def _load_image_from_file(self, start_id: int, end_id: int):
        print(Color['b'] + str(start_id) + " -> " + str(end_id) + Color.reset)
        for i in range(start_id, end_id):
            self._pokemons.append(Pokemon(i))

    def __repr__(self):
        return f'<{self.__class__.__name__}: {len(self._pokemons)} Pokemons>'

    def __str__(self):
        return f'{self.__class__.__name__}({self._team_1}, {self._team_2}, {len(self._pokemons)})'


if __name__ == '__main__':
    game_init = GameInit()
    print(game_init)
