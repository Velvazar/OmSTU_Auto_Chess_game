import random
from src.adapters.player_adapter import PlayerAdapter
from src.adapters.unit_adapter import UnitAdapter
from src.base.icommand import ICommand
from src.config.read_cofig_command import ReadConfigCommand
from src.ioc.ioc_resolve import ioc_resolve
from src.universal_object.universal_object import UniversalObject


class GameInstance:
    def __init__(self):
        self.game_participants = []
        self.first_units = []
        self.second_units = []
        self.is_first_player = bool()
        self.last_dead_player = PlayerAdapter(UniversalObject())
        ReadConfigCommand("config.json")()


class FightInstance:
    def __init__(self, game_instance: GameInstance):
        self.game_instance = game_instance
        self.player1_unit = UnitAdapter(UniversalObject())
        self.player2_unit = UnitAdapter(UniversalObject())
        self.inventory_first = []
        self.inventory_second = []
        self.attack_points = []
        self.defence_points = []


class SplitPlayersCommand(ICommand):
    def __init__(self, game_instance: GameInstance):
        self.game_instance = game_instance

    def __call__(self) -> None:
        player_list = ioc_resolve("players")
        self.game_instance.game_participants.clear()

        if len(player_list) % 2 == 1:
            self.game_instance.last_dead_player.set_health(1)
            player_list.append(self.game_instance.last_dead_player)

        for i in range(0, len(player_list), 2):
            player1 = player_list[i]
            player2 = player_list[i + 1]
            self.game_instance.game_participants.append([player1, player2])


class RoundStartCommand(ICommand):
    def __init__(self, game_instance: GameInstance, pair_index: int):
        self.game_instance = game_instance
        self.pair_index = pair_index

    def __call__(self) -> None:
        participants_array = self.game_instance.game_participants

        current_players = participants_array[self.pair_index]
        player1 = current_players[0]
        player2 = current_players[1]

        self.game_instance.first_units = player1.get_alive_units()
        self.game_instance.second_units = player2.get_alive_units()

        self.game_instance.is_first_player = (random.random() == 1)


class InitFightUnits(ICommand):
    def __init__(self, fight_instance: FightInstance):
        self.fight_instance = fight_instance
        self.game_instance = self.fight_instance.game_instance

    def __call__(self) -> None:
        alive_units1 = self.game_instance.first_units
        alive_units2 = self.game_instance.second_units

        if self.game_instance.is_first_player:
            self.fight_instance.player1_unit = alive_units1[0]
            self.fight_instance.player2_unit = alive_units2[random.randint(0, len(alive_units2)) - 1]
        else:
            self.fight_instance.player1_unit = alive_units1[random.randint(0, len(alive_units1)) - 1]
            self.fight_instance.player2_unit = alive_units2[0]

        unit1 = self.fight_instance.player1_unit
        unit2 = self.fight_instance.player2_unit

        inventory1 = unit1.get_inventory()
        inventory2 = unit2.get_inventory()

        self.fight_instance.inventory_first = inventory1
        self.fight_instance.inventory_second = inventory2


class CalcFightPoints(ICommand):
    def __init__(self, fight_instance: FightInstance):
        self.fight_instance = fight_instance

    def __call__(self) -> None:
        self.fight_instance.attack_points.append(self.fight_instance.player1_unit.get_base_attack())
        self.fight_instance.attack_points.append(self.fight_instance.player2_unit.get_base_attack())

        self.fight_instance.defence_points.append(self.fight_instance.player1_unit.get_health())
        self.fight_instance.defence_points.append(self.fight_instance.player2_unit.get_health())

        for i in range(len(self.fight_instance.inventory_first)):
            if self.fight_instance.inventory_first[i].get_effected_property() == "attack":
                self.fight_instance.attack_points[0] += self.fight_instance.inventory_first[i].get_value()
            elif self.fight_instance.inventory_first[i].get_effected_property() == "defend":
                self.fight_instance.defence_points[0] += self.fight_instance.inventory_first[i].get_value()

        for i in range(len(self.fight_instance.inventory_second)):
            if self.fight_instance.inventory_second[i].get_effected_property() == "attack":
                self.fight_instance.attack_points[1] += self.fight_instance.inventory_second[i].get_value()
            elif self.fight_instance.inventory_second[i].get_effected_property() == "defend":
                self.fight_instance.defence_points[1] += self.fight_instance.inventory_second[i].get_value()


class ProcessFight(ICommand):
    def __init__(self, fight_instance: FightInstance, pair_index: int):
        self.fight_instance = fight_instance
        self.pair_index = pair_index
        self.game_instance = self.fight_instance.game_instance

    def __call__(self) -> None:
        self.fight_instance.player1_unit.set_health(self.fight_instance.defence_points[0] - self.fight_instance.attack_points[1])
        self.fight_instance.player2_unit.set_health(self.fight_instance.defence_points[1] - self.fight_instance.attack_points[0])

        print("Unit of Player {0} damaged {1} hp".format(1, self.fight_instance.attack_points[0]))
        print("Unit of Player {0} damaged {1} hp".format(2, self.fight_instance.attack_points[1]))

        participants_array = self.game_instance.game_participants
        current_players = participants_array[self.pair_index]
        player1 = current_players[0]
        player2 = current_players[1]

        self.game_instance.is_first_player = not self.game_instance.is_first_player
        self.game_instance.first_units = player1.get_alive_units()
        self.game_instance.second_units = player2.get_alive_units()


class RoundFinishCommand(ICommand):
    def __init__(self, game_instance: GameInstance, pair_index: int):
        self.pair_index = pair_index
        self.game_instance = game_instance

    def __call__(self) -> None:
        participants_array = self.game_instance.game_participants
        current_players = participants_array[self.pair_index]
        player1 = current_players[0]
        player2 = current_players[1]

        player1.set_health(player1.get_health() - len(self.game_instance.second_units))
        player2.set_health(player2.get_health() - len(self.game_instance.first_units))

        player_list = ioc_resolve("players")

        if (player1.get_health() <= 0 and player1 in player_list):
            self.game_instance.last_dead_player = player1
            player_list.remove(player1)

        if (player2.get_health() <= 0 and player2 in player_list):
            self.game_instance.last_dead_player = player2
            player_list.remove(player2)
