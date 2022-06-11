from src.universal_object.universal_object import UniversalObject


class InventoryItemAdapter:

    def __init__(self, obj: UniversalObject):
        self.__object = obj

    def get_name(self) -> str:
        return self.__object.get_property("name")

    def set_name(self, name: str):
        self.__object.set_property("name", name)

    def get_effected_property(self) -> str:
        return self.__object.get_property("effected_property")

    def set_effected_property(self, value: str):
        self.__object.set_property("effected_property", value)

    def get_value(self) -> int:
        return self.__object.get_property("value")

    def set_value(self, value: int):
        self.__object.set_property("value", value)
