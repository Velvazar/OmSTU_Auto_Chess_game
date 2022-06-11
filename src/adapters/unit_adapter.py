from src.adapters.inventory_item_adapter import InventoryItemAdapter
from src.universal_object.universal_object import UniversalObject


class UnitAdapter:

    def __init__(self, obj: UniversalObject):
        self.__object = obj
        obj.set_property("inventory", [])

    def get_health(self) -> int:
        return self.__object.get_property("health")

    def set_health(self, value: int):
        self.__object.set_property("health", value)

    def get_base_attack(self) -> int:
        return self.__object.get_property("base_attack")

    def set_base_attack(self, value: int):
        self.__object.set_property("base_attack", value)

    def get_inventory(self) -> list:
        return self.__object.get_property("inventory")

    def add_item(self, item: InventoryItemAdapter):
        self.__object.get_property("inventory").append(item)
