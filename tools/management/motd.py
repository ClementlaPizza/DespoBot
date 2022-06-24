from tools.generator.file import *
from safe import PREFIX

class ManagementMotd(FileGenerator):
	"""docstring for ManagementMotd"""
	def __init__(self, file):
		super(ManagementMotd, self).__init__(file)
		self.list_motd = self.GetContentList()
		self.len_list = len(self.list_motd)
		self.index = 0
		self.update_file = False

	def AddMotd(self, message):
		message = self.ClearMessage(message)
		self.list_motd.append(message)
		self.len_list += 1
		self.update_file = True
		pass

	def DelMotd(self, message):
		number = message.split()[2]
		if self.len_list < int(number) or not number.isnumeric():
			return
		index = int(number) - 1
		del self.list_motd[index]
		self.len_list -= 1
		self.update_file = True
		pass

	def GetMotd(self):
		self.list_motd = self.UpdateContentList()
		self.len_list = len(self.list_motd)
		value = self.list_motd[self.index]
		self.index += 1
		if self.index >= self.len_list:
			self.index = 0
			pass
		return value

	def GetMotds(self):
		value = []
		number = 1
		for motd in self.list_motd:
			value.append(f"{number} - {motd}")
			number += 1
			pass
		self.SaveFile()
		return "\n".join(value)

	def ClearMessage(self, message):
		message = message.replace(f"{PREFIX}motd add ","")
		message = message.splitlines()[0]
		return message

	def DoAction(self, message=""):
		if len(message.split()) > 2 and message.split()[1] == "add":
			self.AddMotd(message)
			return self.GetMotds()
		elif len(message.split()) > 2 and message.split()[1] == "del":
			self.DelMotd(message)
			return self.GetMotds()
		elif len(message.split()) == 1:
			return self.GetMotds()
		else:
			return self.GetMotd()

	def SaveFile(self):
		if self.update_file:
			self.update_file = False
			self.WriteFile("\n".join(self.list_motd))