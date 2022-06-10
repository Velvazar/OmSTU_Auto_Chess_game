from typing import List
from src.base.command_exception import CommandException
from src.base.icommand import ICommand


class MacroCommand(ICommand):
    def __init__(self, commands: List[ICommand]):
        self.__commands = commands

    def __call__(self) -> None:
        for c in self.__commands:
            try:
                c.__call__()
            except CommandException as e:
                print(e)
