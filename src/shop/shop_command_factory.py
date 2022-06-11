from src.adapters.player_adapter import PlayerAdapter
from src.adapters.sellable_item_adapter import SellableItemAdapter
from src.adapters.unit_adapter import UnitAdapter
from src.ioc.ioc_resolve import ioc_resolve
from src.shop.buy_item_command import BuyItemCommand
from src.shop.buy_unit_command import BuyUnitCommand


class ShopCommandFactory:

    def create_command_for_buying_unit(self, unit: SellableItemAdapter, player: PlayerAdapter):
        return BuyUnitCommand(unit, player, ioc_resolve('sellable_units'),
                              ioc_resolve("player_max_unit_number"))

    def create_command_for_buying_item(self, item: SellableItemAdapter, player: PlayerAdapter, unit_to_set_item: UnitAdapter):
        return BuyItemCommand(item, player, unit_to_set_item, ioc_resolve('sellable_items'))
