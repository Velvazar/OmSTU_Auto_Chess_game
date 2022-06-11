from src.adapters.inventory_item_adapter import InventoryItemAdapter
from src.adapters.player_adapter import PlayerAdapter
from src.adapters.sellable_item_adapter import SellableItemAdapter
from src.adapters.unit_adapter import UnitAdapter
from src.base.icommand import ICommand


class BuyItemCommand(ICommand):

    def __init__(self, item: SellableItemAdapter, player: PlayerAdapter, unit_to_set_item: UnitAdapter, sellable_items: list):
        self.item = item
        self.player = player
        self.unit_to_set_item = unit_to_set_item
        self.sellable_items = sellable_items

    def __call__(self):
        if self.item in self.sellable_items and self.player.get_money() >= self.item.get_cost():
            self.sellable_items.remove(self.item)
            self.unit_to_set_item.get_inventory().append(InventoryItemAdapter(self.item.get_object()))
            self.player.set_money(self.player.get_money() - self.item.get_cost())
