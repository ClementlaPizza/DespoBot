import discord
from discord.ext import commands
from ressources.safe import *

class Embed(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
		pass

	@commands.command()
	@commands.has_role(ROLE_MODERATEUR)
	async def embed(self, ctx, arg=None):
		message = ctx.message.content.splitlines()
		#print(message)
		await ctx.message.delete()
		title = message[0].split()
		title = " ".join(title[1:])
		#print(title)
		description = message[1:]
		description = "\n".join(description)
		#print(description)
		embed=discord.Embed(title=title, description=description, color=0x8c00ff)
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Embed(bot))