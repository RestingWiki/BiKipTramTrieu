import concurrent.futures
import time

from requests import Response, get as requests_get


class StatusError(Exception):
    def __init__(self, response: Response):
        super().__init__(f'Status code {response.status_code}: {response.text}')


class Pokemon:
    def __init__(self, _dict: dict):
        # @formatter:off
        self._id: int       = _dict['id']
        self._name: str     = _dict['name']
        self._height: int   = _dict['height']
        self._weight: int   = _dict['weight']

        type_list: list = _dict['types']
        self._type_1: str   = type_list[0]['type']['name']
        if len(type_list) == 2:
            self._type_2: str = type_list[1]['type']['name']
        else:
            self._type_2: str = 'null'

        self._hp: int       = _dict['stats'][0]['base_stat']
        self._atk: int      = _dict['stats'][1]['base_stat']
        self._def: int      = _dict['stats'][2]['base_stat']
        self._sp_atk: int   = _dict['stats'][3]['base_stat']
        self._sp_def: int   = _dict['stats'][4]['base_stat']
        self._speed: int    = _dict['stats'][5]['base_stat']
        # @formatter:on
        self._image: str = (f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official'
                            f'-artwork/{self._id}.png')

    def csv(self) -> str:
        return (f'{self._id},{self._name},{self._height},{self._weight},{self._type_1},{self._type_2},{self._hp},'
                f'{self._atk},{self._def},{self._sp_atk},{self._sp_def},{self._speed},{self._image}')


def get_pokemon_data(pokemon_id: int) -> str:
    response: Response = requests_get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')

    if response.status_code == 200:
        response_dict: dict = response.json()
        pokemon: Pokemon = Pokemon(response_dict)
        return pokemon.csv()
    else:
        raise StatusError(response)


def main():
    with open('pokemon_threading.csv', 'a') as csv:
        csv.write(f'id,name,height,weight,type1,type2,hp,atk,def,sp_atk,sp_def,speed,image\n')

        def process_pokemon(i):
            try:
                csv.write(f'{get_pokemon_data(i)}\n')
                print(f'\033[92;1m{i} pokemons have been processed\033[0m')
            except StatusError as e:
                print(f'\033[91;1mError processing Pokemon {i}: {e}\033[0m')

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(process_pokemon, range(1, 1027))


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'\033[0mIt take {end_time - start_time}s to complete!\033[94;1m')
