from typing import NoReturn, Dict, List

from src.pokemon import Pokemon


class GameInit:

    def __init__(self, team_1: int = 3, team_2: int = 3) -> NoReturn:
        """

        :param team_1:
        :param team_2:
        """

        self._team_1: int = ...
        self._team_2: int = ...
        self._pokemons: List[Pokemon] = ...
        ...

    def get_pokemons(self, _id: int) -> Pokemon:
        """

        :param _id:
        :return: Pokémon
        """
        return self._pokemons[_id - 1]

    @staticmethod
    def get_pokemon_dict_data() -> Dict[int, str]:
        """
        Diction with the key is id, value is Pokémon string.

        Example:
        {1,'1,bulbasaur,64,7,69,grass,poison,45,49,49,65,65,45'}

        :return: Diction[int (id), str (Pokémon csv string)]
        """
        ...

    def _load_Image(self) -> NoReturn:
        ...

    def _load_image_from_file(self, start_id: int, end_id: int) -> NoReturn:
        ...

    def __repr__(self) -> str:
        ...

    def __str__(self):
        ...
