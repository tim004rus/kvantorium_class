# class A():
# 	"""docstring for A"""
# 	def __init__(self, arg):
# 		self.field_1 = arg
# 		print("1")
# class B(A):
# 	"""docstring for B"""
# 	def __init__(self, arg):
# 		super(A, self).__init__()
# 		self.field_2 = arg
# 		print(self.field_2)
# b = B(1)


drive_types = ['AWD', 'FWD', 'RWD']
class Vehicle():
	"""docstring for Vehicle"""
	def __init__(self, engine_type, weight, max_speed):
		self.engine_type = engine_type
		self.weight = weight
		self.max_speed = max_speed
		print(self.engine_type)

class Car(Vehicle):
	"""docstring for Car"""
	drive_types = ['AWD', 'FWD', 'RWD']

	def __init__(self, engine_type, weight, max_speed, drive):
		super(Car, self).__init__(engine_type, weight, max_speed, drive)
		self.drive = drive
		print(self.engine_type)
		print(self.weight)
		print(self.max_speed)
		print(self.drive)

	def upgrade(self, upgrade_speed):
		try:
			self.max_speed += upgrade_speed
		except TypeError as e:
			print("Error")
		print("Max speed: %s" % self.max_speed)


car = Car(engine_type = 'V6, gas ', weight = 1000, max_speed = 200, drive = drive_types[0])
car.upgrade(20)