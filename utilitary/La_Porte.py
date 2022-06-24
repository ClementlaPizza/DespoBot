import discord
from discord.ext import commands
import random
from ressources.safe import *
import datetime
import asyncio


class La_Porte(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

# ENTRÉE
	@commands.Cog.listener()
	async def on_member_join(self, member):

	#INFO SERVER
		guild = self.bot.get_guild(SERVER)
		channel = guild.get_channel(776073773874413639) #Les Nouveaux
		role_petitdespote = guild.get_role(491952140005408770)
		role_bot = guild.get_role(560359722256171024)
	
	#EMOJI RANDOM
		emoji_random = random.randint(1,5)
		if emoji_random == 1:
			emoji = self.bot.get_emoji(562123809273020416) #Gobelin
		elif emoji_random == 2:
			emoji = self.bot.get_emoji(679862415428812815) #Kappa
		elif emoji_random == 3:
			emoji = self.bot.get_emoji(561697556782907412) #Poisson Rouge
		elif emoji_random == 4:
			emoji = self.bot.get_emoji(735113500980150343) #Mouton
		elif emoji_random == 5:
			emoji = self.bot.get_emoji(776139493420957746) #Nain
		
	#CALCULATOR (MEMBERS - BOT)	
		Members = len(guild.members) - len(role_bot.members)

	#EMBED
		embed=discord.Embed(title=f'{member.name} rejoins la {guild.name}', description=f"Bienvenue {member.mention}", color=member.color)
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_footer(text=f"{Members} membres", icon_url=emoji.url)		
		
	#ADD ROLE
		await member.add_roles(role_petitdespote)

	#SEND MESSAGE
		await channel.send(embed=embed)

# SORTIE
	@commands.Cog.listener()
	async def on_member_remove(self, member):
	
	#INFO SERVER
		guild = self.bot.get_guild(SERVER)
		channel = guild.get_channel(734814575064514611) #Logs
		
	#CALCULATOR (MEMBERS - BOT)	
		Members = len(guild.members) - len(guild.get_role(560359722256171024).members) - 1

	#ROLES
		roles = member.roles
		del roles[0]
		roles_list = f"\n> ".join([str(r.name) for r in roles])

	#EMBED
		embed = discord.Embed(
			title=f'Un membres viens de quitter la {member.guild.name}',
			description=f"Mention : {member.mention}\nName : **{member.name}**\nID : **{member.id}**\nSur le serv depuis le : **{str(member.joined_at).split(' ')[0]}**\n**{len(member.roles)-1}** Role(s) : \n> **{roles_list}**",
			color=0xff0000)
		embed.set_footer(text=f"{Members} membres")
		
	#SEND MESSAGE
		await channel.send(embed=embed)

def setup(bot):
	bot.add_cog(La_Porte(bot))