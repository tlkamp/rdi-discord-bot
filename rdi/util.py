from functools import wraps


def author_is_boozemeister(func):
    @wraps(func)
    async def _impl(self, *args, **kwargs):
        ctx = args[0]
        if self.game_exists(ctx):
            if ctx.author == self.games[ctx.guild][ctx.channel].boozemeister:
                return await func(self, *args, **kwargs)
            else:
                return await \
                    ctx.send(f"{ctx.author} is not the Boozemeister! Only the Boozemeister can perform this action.")
    return _impl


def author_in_game(func):
    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        ctx = args[0]
        if self.game_exists(ctx):
            if ctx.author.display_name in self.game_for_guild_channel(ctx).players.keys():
                return await func(self, *args, **kwargs)
            return await ctx.send(f"{ctx.author} is not in the game!")
    return wrapper
