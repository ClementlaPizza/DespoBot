import discord
from discord.ext.commands import RoleConverter, EmojiConverter
from tools.generator.json import JsonGenerator

class RoleChoiceManagement(JsonGenerator):
	"""docstring for RoleChoiceManagement"""
	def __init__(self, file):
		super(RoleChoiceManagement, self).__init__(file)
		self.json = self.load()
		self.roleconvert = RoleConverter()
		self.emojiconvert = EmojiConverter()
		self.update_file = False
		self.role = ""
		self.emoji = ""
		
# Check cmd
	def cmdCheck(self, message):
		if len(message) == 0:
			return True
		return False
	
	def cmdAdd(self, message):
		if ((message[0]).lower() == "add") and (len(message) == 3):
			return False
		return True

# Role for add
	async def addRole(self, ctx, message):
	# convert
		try:
			self.role = await self.roleconvert.convert(ctx, message[1])
		except discord.ext.commands.errors.RoleNotFound:
			pass
	# exist
		if self.getItems(self.role.id, "role_id") == self.role.id:
			return True
		return False

# Emoji for add
	async def addEmoji(self, ctx, message):
	# convert
		try:
			self.emoji = await self.emojiconvert.convert(ctx, message[2])
		except discord.ext.commands.errors.EmojiNotFound:
			pass
	# exist
		for keys in self.json:
			if self.getItems(keys, "emoji_id") == self.emoji.id:
				return True
		return False

# Action
	async def ActionAdd(self, ctx, message):
		if self.cmdCheck(message):
			return False
		if self.cmdAdd(message):
			return False
		if await self.addRole(ctx, message):
			return False
		if await self.addEmoji(ctx,message):
			return False
		return True

# Json
	def addJson(self):
		self.setItems(self.role.id ,"role_name", self.role.name)
		self.setItems(self.role.id, "role_id", self.role.id)
		self.setItems(self.role.id, "role_mention", self.role.mention)
		self.setItems(self.role.id, "emoji_name", self.emoji.name)
		self.setItems(self.role.id, "emoji_id", self.emoji.id)
		self.setItems(self.role.id, "emoji_mention", str(self.emoji))
		self.save()