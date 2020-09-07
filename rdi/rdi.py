from redbot.core import commands
from redbot.core import Config
import discord
from .player import Player
from .game import Game
import logging

logger = logging.getLogger(__name__)


class RedDragonInn(commands.Cog):
    def __init__(self):
        self.config = Config.get_conf(self, identifier=999999999999, force_registration=True)
        self.games = dict()

    @commands.group()
    @commands.guild_only()
    async def rdi(self, ctx):
        pass

    @rdi.command()
    async def start(self, ctx):
        """Start a game of Red Dragon Inn!"""
        if ctx.guild in self.games.keys():
            guild_games = self.games[ctx.guild]
            if ctx.channel in guild_games.keys() and guild_games[ctx.channel] is not None:
                await ctx.send("Only one game can be active at a time.")
                return
        else:
            self.games[ctx.guild] = dict()

        g = Game(ctx.author)
        self.games[ctx.guild][ctx.channel] = g
        await ctx.send(f"{ctx.author.display_name} has started a game of Red Dragon Inn!")
        await ctx.send(f"Use `{ctx.clean_prefix}play` to add yourself to the game.")
        await ctx.send(g.stats())

    @rdi.command()
    async def play(self, ctx, character: str = ""):
        """
        Add yourself or another player to the game.
        You must be the Boozemeister to add players other than yourself.
        """
        self.games[ctx.guild][ctx.channel].add_player(Player(ctx.author.display_name, character))
        await ctx.send(f"{ctx.author.display_name} added to game.")
        await self.stats(ctx)

    @rdi.command(aliases=["add"])
    async def addplayer(self, ctx, player: discord.user.User, character=""):
        """Add another player to the game. Only the boozemeister can add other players."""
        if ctx.author is self.games[ctx.guild][ctx.channel].boozemeister:
            self.games[ctx.guild][ctx.channel].add_player(Player(player.display_name, character))
            await ctx.send(f"Player {player} added to the game.")
            await self.stats(ctx)
        else:
            await ctx.send("Only the boozemeister can add other players to a game.")

    @rdi.command()
    async def stats(self, ctx):
        """Display all players stats"""
        await ctx.send(self.games[ctx.guild][ctx.channel].stats())
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

    @rdi.command(aliases=["end"])
    async def end_game(self, ctx):
        """end the current Red Dragon Inn game"""
        if ctx.author == self.games[ctx.guild][ctx.channel].boozemeister:
            del self.games[ctx.guild][ctx.channel]
            await ctx.send(f"The Red Dragon Inn game for {ctx.channel} has ended.")
        else:
            await ctx.send("Only the boozemeister can end the game.")
