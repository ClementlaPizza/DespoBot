# ready.py

from discord.ext import commands
from safe import BOT_VERSION, BOT_VERSION_NAME
import datetime
import os

class Ready(commands.Cog):
	print((datetime.datetime.today()).strftime("%d/%m/%y - %H:%M:%S"), "Bot in load")
	print()
	def __init__(self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_ready(self):
		print((datetime.datetime.today()).strftime("%d/%m/%y - %H:%M:%S"), "Bot online")
		print((datetime.datetime.today()).strftime("%d/%m/%y - %H:%M:%S"), f"Version {BOT_VERSION} : {BOT_VERSION_NAME}")
		print()

def setup(bot):
	bot.add_cog(Ready(bot))