import concurrent.futures
import time

from requests import Response, get as requests_get

from pokemon import Pokemon


class StatusError(Exception):
    def __init__(self, response: Response):
        super().__init__(f'Status code {response.status_code} - {response.text}')


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
    start_time = time.perf_counter()
    main()
    print(f'\033[0mIt take {time.perf_counter() - start_time}s to complete!\033[94;1m')
