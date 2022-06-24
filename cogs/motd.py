import discord
from discord.ext import commands, tasks
import asyncio
from ressources.secret import *

time = 240 #Timer du Motd

class Motd(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	async def status_task(self):
		while True:
			await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=f"Le choix de Roles est présent"))
			await asyncio.sleep(time)
			guild = self.bot.get_guild(server)
			despotikbot = guild.get_role(560359722256171024)
			botcounter = len(despotikbot.members)
			await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{guild.member_count - botcounter} membres sur le serveur"))
			await asyncio.sleep(time)
			await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=f"Bras de fer contre BobdelaProd"))
			await asyncio.sleep(time)
			await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"Mono bleu 😉"))
			await asyncio.sleep(time)
	
	@commands.Cog.listener()
	async def on_ready(self):
		self.bot.loop.create_task(self.status_task())

def setup(bot):
	motd = Motd(bot)
	bot.add_cog(motd)