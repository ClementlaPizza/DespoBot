#Ready.py

import discord
from discord.ext import commands
from info.version import *
from ressources.safe import *
import asyncio
	
print("Starting the bot")

class Ready(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print('Bot online')
		print(f'{self.bot.user.name} in version', VERSION,f" : ",VERSIONNAME)
        
def setup(bot):
	bot.add_cog(Ready(bot))