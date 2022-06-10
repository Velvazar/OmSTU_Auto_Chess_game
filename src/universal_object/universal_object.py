from typing import Any
from src.universal_object.iuobject import IUObject


class UniversalObject(IUObject):

    def __init__(self):
        self.__container = {}

    def get_property(self, name: str) -> Any:
        if name in self.__container:
            return self.__container[name]
        else:
            return None

    def set_property(self, name: str, value: Any) -> None:
        self.__container[name] = value
