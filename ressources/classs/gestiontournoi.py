# gestiontournoi.py

import os
import json

class GestionTournoi(object):
	"""docstring for GestionTournoi"""
	def __init__(self, path_fichier=None):
		super(GestionTournoi, self).__init__()
		self.path_fichier = path_fichier 
		self.dico = self.load_dico()
		pass
		
# Chargement dico		
	def load_dico(self):
		if os.path.exists(self.path_fichier):
			fichier = open(self.path_fichier, "r", encoding="utf8")
			value = fichier.read()
			fichier.close()
			return json.loads(value)
		return {}

#DICO
	def add(self, discord_name, discord_id, mtga_id, twitch_name, pays):
		self.dico[discord_id] = [discord_name, mtga_id, twitch_name, pays]
		pass
	def order(self):
		DICO = self.dico.copy()
		self.dico = dict(sorted(DICO.items()))
		pass
	def getDico(self):
		return self.dico
	def save(self):
		value = json.dumps( self.dico, indent="\t" )
		#print(f"Json Save {self.path_fichier}")
		#print(f"Save: {value}")
		fichier = open(self.path_fichier, "w", encoding="utf8")
		fichier.write(value)
		fichier.close()
		pass
