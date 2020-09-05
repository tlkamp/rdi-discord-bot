from redbot.core import commands
from redbot.core import Config


class RedDragonInn(commands.Cog):
    def __init__(self):
        self.config = Config.get_conf(self, identifier=999999999999, force_registration=True)

    @commands.group()
    @commands.guild_only()
    async def rdi(self, ctx):
        pass

    @rdi.command()
    async def start(self, ctx, boozemeister: str, *players):
        """Start a game of Red Dragon Inn!"""
        await ctx.send(f"Players: {players}, Boozemeister: {boozemeister}")
        pass

    @rdi.command()
    async def stats(self, ctx):
        """Display all players stats"""
        pass

    @rdi.command()
    async def fortitude(self, ctx, value: int):
        """Add or remove fortitude from your character"""
        pass

    @rdi.command()
    async def alcohol(self, ctx, value: int):
        """Add or remove alcohol content from your character"""
        pass

    @rdi.command()
    async def gold(self, ctx, value: int):
        """Add or remove gold from your pot. """
        pass

    @rdi.command()
    async def buy_drink(self, ctx, player: str, count: int):
        """Buy a drink for your friend! Adds [count] drinks to their Drink Me! pile"""
        pass

    @rdi.command()
    async def drink(self, ctx):
        """Removes a drink from your Drink Me! pile."""
        pass

    @rdi.command()
    async def end_game(self, ctx):
        """end the current Red Dragon Inn game"""
        pass
