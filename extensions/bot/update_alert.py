# update_alert.py

from discord.ext import commands, tasks
from safe import BOT_VERSION, BOT_VERSION_NAME, OWNER_ID
import os
import requests
import datetime

class Update_Alert(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.compare = version_comparison(BOT_VERSION)
		self.counter = 0
		self.counter2 = 0
	
	@commands.Cog.listener()
	async def on_ready(self):
		self.check.start()

	@tasks.loop(hours=10.0)
	async def check(self):
		if self.compare.Compare():
			self.counter += 1
			tag = self.compare.GithubRequest["tag_name"]
			url = self.compare.GithubRequest["url"]
			if self.counter != 5:
				print((datetime.datetime.today()).strftime("%d/%m/%y - %H:%M:%S"), f"Alert {self.counter}/5 : New version available")
				print((datetime.datetime.today()).strftime("%d/%m/%y - %H:%M:%S"), "---------BOT-----------")
				print((datetime.datetime.today()).strftime("%d/%m/%y - %H:%M:%S"), f"> Bot = v{BOT_VERSION}")
				print((datetime.datetime.today()).strftime("%d/%m/%y - %H:%M:%S"), "--------Github---------")
				print((datetime.datetime.today()).strftime("%d/%m/%y - %H:%M:%S"), f"> {tag}")
				print((datetime.datetime.today()).strftime("%d/%m/%y - %H:%M:%S"), f"> {url}")
				print()
			else:
				print((datetime.datetime.today()).strftime("%d/%m/%y - %H:%M:%S"), f"Alert {self.counter}/5 : New version available")
				print((datetime.datetime.today()).strftime("%d/%m/%y - %H:%M:%S"), f"Message sent to admin")
				print()
				owner = await self.bot.fetch_user(OWNER_ID)
				await owner.send(f"New version available\nBot\n> {BOT_VERSION}\nGithub\n> {tag}\n> {url}")
				self.check2.start()
				self.check.stop()
		pass

	@tasks.loop(hours=120.0)
	async def check2(self):
		if self.counter2 == 0:
			self.counter2 += 1
			self.counter == 0
		else:
			self.check.start()
			self.check2.stop()

def setup(bot):
	bot.add_cog(Update_Alert(bot))
	
class version_comparison(object):
	"""docstring for version_comparison"""
	def __init__(self, bot_version):
		super(version_comparison, self).__init__()
		self.listversion = {"X":{"Github":0, "Bot":0}, "Y":{"Github":0, "Bot":0}, "Z":{"Github":0, "Bot":0}}
		self.GithubRequest = (requests.get('https://api.github.com/repos/ClementlaPizza/DespoBot/releases/latest')).json()
		self.GithubTag()
		self.BotVersion(bot_version)

	def BotVersion(self, numbers):
		counter = 0
		bot_version = numbers.split(".")
		for xyz in self.listversion:
			self.listversion[xyz]["Bot"] = bot_version[counter]
			counter += 1
		return self.listversion

	def GithubTag(self):
		counter = 0
		tag = (self.GithubRequest["tag_name"]).replace("v","").split(".")
		self.ShareGithub = self.GithubRequest["tag_name"]
		for xyz in self.listversion:
			self.listversion[xyz]["Github"] = tag[counter]
			counter += 1
		return self.listversion

	def Compare(self):
		xyz = self.listversion
		x = xyz["X"]
		y = xyz["Y"]
		z = xyz["Z"]
		if (x["Github"] > x["Bot"]):
			# print("Check X")
			return True
		elif (x["Github"] == x["Bot"]) and (y["Github"] > y["Bot"]):
			# print("Check Y")
			return True
		elif (x["Github"] == x["Bot"]) and (y["Github"] == y["Bot"]) and (z["Github"] > z["Bot"]):
			# print("Check Z")
			return True
		return False
		