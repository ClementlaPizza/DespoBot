# Roles_Choice.py

from tools.json import Generator_Json
from tools.embed import Generator_Embed
import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup, CommandPermission, Option
from safe import GUILD_ID, ROLE_ARCHITECTE

class role_choice(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.json = Generator_Json("data/role_config.json")
		self.embed = Generator_Embed()

	choice_command = SlashCommandGroup(
			"role",
			"Role",
			guild_ids=[GUILD_ID],
			permissions=[CommandPermission("owner", 2, True)]
		)

	@choice_command.command()
	async def add(self, ctx:discord.ApplicationContext,
		channel: Option(str, "#Channel"),
		role: Option(str, "@role"),
		description: Option(str, "Description pour le role"),
		emoji: Option(str, "Emoji pour le role")):
		await ctx.respond(f"{channel}, {role}, {description}, {emoji}")

def setup(bot):
	bot.add_cog(role_choice(bot))