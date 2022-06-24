import discord
import random
from discord.ext import commands, tasks
from ressources.safe import *

# Start
class Dice(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

#Commande
	@commands.command()
	async def de(self, ctx, arg="20"):
		if int(arg) < 2 or int(arg) > 200:
			arg=20
			pass
		hasard = random.randint(1,int(arg)) 

#PILE OU FACE
		if int(arg) == 2:
			embed_title = f'{ctx.author.name} lance une pièce'
			if hasard == 1: #FACE
				embed_description = f"TU AS FAIT FACE !!!"
			elif hasard == 2: #PILE
				embed_description = f"TU AS FAIT PILE !!!"

#DICE
		if int(arg) > 2:
			embed_title = f'{ctx.author.name} lance un dé {arg}'
			embed_description = f"TU AS FAIT {hasard}"
			if int(arg) == 20:
				if hasard == 1: #FUMBLE
					embed_description = f"TU AS FAIT UN FUMBLE !!!"
				elif hasard == 20: #CRITIQUE
					embed_description = f"TU AS FAIT UN CRITIQUE !!!"


#EMBED AND SEND
		embed=discord.Embed(title=embed_title, description=embed_description, color=ctx.author.color)
		embed_image = f"{arg}/{hasard}"
		embed.set_thumbnail(url=f"https://clementlapizza.com/Discord%20Bot/DespoBot/ressources/Dice/{embed_image}.png")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Dice(bot))