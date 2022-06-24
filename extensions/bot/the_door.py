# the_door.py

from discord.ext import commands
from tools.embed import Generator_Embed
from data.door import ROLE_PTIT_DESPOTE, CHANNEL_NEW, CHANNEL_LOG

class The_Door(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.embed = Generator_Embed()

# Entry
	@commands.Cog.listener()
	async def on_member_join(self, member):
		self.embed.setTitle("Bienvenue dans la DespotikFamily")
		self.embed.setDescription(f"{member.mention}")
		self.embed.setColorRandom()
		self.embed.setFooter(f"{member.guild.member_count} membres")
		self.embed.setTimestamp(int(round(datetime.utcnow().timestamp())))
		self.embed.setThumbnail("".join(str(member.avatar_url).split("?")[0]))
		channel = member.guild.get_channel(CHANNEL_NEW)
		embed = discord.Embed.from_dict(self.embed.getDico())
		await channel.send(embed=embed)
		await member.add_roles(ROLE_PTIT_DESPOTE)

# Counter for log
		embed=discord.Embed(title=f'Nombre de membres sur le serveurs', description=f"{Members} membres")
		channel = guild.get_channel(CHANNEL_LOG)
		await channel.send(embed=embed)

# Leave
	@commands.Cog.listener()
	async def on_member_remove(self, member):
		self.embed.setTitle("Un membre viens de quitter la DespotikFamily")
		self.embed.setColor(0x992d22)
		self.embed.setTimestamp(int(round(datetime.utcnow().timestamp())))
		self.embed.setFooter(f"{member.guild.member_count} membres")
		self.embed.setField("Mention:",f"{member.mention}", True)
		self.embed.setField("Nom:",f"{member.display_name}#{member.discriminator}", True)
		self.embed.setField("ID:",f"{member.id}", True)
		since_time_convert = str(member.joined_at.timestamp()).split(".")[0]
		self.embed.setField("Sur le serveur depuis le :",f"<t:{since_time_convert}:D>", False)
		roles_member = member.roles[1:]
		roles_guild = member.guild.roles[1:]
		roles_list = f"\n> ".join([str(r.name) for r in roles_member])
		self.embed.setField("Les Roles:",f"**{(len(roles_member))}**/{(len(roles_guild))} dont: \n> {roles_list}", False)
		channel = member.guild.get_channel(CHANNEL_LOG)
		embed = discord.Embed.from_dict(self.embed.getDico())
		await channel.send(embed=embed)

def setup(bot):
	bot.add_cog(The_Door(bot))