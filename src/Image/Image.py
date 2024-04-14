import os
from typing import BinaryIO

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

IMAGE_PATH: str = os.path.join(os.path.dirname(__file__), 'PokeImage')


class Image:

    def __init__(self, _id):
        self._id = _id
        self._path = os.path.join(IMAGE_PATH, f'{_id}.png')

    def show(self):
        img = mpimg.imread(self._path)
        plt.imshow(img)
        plt.axis('off')
        plt.show()

    def bin(self) -> BinaryIO:
        return open(self._path, 'rb')


if __name__ == '__main__':
    poke = Image(3)

    poke.show()

