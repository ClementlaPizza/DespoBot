import discord
from discord.ext import commands
from ressources.safe import *
from ressources.variables.roles import *

class Choix_de_Role(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

# Role reaction

	#Button
	@commands.command()
	@commands.has_permissions(administrator=True)
	async def role(self, ctx):
		if ctx.message.channel.id == CHANNEL:
			await ctx.message.delete()
			embed=discord.Embed(title="Choisis tes rôles:",
				description=f"{EMBED_MTG}\n{EMBED_SUPERCELL}\n{EMBED_PILOTE}\n{EMBED_AVENTURIER}\n{EMBED_MC}\n{EMBED_JDR}")
			embed.set_image(url="https://media.giphy.com/media/vOPdEdL3VA9yqce33J/giphy.gif")
			embed.set_footer(text="Clic sur les émotes en dessous")
			await ctx.send(embed=embed)
			for emoji in (EMOTE_MAGIC, EMOTE_SUPERCELL, EMOTE_PILOTE, EMOTE_AVENTURIER, EMOTE_MINECRAFT, EMOTE_JDR):
				await ctx.channel.last_message.add_reaction(emoji)

#Clic emote
	@commands.Cog.listener()
	async def on_raw_reaction_add(self, emote):
		if emote.channel_id == CHANNEL:
			if not DESPOBOT_ID == emote.member.id:
			#Variable	
				channel = self.bot.get_guild(SERVER).get_channel(CHANNEL)
				message = channel.get_partial_message(channel.last_message_id)
				member = self.bot.get_guild(SERVER).get_member(emote.member.id)
			
				for i in range(0,len(LIST_ROLES)):
					if str(emote.emoji) == LIST_EMOTES[i]:
						role = self.bot.get_guild(SERVER).get_role(LIST_ROLES[i])
						await message.remove_reaction(LIST_EMOTES[i], emote.member)
						if role not in member.roles:
							await member.add_roles(role)
							await member.send(LIST_TXTA[i])
						else:
							await member.remove_roles(role)
							await member.send(LIST_TXTR[i]) 
					pass

def setup(bot):
	bot.add_cog(Choix_de_Role(bot))