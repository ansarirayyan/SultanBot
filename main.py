import discord
from profanity_filter import ProfanityFilter

client = discord.Client()

pf = ProfanityFilter()

# profanity-filter settings
pf.censor_char = '@'
#pf.censor_whole_words = False
pf.extra_profane_word_dictionaries = {'en': {'dumbass'}}

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #await message.channel.send("DESTUR! SULTAN SALAHUDDEEN ES-STEVE EL-BOWMAN HAN EL-HAJI HAZRETLERI!") # something gone wronf the last time I tried this THIS DOESN'T DO ANYTHING

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
    if message.content.startswith('sultanim anti-fbi'):
        await message.channel.send("In case of an investigation by a federal or local authority, " + message.author.mention + " does not include himself/herself in any groups mentioned or condones any of the actions or language used in this establishment. " + message.author.mention + " is simply a third-party bystander.")

    if pf.is_profane(message.content):
        if ("screw" in message.content) or ("fart" in message.content): # whitelisted terms
            pass
        else:
            latestMsg = message.content
            latestMsgArray = latestMsg.split() # technically it's not an array but a list but who cares also Geany doesn't have a quick way to Find and Replace like Atom
            print(len(latestMsgArray))
            i = len(latestMsgArray)
            while (i > 0):
                if pf.is_profane(latestMsgArray[i-1]) == True:
                    await message.delete()
                    lsWordIndex = list(latestMsgArray[i-1])
                    firstLetterOfWord = lsWordIndex[0]
                    i2 = len(lsWordIndex)
                    while (i2 > 0):
                        lsWordIndex[i2 - 1] = "-"
                        i2 = i2 - 1
                    lsWordIndex[0] = firstLetterOfWord
                    print (str(lsWordIndex))
                    latestMsgArray[i-1] = ''.join(lsWordIndex)
                    cleanMsg = ' '.join(latestMsgArray)
                    await message.channel.send(str(message.author) + ": " + cleanMsg)
                    print(pf.censor(str(message.content)))
                    await message.channel.send(embed = discord.Embed(description = "Ey " + message.author.mention + ", do not mix with the wolves for that they eat the jackals.", color = discord.Color.red())) # For the record, I am not of Turkish origin
                else:
                    pass
                i = i - 1
            #await message.delete()
            #await message.channel.send(str(message.author) + ": " + pf.censor(str(message.content)))
            #print(pf.censor(str(message.content)))
            #await message.channel.send(embed = discord.Embed(description = "Ey " + message.author.mention + ", do not mix with the wolves for that they eat the jackals.", color = discord.Color.red())) # For the record, I am not of Turkish origin
            #embed_dict["color"] = f54b4b

    if message.content.startswith('sultanim khanos'):
        if message.author.id == 617827708289941524:
            i = 3
            while (i > 0):
                await message.channel.send("KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !!") # was going to put each line individually 35 times put apparently there's a delay
                i = i - 1
        else:
            await message.channel.send("Only KHANOS THE STRONGEST is allowed to execute this command")

client.run('Njk1NTI0MzA1NzczMjY0OTg3.XorU2Q.ncmwYKc18lLVlvsWlKHALi_WW5s') # GET RID OF THIS BEFORE PUSHING!!!!!!!!!!!!! (but of course, I don't)
