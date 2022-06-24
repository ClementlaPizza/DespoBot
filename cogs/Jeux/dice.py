import discord
import random
from discord.ext import commands, tasks
from ressources.secret import *
from discord_slash import SlashCommand, cog_ext
from discord_slash.utils.manage_commands import create_option, create_choice

class Dice(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
	@cog_ext.cog_slash(name="Dé", 
	guild_ids=[server],
	description="Juste un dé, ni plus, ni moins",
			 options=[
			   create_option(
				 name="chiffre",
				 description="Choisi un chiffre entre 2 et 100.",
				 option_type=3,
				 required=False,
				  )
			 ])
	async def deslash(self, ctx, chiffre="20"):
		if int(chiffre) < 2 or int(chiffre) > 200:
			chiffre=20
			pass
		color = discord.Colour.random()
		member = ctx.author.name
		embed=discord.Embed(color=color, title="Le Dé 🎲")
		embed.add_field(inline=False, name=f'{member} lance un dé {chiffre}', value=f'{random.randint(1,int(chiffre))}')
		await ctx.send(embed=embed)

	@commands.command()
	async def de(self, ctx, arg="20"):
		if int(arg) < 2 or int(arg) > 200:
			arg=20
			pass
		authorname = ctx.author.name
		color = ctx.author.color
		hasard = random.randint(1,int(arg))
		embed=discord.Embed(color=color, title="Le Dé 🎲")
		embed.add_field(inline=False, name=f'{authorname} lance un dé {arg}', value=hasard)
		if int(arg) == 20:
			if hasard == 20:
				embed.add_field(inline=False, name=f'CRITIQUE', value='GG')			
			elif hasard == 1:
				embed.add_field(inline=False, name=f'FUMBLE', value='Dommage')
		await ctx.send(embed=embed)

def setup(bot):
	Dede = Dice(bot)
	bot.add_cog(Dede)