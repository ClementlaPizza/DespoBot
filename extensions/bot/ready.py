# ready.py

import discord
from discord.ext import commands, tasks
from safe import VERSION_BOT
from tools.management.motd import ManagementMotd
from tools.generator.file import *

print("Starting the bot")

class Ready(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
		self.management_motd = ManagementMotd("./data/motd.txt")
		self.file_generator = FileGenerator("README.md")
		pass

	@commands.Cog.listener()
	async def on_ready(self):
# start bot
		print('Bot online')
		print("Bot in version " + VERSION_BOT)
		print("\n\n\n")
		self.change_motd.start()
		pass
	
# Update : README.md (VERSION)
		content = f'<img alt="Last version" src="https://img.shields.io/static/v1?style=for-the-badge&logo=github&label=Version&color=blue&message={VERSION_BOT}">'
		self.file_generator.EditLine(7, content)
		pass

# Motd
	@tasks.loop(seconds=3600.0)
	async def change_motd(self):
		awnser = self.management_motd.DoAction()
		await self.bot.change_presence(activity = discord.Game(awnser))
		pass


def setup(bot):
	bot.add_cog(Ready(bot))