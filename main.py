import os
from keep_alive import keep_alive
from discord.ext import commands

bot = commands.Bot(
	command_prefix="!", 
	case_insensitive=True 
)

bot.author_id = 756816729992331304 

@bot.event 
async def on_ready():
    print("logged in to " + str(bot.user))

extensions = [
	'cogs.debug'
]

if __name__ == '__main__': 
	for extension in extensions:
		bot.load_extension(extension) 

keep_alive()  
bot.run(os.environ['DISCORD_BOT_SECRET']) 