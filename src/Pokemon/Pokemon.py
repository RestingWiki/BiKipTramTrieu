import os

from src.PokeItem import PokeItem

DATA_PATH = os.path.join(os.path.dirname(__file__), 'Pokemon_dataset.csv')


class Pokemon:

    def __init__(self, _id):
        # @formatter:off
        self._id        = DICT_DATA['_id']
        self._name      = DICT_DATA['_name']
        self._type1     = DICT_DATA['_type1']
        self._type2     = DICT_DATA['_type2']
        self._hp        = DICT_DATA['_hp']
        self._atk       = DICT_DATA['_atk']
        self._def       = DICT_DATA['_def']
        self._speed     = DICT_DATA['_speed']
        self._sp_atk    = DICT_DATA['_sp_atk']
        self._sp_def    = DICT_DATA['_sp_def']
        self._image     = DICT_DATA['_image']
        self._status    = DICT_DATA['_status']
        # @formatter:on

    def show_image(self):
        pass

    def attack(self):
        pass

    def taken_damage(self, damage_taken):
        pass

    def defense(self, damage_taken):
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

    def 

