from typing import Any, Dict, List


class Pokemon:
    def __init__(self, _dict: Dict[str, Any]) -> None:
        # @formatter:off
        self._id: int       = _dict['id']
        self._name: str     = _dict['name']
        self._base_exp: int = _dict['base_experience']
        self._height: int   = _dict['height']
        self._weight: int   = _dict['weight']

        types: List[Dict[str, Any]] = _dict['types']
        self._type_1: str = types[0]['type']['name']
        self._type_2: str = types[1]['type']['name'] if len(types) > 1 else 'null'

        stats: List[Dict[str, Any]] = _dict['stats']
        self._hp: int       = stats[0]['base_stat']
        self._atk: int      = stats[1]['base_stat']
        self._def: int      = stats[2]['base_stat']
        self._sp_atk: int   = stats[3]['base_stat']
        self._sp_def: int   = stats[4]['base_stat']
        self._speed: int    = stats[5]['base_stat']

        self._image: str = (f'https://raw.githubusercontent.com/PokeAPI/sprites/'
                            f'master/sprites/pokemon/other/official-artwork/{self._id}.png')
        # @formatter:on

    def csv(self) -> str:
        return ','.join(str(value) for value in self.__dict__.values())

    @property
    def type1(self) -> str:
        return self._type_1

    @property
    def type2(self) -> str:
        return self._type_2

    # def label(self) -> str:
    #     return ','.join(
    #         attr[1:] for attr in dir(self) if not attr.startswith('_') and not callable(getattr(self, attr))
    #     )
