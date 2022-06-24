# The door

import discord
from discord.ext import commands
from tools.generator.embed import EmbedGenerator
from datetime import datetime
import random
from safe import ROLE_PETIT_DESPOTE, CHANNEL_LOG, CHANNEL_NEW_MEMBER

class Door(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
		self.embedcreator = EmbedGenerator()

# Entry
	@commands.Cog.listener()
	async def on_member_join(self, member):
	# title
		self.embedcreator.setTitle("Bienvenue dans la DespotikFamily")
	# description
		self.embedcreator.setDescription(f"{member.mention} \n \n Choisi à quoi tu joues : <#859203775608389634>")
	# color
		self.embedcreator.setColorRandom()
	# footer
		self.embedcreator.setFooter(f"{member.guild.member_count} membres", f"{emojis_list[random.randint(0,len(emojis_list))].url}")
	# time
		self.embedcreator.setTimestamp(int(round(datetime.utcnow().timestamp())))
	# thumbnail
		self.embedcreator.setThumbnail("".join(str(member.avatar_url).split("?")[0]))
	# send
		channel = member.guild.get_channel(CHANNEL_NEW_MEMBER)
		embed = discord.Embed.from_dict(self.embedcreator.getDico())
		await channel.send(embed=embed)
	# add role
		await member.add_roles(ROLE_PETIT_DESPOTE)

# Leave
	@commands.Cog.listener()
	async def on_member_remove(self, member):
	# Title
		self.embedcreator.setTitle("Un membre viens de quitter la DespotikFamily")
	# Color
		self.embedcreator.setColor(0x992d22)
	# Footer
		self.embedcreator.setTimestamp(int(round(datetime.utcnow().timestamp())))
		self.embedcreator.setFooter(f"{member.guild.member_count} membres")
	# Fields Member
		self.embedcreator.setField("Mention:",f"{member.mention}", True)
		self.embedcreator.setField("Nom:",f"{member.display_name}#{member.discriminator}", True)
		self.embedcreator.setField("ID:",f"{member.id}", True)
	# Field Since
		since_time_convert = str(member.joined_at.timestamp()).split(".")[0]
		self.embedcreator.setField("Sur le serveur depuis le :",f"<t:{since_time_convert}:D>", False)
	# Field Role
		roles_member = member.roles[1:]
		roles_guild = member.guild.roles[1:]
		roles_list = f"\n> ".join([str(r.name) for r in roles_member])
		self.embedcreator.setField("Les Roles:",f"**{(len(roles_member))}**/{(len(roles_guild))} dont: \n> {roles_list}", False)
	# Send
		channel = member.guild.get_channel(CHANNEL_LOG)
		embed = discord.Embed.from_dict(self.embedcreator.getDico())
		await channel.send(embed=embed)

def setup(bot):
	bot.add_cog(Door(bot))