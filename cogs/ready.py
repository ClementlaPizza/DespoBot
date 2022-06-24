import discord
import time
from discord.ext import commands
from discord_components import DiscordComponents
from ressources.version import *
import asyncio

print(time.strftime("%D %H:%M:%S"), "Démarrage du bot en cours")

class Ready(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		DiscordComponents(self.bot)
		print(time.strftime("%D %H:%M:%S"), 'Bot en ligne')
		print(time.strftime("%D %H:%M:%S"), f'{self.bot.user.name} en version', version)

def setup(bot):
	bot.add_cog(Ready(bot))