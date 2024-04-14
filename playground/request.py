import concurrent.futures
import csv
import os
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
        print(pokemon.csv())
        return pokemon.csv()
    else:
        raise StatusError(response)


def write_pokemon_data_by_type(data):
    # Assuming the first value in your CSV data is the Pokémon type
    data_list = data.split(',')
    pokemon_type = data_list[5]  # Adjust index if needed
    filename = f'pokemon_{pokemon_type}.csv'
    # Determine if the file already exists to decide whether to write headers
    file_exists = os.path.isfile(filename)

    headers = 'id,name,height,weight,type1,type2,hp,atk,def,sp_atk,sp_def,speed,image\n'
    with open(filename, 'a') as csv:
        if not file_exists:
            csv.write(headers)
        csv.write(f'{data}\n')


def process_pokemon_type(i):
    try:
        pokemon_data = get_pokemon_data(i)
        write_pokemon_data_by_type(pokemon_data)
        print(f'\033[92;1m{i} pokemons have been processed\033[0m')
    except StatusError as e:
        print(f'\033[91;1mError processing Pokemon {i}: {e}\033[0m')


def main():
    with open('pokemon_threading.csv', 'a') as csv:
        csv.write(f'id,name,base_exp,height,weight,type1,type2,hp,atk,def,sp_atk,sp_def,speed,image\n')

        def process_pokemon(i):
            try:
                csv.write(f'{get_pokemon_data(i)}\n')
                print(f'\033[92;1m{i} pokemons have been processed\033[0m')
            except StatusError as e:
                print(f'\033[91;1mError processing Pokemon {i}: {e}\033[0m')

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(process_pokemon, range(1, 1025))


def main():
    start_time = time.perf_counter()
    # main()
    print(f'\033[0mIt take {time.perf_counter() - start_time}s to complete!\033[94;1m')
    # Read the CSV file into a list of rows
    rows = list(csv.reader(open('pokemon_threading.csv')))

    # Now, 'rows' is a list where each element is a list representing a row in the CSV file
    # Bubblesort
    rows = rows[1:]
    for i in range(len(rows)):
        for j in range(len(rows) - 1):
            if int(rows[j][0]) > int(rows[j + 1][0]):
                rows[j], rows[j + 1] = rows[j + 1], rows[j]

    for r in rows:
        print(r)
    with open('sorted_pokemon.csv', 'w', newline='\n') as sortedCSV:
        # Rows [[]]: a sorted list, each row is a list of pokemon attributes
        for line in rows:
            sortedCSV.write(','.join(line) + '\n')
        print("Finished writing sorted csv!")


if __name__ == "__main__":
    pokemon_data = get_pokemon_data(773)
