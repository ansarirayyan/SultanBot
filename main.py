import discord
from profanity_filter import ProfanityFilter

client = discord.Client()

pf = ProfanityFilter()

pf.extra_profane_word_dictionaries = {'en': {'dumbass', 'MOTHERFUCKERS', 'motherfuckers', 'benchod', 'madrachod', 'BENCHOD', 'MADRACHOD'}} # not case insensitive; should I add dhigger (the n word for Indians)... nah

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="52 Stories by Omar Waseem on Spotify and iTunes", title="52 Stories", color=discord.Color.green())) # selmshots left the podcast :(
	#await client.change_presence(activity=discord.Spotify(type=discord.ActivityType.listening, name="Spotify", title="52 Stories"))
	#await client.change_presence(activity=discord.Spotify(title="52 Stories"))

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
		latestMsg = message.content
		latestMsgArray = latestMsg.split() # technically it's not an array but a list but who cares also Geany doesn't have a quick way to Find and Replace like Atom actually it does dumby but guess what too lazy to find it again
		print(len(latestMsgArray))
		i = len(latestMsgArray)
		containgExceptionWordsOnly = True
		while (i > 0): # TODO: If the profane term is in quotes (is that the right, slang way to say it), then it censors everything after the first quotetion mark which is an issue THIS NEEDS TO BE FIXED
			if ("screw" in latestMsgArray[i-1]) or ("fart" in latestMsgArray[i-1]) or ("damn" in latestMsgArray[i-1]) or ("DAMN" in latestMsgArray[i-1]) or ("gay" in latestMsgArray[i-1]) or ("hell" in latestMsgArray[i-1]) or ("HELL" in latestMsgArray[i-1]) or ("nazi" in latestMsgArray[i-1]) or ("NAZI" in latestMsgArray[i-1]) or ("retarded" in latestMsgArray[i-1]) or ("RETARDED" in latestMsgArray[i-1] or ("HELL" in latestMsgArray[i-1]) or ("SCREW" in latestMsgArray[i-1]) or ("Damn" in latestMsgArray[i-1]) or ("paki" in latestMsgArray[i-1]) or ("PAKI" in latestMsgArray[i-1])): # whitelisted terms, yes ik words like dAmN won't be whitelisted but whatever also some of these words may not be what I personally consider to be not a bad word also there really should be like a list or array or something rather than having a gazillion in statements
				cleanMsg = ' '.join(latestMsgArray)
			elif pf.is_profane(latestMsgArray[i-1]) == True:
				lsWordIndex = list(latestMsgArray[i-1]) # converts profane term to a list
				firstLetterOfWord = lsWordIndex[0]
				i2 = len(lsWordIndex)
				while (i2 > 0):
					lsWordIndex[i2 - 1] = "-"
					i2 = i2 - 1
				lsWordIndex[0] = firstLetterOfWord
				print (str(lsWordIndex))
				latestMsgArray[i-1] = ''.join(lsWordIndex)
				cleanMsg = ' '.join(latestMsgArray)
				containgExceptionWordsOnly = False
			else:
				pass
			i = i - 1
		if (containgExceptionWordsOnly == True):
			pass
		else:
			await message.delete()
			await message.channel.send(str(message.author) + ": " + cleanMsg)
			# await message.channel.send(embed = discord.Embed(description = "Ey " + message.author.mention + ", do not mix with the wolves for that they eat the jackals.", color = discord.Color.red())) # For the record, I am not of Turkish origin

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
		#with open("settings", "w+") as f:
		#	data = f.readlines
		#for line in data: yeah idk how this would've worked anyways if not in the `with` block
		#	if line.__contains__("safepurge"):
		#		if "True" in line:
		#			safepurge = True
		#		elif "False" in line:
		#			safepurge = False
		#		else:
		#			await message.channel.send("Something gone wrong, please tell Rayyan or just post an issue on GitHub")
		with open('settings') as f:
			if 'True' in f.read(): # only one setting so not future prood but who really cares
				#print("true")
				safepurge = True
			else:
				safepurge = False
		cmdReceived = message.content
		number_str = cmdReceived.replace ("sultanim purge ", "")
		number = int(number_str)
		if safepurge == False:
			print("Purging " + number_str + " lines, including pinned messages (if any).")
#			number = int(number_str)
			await message.delete()
			await message.channel.purge(limit=number)
		elif safepurge == True:
			print("Purging " + number_str + " lines, excluding pinned messages (if any).")
			newNumber = number + 1
			messages = await message.channel.history(limit=newNumber).flatten()
			#print(messages)
			#i = len(messages) - 1
			#while (i + 1) > 0:
			i = 0
			while i < len(messages):
				msg = messages[i]
				#print(msg.pinned) # ok, so something def wrong with this thing, as its all saying false no matter what OH SHOOT JUST REALIZED SOMETHING I PUT MESSAGE NOT MSG MESSAGE IS ALWAYS GONNA BE BENIM AHMAK AAAAAAAA
				if msg.pinned == False: # when chaning this to True; it goes to the else
					#msg = messages[i]
					await msg.delete()
				else:
					#pass
					print("\nThe following message was supposed to be deleted: " + str(messages[i]) + "\n") # interesting, so not even realizing that it's pinned
				# i = i - 1
				i = i + 1
			# await message.delete()

client.run('')
