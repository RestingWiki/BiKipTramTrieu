from src.poke_skill import PokeSkill
from src.event.IEvent import IEvent
from src.event.EventException import SkillEventException


class SkillEvent(IEvent):

    def __init__(self, _pokemon, _team_list: list):
        self._team_list = _team_list
        self._pokemon = _pokemon
        self._skill_effect = self.__find_skill()

    def active_event(self):
        map(lambda enemy: self._skill_effect(self._pokemon, enemy), self._team_list)

    def __find_skill(self):
        poke_type = self._pokemon['type1']  # TODO: HOW TO KNOW WHETHER TYPE1 OR TYPE2
        if hasattr(PokeSkill, poke_type):
            return getattr(PokeSkill, poke_type)
        else:
            raise SkillEventException

    def __str__(self):
        return f'{self._pokemon} fucks {[self._team_list]} by {self._skill_effect}'
