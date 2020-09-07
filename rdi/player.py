class Player:
    def __init__(self, discord_user, character: str = "", boozemeister: bool = False):
        # Set the default values
        self._fortitude = 20
        self._alcohol = 0
        self._gold = 10
        self.character = character
        self.discord_user = discord_user
        self._drinks = 1
        self.lost = False
        self.is_boozemeister = boozemeister

    def __repr__(self):
        return f"{self.discord_user}{'*' if self.is_boozemeister else ''}"

    def drink(self):
        self.drinks -= 1

    def fortitude(self):
        return self._fortitude

    def gold(self):
        return self._gold

    def alcohol(self):
        return self._alcohol

    def drinks(self):
        return self._drinks

    def update_gold(self, value: int):
        self._gold += value

    def update_alcohol(self, value: int):
        self._alcohol += value

    def update_fortitude(self, value: int):
        self._fortitude += value

