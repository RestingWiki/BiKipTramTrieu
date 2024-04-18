from typing import List

from src.poke_skill import PokeSkill
from src.pokemon import Pokemon
from src.event.IEvent import IEvent
from src.event.EventException import SkillEventException


class SkillEvent(IEvent):

    def __init__(self, _user: Pokemon, _ally_list: List, _enemy_list: List):
        self._user = _user
        self._enemy_list = _enemy_list
        self._ally_list = _ally_list
        self._skill_effect = self.__find_skill()

    def active_event(self):
        # map similar to code
        # for enemy in self._enemy_list:
        #     self._skill_effect(self._pokemon, enemy)
        # map(lambda enemy: self._skill_effect(self._user, enemy), self._enemy_list)
        pass

    def __find_skill(self):
        poke_type = self._pokemon['type1']  # TODO: HOW TO KNOW WHETHER TYPE1 OR TYPE2
        if hasattr(PokeSkill, poke_type):
            return getattr(PokeSkill, poke_type)
        else:
            raise SkillEventException

    def __str__(self):
        return f'{self._pokemon} fucks {[self._enemy_list]} by {self._skill_effect}'
