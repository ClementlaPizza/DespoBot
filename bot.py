#!E:\Program Files\Python310\venv\despobot\Scripts\python.exe

# bot.py

import discord
from discord.ext import commands
import os
from safe import BOT_TOKEN, BOT_PREFIX

bot = commands.Bot(command_prefix=BOT_PREFIX, intents=discord.Intents.all())
bot.remove_command("help")

@bot.command()
async def load(ctx, extension):
	bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
	bot.unload_extension(f'cogs.{extension}')

for folder in os.listdir("extensions"):
	if "README.md" != folder:
		for file in os.listdir(f"extensions/{folder}"):
			if file.endswith('.py'):
				if folder == "Bot":
					bot.load_extension(f'extensions.{folder}.{file[:-3]}')
				if folder == "Members":
					bot.load_extension(f'extensions.{folder}.{file[:-3]}')


bot.run(BOT_TOKEN)