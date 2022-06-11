import unittest

from src.adapters.inventory_item_adapter import InventoryItemAdapter
from src.adapters.player_adapter import PlayerAdapter
from src.adapters.sellable_item_adapter import SellableItemAdapter
from src.adapters.unit_adapter import UnitAdapter
from src.shop.buy_item_command import BuyItemCommand
from src.universal_object.universal_object import UniversalObject


class TestBuyItemCommand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        obj = UniversalObject()
        cls.sellable_unit = SellableItemAdapter(obj)
        cls.sellable_unit.set_cost(5)
        cls.unit = UnitAdapter(obj)

    def test_buy_item(self):
        obj = UniversalObject()
        sellable_item = SellableItemAdapter(obj)
        item = InventoryItemAdapter(obj)
        item.set_name("test name")
        sellable_item.set_cost(5)
        sellable_items = [sellable_item]
        player = PlayerAdapter(UniversalObject())
        player.set_money(10)
        player.add_unit(self.unit)

        BuyItemCommand(sellable_item, player, self.unit, sellable_items)()

        self.assertEqual(player.get_money(), 5)
        self.assertFalse(sellable_item in sellable_items)
        self.assertEqual(len(self.unit.get_inventory()), 1)
        self.assertEqual(self.unit.get_inventory()[0].get_name(), "test name")

    def test_not_enough_money(self):
        sellable_item = SellableItemAdapter(UniversalObject())
        sellable_item.set_cost(10)
        sellable_items = [sellable_item]

        player = PlayerAdapter(UniversalObject())
        player.set_money(5)

        BuyItemCommand(sellable_item, player, self.unit, sellable_items)()

        self.assertEqual(player.get_money(), 5)
        self.assertTrue(sellable_item in sellable_items)
