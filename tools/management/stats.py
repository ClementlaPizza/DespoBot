from safe import ROLE_MODERATOR

class ManagementStats(object):
	"""docstring for ManagementStats"""
	def __init__(self, arg=None):
		super(ManagementStats, self).__init__()
		self.arg = arg
		self.convert_mention = ""
	
	def checkMember(self, member):
		if "<@!" in member and not "<@&" in member:
			return True
		else:
			return False
		pass

	def checkBot(self, member):
		if member.bot:
			return True
		else:
			return False

	def checkRole(self, role):
		if "<@&" in role and not "<@!" in role:
			return True
		else:
			return False

	def checkModeratorRole(self, roles):
		roles_exist = False
		for r in roles:
			if r.id == ROLE_MODERATOR:
				roles_exist = True
				break
			pass
		return roles_exist

	def checkChannelorCategory(self, channel):
		if "<#" in channel:
			return True
		else:
			return False
		pass

	def checkChannelType(self, channel):
		pass

	def checkCmdVarRoles(self, cmd):
		check_alias = False
		alias_roles = ["role", "roles", "rôle", "rôles"]
		cmd = cmd.lower()
		for cmda in alias_roles:
			if cmda in cmd:
				# print(True)
				check_alias = True
		return check_alias

	def checkCmdVarServer(self, cmd):
		check_alias = False
		# print(var)
		cmd = cmd.lower()
		# print(cmd)
		alias_server = ["server","serveur","df","despotikfamily"]
		# print(alias_server)
		for cmda in alias_server:
			if cmda in cmd:
				# print(True)
				check_alias = True
		return check_alias

	def checkEmoji(self, emoji):
		emoji_chek = False
		for e in emoji:
			if not e.animated:
				emoji_chek = True
				# print(e)
		return emoji_chek

	def checkEmojiAnimated(self, emoji):
		emoji_chek = False
		for e in emoji:
			if not e.animated:
				emoji_chek = True
				# print(e)
		return emoji_chek

	def ConvertMention(self, mention):
		if self.checkMember(mention):
			self.convert_mention = int(mention.replace("<", "").replace("@", "").replace("!", "").replace(">", ""))
		elif self.checkRole(mention):
			self.convert_mention = int(mention.replace("<", "").replace("@", "").replace("&", "").replace(">", ""))
		elif self.checkChannelorCategory(mention):
			self.convert_mention = int(mention.replace("<", "").replace("#", "").replace(">", ""))
		return self.convert_mention

	def CountOnlineMember(self,members):
		count_member = 0
		for m in members:
			if not "offline" in m.status:
				count_member += 1
		return count_member

	def CountEmoji(self, emoji):
		emoji_count = 0
		for e in emoji:
			if not e.animated:
				emoji_count += 1
				# print(e)
		return emoji_count

	def CountEmojiAnimated(self, emoji):
		emoji_count = 0
		for e in emoji:
			if e.animated:
				emoji_count += 1
				# print(e)
		return emoji_count

	def PercentageCalculator(self,first,two):
		if not two:
			return f"{round((first*100),2)}%"
		calcul = first / two
		return f"{round((calcul*100),2)}%"

	def Top3Role(self, roles):
		role_dict = {}
		for r in roles:
			role_dict[r.mention] = len(r.members)
			pass
		# print(role_dict)
		if role_dict:
		# delete everyone
			if "<@&367403580015116288>" in role_dict.keys():
				del role_dict["<@&367403580015116288>"]
		#delete petit_despote
			if "<@&491952140005408770>" in role_dict.keys():
				del role_dict["<@&491952140005408770>"]
		# sort
			role_dict = dict(sorted(role_dict.items(), key=lambda x:x[1], reverse=True)[:3])
			# print("\n", role_dict)
		return role_dict

	def RoleSort(self, roles, members):
		# init
		role_dict = {}
		# search
		for r in roles:
			percentage = self.PercentageCalculator(len(r.members),len(members))
			role_dict[r.mention] = (len(r.members),percentage)
			pass
		# check
		if role_dict:
		# delete everyone
			if "<@&367403580015116288>" in role_dict.keys():
				del role_dict["<@&367403580015116288>"]
		# sort
			role_dict = dict(sorted(role_dict.items(), key=lambda x:x[1], reverse=True))

		# print("\n", role_dict)
		return role_dict