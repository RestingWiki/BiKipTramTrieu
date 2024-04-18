from typing import NoReturn, List, Any

from src.Image import Image
from src.poke_item import PokeItem
from src.event import SkillEvent

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

    def __init__(self, _id: int) -> NoReturn:
        # @formatter:off
        self._id: int      = ...
        self._name: str    = ...
        self._type1: str  = ...
        self._type2: str  = ...
        self._hp: int      = ...
        self._atk: int     = ...
        self._def: int     = ...
        self._speed: int   = ...
        self._sp_atk: int  = ...
        self._sp_def: int  = ...
        self._image: Image = ...
        self._status: bool  = ...
        # @formatter:on

    def show_image(self) -> NoReturn:
        """

        """
        ...

    def attack(self, other: Pokemon) -> NoReturn:
        """
        :return: NoReturn
        """
        ...

    def taken_damage(self, damage_taken: int) -> int:
        """
        :param damage_taken: The amount of damage taken.
        :return: The amount of damage taken of this Pokémon.
        """
        ...

    def defend(self, other: Pokemon) -> NoReturn:
        """
        :return: NoReturn
        """
        ...

    def use_skill_1(self, allies: List, enemies: List) -> SkillEvent:
        """
        :param allies: List of allies Pokémon
        :param enemies: List of enemy Pokémon
        :return: NoReturn
        """
        ...

    def use_skill_2(self, allies: List, enemies: List) -> SkillEvent:
        """
        :param allies: List of allies Pokémon
        :param enemies: List of enemy Pokémon
        :return: NoReturn
        """
        ...

    def use_item(self, item: PokeItem) -> NoReturn:
        """
        :param item: Arena instance of poke_item
        :return: NoReturn
        """
        ...

    def run(self) -> NoReturn:
        """
        :return: Why is this here?
        """
        ...

    def interact(self) -> NoReturn:
        """
        Idle animation
        :return: NoReturn
        """
        ...

    def __getitem__(self, attribute: str) -> Any:
        """
        :param attribute: The name of the attribute to access.
        :return: The value of the specified attribute, or None if the attribute does not exist.
        """
        ...

    def _die(self) -> NoReturn:
        """
        Modify the Pokémon status to un-alive
        :return: NoReturn
        """
        ...

    @staticmethod
    def _get_data_from_csv(_id: int) -> List:
        """

        :param _id:
        :return:
        """
        ...

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...
