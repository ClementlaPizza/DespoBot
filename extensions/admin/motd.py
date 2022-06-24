# motd.py

import discord
from discord.ext import commands
from tools.generator.embed import EmbedGenerator
from safe import ROLE_ARCHITECTE
from tools.management.motd import ManagementMotd

class MOTD(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.embedcreator = EmbedGenerator()
		self.management_motd = ManagementMotd("./data/motd.txt")
		pass

	@commands.command()
	@commands.has_any_role(ROLE_ARCHITECTE)
	async def motd(self, ctx):
		awnser = self.management_motd.DoAction(ctx.message.content)
		print(ctx.message.content)
		print(f"reponse : {awnser}")
		
		if awnser:
			self.embedcreator.setTitle("Menu du MOTD")
			self.embedcreator.setDescription(awnser)
			embed = discord.Embed.from_dict(self.embedcreator.getDico())
			await ctx.send(embed=embed)
			pass

def setup(bot):
	bot.add_cog(MOTD(bot))

