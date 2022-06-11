from abc import ABC, abstractmethod

from src.adapters.player_adapter import PlayerAdapter
from src.adapters.sellable_item_adapter import SellableItemAdapter
from src.adapters.unit_adapter import UnitAdapter


class IShop(ABC):

    @abstractmethod
    def get_sellable_units(self) -> list:
        ...

    @abstractmethod
    def get_sellable_items(self) -> list:
        ...

    @abstractmethod
    def sell_unit(self, unit: SellableItemAdapter, player: PlayerAdapter) -> None:
        ...

    @abstractmethod
    def sell_item(self, item: SellableItemAdapter, player: PlayerAdapter,
                  unit_to_set_item: UnitAdapter) -> None:
        ...
