import random

from numpy.random import choice

from src.event.EventException import SkillEventException, NoSkillException
from src.event.IEvent import IEvent
from src.poke_skill import PokeSkill
from src.pokemon import Pokemon

# @formatter:off
skill_type_map = {
    PokeSkill.bug:          2,
    PokeSkill.dark:         0,
    PokeSkill.dragon:       0,
    PokeSkill.electric:     4,
    PokeSkill.fairy:        0,
    PokeSkill.fighting:     4,
    PokeSkill.fire:         4,
    PokeSkill.flying:       0,
    PokeSkill.ghost:        3,
    PokeSkill.grass:        1,
    PokeSkill.ground:       4,
    PokeSkill.ice:          4,
    PokeSkill.normal:       0,
    PokeSkill.poison:       4,
    PokeSkill.psychic:      2,
    PokeSkill.rock:         0,
    PokeSkill.steel:        2,
    PokeSkill.water:        3,
}
# @formatter.on

class SkillEvent(IEvent):

    def __init__(self, _user: Pokemon, _ally_list, _enemy_list):
        self._user = _user
        self._enemy_list = _enemy_list
        self._ally_list = _ally_list
        self._skill_effect = self.__find_skill()

    def active_event(self):
        _type = skill_type_map[self._skill_effect]

        if _type == 0:  # Self-buff
            self._skill_effect(self._user, self._user)
        elif _type == 1:  # Ally buff
            target: Pokemon = self._user
            while target is self._user:
                target = choice(self._ally_list)
            self._skill_effect(self._user, target)
        elif _type == 2:  # Enemy
            target = random.choice(self._enemy_list)
            self._skill_effect(self._user, target)
        elif _type == 3:  # Allies
            map(lambda ally: self._skill_effect(self._user, ally), self._ally_list)
        elif _type == 4:  # Enemies
            map(lambda enemy: self._skill_effect(self._user, enemy), self._enemy_list)
        else:
            raise NoSkillException

    def __find_skill(self):
        poke_type = self._user['type1']  # TODO: HOW TO KNOW WHETHER TYPE1 OR TYPE2
        if hasattr(PokeSkill, poke_type):
            return getattr(PokeSkill, poke_type)
        else:
            raise SkillEventException

    def __str__(self):
        return f'{self._user} fucks {[self._enemy_list]} by {self._skill_effect}'
