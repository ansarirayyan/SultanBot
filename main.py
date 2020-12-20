import discord
from profanity_filter import ProfanityFilter

client = discord.Client()

pf = ProfanityFilter()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="52 Stories by Omar Waseem on Spotify and iTunes", title="52 Stories", color=discord.Color.green())) # selmshots left the podcast :(

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
		await message.channel.send("In case of an investigation by a federal or local authority, " + message.author.mention + " does not include himself/herself in any groups mentioned or condones any of the actions or language used in this establishment. " + message.author.mention + " is simply a third-party bystander.")

	if pf.is_profane(message.content):
		latestMsg = message.content

		latestMsgPreservedCase = latestMsg
		latestMsg = latestMsg.lower()

		latestMsgLs = latestMsg.split()
		latestMsgLsPreservedCase = latestMsgPreservedCase.split()

		i = len(latestMsgLs)
		containgExceptionWordsOnly = True
		while (i > 0): # TODO: If the profane term is in quotes (is that the right, slang way to say it), then it censors everything after the first quotetion mark which is an issue THIS NEEDS TO BE FIXED
			if ("screw" in latestMsgLs[i-1]) or ("fart" in latestMsgLs[i-1]) or ("damn" in latestMsgLs[i-1]) or ("gay" in latestMsgLs[i-1]) or ("hell" in latestMsgLs[i-1]) or ("nazi" in latestMsgLs[i-1]) or ("retarded" in latestMsgLs[i-1]) or ("paki" in latestMsgLs[i-1]) or ("flipping" in latestMsgLs[i-1]): # whitelisted terms, yes ik words like dAmN won't be whitelisted but whatever also some of these words may not be what I personally consider to be not a bad word also there really should be like a list or array or something rather than having a gazillion in statements
				cleanMsg = ' '.join(latestMsgLs)
			elif pf.is_profane(latestMsgLs[i-1]) == True:
				lsWordIndex = list(latestMsgLsPreservedCase[i-1]) # converts profane term to a list
				firstLetterOfWord = lsWordIndex[0]

				i2 = len(lsWordIndex)
				while (i2 > 0):
					lsWordIndex[i2 - 1] = "-"
					i2 = i2 - 1

				lsWordIndex[0] = firstLetterOfWord

				latestMsgLsPreservedCase[i-1] = ''.join(lsWordIndex)
				cleanMsg = ' '.join(latestMsgLsPreservedCase)
				containgExceptionWordsOnly = False
			else:
				pass
			i = i - 1
		if (containgExceptionWordsOnly == True):
			pass
		else:
			await message.delete()
			await message.channel.send(str(message.author) + ": " + cleanMsg)

	if message.content.startswith('sultanim khanos'):
		if message.author.id == 617827708289941524:
			i = 3
			while (i > 0):
				await message.channel.send("KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !! KHANOS THE STRONGEST !!") # was going to put each line individually 35 times put apparently there's a delay
				i = i - 1
		else:
			await message.channel.send("Only KHANOS THE STRONGEST is allowed to execute this command")
	if message.content.startswith("sultanim purge"):
		global safepurge
		with open('settings') as f:
			if 'True' in f.read(): # only one setting so not future proof also not server-specific so not good for large-scale implementation
				safepurge = True
			else:
				safepurge = False
		cmdReceived = message.content
		number_str = cmdReceived.replace ("sultanim purge ", "")
		number = int(number_str)
		if safepurge == False:
			await message.delete()
			await message.channel.purge(limit=number)
		elif safepurge == True:
			newNumber = number + 1
			messages = await message.channel.history(limit=newNumber).flatten()
			i = 0
			while i < len(messages):
				msg = messages[i]
				if msg.pinned == False: # when chaning this to True; it goes to the else
					await msg.delete()
				i = i + 1

client.run('')
