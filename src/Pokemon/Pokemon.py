from src.PokeItem import PokeItem
from src.GameInit import LoadData


class Pokemon:

    def __init__(self, _id):
        data: list = Pokemon._get_data_from_csv(_id)
        # @formatter:off
        self._id        = data[0]
        self._name      = data[1]
        # self._base_exp  = data[2]
        # self._height    = data[3]
        # self._weight    = data[4]
        self._type1     = data[5]
        self._type2     = data[6]
        self._hp        = data[7]
        self._atk       = data[8]
        self._def       = data[9]
        self._sp_atk    = data[10]
        self._sp_def    = data[11]
        self._speed     = data[12]
        self._image     = data[13]
        self._status    = 'alive'
        # @formatter:on

    def show_image(self):
        pass

    def attack(self):
        pass

    def taken_damage(self, damage_taken):
        pass

    def defend(self, damage_taken):
        pass

    def use_skill_1(self, num):
        pass

    def use_skill_2(self, num):
        pass

    def use_item(self, item: PokeItem):
        pass

    def run(self):
        pass

    def interact(self):
        pass

    def __getitem__(self, attribute):
        return self.__dict__.get(attribute)

    def _die(self):
        pass

    @staticmethod
    def _get_data_from_csv(_id):
        a: list = LoadData().get(_id).split(',')
        return a


if __name__ == '__main__':
    list_of_poke: list = [Pokemon(i) for i in range(1, 101)]

    for i in list_of_poke:
        print(i.__dict__)
