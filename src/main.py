from src.util import perf
from src.game_init import GameInit
from nguyenpanda.swan import Color

from time import perf_counter

@perf(precision=2, unit='s')
def main():
    game_initial = GameInit()
    print(game_initial)

if __name__ == '__main__':
    print(Color['c'] + 'START!!!' + Color.reset)

    start = perf_counter()
    main()
    end = perf_counter()

    print(Color['c'] + 'END' + Color.reset)
    print('Finished in ' + Color['y'] + f'{end - start}' + Color.reset + 's')

