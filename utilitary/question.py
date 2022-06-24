import discord
from discord.ext import commands

class Question(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
		pass

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def question(self, ctx, *args):
		question = ' '.join(args)
		await ctx.message.delete()
		emoji_yes = "✅"
		emoji_no = "❌"
		# print(f"arg {question}")
		if question == "":
			await ctx.author.send(f"Tu as oublié d'écrire ta question {ctx.author.mention}\nExemple : \n> !question Billy est t'il sympa ?")
		elif "<@" in question:
			await ctx.author.send(f"Dans ta question, tu as mit une mention. Pour eviter toute erreur, nous ne pouvons pas mettre de mention dans un titre d'embed. \nVoici un exemple de la commande: \n> !question Billy est t'il sympa ?")
		else: 
			embed = discord.Embed(title=question, color=discord.Colour.random())
			embed.set_footer(text=f"Question par {ctx.author.name}", icon_url=ctx.author.avatar_url)
			message = await ctx.channel.send(embed=embed)
			await message.add_reaction(emoji_yes)
			await message.add_reaction(emoji_no)

def setup(bot):
	bot.add_cog(Question(bot))