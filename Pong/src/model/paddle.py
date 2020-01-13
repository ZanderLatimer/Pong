class Paddle():

	def __init__(self, dimensions, location, speed):
		self.dimensions = dimensions
		self.location = location
		self.speed = speed

	def get_dimensions(self):
		return self.dimensions

	def get_speed(self):
		return self.speed

	def get_location(self):
		return self.location

	def set_dimensions(self):
		pass

	def set_speed(self):
		pass

	def set_location(self, xcoo, ycoo):
		self.location["xcoo"] = xcoo
		self.location["ycoo"] = ycoo

	def update_location(self, xdelta, ydelta):
		self.location["xcoo"] += xdelta
		self.location["ycoo"] += ydelta