from typing import List
import unittest
from src.base.icommand import ICommand
from src.base.macro_command import MacroCommand
from src.game.initialize_command import InitializeStateCommand

from src.game.main_game import CalcFightPoints, FightInstance, GameInstance, InitFightUnits, ProcessFight, RoundFinishCommand
from src.game.main_game import RoundStartCommand, SplitPlayersCommand
from src.shop.initialize_shop_command import InitializeShopCommand
from src.shop.players_autoshopping_command import PlayersAutoshoppingCommand


class TestGame(unittest.TestCase):
    def test_first_test(self):
        game_instance = GameInstance()
        init_command = InitializeStateCommand(game_instance)
        init_shop_command = InitializeShopCommand()
        autoshopping_command = PlayersAutoshoppingCommand(game_instance)
        split_command = SplitPlayersCommand(game_instance)

        commands: List[ICommand] = [
            init_command,
            init_shop_command,
            autoshopping_command,
            split_command
        ]

        mc = MacroCommand(commands)
        mc()

        for i in range(len(game_instance.game_participants)):
            round_start_command = RoundStartCommand(game_instance, i)
            commands2: List[ICommand] = [
                round_start_command
            ]
            mc2 = MacroCommand(commands2)
            mc2()

            while len(game_instance.first_units) > 0 and len(game_instance.second_units) > 0:
                fight_instance = FightInstance(game_instance)
                init_fight_command = InitFightUnits(fight_instance)
                calc_fight_points_command = CalcFightPoints(fight_instance)
                process_fight_command = ProcessFight(fight_instance, i)

                commands3: List[ICommand] = [
                    init_fight_command,
                    calc_fight_points_command,
                    process_fight_command
                ]

                mc3 = MacroCommand(commands3)
                mc3()

            round_finish_command = RoundFinishCommand(game_instance, i)
            commands4: List[ICommand] = [
                round_finish_command
            ]

            mc4 = MacroCommand(commands4)
            mc4()
