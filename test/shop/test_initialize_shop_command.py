import unittest

from src.ioc.ioc_resolve import ioc_resolve
from src.shop.initialize_shop_command import InitializeShopCommand


class TestInitializeShopCommand(unittest.TestCase):

    def test_initialize(self):
        InitializeShopCommand()()
        self.assertGreater(len(ioc_resolve('sellable_units')), 0)
        self.assertGreater(len(ioc_resolve('sellable_items')), 0)
