import discord
import random
from discord.ext import commands
from ressources.safe import *
from info.version import *
import asyncio
from ressources.variables.idtagmtga import *
from ressources.classs.gestionmagicidtag import *

class IdTagMagic(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
		self.gestionmagicidtag = GestionMagicIDTag("./ressources/json/idmagic.json")
		pass

# Verification channel
	#Channel
	def check_channel(ctx):
		return ctx.channel.id == CHANNEL_IDTAG
	#Embed
	def getEmbedMessage(self, msg):
		if not msg.embeds:
			return False
		return True
	# Check si idtag est mentionner
	def getcmdmentionidtag(self, args):
		if not args:
			return False
		return True

# Ecoute
	@commands.Cog.listener()
	async def on_message(self, message):
		ctx = await self.bot.get_context(message)
		if not message.author.id == DESPOBOT_ID and message.channel.id == CHANNEL_IDTAG and not ctx.command == self.commandaddidtag and not ctx.command == self.commanddelidtag:
			#print(ctx.command)
			#print(self.commandaddidtag)
		#Variables
			idtagmagic = message.content
			mentiondiscord = message.author.id
			isExistNameDiscord = self.gestionmagicidtag.isExistNameDiscord(mentiondiscord)
			isExistIdTag = self.gestionmagicidtag.isExistIdTag(idtagmagic)
			ifcharactersallowed = self.gestionmagicidtag.charIsGood(idtagmagic)
			checkIdTag = self.gestionmagicidtag.checkIdTag(idtagmagic)
			channel = message.channel
		#Supprimé
			await message.delete()
			##print(f"Message supprimé dans on_message")
		#Verification
			if not isExistNameDiscord and not isExistIdTag and ifcharactersallowed and checkIdTag:
				#print(f"------- ECOUTE OK ------- les conditions isExistNameDiscord = {isExistNameDiscord} / isExistIdTag = {isExistIdTag} / ifcharactersallowed = {ifcharactersallowed} / checkIdTag = {checkIdTag}")
				#print(mentiondiscord)
				self.gestionmagicidtag.ajouter(idtagmagic, int(mentiondiscord))
				self.gestionmagicidtag.order()
				self.gestionmagicidtag.save()
				dico = self.gestionmagicidtag.getDicoEmbed()
				embed = discord.Embed.from_dict(dico)
				async for message in message.channel.history(limit=1):
					last_message = message
					pass
				message_with_embed = self.getEmbedMessage(last_message)
		#embed non existant
				if not message_with_embed:		
					await channel.send(embed=embed)
					pass
		#embed deja existant		
				else:
					await last_message.edit(embed=embed)
					pass
			else:
				if not ctx.command == self.commandaddidtag and not ctx.command == self.commanddelidtag:
					#print(f"------- ECOUTE NOT OK ------- pas une bonne commande")
					return
				else: 
					#print(f"------- ECOUTE NOT OK ------- les conditions isExistNameDiscord = {isExistNameDiscord} / isExistIdTag = {isExistIdTag} / ifcharactersallowed = {ifcharactersallowed} / checkIdTag = {checkIdTag}")
					return
		pass	

# Membre non existant
	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if ctx.channel.id == CHANNEL_IDTAG:
			if isinstance(error, commands.MemberNotFound):
				await ctx.message.delete()
				return
			raise error
		pass

# Commande add
	@commands.command(aliases=["add"])
	@commands.check(check_channel)
	@commands.has_role(ROLE_MODERATEUR)
	async def commandaddidtag(self, ctx, mentiondiscord: discord.Member = None, *idtagmagic):
		#print(f"Verification de l argument mentiondiscord dans la commande = {mentiondiscord}")
		#print(f"Verification de l argument idtagmagic dans la commande = {idtagmagic}")
		idtagmagic = " ".join(map(str, idtagmagic))
		#print(f"Verification de l argument idtagmagic apres join = {idtagmagic}")
		idtagmagicmentionner = self.getcmdmentionidtag(idtagmagic)
		#print(mentiondiscord)
		#print(ctx.author.mention)
		if mentiondiscord and idtagmagicmentionner:
		#Variables
			mentiondiscord = mentiondiscord.id
			isExistNameDiscord = self.gestionmagicidtag.isExistNameDiscord(mentiondiscord)
			isExistIdTag = self.gestionmagicidtag.isExistIdTag(idtagmagic)
			ifcharactersallowed = self.gestionmagicidtag.charIsGood(idtagmagic)
			checkIdTag = self.gestionmagicidtag.checkIdTag(idtagmagic)
		
		#Supprimé
			await ctx.message.delete()
			#print(f"Commande {self.commandaddidtag} par {ctx.author.display_name} valide et supprimé")
		#Verification
			if not isExistNameDiscord and not isExistIdTag and ifcharactersallowed and checkIdTag:
				#print(f"------- COMMANDE OK ------- les conditions isExistNameDiscord = {isExistNameDiscord} / isExistIdTag = {isExistIdTag} / ifcharactersallowed = {ifcharactersallowed} / checkIdTag = {checkIdTag}")
				#print(mentiondiscord)
				self.gestionmagicidtag.ajouter(idtagmagic, int(mentiondiscord))
				self.gestionmagicidtag.order()
				self.gestionmagicidtag.save()
				dico = self.gestionmagicidtag.getDicoEmbed()
				embed = discord.Embed.from_dict(dico)
				async for message in ctx.channel.history(limit=1):
					last_message = message
					pass
				message_with_embed = self.getEmbedMessage(last_message)
		#embed non existant
				if not message_with_embed:		
					await ctx.send(embed=embed)
					pass
		#embed deja existant		
				else:
					await last_message.edit(embed=embed)
					pass
			else:
				#print(f"------- COMMANDE NOT OK ------- les conditions isExistNameDiscord = {isExistNameDiscord} / isExistIdTag = {isExistIdTag} / ifcharactersallowed = {ifcharactersallowed} / checkIdTag = {checkIdTag}")
				return

		else:
			await ctx.message.delete()
			#print(f"Commande {self.commandaddidtag} par {ctx.author.display_name} supprimé")
			pass

# Commande del
	@commands.command(aliases=["del"])
	@commands.check(check_channel)
	@commands.has_role(ROLE_MODERATEUR)
	async def commanddelidtag(self, ctx, *args):
		message = " ".join(map(str, args))
		isExistIdTag = self.gestionmagicidtag.isExistIdTag(message)
		mention = ctx.message.mentions
		delete = await ctx.message.delete()
		if mention:
			iddiscord = mention[0].id
			isExistNameDiscord = self.gestionmagicidtag.isExistNameDiscord(iddiscord)
			if isExistNameDiscord:
				#print(f"Mention identique = {iddiscord}")
				self.gestionmagicidtag.delbynamediscord(iddiscord)
				self.gestionmagicidtag.save()
				dico = self.gestionmagicidtag.getDicoEmbed()
				embed = discord.Embed.from_dict(dico)
				async for message in ctx.channel.history(limit=1):
					last_message = message
					pass
				message_with_embed = self.getEmbedMessage(last_message)
				#embed non existant
				if not message_with_embed:		
					await ctx.send(embed=embed)
					pass
				#embed deja existant
				else:
					await last_message.edit(embed=embed)
					pass
			else:
				#print(f"Pas de mention identique = {iddiscord}")
				pass
		elif isExistIdTag and not mention:
			self.gestionmagicidtag.delbyidtag(message)
			self.gestionmagicidtag.save()
			dico = self.gestionmagicidtag.getDicoEmbed()
			embed = discord.Embed.from_dict(dico)
			async for message in ctx.channel.history(limit=1):
				last_message = message
				pass
			message_with_embed = self.getEmbedMessage(last_message)
			#embed non existant
			if not message_with_embed:		
				await ctx.send(embed=embed)
				pass
			#embed deja existant
			else:
				await last_message.edit(embed=embed)
				pass
			##print(f"IDTAG exist = {message}")
			pass
		else:
			##print(f"Mention et idtag non trouver")
			pass
# Ecoute

# Bot
def setup(bot):
	bot.add_cog(IdTagMagic(bot))