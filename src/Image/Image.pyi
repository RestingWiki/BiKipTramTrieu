import numpy as np

from typing import NoReturn

class Image:

    def __init__(self, _id) -> NoReturn:
        """

        :param _id:
        """
        self._id: int = ...
        self._img: np.ndarray = ...
        ...

    def show(self) -> NoReturn:
        """

        :return:
        """
        ...

    def image_data(self) -> np.ndarray:
        """

        :return:
        """
        ...
