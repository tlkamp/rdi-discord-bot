import discord


class Player:
    def __init__(self, discord_user, character: str = ""):
        # Set the default values
        self.fortitude = 20
        self.alcohol = 0
        self.gold = 10
        self.character = character
        self.discord_user = discord_user
        self.drinks = 1

    def __repr__(self):
        return f"{self.discord_user}"

    def drink(self):
        self.drinks -= 1

