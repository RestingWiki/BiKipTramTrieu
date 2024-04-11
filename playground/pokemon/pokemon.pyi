from typing import Any
import PokeItem

class Pokemon:
    """
    Pokémon class has the following attributes:
        - _id: int
        - _name: str
        - _height: int
        - _weight: int
        - _type_1: str
        - _type_2: str (if don't have a second type, it is 'null')
        - _hp: int
        - _atk: int
        - _def: int
        - _sp_atk: int
        - _sp_def: int
        - _speed: int
        - _image: str
    """

    def __init__(self, _dict: dict[str, Any]) -> None:
        """
        Pokémon constructor

        :param _dict: A dictionary, which is converted json into a Python dictionary,
            contains the Pokémon attributes
        """
        self._id: int = ...
        self._name: str = ...
        self._base_exp: int = ...
        self._height: int = ...
        self._weight: int = ...
        self._type_1: str = ...
        self._type_2: str = ...
        self._hp:  int = ...
        self._atk: int = ...
        self._def: int = ...
        self._sp_atk: int = ...
        self._sp_def: int = ...
        self._speed: int = ...
        self._image: str = ...

    def csv(self) -> str:
        """
        :return: Returns a csv string of the Pokémon attributes
        """
        ...

    @property
    def type1(self) -> str:
        """
        :return: Returns the first type of the Pokémon
        """
        ...

    @property
    def type2(self) -> str:
        """
        :return: Returns the second type of the Pokémon
        """
        ...
