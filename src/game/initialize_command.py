from src.adapters.player_adapter import PlayerAdapter
from src.adapters.unit_adapter import UnitAdapter
from src.base.icommand import ICommand
from src.game.main_game import GameInstance
from src.ioc.ioc_resolve import ioc_resolve
from src.universal_object.universal_object import UniversalObject


class InitializeStateCommand(ICommand):
    def __init__(self, game_instance: GameInstance):
        self.game_instance = game_instance

    def __call__(self):
        players = []
        for i in range(8):
            player = PlayerAdapter(UniversalObject())
            player.set_name("Player {}".format(i))
            player.set_health(ioc_resolve("player_default_health"))
            player.set_money(ioc_resolve("player_default_money_count"))

            unit = UnitAdapter(UniversalObject())
            unit.set_health(ioc_resolve("unit_default_health"))
            unit.set_base_attack(ioc_resolve("unit_default_base_attack"))

            player.add_unit(unit)
            players.append(player)

        for i in range(4):
            unit = UnitAdapter(UniversalObject())
            unit.set_health(10)
            unit.set_base_attack(3)
            players[0].add_unit(unit)

        ioc_resolve("IoC.Register", "players", lambda: players)()
