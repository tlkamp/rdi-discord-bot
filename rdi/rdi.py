from redbot.core import commands
from redbot.core import Config
import discord
from .player import Player
from .game import Game
import logging
from .util import *

logger = logging.getLogger(__name__)


class RedDragonInn(commands.Cog):
    def __init__(self):
        self.config = Config.get_conf(self, identifier=999999999999, force_registration=True)
        self.games = dict()
        super().__init__()

    @commands.group()
    @commands.guild_only()
    async def rdi(self, ctx):
        pass

    # Game setup
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
        await ctx.send(f"Use `{ctx.clean_prefix}rdi play` to add yourself to the game.")
        await self.stats(ctx)

    @rdi.command()
    @game_exists
    @author_is_boozemeister
    async def end(self, ctx):
        """End the current Red Dragon Inn game"""
        del self.games[ctx.guild][ctx.channel]
        await ctx.send(f"The Red Dragon Inn game for {ctx.channel} has ended.")

    @rdi.command()
    @game_exists
    async def play(self, ctx, character: str = ""):
        """
        Join the game of Red Dragon Inn!
        """
        self.games[ctx.guild][ctx.channel].add_player(Player(ctx.author.display_name, character))
        await ctx.send(f"{ctx.author.display_name} added to game.")
        await self.stats(ctx)

    @rdi.command(aliases=["randomize", "rt"])
    @game_exists
    @author_is_boozemeister
    async def random(self, ctx):
        """Randomize the turn order. Only the boozemeister can randomize the turn order."""
        import random
        game = self.game_for_guild_channel(ctx)
        temp = list(game.players.items())
        random.shuffle(temp)
        game.players = dict(temp)
        await self.stats(ctx)

    @rdi.command(aliases=["add"])
    @game_exists
    @author_is_boozemeister
    async def addplayer(self, ctx, player: discord.user.User, character=""):
        """Add another player to the game. Only the boozemeister can add other players."""
        self.games[ctx.guild][ctx.channel].add_player(Player(player.display_name, character))
        await ctx.send(f"Player {player} added to the game.")
        await self.stats(ctx)

    @rdi.command()
    @game_exists
    async def stats(self, ctx):
        """Display all players stats"""
        await ctx.send(self.games[ctx.guild][ctx.channel].stats())

    # Player Actions
    @rdi.command()
    @game_exists
    async def fortitude(self, ctx, value: int):
        """Add or remove fortitude from your character"""
        game = self.game_for_guild_channel(ctx)
        game.players[ctx.author.display_name].update_fortitude(value)
        await self.stats(ctx)

    @rdi.command()
    @game_exists
    async def alcohol(self, ctx, value: int):
        """Have another or sober up!"""
        game = self.game_for_guild_channel(ctx)
        game.players[ctx.author.display_name].update_alcohol(value)
        await self.stats(ctx)

    @rdi.command()
    @game_exists
    async def gold(self, ctx, value: int):
        """Add or remove gold from your pot. """
        game = self.game_for_guild_channel(ctx)
        game.players[ctx.author.display_name].update_gold(value)
        await self.stats(ctx)

    @rdi.command()
    @game_exists
    @author_in_game
    async def buy(self, ctx, player: discord.user.User, count: int):
        """Buy a drink for your friend! Adds [count] drinks to their Drink Me! pile"""
        if self.player_in_game(ctx, player):
            game = self.game_for_guild_channel(ctx)
            # TODO: drinks is a method
            game.players[player.display_name].drinks += count
            await self.stats(ctx)

    @rdi.command()
    @game_exists
    @author_in_game
    async def drink(self, ctx):
        """Removes a drink from your Drink Me! pile."""
        game = self.game_for_guild_channel(ctx)
        game.players[ctx.author.display_name].drink()
        await self.stats(ctx)

    # Game Rules
    @rdi.command(aliases=["gr"])
    async def gamerules(self, ctx):
        """View the rules for Red Dragon Inn."""
        game_rules = "https://slugfestgames.com/games/rdi/"
        virtual_rdi_rules = "https://slugfestgames.com/teleconference-rdi/"
        await ctx.send("**Red Dragon Inn Rules**")
        await ctx.send(f"Game & Character Rules - {game_rules}")
        await ctx.send(f"Remote RDI Rules - {virtual_rdi_rules}")
        await ctx.send("REMEMBER: This only works if you are honest. Please don't make us regret playing with you.")

    @rdi.command(aliases=["hr"])
    @game_exists
    async def houserules(self, ctx):
        """View the house rules in play for the current game of Red Dragon Inn."""
        game = self.game_for_guild_channel(ctx)
        await ctx.send("**House Rules**")
        for num, rule in game.get_rules():
            await ctx.send(f"{num}. {rule}")

    @rdi.command(aliases=["newrule", "nr", "ar"])
    @game_exists
    @author_is_boozemeister
    async def addrule(self, ctx, rule: str):
        """Add a new house rule for the current game. Only the boozemeister can add house rules."""
        game = self.game_for_guild_channel(ctx)
        game.house_rules.append(rule)
        await ctx.send("New house rule added.")
        await self.houserules(ctx)

    @rdi.command()
    @game_exists
    @author_is_boozemeister
    async def removerule(self, ctx, rule: int):
        """Remove a house rule. Only the boozemeister can remove house rules."""
        game = self.game_for_guild_channel(ctx)
        # The rule numbers are offset by 1 for the users.
        del game.house_rules[rule-1]
        await self.houserules(ctx)

    @rdi.command()
    async def rules(self, ctx):
        """View all rules in effect for the current game of Red Dragon Inn"""
        await self.gamerules(ctx)
        await self.houserules(ctx)

    # Helper functions for checking Game existence and Boozemisterness
    def game_for_guild_channel(self, ctx) -> Game:
        return self.games[ctx.guild][ctx.channel]

    def player_in_game(self, ctx, player: discord.user.User) -> bool:
        return player.display_name in self.game_for_guild_channel(ctx).players.keys()
