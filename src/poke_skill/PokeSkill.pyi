from typing import NoReturn

from src.pokemon import Pokemon


class PokeSkill:

    @staticmethod
    def do(p1: Pokemon, p2: Pokemon) -> NoReturn:
        ...

    @staticmethod
    def dark(p1: Pokemon, p2: Pokemon) -> NoReturn:
        ...

    @staticmethod
    def dragon(p1: Pokemon, p2: Pokemon) -> NoReturn:
        ...

    @staticmethod
    def electric(p1: Pokemon, p2: Pokemon) -> NoReturn:
        ...

    @staticmethod
    def fairy(p1: Pokemon, p2: Pokemon) -> NoReturn:
        ...

    @staticmethod
    def fighting(p1: Pokemon, p2: Pokemon) -> NoReturn:
        ...

    @staticmethod
    def fire(p1: Pokemon, p2: Pokemon) -> NoReturn:
        ...

    @staticmethod
    def flying(p1: Pokemon, p2: Pokemon) -> NoReturn:
        ...

    @staticmethod
    def ghost(p1: Pokemon, p2: Pokemon) -> NoReturn:
        ...

    @staticmethod
    def grass(p1: Pokemon, p2: Pokemon) -> NoReturn:
        ...

    @staticmethod
    def ground(p1: Pokemon, p2: Pokemon) -> NoReturn:
        ...

    @staticmethod
    def ice(p1: Pokemon, p2: Pokemon) -> NoReturn:
        ...

    @staticmethod
    def normal(p1: Pokemon, p2: Pokemon) -> NoReturn:
        ...

    @staticmethod
    def poison(p1: Pokemon, p2: Pokemon) -> NoReturn:
        ...

    @staticmethod
    def psychic(p1: Pokemon, p2: Pokemon) -> NoReturn:
        ...

    @staticmethod
    def rock(p1: Pokemon, p2: Pokemon) -> NoReturn:
        ...

    @staticmethod
    def steel(p1: Pokemon, p2: Pokemon) -> NoReturn:
        ...

    @staticmethod
    def water(p1: Pokemon, p2: Pokemon) -> NoReturn:
        ...
