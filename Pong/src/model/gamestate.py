import math
from model import paddle, ball

PADDLE_HEIGHT = 75

class GameState():

	def __init__(self, window_size):
		self.window_size = window_size
		self.paddle1 = paddle.Paddle({"width":15, "height":PADDLE_HEIGHT}, 
									 {"xcoo": 25, "ycoo": (window_size["height"]//2) - PADDLE_HEIGHT//2}, 
									 1)
		self.paddle2 = paddle.Paddle({"width":15, "height":PADDLE_HEIGHT}, 
									 {"xcoo": window_size["width"] - 15 - 25, "ycoo": (window_size["height"]//2) - PADDLE_HEIGHT//2}, 
									 1)
		self.ball = ball.Ball(10, {"xcoo": 300, "ycoo": 300}, 1, 45)

	def get_paddle1_location(self):
		''' Returns the location of the leftmost paddle '''

		return self.paddle1.get_location()

	def get_paddle1_dimensions(self):
		''' Returns the dimensions of the leftmost paddle '''

		return self.paddle1.get_dimensions()

	def update_paddle1_location(self, xdelta, ydelta):
		''' Updates the location of the leftmost paddle.
			Make sure that the paddle stays within bounds. '''

		# Checks if paddle is moving upwards out of bounds
		if (self.paddle1.get_location()["ycoo"] + ydelta) < 0:
			self.paddle1.set_location(self.paddle1.get_location()["xcoo"], 0)

		# Checks if paddle is moving downwards out of bounds
		elif (self.paddle1.get_location()["ycoo"] + ydelta) > (self.window_size["height"] - self.paddle1.get_dimensions()["height"]):
			self.paddle1.set_location(self.paddle1.get_location()["xcoo"], self.window_size["height"] - self.paddle1.get_dimensions()["height"])
		# Otherwise moves the paddle
		else:
			self.paddle1.update_location(xdelta, ydelta)


	def get_paddle2_location(self):
		''' Returns the location of the leftmost paddle '''

		return self.paddle2.get_location()

	def get_paddle2_dimensions(self):
		''' Returns the dimensions of the leftmost paddle '''

		return self.paddle2.get_dimensions()

	def update_paddle2_location(self, xdelta, ydelta):
		''' Updates the location of the leftmost paddle.
			Make sure that the paddle stays within bounds. '''

		# Checks if paddle is moving upwards out of bounds
		if (self.paddle2.get_location()["ycoo"] + ydelta) < 0:
			self.paddle2.set_location(self.paddle2.get_location()["xcoo"], 0)

		# Checks if paddle is moving downwards out of bounds
		elif (self.paddle2.get_location()["ycoo"] + ydelta) > (self.window_size["height"] - self.paddle2.get_dimensions()["height"]):
			self.paddle2.set_location(self.paddle2.get_location()["xcoo"], self.window_size["height"] - self.paddle2.get_dimensions()["height"])

		# Otherwise moves the paddle
		else:
			self.paddle2.update_location(xdelta, ydelta)

	def get_ball_vector(self):
		return {"xcoo": self.ball.get_location()["xcoo"], 
				"ycoo": self.ball.get_location()["ycoo"], 
				"speed": self.ball.get_speed(), 
				"direction": self.ball.get_direction()}

	def get_ball_location(self):
		return self.ball.get_location()

	def get_ball_size(self):
		return self.ball.get_size()

	def update_ball_location(self):
		direction = self.ball.get_direction() * math.pi / 180
		xcoo = self.ball.get_location()["xcoo"] + (1 * self.ball.get_speed()) * math.cos(direction)
		ycoo = self.ball.get_location()["ycoo"] + (1 * self.ball.get_speed()) * math.sin(direction)

		self.ball.set_location(xcoo, ycoo)