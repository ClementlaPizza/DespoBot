# file generator

import os

class Generator_File(object):
	"""docstring for Generator_File"""
	def __init__(self, path_file):
		super(Generator_File, self).__init__()
		self.path_file = path_file
		self.Create()
		self.Load()

	def Create(self):
		if not os.path.exists(self.path_file):
			file = open(self.path_file, "w", encoding="utf8")
			# print(self.path_file)
			file.write("")
			file.close()
			pass
		pass

	def Load(self):
		file = open(self.path_file, "r", encoding="utf8")
		self.read_file = file.read()
		file.close()
		pass

	def Write(self, content=""):
		file = open(self.path_file, "w", encoding="utf8")
		file.write(content)
		# print(f"WriteFile {content}")
		file.close()
		pass

	def AddContent(self, content=""):
		file = open(self.path_file, "a", encoding="utf8")
		file.write(content)
		# print(f"AddContent {content}")
		file.close()
		pass

	def AddLine(self, content="\n"):
		file = open(self.path_file, "a", encoding="utf8")
		file.write("\n" + content)
		# print(f"AddLine {content}")
		file.close()
		pass
		pass

	def EditLine(self, number, content=""):
		read = self.GetContentList()
		if number > len(read):
			return False
		read[number-1] = content
		self.WriteFile("\n".join(read))

	def GetContent(self):
		return self.read_file

	def GetContentList(self):
		return self.read_file.splitlines()

	def UpdateContentList(self):
		self.LoadFile()
		return self.GetContentList()