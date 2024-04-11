import os
from nguyenpanda.swan import Color


class LoadData:
    __POKE_DATA_SET = None

    def __new__(cls):
        if cls.__POKE_DATA_SET is None:
            cls.__get_data()
        return cls.__POKE_DATA_SET

    @classmethod
    def __get_data(cls):
        print(Color['cyan'] + '__get_data' + Color.reset)  # TODO: DELETE

        cls.__POKE_DATA_SET = {}
        DATA_PATH = os.path.join(os.path.dirname(__file__), 'Pokemon_dataset.csv')
        with open(DATA_PATH, 'r') as f:
            for line, text in enumerate(f):
                if line == 0:
                    continue
                cls.__POKE_DATA_SET[line] = text.strip()


if __name__ == '__main__':
    a = LoadData()
    for i in a.values():
        print(i)
