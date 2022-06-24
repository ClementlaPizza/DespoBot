# Bot.py

from ressources.secret import *
import discord
import os
from discord.ext import commands
from discord_slash import SlashCommand

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True, sync_on_cog_reload = True)

@bot.command()
async def load(ctx, extension):
	bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
	bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.{filename[:-3]}')

for filename in os.listdir('./cogs/Jeux'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.Jeux.{filename[:-3]}')

for filename in os.listdir('./cogs/Moderations'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.Moderations.{filename[:-3]}')

#RUN
bot.run(token)