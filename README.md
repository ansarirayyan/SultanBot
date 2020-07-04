# Introduction
[SultanBot](https://github.com/ansarirayyan/SultanBot/) is a Discord guild/server bot made using the [`discord.py`](https://discordpy.readthedocs.io/en/latest/) library. The aim of this project is to port all the awesome and non-redundant features of [awaaz](https://github.com/ansarirayyan/awaaz/) into what Discord might consider as a proper bot. You can either simply add the bot to your server which is already hosted by me (may be down from time-to-time) or deploy it yourself!

# Add to Server
To add to your server, simply visit [this URL](https://discordapp.com/api/oauth2/authorize?client_id=695524305773264987&permissions=8&scope=bot).

# Behavior/Usage
* `sultanim spam` will spam the chat a bit
* `sultanim anti-fbi` will attempt to free the user who executes it of any legal trouble
* automatic profanity manager which censors cuss words from messages and posts a warning
* `sultanim purge <number_of_messages>` with safepurge feature (basically, no pinned messages are deleted; if you would like to turn this off, change `True` to `False` in the `settings` file

# Installation

If you really insist on deploying this on your own (for whatever reason that may be, including me not hosting the bot anymore), then simply do as the following outlines.

The first step is to register an application and obtain a Discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications).

Please insert this bot token between the quotation marks of the `client.run()` statement, likely towards the end of `main.py`. 

Attempt to run the script. 

On UNIX and UNIX-like machines:
```python3 main.py```

On Windows machines:
```py main.py```

The message `We have logged in as <DiscordTag>` will likely be displayed.

If you are unable to get this to work, then please refer to the next sub-section of this README.md file.

## Debugging
* If you are facing an issue such as `discord.errors.Forbidden: 403 Forbidden (error code: 60003): Two factor is required for this operation`, then please refer to [this GitHub Issues post](https://github.com/discord/discord-api-docs/issues/69). In short, you need to enable two factor authentication on the account which owns the bot.
* Upon running the program, you may receive missing module errors. Simply install the libraries mentioned.
* After the successful installation of `profanity-filter`, one may still receive errors related to the `spacey` library. Simply refer to [this GitHub Issues page]. Append `sudo` to the beginning of both parts of the command if needed. Also, one might want to try replacing `python` with `py` if his or her platform that he or she wishes to deploy is that of Microsoft's Windows.
* If there is some unexpected behavior occuring related to the bad language filter, then please make sure that you did not install the "Deep Analysis" version of `profanity-filter`.

If nothing here helps, then please [post an Issue](https://github.com/ansarirayyan/SultanBot/issues)!

# To-Do List

Not everything on my to-do list but some, as well as some not literally written down in my "idea journal."

* make a separate file for all the functions [like in awaaz](https://raw.githubusercontent.com/ansarirayyan/awaaz/master/python/actions.py)
* mute after a certain amount of instances where the user in question uses profanity
* maybe utilize the `Issues` tab to track to-dos and stuff, as well as post all the ideas from my tiny journal while I'm at it (low-priority)
* bundle all those bad word exceptions into a list or something if possible
* somehow make all the bad word exceptions case insensitive, or generate all possible capitilization combinations and paste into a text file for the program to use
