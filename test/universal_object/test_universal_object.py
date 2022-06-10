import unittest

from src.universal_object.universal_object import UniversalObject


class TestUniversalObject(unittest.TestCase):

    def test_get_existing_value(self):
        uobject = UniversalObject()
        uobject.set_property("test_property", "test_value")
        self.assertEqual(uobject.get_property("test_property"), "test_value")

    def test_get_missing_value(self):
        uobject = UniversalObject()
        self.assertEqual(uobject.get_property("test_property"), None)
