import threading

import requests

from src.game_init import GameInit

game = GameInit()


def get_image_from_response(_id: int):
    response = requests.get(game.get_pokemons(_id)['image'])
    if response.status_code == 200:
        with open(f'PokeImage/{_id}.png', 'wb') as file:
            file.write(response.content)
        print(f'Pokemon {_id} downloaded successfully.')
    else:
        print(f'Failed to download Pokemon {_id}. Status code:', response.status_code)


def download_images(start_id, end_id):
    for i in range(start_id, end_id):
        get_image_from_response(i)


def main():
    start_id = 1
    end_id = 1026  # Range is [start_id, end_id)
    num_threads = 10
    threads = []
    ids_per_thread = (end_id - start_id) // num_threads
    for i in range(num_threads):
        thread_start_id = start_id + i * ids_per_thread
        thread_end_id = start_id + (i + 1) * ids_per_thread
        thread = threading.Thread(target=download_images, args=(thread_start_id, thread_end_id))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()
