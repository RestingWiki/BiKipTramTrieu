from src.game_init import GameInit
from nguyenpanda.swan import Color

from time import perf_counter

if __name__ == '__main__':
    print(Color['c'] + 'START!!!' + Color.reset)

    start = perf_counter()
    game_initial = GameInit()
    end = perf_counter()

    print(Color['c'] + 'END' + Color.reset)
    print('Finished in ' + Color['y'] + f'{end - start}' + Color.reset + 's')

