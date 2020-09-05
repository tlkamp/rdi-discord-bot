from redbot.core.commands import Cog, command, guild_only
from redbot.core import Config


class RDI(Cog):
    def __init__(self):
        self.config = Config.get_conf(self, identifier=999999999999, force_registration=True)

    @command()
    @guild_only()
    async def start(self, ctx, players: list, boozemeister: str):
        """Start a game of Red Dragon Inn!"""
        await ctx.send(f'Game started! Players: {players} / Boozemeister: {boozemeister}')

    @command()
    @guild_only()
    async def stats(self, ctx):
        """Display all players stats"""
        pass

    @command()
    @guild_only()
    async def fortitude(self, ctx, value: int):
        """Add or remove fortitude from your character"""
        pass

    @command()
    @guild_only()
    async def alcohol(self, ctx, value: int):
        """Add or remove alcohol content from your character"""
        pass

    @command()
    @guild_only()
    async def gold(self, ctx, value: int):
        """Add or remove gold from your pot. """
        pass

    @command()
    @guild_only()
    async def buy_drink(self, ctx, player: str, count: int):
        """Buy a drink for your friend! Adds [count] drinks to their Drink Me! pile"""
        pass
