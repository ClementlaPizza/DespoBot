#clear commands

import discord
from discord.ext import commands
import asyncio

class Clear(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=['purge'])
	@commands.has_permissions(manage_messages=True)
	async def clear(self, ctx, arg = None):
		author = ctx.author.mention
		channel = ctx.channel.mention
		log = self.bot.get_channel(734814575064514611)
		await ctx.message.delete()
		if arg == None:
			await ctx.author.send('Tu doit mettre un chiffre en 1 et 50 pour supprimé plusieurs messages')
		if int(arg) < 1 or int(arg) > 50:
			await ctx.author.send('Tu doit choisir un chiffre en 1 et 50 pour supprimé plusieurs messages')
		else:
			await ctx.channel.purge(limit=int(arg))
			await ctx.send(f'{author} viens de supprimé {arg} message(s)', delete_after=10)
			await asyncio.sleep(10)
			await log.send(f'{author} viens de supprimé {arg} message(s) dans le channel {channel}')

def setup(bot):
	bot.add_cog(Clear(bot))