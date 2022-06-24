# choice_role.py

import discord
from discord.ext import commands
from safe import DESPOTIK_FAMILY, CHANNEL_ROLE_CHOICE
from tools.generator.embed import EmbedGenerator
from tools.management.choice_role import RoleChoiceManagement


class RoleChoice(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.embed = EmbedGenerator()
		self.management = RoleChoiceManagement("data/role_choice.json")
		pass






	@commands.command()
	@commands.has_permissions(administrator=True)
	async def test(self, ctx):
		view = DropdownView()

		await ctx.send("ceci est un test de menu", view=view)










def setup(bot):
	bot.add_cog(RoleChoice(bot))















class Dropdown(discord.ui.Select):
	def __init__(self):

		# Set the options that will be presented inside the dropdown
		options = [
			discord.SelectOption(label="Red", description="Your favourite colour is red", emoji="🟥"),
			discord.SelectOption(label="Green", description="Your favourite colour is green", emoji="🟩"),
			discord.SelectOption(label="Blue", description="Your favourite colour is blue", emoji="🟦"),
		]
		super().__init__(
			placeholder="Choose your favourite colour...",
			min_values=0,
			max_values=3,
			options=options,
		)

	async def callback(self, interaction: discord.Interaction):
		# Use the interaction object to send a response message containing
		# The user's favourite colour or choice. The self object refers to the
		# Select object, and the values attribute gets a list of the user's
		# selected options. We only want the first one.
		await interaction.response.send_message(f"Your favourite colour is {', '.join(self.values)}")


class DropdownView(discord.ui.View):
	def __init__(self):
		super().__init__()

		# Adds the dropdown to our view object.
		self.add_item(Dropdown())