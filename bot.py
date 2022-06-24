#!"E:\Program Files\Python310\venv\despobot\Scripts\python.exe"

from ressources.safe import *
import discord
import os
from discord.ext import commands
from info.version import *

#Le bot
bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())
bot.remove_command("help")

@bot.command()
async def load(ctx, extension):
	bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
	bot.unload_extension(f'cogs.{extension}')

if PREFIX == "!": # Mode normal
	for filename in os.listdir('./utilitary'):
		if filename.endswith('.py'):
			bot.load_extension(f'utilitary.{filename[:-3]}')

	for filename in os.listdir('./games'):
		if filename.endswith('.py'):
			bot.load_extension(f'games.{filename[:-3]}')

else: # Mode test / Labo
	for filename in os.listdir('./labo'):
		if filename.endswith('.py'):
			bot.load_extension(f'labo.{filename[:-3]}')

#RUN
bot.run(TOKEN)