import tkinter as tk

from view import views
from controller import controllers

APPLICATION_TITLE = "Pong"
WINDOW_WIDTH = "600"
WINDOW_HEIGHT = "600"

class Application(tk.Tk):
	''' Main application window '''

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		# Adds persistent menu bar to application window
		menubar = tk.Menu(self)
		filemenu = tk.Menu(menubar, tearoff=0)
		filemenu.add_command(label="Exit", command=self.quit)
		menubar.add_cascade(label="File", menu=filemenu)

		self._frame = None
		self.config(menu=menubar)
		self.title(APPLICATION_TITLE)
		self.geometry("{0}x{1}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
		self.resizable(False, False)

	def show_view(self, view):
		''' Show a given view on the main application window '''
		
		if self._frame is not None:
			self._frame.destroy()
		self._frame = view
		self._frame.pack(fill="both", expand=True)


if __name__ == "__main__":
	''' Entry point into the program
		Creates application window and master controller '''

	app = Application()
	controllers.MasterController(app)

	# Centers the application window on the screen
	screen_width = app.winfo_screenwidth()
	screen_height = app.winfo_screenheight()
	xpos = (screen_width/2) - (int(WINDOW_WIDTH)/2)
	ypos = (screen_height/2) - (int(WINDOW_HEIGHT)/2)
	app.geometry('{0}x{1}+{2}+{3}'.format(WINDOW_WIDTH, WINDOW_HEIGHT, int(xpos), int(ypos)))

	app.mainloop()