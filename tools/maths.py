# Maths Generator

class Generator_Maths(object):
	"""docstring for Generator_Maths"""
	def __init__(self, arg=None):
		super(Generator_Maths, self).__init__()
		self.arg = arg

# methods
	def addition(self, *numbers):
		# print(self.check_Numbers(numbers))
		result = 0
		for x in self.check_Numbers(numbers):
			result = result + int(x)
			pass
		return result

	def subtraction(self, *numbers):
		result = 0
		for x in self.check_Numbers(numbers):
			result = result - int(x)
			pass
		return result

	def multiplication(self, *numbers):
		result = 1
		for x in self.check_Numbers(numbers):
			result = result * int(x)
			pass
		return result

	def division(self, *numbers):
		result = 1
		for x in self.check_Numbers(numbers):
			# print(x)
			if int(x) == 0:
				print("x = 0")
				return result
			result = result / int(x)
			pass
		# print(result)
		return result

	def percentage(self, number1, number2):
		result = (int(number1) / (int(number2)))*100
		result = round(result, 2)
		return f"{result}%"

# Check
	def check_Numbers(self, numbers):
		numbers = list(numbers)
		number_list = []
		for x in numbers:
			if type(x) == tuple:
				numbers = self.Convert_tuple_to_list(x)
			pass
		for n in numbers:
			if n != None and n.isdigit():
				number_list.append(n)
			pass
		return number_list



# Convert
	def Convert_tuple_to_list(self, tuplearg):
		return list(tuplearg)