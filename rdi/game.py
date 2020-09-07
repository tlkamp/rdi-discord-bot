from .player import Player
from prettytable import PrettyTable
from discord.user import User


class Game:
    def __init__(self, boozemeister: User):
        self.boozemeister = boozemeister
        self.players = [Player(boozemeister.display_name)]

    def stats(self):
        columns = ["player", "character", "fortitude", "alcohol", "gold", "drinks"]
        table = PrettyTable(field_names=columns)
        for p in self.players:
           table.add_row([p.discord_user, p.character, p.fortitude, p.alcohol, p.gold, p.drinks])
        return f"```{table}```"

    def add_player(self, player: Player):
        self.players.append(player)
