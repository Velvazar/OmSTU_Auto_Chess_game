import unittest

from src.ioc.ioc_exception import IocException
from src.ioc.ioc_resolve import ioc_resolve


class TestIocContainer(unittest.TestCase):

    def test_get_existing_value(self):
        ioc_resolve("IoC.Register", "test_property", lambda: "test_value")()
        self.assertEqual(ioc_resolve("test_property"), "test_value")

    def test_get_missing_value(self):
        self.assertRaises(IocException, ioc_resolve, "missing_property")
