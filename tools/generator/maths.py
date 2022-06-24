# maths.py

class GeneratorMaths(object):
	"""docstring for GeneratorMaths"""
	def __init__(self, arg):
		super(GeneratorMaths, self).__init__()
		self.arg = arg

	def Percentage(self,first,two):
		if not two:
			return f"{round((first*100),2)}%"
		calcul = first / two
		return f"{round((calcul*100),2)}%"