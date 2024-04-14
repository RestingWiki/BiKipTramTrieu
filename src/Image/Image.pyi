from typing import BinaryIO, NoReturn

class Image:

    def __init__(self, _id):
        """

        :param _id:
        """
        self._id: int = ...
        self._path: str = ...

    def show(self) -> NoReturn:
        """

        :return:
        """
        ...

    def bin(self) -> BinaryIO:
        """

        :return:
        """
        ...
