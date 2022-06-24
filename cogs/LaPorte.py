import discord
from discord.ext import commands, tasks
from ressources.secret import *

class LaPorte(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	#NEW MEMBER
	@commands.Cog.listener()
	async def on_member_join(self, member):
	    guild = self.bot.get_guild(server) #Le serveur actuel du bot
	    channel = guild.get_channel(776073773874413639) #Channel Nouveau
	    embed=discord.Embed(color=discord.Colour.random())
	    embed.set_author(name="Un nouveau membre viens de rejoindre le serveur", icon_url=member.avatar_url)
	    embed.add_field(name=f"Bienvenue sur le serveur de la {guild.name}", value=member.mention, inline=False)
	    embed.set_footer(text=f"{guild.member_count} membres")
	    await channel.send(embed=embed)

	#LEAVE MEMBRE
	@commands.Cog.listener()
	async def on_member_remove(self, member):
	    guild = self.bot.get_guild(server)
	    channel = guild.get_channel(734814575064514611) #Channel log
	    embed=discord.Embed(color=0xff0000)
	    embed.set_author(name="Un membre à quitter le serveur", icon_url=member.avatar_url)
	    embed.add_field(name=member.name, value=member.mention, inline=False)
	    embed.set_footer(text=f"{guild.member_count} membres")
	    await channel.send(embed=embed)

def setup(bot):
	porte = LaPorte(bot)
	bot.add_cog(porte)