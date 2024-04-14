from src.pokemon import Pokemon
from src.util import perf


class PokeSkill:

    @staticmethod
    def bug(aggressor, target):
        return aggressor + target

    @staticmethod
    def dark(aggressor, target):
        return aggressor + target

    @staticmethod
    def dragon(aggressor, target):
        return aggressor + target

    @staticmethod
    def electric(aggressor, target):
        return aggressor + target

    @staticmethod
    def fairy(aggressor, target):
        return aggressor + target

    @staticmethod
    def fighting(aggressor, target):
        return aggressor + target

    @staticmethod
    def fire(aggressor, target):
        return aggressor + target

    @staticmethod
    def flying(aggressor, target):
        return aggressor + target

    @staticmethod
    def ghost(aggressor, target):
        return aggressor + target

    @staticmethod
    def grass(aggressor, target):
        return aggressor + target

    @staticmethod
    def ground(aggressor, target):
        return aggressor + target

    @staticmethod
    def ice(aggressor, target):
        return aggressor + target

    @staticmethod
    def normal(aggressor, target):
        return aggressor + target

    @staticmethod
    def poison(aggressor, target):
        return aggressor + target

    @staticmethod
    def psychic(aggressor, target):
        return aggressor + target

    @staticmethod
    def rock(aggressor, target):
        return aggressor + target

    @staticmethod
    def steel(aggressor, target):
        return aggressor + target

    @staticmethod
    def water(aggressor, target):
        return aggressor + target


pokemons = [Pokemon(1)]

@perf(unit='ns')
def test1():
    skill_mapping = {name: func for name, func in PokeSkill.__dict__.items() if callable(func)}

    for pokemon in pokemons:
        pokemon_type = pokemon['type1']
        if pokemon_type in skill_mapping:
            skill_func = skill_mapping[pokemon_type]
            print(skill_func(1, 3))


@perf(unit='ns')
def test2():
    for pokemon in pokemons:
        if pokemon['type1'] == 'bug':
            print(PokeSkill.bug(1, 3))
        elif pokemon['type1'] == 'dark':
            print(PokeSkill.dark(1, 3))
        elif pokemon['type1'] == 'dragon':
            print(PokeSkill.dragon(1, 3))
        elif pokemon['type1'] == 'electric':
            print(PokeSkill.electric(1, 3))
        elif pokemon['type1'] == 'dragon':
            print(PokeSkill.dragon(1, 3))
        elif pokemon['type1'] == 'fairy':
            print(PokeSkill.fairy(1, 3))
        elif pokemon['type1'] == 'fighting':
            print(PokeSkill.fighting(1, 3))
        elif pokemon['type1'] == 'fire':
            print(PokeSkill.fire(1, 3))
        elif pokemon['type1'] == 'flying':
            print(PokeSkill.flying(1, 3))
        elif pokemon['type1'] == 'ice':
            print(PokeSkill.ice(1, 3))
        elif pokemon['type1'] == 'ghost':
            print(PokeSkill.ghost(1, 3))
        elif pokemon['type1'] == 'grass':
            print(PokeSkill.grass(1, 3))
        elif pokemon['type1'] == 'ground':
            print(PokeSkill.ground(1, 3))
        elif pokemon['type1'] == 'normal':
            print(PokeSkill.normal(1, 3))
        elif pokemon['type1'] == 'poison':
            print(PokeSkill.poison(1, 3))
        elif pokemon['type1'] == 'psychic':
            print(PokeSkill.psychic(1, 3))
        elif pokemon['type1'] == 'rock':
            print(PokeSkill.rock(1, 3))
        elif pokemon['type1'] == 'steel':
            print(PokeSkill.steel(1, 3))
        elif pokemon['type1'] == 'water':
            print(PokeSkill.water(1, 3))
        elif pokemon['type1'] == 'null':
            pass
        else:
            print(pokemon['type1'])
            raise AssertionError


if __name__ == '__main__':
    # test1()
    # test2()
    # pokemon = Pokemon(1)

    print(hasattr(PokeSkill, 'bug'))
    print(getattr(PokeSkill, 'bug')(1, 3))
