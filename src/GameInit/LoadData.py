import os

DATA_PATH = os.path.join(os.path.dirname(__file__), 'Pokemon_dataset.csv')


class LoadData:
    __POKE_DATA_SET = None

    def __new__(cls):
        if cls.__POKE_DATA_SET is None:
            cls.__get_data()
        return cls.__POKE_DATA_SET

    @classmethod
    def __get_data(cls):
        cls.__POKE_DATA_SET = {}

        with open(DATA_PATH, 'r') as f:
            for line, text in enumerate(f):
                cls.__POKE_DATA_SET[line] = text.strip()

if __name__ == '__main__':
    a = LoadData()
    print(type(a))
    print(len(a))
    for i, j in a:
        print(i, j)