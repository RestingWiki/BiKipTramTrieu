import os

DATA_PATH = os.path.join(os.path.dirname(__file__), 'Pokemon_dataset.csv')

if __name__ == "__main__":
    with open(DATA_PATH, 'r') as f:
        for line, text in enumerate(f):
            print(line, text.strip())
