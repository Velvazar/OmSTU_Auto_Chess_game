from src.adapters.unit_adapter import UnitAdapter
from src.universal_object.universal_object import UniversalObject


class PlayerAdapter:

    def __init__(self, obj: UniversalObject):
        self.__object = obj
        obj.set_property("units", [])

    def get_name(self) -> str:
        return self.__object.get_property("name")

    def set_name(self, name: str):
        self.__object.set_property("name", name)

    def get_health(self) -> int:
        return self.__object.get_property("health")

    def set_health(self, value: int):
        self.__object.set_property("health", value)

    def get_money(self) -> int:
        return self.__object.get_property("money")

    def set_money(self, value: int):
        self.__object.set_property("money", value)

    def get_units(self) -> list:
        return self.__object.get_property("units")

    def add_unit(self, unit: UnitAdapter):
        self.__object.get_property("units").append(unit)

    def get_alive_units(self) -> list:
        units = self.get_units()
        alive_units = []
        for i in range(len(units)):
            if units[i].get_health() > 0:
                alive_units.append(units[i])

        return alive_units
