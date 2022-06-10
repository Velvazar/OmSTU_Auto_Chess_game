import unittest
from unittest.mock import MagicMock
from src.base.icommand import ICommand
from src.base.macro_command import MacroCommand


class TestMacroCommand(unittest.TestCase):

    def test_macro_command_correct(self):
        ICommand.__abstractmethods__ = frozenset()
        mocked_command = ICommand()
        mocked_command.__call__ = MagicMock(return_value=None)
        macro_command = MacroCommand([mocked_command])
        macro_command.__call__()
        mocked_command.__call__.assert_called()
