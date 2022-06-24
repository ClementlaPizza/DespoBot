from ressources.secret import *
import discord
from discord.ext import commands, tasks
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType

	#Listes des boutons
BOUTON1 = "rules"
BOUTON2 = "Magic The Gathering"
BOUTON3 = "Clasheur"
BOUTON4 = "Pilotes"
BOUTON5 = "Survival"
BOUTON6 = "Roliste"
BOUTON7 = "Minecraft"
	
	#Listes des roles
PETIT_DESPOTE = 491952140005408770
PLANESWALKER = 692578643616202842
CLASHEUR = 539284221051797524
PILOTES = 556132462007418900
AVENTURIER = 815316705299398696
MINECRAFTEUX = 734469016784994304
ROLISTES = 648358321522343976

class LesBoutons(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def rules_button(self, ctx):
		await ctx.message.delete()
		await ctx.send("Êtes-vous d'accord avec le règlement ?", components=[Button(custom_id=BOUTON1 ,style=ButtonStyle.green, label="J'approuve le règlement", emoji="👍"),])

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def roles_buttons(self, ctx):
		await ctx.message.delete()

		await ctx.send("https://media.giphy.com/media/vOPdEdL3VA9yqce33J/giphy.gif", 
			components=[[
						Button(custom_id=BOUTON2 ,style=ButtonStyle.green, label=BOUTON2, emoji=self.bot.get_emoji(776137484173443083)),
						Button(custom_id=BOUTON3 ,style=ButtonStyle.green, label=BOUTON3, emoji=self.bot.get_emoji(562123809273020416)),
						Button(custom_id=BOUTON4 ,style=ButtonStyle.green, label=BOUTON4, emoji=self.bot.get_emoji(776139240618065930)),],
						[
						Button(custom_id=BOUTON5 ,style=ButtonStyle.green, label=BOUTON5, emoji=self.bot.get_emoji(776138667244650516)),
						Button(custom_id=BOUTON6 ,style=ButtonStyle.green, label=BOUTON6, emoji=self.bot.get_emoji(703926133661630514)),
						Button(custom_id=BOUTON7 ,style=ButtonStyle.green, label=BOUTON7, emoji=self.bot.get_emoji(735113500980150343)),]
			])

	@commands.Cog.listener()
	async def on_button_click(self, res):
		member = res.guild.get_member(res.author.id)
		if res.component.id == BOUTON1:
			role = res.guild.get_role(PETIT_DESPOTE)
			if role in member.roles:
				await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"Tu as déjà approuvé le règlement", ephemeral=True)
			else:
				await member.add_roles(role)
				await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"Bienvenue dans la DespotikFamily", ephemeral=True)

		elif res.component.id == BOUTON2:
			role = res.guild.get_role(PLANESWALKER)
			if role in member.roles:
				await member.remove_roles(role)
				await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"Rôle : {res.component.label} retiré", ephemeral=True)
			else:
				await member.add_roles(role)
				await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"Rôle : {res.component.label} choisi", ephemeral=True)	
		
		elif res.component.id == BOUTON3:
			role = res.guild.get_role(CLASHEUR)
			if role in member.roles:
				await member.remove_roles(role)
				await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"Rôle : {res.component.label} retiré", ephemeral=True)
			else:
				await member.add_roles(role)
				await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"Rôle : {res.component.label} choisi", ephemeral=True)	
		
		elif res.component.id == BOUTON4:
			role = res.guild.get_role(PILOTES)
			if role in member.roles:
				await member.remove_roles(role)
				await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"Rôle : {res.component.label} retiré", ephemeral=True)
			else:
				await member.add_roles(role)
				await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"Rôle : {res.component.label} choisi", ephemeral=True)	
		
		elif res.component.id == BOUTON5:
			role = res.guild.get_role(AVENTURIER)
			if role in member.roles:
				await member.remove_roles(role)
				await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"Rôle : {res.component.label} retiré", ephemeral=True)
			else:
				await member.add_roles(role)
				await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"Rôle : {res.component.label} choisi", ephemeral=True)	
		
		elif res.component.id == BOUTON6:
			role = res.guild.get_role(ROLISTES)
			if role in member.roles:
				await member.remove_roles(role)
				await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"Rôle : {res.component.label} retiré", ephemeral=True)
			else:
				await member.add_roles(role)
				await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"Rôle : {res.component.label} choisi", ephemeral=True)	

		elif res.component.id == BOUTON7:
			role = res.guild.get_role(MINECRAFTEUX)
			if role in member.roles:
				await member.remove_roles(role)
				await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"Rôle : {res.component.label} retiré", ephemeral=True)
			else:
				await member.add_roles(role)
				await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"Rôle : {res.component.label} choisi", ephemeral=True)	
										
		pass
		
def setup(bot):
	bot.add_cog(LesBoutons(bot))