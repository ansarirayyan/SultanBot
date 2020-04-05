import discord
from profanity_filter import ProfanityFilter

client = discord.Client()

pf = ProfanityFilter()

pf.censor_char = '@'

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
            await message.channel.send(message.author.mention + ", you are not allowed to execute this command on orders of the Emirate's Council of Wells.")
        elif ((message.author.id == 405500127198052363) and (message.channel.id == 695704051794313316)):
            i = 1
            while (i <= 3):
                await message.channel.send("SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! SPAM !!! ")
                i = i + 1
        else:
            await message.channel.send("Something gone wrong. Contact mohdhaadiansari@gmail.com to get this resolved... Or not.")
    if message.content.startswith('sultanim anti-fbi'):
        await message.channel.send("In case of an investigation by a federal or local authority, " + message.author.mention + " does not include himself/herself in any groups mentioned or condones any of the actions or language used in this establishment. " + message.author.mention + " is simply a third-party bystander.")

    if pf.is_profane(message.content):
        await message.delete()
        await message.channel.send(str(message.author) + ": " + pf.censor(str(message.content)))
        print(pf.censor(str(message.content)))
        await message.channel.send("Ey " + message.author.mention + ", do not mix with the wolves for that they eat the jackals.") # For the record, I am not of Turkish origin
        
    if message.content.startswith('sultanim khanos'):
        if message.author.id == 617827708289941524:
            i = 3
            while (i > 0):
                await message.channel.send("KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !!") # was going to put each line individually 35 times put apparently there's a delay
                i = i - 1
        else:
            await message.channel.send("Only KHANOS THE STRONGEST is allowed to execute this command")

client.run('Njk1NTI0MzA1NzczMjY0OTg3.XogoxA.RVmKiK-OdEyC4tiI81-uv51tprw') # GET RID OF THIS BEFORE PUSHING!!!!!!!!!!!!!
