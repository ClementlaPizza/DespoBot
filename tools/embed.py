# generator embed.py

import datetime
import random

class Generator_Embed(object):
	"""docstring for Generator_Embed"""
	def __init__(self, arg=None):
		super(Generator_Embed, self).__init__()
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
		pass

# GET DICO
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

# SET EMBED
	def setTitle(self, title):
		self.title = title
		pass

	def setDescription(self, description):
		if description == None:
			return
		self.description = description
		pass

	def setColor(self, color):
		self.color = color
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
		pass

	def setFooter(self, text, icon_url=None):
		self.footer = {"text":text,"icon_url":icon_url}
		pass

	def setImage(self, url, height=None, width=None):
		if (height and not width) or (not height and width):
			return False
		self.image = {"url":url, "height":height, "width":width}
		pass

	def setThumbnail(self, url, height=None, width=None):
		if (height and not width) or (not height and width):
			return False
		self.thumbnail = {"url":url, "height":height, "width":width}
		pass

	def setTimestamp(self, timevar):
		if type(timevar) is datetime.datetime:
			timevar = timevar.split(".")
			self.timestamp = str(timevar)
			pass
		elif type(timevar) is int:
			self.timestamp = str(datetime.datetime.fromtimestamp(timevar))
			pass
		pass
		
# Edit
	def editTitle(self, message, title):
		dico_embed = message.copy()
		dico_embed["title"] = title
		return dico_embed

	def editDescription(self, message, description):
		dico_embed = message.copy()
		dico_embed["description"] = description
		return dico_embed

	def editColor(self, message, color):
		dico_embed = message.copy()
		dico_embed["color"] = int(color)
		return dico_embed

	def editAuthor(self, message, author, url=None, icon=None):
		dico_embed = message.copy()
		dico_embed["author"] = {"name":author,"url":self.author_url,"icon_url":self.author_icon}
		return dico_embed

	def editImage(self, message, url, height=None, width=None):
		dico_embed = message.copy()
		dico_embed["image"] = {"url":url, "height":height, "width":width}
		return dico_embed

	def editFooter(self, message, text, icon_url=None):
		dico_embed = message.copy()
		dico_embed["footer"] = {"text":text,"icon_url":icon_url}
		return dico_embed

	def editThumbnail(self, message, url, height=None, width=None):
		dico_embed = message.copy()
		dico_embed["thumbnail"] = {"url":url, "height":height, "width":width}
		return dico_embed

	def editTimestamp(self, message, timevar):
		dico_embed = message.copy()
		if type(timevar) is datetime.datetime:
			timevar = timevar.split(".")
			dico_embed["timestamp"] = str(timevar)
			pass
		elif type(timevar) is int:
			dico_embed["timestamp"] = str(datetime.datetime.fromtimestamp(timevar))
			pass
		return dico_embed

	def editField(self, message, index, name, value, inline=False):
		dico_embed = message.copy()
		index = int(index) - 1
		fields = []
		for key, value in dico_embed.items():
			if key == "fields":
				fields = value
			pass
		fields[index] = {'name': name, 'value': value, 'inline': inline}
		dico_embed["fields"] = fields
		return dico_embed

# Delete
	def remove(self, message, arg, indexfield=None):
		dico_embed = message.copy()
	
	# Classic
		if arg != ("field" or "color"):
			for key in dico_embed.keys():
				if arg == key:
					dico_embed[key] = ""

	# Fields
		if (arg == "field") and (indexfield != None) and (indexfield.isdigit()):
			fields = dico_embed["fields"]
			index = int(indexfield) - 1
			print("fields")
			print(len(fields))
			print(index)

			if (index > 0) and (len(fields) > index):
				print("index > 0 + field > index")
				del fields[index]
				dico_embed["fields"] = fields

			if (index==0) and (len(fields) == 1):
				print("index=0 + field = 1")
				dico_embed["fields"] = []

		return dico_embed