from src.adapters.player_adapter import PlayerAdapter
from src.adapters.sellable_item_adapter import SellableItemAdapter
from src.adapters.unit_adapter import UnitAdapter
from src.base.icommand import ICommand


class BuyUnitCommand(ICommand):

    def __init__(self, unit: SellableItemAdapter, player: PlayerAdapter, sellable_units: list, max_player_unit_num: int):
        self.unit = unit
        self.player = player
        self.sellable_units = sellable_units
        self.max_player_unit_num = max_player_unit_num

    def __call__(self):
        if self.unit in self.sellable_units and \
                len(self.player.get_units()) < self.max_player_unit_num\
                and self.player.get_money() >= self.unit.get_cost():
            self.sellable_units.remove(self.unit)
            self.player.get_units().append(UnitAdapter(self.unit.get_object()))
            self.player.set_money(self.player.get_money() - self.unit.get_cost())
