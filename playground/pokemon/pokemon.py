class Pokemon:
    def __init__(self, _dict: dict):
        # @formatter:off
        self._id: int       = _dict['id']
        self._name: str     = _dict['name']
        self._height: int   = _dict['height']
        self._weight: int   = _dict['weight']

        type_list: list = _dict['types']
        self._type_1: str   = type_list[0]['type']['name']
        if len(type_list) == 2:
            self._type_2: str = type_list[1]['type']['name']
        else:
            self._type_2: str = 'null'

        self._hp: int       = _dict['stats'][0]['base_stat']
        self._atk: int      = _dict['stats'][1]['base_stat']
        self._def: int      = _dict['stats'][2]['base_stat']
        self._sp_atk: int   = _dict['stats'][3]['base_stat']
        self._sp_def: int   = _dict['stats'][4]['base_stat']
        self._speed: int    = _dict['stats'][5]['base_stat']
        # @formatter:on
        self._image: str = (f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official'
                            f'-artwork/{self._id}.png')

    def csv(self) -> str:
        return (f'{self._id},{self._name},{self._height},{self._weight},{self._type_1},{self._type_2},{self._hp},'
                f'{self._atk},{self._def},{self._sp_atk},{self._sp_def},{self._speed},{self._image}')
