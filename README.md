# rdi-discord-bot
Red Dragon Inn cog for Red-DiscordBot that manages virtual Red Dragon Inn games through Discord.

## Playing Red Dragon Inn
This Cog is intended to help players keep track of game events while playing Red Dragon Inn.

You can find the publisher's recommendation for how to play Red Dragon Inn remotely [here.](http://slugfestgames.com/teleconference-rdi/)

### Starting A Game
To start a game of Red Dragon Inn, issue the following command: `!rdi start`

> **Note**: The user who starts the game becomes the Boozemeister.
> The Boozemeister is added as a player automatically.

### Viewing Player Stats
To view the current Fortitude, Alcohol Content, Gold, and Drink Me! pile of the current players:

`!rdi stats`

### To Add Fortitude, Alcohol Content or Gold to _YOUR_ Character
> **Note:** Negative numbers are accepted by the `fortitude`, `alcohol` and `gold` commands.

`!rdi fortitude <int>`

`!rdi alcohol <int>`

`!rdi gold <int>`

### Buying Drinks
To help your Boozemeister keep track of drinks, tell RDI bot who you're buying drinks for:

`!rdi buy_drink <player>`

### Drinking Drinks
Decrement your current Drink Me! pile count.

`!rdi drink`

### Ending a Game
> **Note**: Only the Boozemeister is allowed to end the game.
`!rdi end_game`
