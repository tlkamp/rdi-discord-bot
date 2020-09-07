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
        Join the game of Red Dragon Inn!
        """
        if self.game_exists(ctx):
            self.games[ctx.guild][ctx.channel].add_player(Player(ctx.author.display_name, character))
            await ctx.send(f"{ctx.author.display_name} added to game.")
            await self.stats(ctx)

    @rdi.command(aliases=["add"])
    async def addplayer(self, ctx, player: discord.user.User, character=""):
        """Add another player to the game. Only the boozemeister can add other players."""
        if self.author_is_boozemeister(ctx):
            self.games[ctx.guild][ctx.channel].add_player(Player(player.display_name, character))
            await ctx.send(f"Player {player} added to the game.")
            await self.stats(ctx)
        else:
            await ctx.send("Only the boozemeister can add other players to a game.")

    @rdi.command()
    async def stats(self, ctx):
        """Display all players stats"""
        if self.game_exists(ctx):
            await ctx.send(self.games[ctx.guild][ctx.channel].stats())

    @rdi.command()
    async def fortitude(self, ctx, value: int):
        """Add or remove fortitude from your character"""
        if self.game_exists(ctx):
            game = self.game_for_guild_channel(ctx)
            game.players[ctx.author.display_name].update_fortitude(value)
            await self.stats(ctx)

    @rdi.command()
    async def alcohol(self, ctx, value: int):
        if self.game_exists(ctx):
            game = self.game_for_guild_channel(ctx)
            game.players[ctx.author.display_name].update_alcohol(value)
            await self.stats(ctx)

    @rdi.command()
    async def gold(self, ctx, value: int):
        """Add or remove gold from your pot. """
        if self.game_exists(ctx):
            game = self.game_for_guild_channel(ctx)
            game.players[ctx.author.display_name].update_gold(value)
            await self.stats(ctx)

    @rdi.command()
    async def buy_drink(self, ctx, player: discord.user.User, count: int):
        """Buy a drink for your friend! Adds [count] drinks to their Drink Me! pile"""
        if self.author_in_game(ctx) and self.player_in_game(ctx, player):
            game = self.game_for_guild_channel(ctx)
            game.players[player.display_name].drinks += count
            await self.stats(ctx)

    @rdi.command()
    async def drink(self, ctx):
        """Removes a drink from your Drink Me! pile."""
        pass

    @rdi.command(aliases=["gr"])
    async def gamerules(self, ctx):
        """View the rules for Red Dragon Inn."""
        pass

    @rdi.command(aliases=["hr"])
    async def houserules(self, ctx):
        """View the house rules in play for the current game of Red Dragon Inn."""
        if self.game_exists(ctx):
            game = self.game_for_guild_channel(ctx)
            await ctx.send("**House Rules**")
            for num, rule in game.get_rules():
                await ctx.send(f"{num}. {rule}")

    @rdi.command(aliases=["newrule", "nr", "ar"])
    async def addrule(self, ctx, rule: str):
        """Add a new house rule for the current game. Only the boozemeister can add house rules."""
        if self.author_is_boozemeister(ctx):
            game = self.game_for_guild_channel(ctx)
            game.house_rules.append(rule)
            await ctx.send("New house rule added.")
            await self.houserules(ctx)
        else:
            ctx.send("Only the boozemeister can add new house rules.")

    @rdi.command()
    async def removerule(self, ctx, rule: int):
        """Remove a house rule. Only the boozemeister can remove house rules."""
        if self.author_is_boozemeister(ctx):
            game = self.game_for_guild_channel(ctx)
            # The rule numbers are offset by 1 for the users.
            del game.house_rules[rule-1]
            await self.houserules(ctx)


    @rdi.command()
    async def rules(self, ctx):
        """View all rules in effect for the current game of Red Dragon Inn"""
        await self.gamerules(ctx)
        await self.houserules(ctx)

    @rdi.command(aliases=["end"])
    async def end_game(self, ctx):
        """end the current Red Dragon Inn game"""
        if self.author_is_boozemeister(ctx):
            del self.games[ctx.guild][ctx.channel]
            await ctx.send(f"The Red Dragon Inn game for {ctx.channel} has ended.")
        else:
            await ctx.send("Only the boozemeister can end the game.")

    # Helper functions for checking Game existence and Boozemisterness
    def game_exists(self, ctx) -> bool:
        return ctx.guild in self.games.keys() and ctx.channel in self.games[ctx.guild] and \
            self.games[ctx.guild][ctx.channel] is not None

    def game_for_guild_channel(self, ctx) -> Game:
        return self.games[ctx.guild][ctx.channel]

    def author_is_boozemeister(self, ctx) -> bool:
        if self.game_exists(ctx):
            if ctx.author == self.games[ctx.guild][ctx.channel].boozemeister:
                return True
        return False

    def author_in_game(self, ctx) -> bool:
        if self.game_exists(ctx):
            return ctx.author.display_name in self.game_for_guild_channel(ctx).players.keys()
        return False

    def player_in_game(self, ctx, player: discord.user.User) -> bool:
        if self.game_exists(ctx):
            return player.display_name in self.game_for_guild_channel(ctx).players.keys()
        return False
