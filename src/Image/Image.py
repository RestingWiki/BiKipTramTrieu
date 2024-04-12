import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

import os

IMAGE_PATH: str = os.path.join(os.path.dirname(__file__), 'PokeImage')


class Image:

    def __init__(self, _id):
        self._id = _id
        self._img = mpimg.imread(os.path.join(IMAGE_PATH, f'{self._id}.png'))

    def show(self):
        plt.imshow(self._img)
        plt.axis('off')
        plt.show()

    def image_data(self) -> np.ndarray:
        return np.array(self._img)


if __name__ == '__main__':
    poke = Image(3)

    a = poke.image_data()
    poke.show()

    print(poke.image_data())
