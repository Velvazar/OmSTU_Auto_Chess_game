from src.universal_object.universal_object import UniversalObject


class SellableItemAdapter:

    def __init__(self, obj: UniversalObject):
        self.__object = obj

    def get_cost(self) -> int:
        return self.__object.get_property("cost")

    def set_cost(self, value: int):
        self.__object.set_property("cost", value)

    def get_object(self) -> UniversalObject:
        return self.__object
