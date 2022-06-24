# embed.py

import discord
from discord.ext import commands
from tools.generator.embed import EmbedGenerator
from safe import PREFIX, ROLE_MODERATOR

class EmbedCreator(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.embedcreator = EmbedGenerator()
		pass

	@commands.command()
	@commands.has_role(ROLE_MODERATOR)
	async def embed(self, ctx):
		message = self.embedcreator.getMessage(ctx.message.content)
		await ctx.message.delete()
		if not message:
			return await ctx.author.send(f"Désolé {ctx.author.mention}\nIl te manque un argument dans ta commande\nExemples:\n```\n{PREFIX}embed Un titre\nUne description (optionnel)```")
		self.embedcreator.setTitle(message)
		self.embedcreator.setDescription(message)
		embed = discord.Embed.from_dict(self.embedcreator.getDico())
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(EmbedCreator(bot))