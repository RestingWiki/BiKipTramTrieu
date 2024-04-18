from src.poke_skill import PokeSkill
from src.pokemon import Pokemon
from src.event.IEvent import IEvent
from src.event.EventException import SkillEventException

from typing import Callable, NoReturn, List


class SkillEvent(IEvent):

    def __init__(self, _user: Pokemon, _ally_list: List, _enemy_list: List) -> NoReturn:
        self._user: Pokemon = ...
        self._ally_list: List = ...
        self._enemy_list: List = ...
        self._skill_effect: Callable[[Pokemon, Pokemon], NoReturn] = ...
        ...

    def active_event(self) -> NoReturn:
        """
        Use the  designated skill
        """
        ...


    def __find_skill(self) -> Callable[[Pokemon, Pokemon], NoReturn]:
        ...

    def __str__(self) -> str:
        ...
