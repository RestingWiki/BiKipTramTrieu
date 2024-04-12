import threading
from src.game_init.load_data2 import LoadData
from src.pokemon import Pokemon
from nguyenpanda.swan import Color

MAX_POKEMON_ID: int = 1025


class GameInit:

    def __init__(self, team_1=3, team_2=3):
        LoadData()
        self._team_1 = team_1
        self._team_2 = team_2
        self._pokemons = []
        # self._pokemons.append(Pokemon(1))
        # self._load_Image()
        self._pokemons = [Pokemon(n) for n in range(1, MAX_POKEMON_ID + 1)]

    def get_pokemons(self, _id: int):
        return self._pokemons[_id - 1]

    @staticmethod
    def get_pokemon_dict_data():
        return LoadData()

    def _load_Image(self):
        start_id = 1
        end_id = 1025  # Range is [start_id, end_id)
        num_threads = 10
        threads = []
        ids_per_thread = (end_id - start_id) // num_threads
        for i in range(num_threads + 1):
            thread_start_id = start_id + i * ids_per_thread
            thread_end_id = start_id + (i + 1) * ids_per_thread
            if thread_start_id == 1021:
                thread_end_id = 1026
            thread = threading.Thread(target=self._load_image_from_file, args=(thread_start_id, thread_end_id))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    def _load_image_from_file(self, startID: int, endID: int):
        print(Color['b'] + str(startID) + " -> " + str(endID) + Color.reset)
        for i in range(startID, endID):
            if i == 1:
                continue
            self._pokemons.append(Pokemon(i))


if __name__ == '__main__':
    game_init = GameInit()
