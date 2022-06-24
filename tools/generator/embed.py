import datetime

import random

# embed_generator.py

class EmbedGenerator(object):
	"""docstring for EmbedGenerator"""
	def __init__(self, arg=None):
		super(EmbedGenerator, self).__init__()
		self.arg = arg
		self.initVar()
# INIT
	def initVar(self):
		self.title = ""
		self.description = ""
		self.color = 1007636
		self.author = "" 
		self.author_url = "https://github.com/ClementlaPizza/"
		self.author_icon = ""
		self.field = []
		self.footer = ""
		self.image = ""
		self.thumbnail = ""
		self.timestamp = ""
		self.message_id = ""
		self.cmd_embed = False
		pass

# GET
	def getDico(self, message = None):
		dico_embed = {}
		dico_embed["title"] = self.title
		dico_embed["description"] = self.description
		dico_embed["color"] = self.color
		dico_embed["author"] = self.author
		dico_embed["fields"] = self.field
		dico_embed["footer"] = self.footer
		dico_embed["image"] = self.image
		dico_embed["thumbnail"] = self.thumbnail
		dico_embed["timestamp"] = self.timestamp
		self.initVar()
		return dico_embed


	def getMessage(self, message):
		if "embed" in message.split()[0]:
			self.cmd_embed = True
			pass
		if " " in message: # Full message
			return message.split(" ",1)[1]
		elif "\n" in message: # Description
			return " \n" + message.split("\n",1)[1]
		return False

# SET
	def setTitle(self, title):
		if "\n" in title:
			title = title.split("\n")[0]
		self.title = title
		pass

	def setDescription(self, description):
		if self.cmd_embed and "\n" in description:
			description = description.split("\n",1)[1]
			self.description = description
		else:
			self.description = description
		pass

	def setColor(self, color):
		self.color = color
		# print(self.color)
		pass

	def setColorRandom(self):
		random_color = lambda: random.randint(0,255)
		color = '%02X%02X%02X' % (random_color(),random_color(),random_color())
		self.color = int(color, 16)
		pass

	def setAuthor(self, author, url=None, icon=None, **kwargs):
		if url:
			self.author_url = url
			pass
		if icon:
			self.author_icon = icon
			pass
		url = kwargs.get("url",None)
		if url:
			self.author_url = url
			pass
		icon = kwargs.get("icon",None)
		if icon:
			self.author_icon = icon
			pass
		self.author = {"name":author,"url":self.author_url,"icon_url":self.author_icon}
		pass

	def setField(self, name, value, inline=False):
		self.field.append({"name":name, "value":value, "inline":inline})
		# print(self.field)
		pass

	def setFooter(self, text, icon_url=None):
		self.footer = {"text":text,"icon_url":icon_url}
		pass

	def setImage(self, url, height=None, width=None):
		# print(f"{height}=hauteur, {width}=largeur")
		if (height and not width) or (not height and width):
			return False
		self.image = {"url":url, "height":height, "width":width}
		pass

	def setThumbnail(self, url, height=None, width=None):
		# print(f"{height}=hauteur, {width}=largeur")
		if (height and not width) or (not height and width):
			return False
		self.thumbnail = {"url":url, "height":height, "width":width}
		pass

	def setTimestamp(self, timevar):
		# timevar = 1640114573
		# print(f"timevar = {timevar} = {type(timevar)}")
		if type(timevar) is datetime.datetime:
			# print("timevar 1")
			timevar = timevar.split(".")
			# print(timevar)
			# print(f"datetime.datetime")
			self.timestamp = str(timevar)
			pass
		elif type(timevar) is int:
			# print("timevar 2")
			# print(f"int")
			self.timestamp = str(datetime.datetime.fromtimestamp(timevar))
			# print(self.timestamp)
			pass
		pass