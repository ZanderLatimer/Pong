import main
from view import views
from model import gamestate

FPS = 60
PADDLE1_UP = "w"
PADDLE1_DOWN = "s"
PADDLE2_UP = "Up"
PADDLE2_DOWN = "Down"

class MasterController():
	''' Controls the flow of the application 
		including changing of views and sub-controllers '''
	def __init__(self, application):
		self.application = application
		self.window_size = None

		start_page_view = views.StartPageView()
		start_page_controller = StartPageController(self, start_page_view)

		self.change_view(start_page_view, start_page_controller)

	def change_view(self, view, controller):
		self.current_view = view
		self.current_controller = controller

		self.application.show_view(self.current_view)


class StartPageController():
	''' Start page for starting new game, changing settings etc.'''
	def __init__(self, master_controller, view):
		self.master_controller = master_controller
		self.view = view

		self.view.test_button.config(command=self.test_button_click)
		self.view.start_game_button.config(command=self.start_game_button_click)

	def test_button_click(self):
		print("Test Button")

	def start_game_button_click(self):
		game_view = views.GameView()
		game_view_controller = GameViewController(self.master_controller, game_view)

		self.master_controller.change_view(game_view, game_view_controller)


class GameViewController():
	''' Controls game logic such as draw commands, updating states,
		user input etc. '''

	def __init__(self, master_controller, view):
		self.master_controller = master_controller
		self.view = view
		self.window_size = {"width": self.view.master.winfo_width(),
							"height": self.view.master.winfo_height()}
		self.gamestate = gamestate.GameState(self.window_size)

		self.key_states = {PADDLE1_UP: False, PADDLE1_DOWN: False, PADDLE2_UP: False, PADDLE2_DOWN: False}

		for char in [PADDLE1_UP, PADDLE1_DOWN, PADDLE2_UP, PADDLE2_DOWN]:
			self.view.master.bind("<KeyPress-%s>" % char, self.key_pressed)
			self.view.master.bind("<KeyRelease-%s>" % char, self.key_released)

		self.game_loop()

	def key_pressed(self, event):
		self.key_states[event.keysym] = True		

	def key_released(self, event):
		self.key_states[event.keysym] = False

	def game_loop(self):
		''' Calls to update the gamestate model and graphics at specified FPS '''

		if self.key_states[PADDLE1_UP] == True:
			self.gamestate.update_paddle1_location(0, -5)
		if self.key_states[PADDLE1_DOWN] == True:
			self.gamestate.update_paddle1_location(0, 5)
		if self.key_states[PADDLE2_UP] == True:
			self.gamestate.update_paddle2_location(0, -5)
		if self.key_states[PADDLE2_DOWN] == True:
			self.gamestate.update_paddle2_location(0, 5)

		self.gamestate.update_ball_location()

		self.view.draw_gamestate(self.gamestate)

		self.view.after(1000//FPS, self.game_loop)

	def paddle1_up_press(self, event):
		''' Moves the leftmost paddle up when the up key is pressed '''

		self.gamestate.update_paddle1_location(0, -5)

	def paddle1_down_press(self, event):
		''' Moves the leftmost paddle down when the down key is presses '''

		self.gamestate.update_paddle1_location(0, 5)

	def paddle2_up_press(self, event):
		''' Moves the leftmost paddle up when the up key is pressed '''

		self.gamestate.update_paddle2_location(0, -5)

	def paddle2_down_press(self, event):
		''' Moves the leftmost paddle down when the down key is presses '''

		self.gamestate.update_paddle2_location(0, 5)