import discord
from profanity import profanity
# from actions import spam

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('sultanim spam'):
        if message.author.id != 405500127198052363:
            i = 1
            while (i <= 3):
                await message.channel.send("SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! ")
                i = i + 1
        elif ((message.author.id == 405500127198052363) and (message.channel.id != 695704051794313316)):
            await message.channel.send(message.author.mention + ", you are not allowed to execute this command on orders of Emirate's Noble Council.")
        elif ((message.author.id == 405500127198052363) and (message.channel.id == 695704051794313316)):
            i = 1
            while (i <= 3):
                await message.channel.send("SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! ")
                i = i + 1
        else:
            await message.channel.send("Something gone wrong. Contact mohdhaadiansari@gmail.com to get this resolved... Or not.")
    if message.content.startswith('sultanim anti-fbi'):
        await message.channel.send("In case of an investigation by a federal or local authority, " + message.author.mention + " does not include himself/herself in any groups mentioned or condones any of the actions or language used in this establishment. " + message.author.mention + " is simply a third-party bystander.")

    if profanity.contains_profanity(message.content):
        await message.delete()
        await message.channel.send(str(message.author) + ": " + profanity.censor(str(message.content)))
        print(profanity.censor(str(message.content)))
        await message.channel.send("Ey " + message.author.mention + ", do not mix with the wolves for that they eat the jackals.") # For the record, I am not of Turkish origin

client.run('') # GET RID OF THIS BEFORE PUSHING!!!!!!!!!!!!!
