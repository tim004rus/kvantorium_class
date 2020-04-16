class Car(object):
	"""Инфо о вашей машине"""
	def __init__(self, year, model):
		self.year = year
		self.model = model

year = int(input("Введите год выпуска вашей машины: "))
model = str(input("Введите название вашей машины: "))

print("Дата выпуска вашей машины:" + int(year))