#!C:\Python37 python3
# -*- coding: UTF-8 -*-

import os
import json
import random

class GestionMagicIDTag(object):
	"""docstring for GestionMagicIDTag"""
# Init
	def __init__(self, path_fichier=None):
		super(GestionMagicIDTag, self).__init__()
		self.path_fichier = path_fichier 
		self.dico = self.load_dico()
		self.setTitle()
		pass

# Chargement dico		
	def load_dico(self):
		if os.path.exists(self.path_fichier):
			fichier = open(self.path_fichier, "r", encoding="utf8")
			value = fichier.read()
			fichier.close()
			return json.loads(value)
		return {}

# Caractere autorisé
	def charIsGood(self, id_tag):
		caracteres_autorise = "#ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz_-0123456798"
		for char in id_tag:
			#print(f"Char (boucle for) = {char}")
			if char not in caracteres_autorise:
				#print(f"Caractere no autorise = {char}")
				return False
		return True

# IDTAG
	def checkIdTag(self, id_tag):
		try:
			char = self.charIsGood(id_tag)
			#print(f"char = {char}")
			if not char:
				return False
			n = id_tag.split("#")[1]
			return n.isnumeric()
		except Exception as e:
			# print(e)
			return False
	def getIdTagByMsg(self, msg):
		return " ".join(msg.content.split()[2:])
	def isExistIdTag(self, id_tag):
		dico = self.dico.copy()
		for key, value in dico.items():
			if value[0] == id_tag:
				return True
			pass
		return False
	def deleteidtag(self, id_tag):
		if not id_tag:
			return
		try:
			del self.dico[id_tag]
			pass
		except Exception as e:
			pass
		pass
	def delbyidtag(self, id_tag):
		DICO = self.dico.copy()
		valeur = None
		for key, value in DICO.items():
			if value[0] == id_tag:
				valeur = key
				break
		self.deleteidtag(valeur)

# Membre discord
	def getIdDiscordByMsg(self, msg):
		return msg.content.split()[1].replace("<","").replace("@","").replace(">","").replace("&","").replace("!","")
	def isExistNameDiscord(self, name_discord):
		dico = self.dico.copy()
		for key, value in dico.items():
			if value[1] == name_discord:
				return True
			pass
		return False
	def deleteDiscord(self, name_discord):
		if not name_discord:
			return
		try:
			del self.dico[name_discord]
			pass
		except Exception as e:
			raise e
		pass
	def delbynamediscord(self, name_discord):
		DICO = self.dico.copy()
		valeur = None
		for key, value in DICO.items():
			if value[1] == name_discord:
				valeur = key
				break
		self.deleteDiscord(valeur)

#DICO
	def ajouter(self, id_tag=None, name_discord=None, compte_twich=""):
		if name_discord and id_tag:
			self.dico[id_tag.lower()] =  [id_tag, name_discord, compte_twich]
			pass
		pass
	def order(self):
		DICO = self.dico.copy()
		self.dico = dict(sorted(DICO.items()))
		pass
	def lecture(self):
		for key, value in self.dico.items():
			print(f"ID tag: {key} Name Discord: {value[1]} Twitch name: {value[2]}")
			pass
		pass
	def getDico(self):
		return self.dico
	def getTailleDico(self):
		return len(self.dico)
	def save(self):
		value = json.dumps( self.dico, indent=4 )
		#print(f"Json Save {self.path_fichier}")
		#print(f"Save: {value}")
		fichier = open(self.path_fichier, "w", encoding="utf8")
		fichier.write(value)
		fichier.close()
		pass

#Embed
	def getDicoEmbed(self):
		dico_embed = {}
		dico_embed["title"] = self.titre
		dico_embed["description"] = self.getEmbedListeIdTag()+"\n"
		dico_embed["color"] = random.choice([0xFF0000, 0x000000, 0x5B98FF, 0x00F629, 0xFFFFFF])
		dico_embed["footer"] = {"text" : f"Il y a {self.getTailleDico()} Planeswalkers\nPour t'ajouter, envoie ton IDTAG", "icon_url": "https://cdn.discordapp.com/attachments/851643141101715486/890721938937372752/mana.gif"}
		# ordre couleur = [Rouge, Noir, Bleu, Vert, Blanc]
		return dico_embed
	def setTitle(self, titre="<:mtga:595322669071859732> __Liste des ID TAG Magic__ <:pw:672937536175341571>"):
		self.titre = titre
		pass
	def getEmbedListeIdTag(self):
		dico = self.dico.copy()
		members = []
		ancienne_lettre = ""
		for key, value in dico.items():
			if key[0].lower() != ancienne_lettre:
				members.append(f":regional_indicator_{key[0].lower()}:")
				ancienne_lettre = key[0].lower()
				pass
			members.append(f"**{value[0]}**\n<@{value[1]}>")
			pass
		return "\n".join(members).replace(">" , ">\n")