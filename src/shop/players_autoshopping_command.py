from random import randint

from src.base.icommand import ICommand
from src.game.main_game import GameInstance
from src.ioc.ioc_resolve import ioc_resolve
from src.shop.shop_command_factory import ShopCommandFactory


class PlayersAutoshoppingCommand(ICommand):

    def __init__(self, game_instance: GameInstance):
        self.game_instance = game_instance
        self.shop_command_factory = ShopCommandFactory()

    def __call__(self):
        players = ioc_resolve("players")
        sellable_units = ioc_resolve('sellable_units')
        sellable_items = ioc_resolve('sellable_items')
        player_max_unit_number = ioc_resolve("player_max_unit_number")

        player_number_non_able_to_buy = 0
        while player_number_non_able_to_buy != len(players):
            player_number_non_able_to_buy = 0
            for i in range(len(players)):
                bought_anything = False
                for j in range(len(sellable_units)):
                    if len(players[i].get_units()) < player_max_unit_number and \
                            players[i].get_money() >= sellable_units[j].get_cost():
                        self.shop_command_factory.create_command_for_buying_unit(sellable_units[j], players[i])()
                        bought_anything = True
                        break
                if not bought_anything:
                    player_number_non_able_to_buy = player_number_non_able_to_buy + 1

        player_number_non_able_to_buy = 0
        while player_number_non_able_to_buy != len(players):
            player_number_non_able_to_buy = 0
            for i in range(len(players)):
                bought_anything = False
                for j in range(len(sellable_items)):
                    if len(players[i].get_units()) > 0 and \
                            players[i].get_money() >= sellable_items[j].get_cost():
                        unit_to_set = players[i].get_units()[randint(0, len(players[i].get_units()) - 1)]
                        self.shop_command_factory.create_command_for_buying_item(sellable_items[j], players[i], unit_to_set)()
                        bought_anything = True
                        break
                if not bought_anything:
                    player_number_non_able_to_buy = player_number_non_able_to_buy + 1
