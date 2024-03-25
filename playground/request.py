from requests import Response, get as requests_get

class Pokemon:
    def __init__(self, _dict: dict):
        # @formatter:off
        self._id: int       = _dict['id']
        self._name: int     = _dict['name']
        self._height: int   = _dict['height']
        self._weight: int   = _dict['weight']
        self._hp: int       = _dict['stats'][0]['base_stat']
        self._atk: int      = _dict['stats'][1]['base_stat']
        self._def: int      = _dict['stats'][2]['base_stat']
        self._sp_atk: int   = _dict['stats'][3]['base_stat']
        self._sp_def: int   = _dict['stats'][4]['base_stat']
        self._speed: int    = _dict['stats'][5]['base_stat']
        # @formatter:on

    def __repr__(self):
        return f'Pokemon({self._id}, {self._name}, {self._height}, {self._weight}, {self._hp}, {self._atk}, {self._def}, {self._sp_atk}, {self._sp_def}, {self._speed})'

    def id(self):
        return self._id

    def csv(self):
        return f'{self._id},{self._name},{self._height},{self._weight},{self._hp},{self._atk},{self._def},{self._sp_atk},{self._sp_def},{self._speed}'

def _getOne(pokemon_id: int) -> str:

    response: Response = requests_get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')

    if response.status_code == 200:
        response_dict: dict = response.json()
        pokemon: Pokemon = Pokemon(response_dict)
        return pokemon.csv()
    else:
        print(f'\033[91;1mFailed to retrieve data for Pokemon with ID \033[93;1m{pokemon_id}\033[0m')

with open('dataset.csv', 'a') as f:
    f.write('id,name,height,weight,hp,atk,def,sp_atk,sp_def,speed\n')
    for i in range(1, 50):
        f.write(f'{_getOne(i)}\n')

