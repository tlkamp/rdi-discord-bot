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

## Rule Management
There are some aspects of Red Dragon Inn that are ambiguous in the official rule documentation, and there are ways to
enhance the game to make it more enjoyable. These kinds of game play changes typically take the form of "house rules". 

House rules are special rules or rule clarifications added to the game's base ruleset to improve gameplay or make certain
situations less ambiguous.

> **Note:** Only the Boozemeister can manage house rules.

### Adding Rules
To add a house rule, provide the rule text _in quotes_.

`!rdi addrule "rule text here"`

### Removing Rules
Make a typo? House rule doesn't create the atmosphere you want? Is the rule so disliked by the players that it needs to be gone?

Remove it!

`!rdi removerule <rule number>`

### Viewing Rules
Did the Boozemeister get carried away with house rules and now you can't remember them all? Don't worry, you're covered.

`!rdi rules` to view _all_ rules

`!rdi gamerules` to view the rules of Red Dragon Inn itself.

`!rdi houserules` to view only the house rules added by the Boozemeister.
