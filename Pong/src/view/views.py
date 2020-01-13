import tkinter as tk
''' HOW TO USE 
	
	To create a new view, create a new view class that extends Tkinter Frame.
	Create your interface inside the new view class, instantiating anything with a 
	function as a class attribute.
	Create a corresponding controller in the controllers.py module.
	Add "command" attributes to interface objects that need them in the __init__
	method of your new controller class using x.config(command=y).
	Create methods with desired behaviour for each of the functions in your controller class.
	'''
class StartPageView(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        tk.Label(self, text="This is the start page").pack(side="top", fill="x", pady=10)
        self.test_button = tk.Button(self, text="Test Button")
        self.test_button.pack()

        self.start_game_button = tk.Button(self, text="Start Game")
        self.start_game_button.pack()

class GameView(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)

        self.canvas = tk.Canvas(self)
        self.canvas.config(background="black")
        self.canvas.pack(fill="both", expand=True)

    def draw_gamestate(self, gamestate):
        ''' Draws the state of the game on the canvas '''

        # Refreshes the canvas
        self.canvas.delete("all")

        # Draws leftmost paddle
        self.canvas.create_rectangle(
            gamestate.get_paddle1_location()["xcoo"], 
            gamestate.get_paddle1_location()["ycoo"], 
            gamestate.get_paddle1_location()["xcoo"] + gamestate.get_paddle1_dimensions()["width"], 
            gamestate.get_paddle1_location()["ycoo"] + gamestate.get_paddle1_dimensions()["height"], 
            fill="blue")
    	
        # Draws rightmost paddle
        self.canvas.create_rectangle(
            gamestate.get_paddle2_location()["xcoo"], 
            gamestate.get_paddle2_location()["ycoo"], 
            gamestate.get_paddle2_location()["xcoo"] + gamestate.get_paddle2_dimensions()["width"], 
            gamestate.get_paddle2_location()["ycoo"] + gamestate.get_paddle2_dimensions()["height"], 
            fill="blue")

        # Draws ball
        self.canvas.create_oval(
            gamestate.get_ball_location()["xcoo"],
            gamestate.get_ball_location()["ycoo"],
            gamestate.get_ball_location()["xcoo"] + gamestate.get_ball_size(),
            gamestate.get_ball_location()["ycoo"] + gamestate.get_ball_size(),
            fill="green")