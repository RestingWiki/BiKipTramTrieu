import numpy as np
from playground_2.Arena import Arena


def main():
    arena = Arena(5)

    teamB = arena.pokeList  # Extract teamB from the arena

    b = np.random.permutation(teamB)[:3]  # Choose 3 distinct pokemon from teamB
    print(b)

    for no in range(3):
        b[no].i = -9999

    for no in range(len(teamB)):
        print(arena.pokeList[no].i, end=' ')


if __name__ == '__main__':
    main()