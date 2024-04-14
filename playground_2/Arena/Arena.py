from typing import Callable


class PokeSkill:

    @staticmethod
    def dark(p1, p2):
        pass

    @staticmethod
    def dragon(p1, p2):
        pass


class SkillEvent:

    def __init__(self, _pokemon, _team_list: list):
        self._team_list = _team_list
        self._pokemon = _pokemon
        self._skill_effect = self.__find_skill()

    def __active_event(self):
        for enemy in self._team_list:
            self._skill_effect(self._pokemon, enemy)

    def __find_skill(self):
        # SOME FINDING LOGIC
        # if ??? == ???:
        #     return
        return PokeSkill.dragon

    def __str__(self):
        return f'{self._pokemon} fucks {[self._team_list]} by {self._skill_effect}'


class Poke:
    def __init__(self, i: int):
        self.i = i

    def use_skill_1(self, team_list: list) -> SkillEvent:
        return SkillEvent(self, team_list)

    def __str__(self):
        return f'{self.__class__.__name__}({self.i})'


class Arena:

    def __init__(self, i: int):
        self.__pokeList_A = [Poke(i) for i in range(5)]
        self.__pokeList_B = [Poke(i) for i in range(5)]

    def __str__(self):
        return f'<{self.__class__.__name__}({len(self.__pokeList)}) - {[p for p in self.__pokeList]}>'

    @property
    def pokeList(self):
        return self.__pokeList

    @pokeList.setter
    def pokeList(self, new_list):
        self.__pokeList = new_list


