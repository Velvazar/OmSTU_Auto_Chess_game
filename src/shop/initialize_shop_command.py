from random import randint

from src.adapters.inventory_item_adapter import InventoryItemAdapter
from src.adapters.sellable_item_adapter import SellableItemAdapter
from src.adapters.unit_adapter import UnitAdapter
from src.base.icommand import ICommand
from src.ioc.ioc_resolve import ioc_resolve
from src.universal_object.universal_object import UniversalObject


class InitializeShopCommand(ICommand):

    def __init__(self):
        ioc_resolve("IoC.Register", 'sellable_units', lambda: [])()
        ioc_resolve("IoC.Register", 'sellable_items', lambda: [])()

    def __call__(self):
        sellable_units = ioc_resolve('sellable_units')
        sellable_items = ioc_resolve('sellable_items')
        for i in range(randint(3, 40)):  # units
            obj = UniversalObject()
            unit = UnitAdapter(obj)
            sellable = SellableItemAdapter(obj)
            unit.set_base_attack(randint(1, 5))
            unit.set_health(randint(2, 12))
            sellable.set_cost(randint(3, 20))
            sellable_units.append(sellable)
        for i in range(randint(3, 20)):  # items
            obj = UniversalObject()
            unit = InventoryItemAdapter(obj)
            sellable = SellableItemAdapter(obj)
            sellable.set_cost(randint(1, 7))
            item_type = "attack"
            if randint(0, 1) == 1:
                item_type = "defend"
            unit.set_name("item {}".format(i))
            unit.set_effected_property(item_type)
            unit.set_value(randint(1, 3))
            sellable_items.append(sellable)
        ioc_resolve("IoC.Register", 'sellable_units', lambda: sellable_units)()
        ioc_resolve("IoC.Register", 'sellable_items', lambda: sellable_items)()
