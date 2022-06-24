#!"E:\Program Files\Python310\venv\despobot\Scripts\python.exe"

import discord
from discord.ext import commands
import os
from safe import TOKEN_DISCORD, PREFIX, ROLE_ARCHITECTE

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())

@bot.command()
async def load(ctx, extension):
	bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
	bot.unload_extension(f'cogs.{extension}')

for folder in os.listdir('./extensions'):
	for filename in os.listdir(f'./extensions/{folder}'):
		if filename.endswith('.py'):
			bot.load_extension(f'extensions.{folder}.{filename[:-3]}')

bot.run(TOKEN_DISCORD)