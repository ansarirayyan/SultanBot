import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('sultanim spam'):
        i = 1
        while (i <= 3):
            await message.channel.send("SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! ")
            i = i + 1
    if message.content.startswith('sultanim anti-fbi'):
        await message.channel.send("In case of an investigation by a federal or local authority, I do not include myself in any groups mentioned or condone any of the actions or language used in this establishment. I am simply a third-party bystander.")

client.run('') # GET RID OF THIS BEFORE PUSHING!!!!!!!!!!!!!
