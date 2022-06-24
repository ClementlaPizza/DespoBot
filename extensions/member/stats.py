# stats.py

import discord
from discord.ext import commands
from tools.generator.embed import EmbedGenerator
from tools.management.stats import ManagementStats
import time
from safe import PREFIX
from safe import ROLE_MODERATOR, ROLE_PETIT_DESPOTE, ROLE_DESPOTIKBOT, ROLE_DESPOTIKBOT_STAGIAIRE

class STATS(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.embedcreator = EmbedGenerator()
		self.managementstats = ManagementStats()
		pass

	@commands.command(aliases=["stat","profil","profile"])
	async def stats(self, ctx, stat_var=""):
		# print(stat_var)
# Message
		await ctx.message.delete()
		cmd_var = ""

# Member or Bot
		if self.managementstats.checkMember(stat_var):
			member_or_bot = ctx.guild.get_member(self.managementstats.ConvertMention(stat_var))
			cmd_var = f"@{member_or_bot.name}"
	# check bot or not
			it_s_a_bot = ""
			if self.managementstats.checkBot(member_or_bot):
				it_s_a_bot = "🤖 C'est un bot"
	# message
			self.embedcreator.setDescription(f"**Stats de {member_or_bot.mention}** \n {it_s_a_bot}")
			self.embedcreator.setThumbnail(f"{member_or_bot.avatar_url}")
			self.embedcreator.setColor(member_or_bot.color.value)
	# Discord join
			discord_join_time = str(time.mktime(member_or_bot.created_at.timetuple())).split(".")[0]
			self.embedcreator.setField(f"> Sur Discord depuis le", f"> <t:{discord_join_time}:D> \n > <t:{discord_join_time}:R>", True)
	# Guild join
			guild_join_time = str(time.mktime(member_or_bot.joined_at.timetuple())).split(".")[0]
			self.embedcreator.setField(f"> Sur le serveur depuis le", f"> <t:{guild_join_time}:D> \n > <t:{guild_join_time}:R>", True)
			pass
	
# Roles (manual == @Mention role)
		elif self.managementstats.checkModeratorRole(ctx.author.roles) and self.managementstats.checkRole(stat_var):
			role = ctx.guild.get_role(self.managementstats.ConvertMention(stat_var))
			cmd_var = f"@{role.name}"
			self.embedcreator.setColor(role.color.value)
					# Title
			self.embedcreator.setDescription(f"**Stats du role : {role.mention}**")
	# Create since
			field_name = f"> Existe depuis le"
			create_time = str(time.mktime(role.created_at.timetuple())).split(".")[0]
			field_value = f"> <t:{create_time}:D> \n > <t:{create_time}:R>"
			self.embedcreator.setField(field_name, field_value, True)
		
	# Number all members
			field_name = f"> Nombre de membres"
			field_value_line1 = f"> **{len(role.members)}**/{len(ctx.guild.members)} membres"
			field_value_line2 = f"> {self.managementstats.PercentageCalculator((len(role.members)),(len(ctx.guild.members)))}"
			field_value = f"{field_value_line1}\n{field_value_line2}"
			self.embedcreator.setField(field_name,field_value,True)
	# Number online members
			field_name = "> Membres en ligne"
			field_value_line1 = f"> **{self.managementstats.CountOnlineMember(role.members)}**/{len(role.members)} membres"
			field_value_line2 = f"> {self.managementstats.PercentageCalculator((self.managementstats.CountOnlineMember(role.members)),(len(role.members)))}"
			field_value = f"{field_value_line1}\n{field_value_line2}"
			self.embedcreator.setField(field_name, field_value, True)

# Roles (all)
		elif self.managementstats.checkCmdVarRoles(stat_var):
			cmd_var = stat_var
			roles = ctx.guild.roles
			count_member = len(ctx.guild.members)
		# start value
			field_value_dict = self.managementstats.RoleSort(roles, ctx.guild.members)
			field_value1 = []
			field_value2 = []
			field_value3 = []
			for mention, stats in field_value_dict.items():
				field_value1.append(f"> {mention}")
				field_value2.append(f"> {str(stats[0])} / {count_member}")
				field_value3.append(f"> {stats[1]}")
				pass

		# field roles	
			field_name = f"> Roles"
			field_value = "\n".join(field_value1)
			self.embedcreator.setField(field_name,field_value, True)

		# field numbers	
			field_name = f"> Nombre de membres"
			field_value = "\n".join(field_value2)
			self.embedcreator.setField(field_name,field_value, True)

		# Field percentages
			field_name = f"> Pourcentages"
			field_value = "\n".join(field_value3)
			self.embedcreator.setField(field_name,field_value, True)

# Channel text, news, stage_voice, voice and Category
		elif self.managementstats.checkChannelorCategory(stat_var):
			channel_or_category = ctx.guild.get_channel(self.managementstats.ConvertMention(stat_var))
			# print(channel_or_category.type)
			self.embedcreator.setDescription(f"**Stats du channel {channel_or_category.mention}**")
			since_time_convert = str(channel_or_category.created_at.timestamp()).split(".")[0]
	# Channel text
			if "text" in channel_or_category.type:
				# print("----- text", channel_or_category.name)
				cmd_var = f"#{channel_or_category.name}"
				self.embedcreator.setField("> Crée le ",f"> <t:{since_time_convert}:D>\n> <t:{since_time_convert}:R>", True)
				self.embedcreator.setField("> Type", f"> Channel textuel", True)
				self.embedcreator.setField("> Categorie", f"> {channel_or_category.category.name}", True)
	# Channel news
			elif "news" in channel_or_category.type:
				# print("----- news")
				cmd_var = f"#{channel_or_category.name}"
				self.embedcreator.setField("> Crée le ",f"> <t:{since_time_convert}:D>\n> <t:{since_time_convert}:R>", True)
				self.embedcreator.setField("> Type", f"> Annonce (news)", True)
				self.embedcreator.setField("> Categorie", f"> {channel_or_category.category.name}", True)
	# Channel stage voice	
			elif "stage_voice" in channel_or_category.type:
				# print("----- stage_voice")
				cmd_var = f"<#{channel_or_category.id}>"
				self.embedcreator.setField("> Crée le ",f"> <t:{since_time_convert}:D>\n> <t:{since_time_convert}:R>", True)
				self.embedcreator.setField("> Type", f"> Salon de conférence", True)
				self.embedcreator.setField("> Categorie", f"> {channel_or_category.category.name}", True)
				self.embedcreator.setField("> En vocal", f"> {len(channel_or_category.members)} personne(s)", True)
				if channel_or_category.topic:
					self.embedcreator.setField("> Theme en cours", f"> {channel_or_category.topic}", True)
				else:
					self.embedcreator.setField("> Theme en cours", f"> Aucun", True)
				self.embedcreator.setField("> File d'attente", f"> {len(channel_or_category.requesting_to_speak)} membre(s) demande la parole", True)
	# Channel voice		
			elif "voice" in channel_or_category.type:
				# print("----- voice")
				cmd_var = f"<#{channel_or_category.id}>"
				self.embedcreator.setField("> Crée le ",f"> <t:{since_time_convert}:D>\n> <t:{since_time_convert}:R>", True)
				self.embedcreator.setField("> Type", f"> Salon vocal", True)
				self.embedcreator.setField("> Categorie", f"> {channel_or_category.category.name}", True)
				self.embedcreator.setField("> En vocal", f"> {len(channel_or_category.members)} personne(s)", True)

	# Category
			else:
				# print("----- category")
				cmd_var = f"<#{channel_or_category.id}>"
				self.embedcreator.setDescription(f"**Stats de la catégorie {channel_or_category.mention}**")
				self.embedcreator.setField("> Crée le ",f"> <t:{since_time_convert}:D>\n> <t:{since_time_convert}:R>", True)
				counter_channel_text = f"{len(channel_or_category.text_channels)}"
				counter_cnahhel_voice = f"{len(channel_or_category.voice_channels)}"
				counter_channel_stage_voice = f"{len(channel_or_category.stage_channels)}"
				counter_channel = f"> {counter_channel_text} textuels \n> {counter_cnahhel_voice} vocaux\n> {counter_channel_stage_voice} salon de conference"
				self.embedcreator.setField("> Channels", counter_channel, True)

		# Channel view
			field_list = []
			for r in channel_or_category.changed_roles:
				# print(r.mention)
				field_list.append(f"> {r.mention}")
				pass
			del field_list[0]
			field_list = '\n'.join(field_list)
			self.embedcreator.setField("> Visible par les roles", field_list, True)

# Server
		elif self.managementstats.checkCmdVarServer(stat_var):
			# print(self.managementstats.checkCmdVarServer(stat_var))
			cmd_var = stat_var
			server = ctx.guild
			self.embedcreator.setDescription(f"**Stats du serveur**")
			since_time_convert = str(server.created_at.timestamp()).split(".")[0]
		
	# Server created
			field_name = "> Serveur crée le "
			field_value_line1 = f"> <t:{since_time_convert}:D>"
			field_value_line2 = f"> <t:{since_time_convert}:R>"
			field_value_line3 = f"> par {server.owner.mention}"
			field_value = f"{field_value_line1}\n{field_value_line2}\n{field_value_line3}"
			self.embedcreator.setField(field_name,field_value, True)
	
	# Members
			field_name = "> Info des membres"
			
			role_info = ctx.guild.get_role(ROLE_PETIT_DESPOTE)
			role_bot_info = ctx.guild.get_role(ROLE_DESPOTIKBOT)
			role_bot2_info = ctx.guild.get_role(ROLE_DESPOTIKBOT_STAGIAIRE)
			
			field_value = []

			field_value.append(f"> **{ctx.guild.member_count}** membres dont:")
			field_value.append(f"> • **{self.managementstats.CountOnlineMember(ctx.guild.members)}** en ligne ({self.managementstats.PercentageCalculator((self.managementstats.CountOnlineMember(ctx.guild.members)),(ctx.guild.member_count))})")
			field_value.append(f"> • **{len(role_info.members)}** {role_info.mention} ({self.managementstats.PercentageCalculator((len(role_info.members)),(ctx.guild.member_count))})")
			calcul_bot = len(role_bot_info.members) + len(role_bot2_info.members)
			field_value.append(f"> • **{calcul_bot}** bots ({self.managementstats.PercentageCalculator(calcul_bot,(ctx.guild.member_count))})")

			field_value = "\n".join(field_value)

			self.embedcreator.setField(field_name,field_value, True)

	# Roles
			roles = ctx.guild.roles

			field_name = "> Roles"

		# start value
			field_value = []

			field_value.append(f"> **{len(roles)-1}** roles")
			field_value.append(f"> Top **3** roles")
			
		# top 1
			top_mention = list(self.managementstats.Top3Role(roles).keys())[0]
			top_count_members = list(self.managementstats.Top3Role(roles).values())[0]
			percentage = self.managementstats.PercentageCalculator(top_count_members,len(ctx.guild.members)) 
			field_value.append(f"> • {top_mention} *{top_count_members} membres ({percentage})*")
			
		# top 2
			top_mention = list(self.managementstats.Top3Role(roles).keys())[1]
			top_count_members = list(self.managementstats.Top3Role(roles).values())[1]
			percentage = self.managementstats.PercentageCalculator(top_count_members,len(ctx.guild.members)) 
			field_value.append(f"> • {top_mention} *{top_count_members} membres ({percentage})*")
			
		# top 3
			top_mention = list(self.managementstats.Top3Role(roles).keys())[2]
			top_count_members = list(self.managementstats.Top3Role(roles).values())[2]
			percentage = self.managementstats.PercentageCalculator(top_count_members,len(ctx.guild.members)) 
			field_value.append(f"> • {top_mention} *{top_count_members} membres ({percentage})*")

		# end value
			field_value = "\n".join(field_value)
			
			self.embedcreator.setField(field_name,field_value, False)

	# Channel and category
			field_name = "> Channels et categories"		
		# start value
			field_value = []	
		# Category
			field_value.append(f"> **{len(ctx.guild.categories)}** catégories")
		# Channels text
			field_value.append(f"> **{len(ctx.guild.text_channels)}** salons textuel")
		# Channels voice
			field_value.append(f"> **{len(ctx.guild.voice_channels)}** salons vocaux")
		# Channels stage voice
			field_value.append(f"> **{len(ctx.guild.stage_channels)}** salons de conference")
		# end value
			field_value = "\n".join(field_value)
			self.embedcreator.setField(field_name,field_value, True)

	# Emojis and sticker
			field_name = "> Emojis"	
		# start value
			field_value = []
		# Title
			field_value.append(f"> **{len(ctx.guild.emojis)}** emojis dont:")	
		# No Animated
			if self.managementstats.checkEmoji(ctx.guild.emojis):
				field_value.append(f"> • **{self.managementstats.CountEmoji(ctx.guild.emojis)}** emojis non animé *({self.managementstats.PercentageCalculator(self.managementstats.CountEmoji(ctx.guild.emojis) , len(ctx.guild.emojis))})*")
		# Animated
			if self.managementstats.checkEmojiAnimated(ctx.guild.emojis):
				field_value.append(f"> • **{self.managementstats.CountEmojiAnimated(ctx.guild.emojis)}** emojis animé *({self.managementstats.PercentageCalculator(self.managementstats.CountEmojiAnimated(ctx.guild.emojis) , len(ctx.guild.emojis))})*")


		# end value
			field_value = "\n".join(field_value)
			self.embedcreator.setField(field_name,field_value, True)

# Command error or not arg == return author stats	
		else: 
			member_or_bot = ctx.author
	# check bot or not
			it_s_a_bot = ""
			if self.managementstats.checkBot(member_or_bot):
				it_s_a_bot = f"🤖 C'est un bot"
	# message
			self.embedcreator.setDescription(f"**Stats de {member_or_bot.mention}** \n {it_s_a_bot}")
			self.embedcreator.setThumbnail(f"{member_or_bot.avatar_url}")
			self.embedcreator.setColor(member_or_bot.color.value)
	# Discord join
			discord_join_time = str(time.mktime(member_or_bot.created_at.timetuple())).split(".")[0]
			self.embedcreator.setField(f"> Sur Discord depuis le", f"> <t:{discord_join_time}:D> \n > <t:{discord_join_time}:R>", True)
	# Guild join
			guild_join_time = str(time.mktime(member_or_bot.joined_at.timetuple())).split(".")[0]
			self.embedcreator.setField(f"> Sur le serveur depuis le", f"> <t:{guild_join_time}:D> \n > <t:{guild_join_time}:R>", True)
		pass

# Embed Send
		self.embedcreator.setTitle("📊\tLes Stats")
		despobot = self.bot.user
		cmd = ctx.message.content.split(" ")[0]
		cmd_message = f"{cmd} {cmd_var}"
		self.embedcreator.setFooter(f"Commande lancé par {ctx.author.name}\n{cmd_message}", f"{ctx.author.avatar_url}")
		self.embedcreator.setTimestamp(int(round(ctx.message.created_at.timestamp())))
		embed = discord.Embed.from_dict(self.embedcreator.getDico())
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(STATS(bot))

