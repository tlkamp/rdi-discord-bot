from .player import Player
from prettytable import PrettyTable
from discord.user import User


class Game:
    def __init__(self, boozemeister: User):
        self.boozemeister = boozemeister
        self.players = dict()
        self.players[boozemeister.display_name] = Player(boozemeister.display_name)

    def stats(self):
        columns = ["player", "character", "fortitude", "alcohol", "gold", "drinks"]
        table = PrettyTable(field_names=columns)
        for k, v in self.players.items():
           table.add_row([v.discord_user, v.character, v.fortitude, v.alcohol, v.gold, v.drinks])
        return f"```{table}```"

    def add_player(self, player: Player):
        self.players[player.discord_user] = player
