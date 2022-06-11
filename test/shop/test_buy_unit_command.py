import unittest

from src.adapters.player_adapter import PlayerAdapter
from src.adapters.sellable_item_adapter import SellableItemAdapter
from src.adapters.unit_adapter import UnitAdapter
from src.shop.buy_unit_command import BuyUnitCommand
from src.universal_object.universal_object import UniversalObject


class TestBuyUnitCommand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        obj = UniversalObject()
        cls.sellable_unit = SellableItemAdapter(obj)
        cls.sellable_unit.set_cost(5)
        cls.unit = UnitAdapter(obj)

    def test_buy_unit(self):
        sellable_units = [self.sellable_unit]
        player = PlayerAdapter(UniversalObject())
        player.set_money(10)

        BuyUnitCommand(self.sellable_unit, player, sellable_units, 7)()

        self.assertEqual(player.get_money(), 5)
        self.assertEqual(len(player.get_units()), 1)
        self.assertFalse(self.sellable_unit in sellable_units)

    def test_too_many_units(self):
        sellable_units = [self.sellable_unit]
        player = PlayerAdapter(UniversalObject())
        player.set_money(10)

        BuyUnitCommand(self.sellable_unit, player, sellable_units, 0)()

        self.assertEqual(player.get_money(), 10)
        self.assertFalse(self.unit in sellable_units)
