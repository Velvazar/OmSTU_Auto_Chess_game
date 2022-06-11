import json

from src.base.icommand import ICommand
from src.ioc.ioc_resolve import ioc_resolve


class ReadConfigCommand(ICommand):

    def __init__(self, file_path):
        self.file_path = file_path

    def __call__(self):
        try:
            with open(self.file_path) as file:
                json_data = json.load(file)
                self.__json_data = json_data
            for key, value in json_data.items():
                ioc_resolve("IoC.Register", key, create_command(value))()

        except FileNotFoundError:
            print("File {} wasn't found".format(self.file_path))
            self.__json_data = {}


def create_command(value):
    return lambda: value
