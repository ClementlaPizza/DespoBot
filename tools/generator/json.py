# json.py
from tools.generator.file import FileGenerator
import json

class JsonGenerator(FileGenerator):
	"""docstring for JsonGenerator"""
	def __init__(self, path_file):
		super(JsonGenerator, self).__init__(path_file)
		self.path_file = path_file
		self.json = self.load()


	def set(self, key, value):
		self.json[str(key)] = value
		pass

	def setJson(self, json):
		self.json = json
		pass

	def setItems(self, key, key2, value):
		key_value = self.get(key)
		key_value[key2] = value
		self.set(key, key_value)
		pass

	def getJson(self):
		return self.json

	def getKeys(self):
		return list(self.json.keys())

	def get(self, key):
		return self.json.get(str(key), {})
	
	def getItems(self, key, key2):
		key_value = self.get(key)
		if key_value and type(key_value) is dict:
			return key_value.get(key2, {})
		return key_value

	def count(self):
		return len(self.json)

	def find(self, word):
		dico_word = {}
		for key, value in self.json.items():
			if type(value) is dict:
				if word.lower() in str(value.values()).lower():
					dico_word[key] = value
					# print(value)
					pass
				pass
			else:
				if word.lower() in str(value).lower():
					dico_word[key] = value
					# print(value)
					pass
				pass
			pass
		return dico_word

	def delete(self, key):
		key_value = self.json.get(key, None)
		if key_value != None:
			del self.json[key]
			pass
		pass

	def load(self):
		try:
			return json.loads(self.GetContent())
		except Exception as JSONDecodeError:
			return {}
		except Exception as e:
			raise e

	def save(self):
		value = json.dumps(self.json, indent="\t")
		self.WriteFile(value)
		pass

	def read(self):
		value = json.dumps(self.json, indent="\t")
		print(value)
		pass
