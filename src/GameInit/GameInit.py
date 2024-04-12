from src.GameInit import LoadData
from src.Pokemon import Pokemon

MAX_POKEMON_ID: int = 1025


class GameInit:

    def __init__(self, team_1=3, team_2=3):
        self._team_1 = team_1
        self._team_2 = team_2
        self._pokemons = [Pokemon(n) for n in range(1, MAX_POKEMON_ID + 1)]

    def get_pokemons(self, _id: int):
        return self._pokemons[_id - 1]

    @staticmethod
    def get_pokemon_dict_data():
        return LoadData()


if __name__ == '__main__':
    game_init = GameInit()

