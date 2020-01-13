class Ball():

	def __init__(self, size, location, speed, direction):
		self.size = size
		self.location = location
		self.speed = speed
		self.direction = direction

	def get_location(self):
		return self.location

	def get_size(self):
		return self.size

	def get_speed(self):
		return self.speed

	def get_direction(self):
		return self.direction

	def set_location(self, xcoo, ycoo):
		self.location["xcoo"] = xcoo
		self.location["ycoo"] = ycoo

	def set_direction(self, direction):
		self.direction = direction % 360