# Introduction
[SultanBot](https://github.com/ansarirayyan/SultanBot/) is a Discord guild/server bot made using the [`discord.py`](https://discordpy.readthedocs.io/en/latest/) library. The aim of this project is to port all the awesome and non-redundant features of [awaaz](https://github.com/ansarirayyan/awaaz/) into what Discord might consider as a proper bot.

# Behavior/Usage

* `sultanim spam` will spam the chat a bit
* `sultanim anti-fbi` will attempt to free the user who executes it of any legal trouble
* automatic profanity manager which censors cuss words from messages and posts a warning

# Installation

Register a `bot` token from the [Discord Developer Portal](https://discordapp.com/developers) by creating a `Bot` in an `Application`. Look at the last line of `main.py` and paste the token in the quotes. Install all the necessary modules needed if prompted to when running `main.py`. If you get some kind of `spacey` error AFTER installing the `profanity-filter` module, then refer to [this GitHub issue page](https://github.com/explosion/spaCy/issues/1721#issuecomment-368444483) on possible fixes. The highlighted answer worked for me personally on Linux after appending `sudo` to both parts of the command and running it in the Terminal. Upon running the command successfully you will see `We have logged in as <DiscordTag>` in the ouput with no further error messages. Have fun!

# To-Do List
* make a separate file for all the functions [like in awaaz](https://raw.githubusercontent.com/ansarirayyan/awaaz/master/python/actions.py)
* mute after a certain amount of instances where the user in question uses profanity
* implement the pool system in `profanity` with `profanity-filter`
