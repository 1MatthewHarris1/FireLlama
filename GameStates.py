from State import State
from Utilities import Window

class MainMenu(State):

	name = 'main_menu'

	def __init__(self, name = None):
		super(MainMenu, self).__init__(name)
		
	def prompt(self):

		self.main_menu_window.display()
		self.input_ = input('What would you like to do?: ')

	def procedure(self):

		self.main_menu_window = Window(text = 
		'You are at the main menu\n\nPlay: play\nExit: exit\nCredits: credits', clearing = True)
		self.prompt()

class Exit(State):

	name = 'exit'

	def __init__(self, name = None):
		super(Exit, self).__init__(name)
	
	def prompt(self):
		pass

	def procedure(self):
		
		self.exit_window = Window(text = 'The game will now exit')
		self.exit_window.display()

class Credits(State):

	name = 'credits'

	def __init__(self, name = None):
		super(Credits, self).__init__(name)

	def prompt(self):
		input('Press Enter')

	def procedure(self):

		self.credits_window = Window(text = 'It was all me!', clearing = True)
		self.credits_window.display()
		self.prompt()

class GameStart(State):

	name = 'game_start'

	def __init__(self, name = None):
		super(GameStart, self).__init__(name)

	def prompt(self):
		input('Press Enter')

	def procedure(self):

		self.game_start_window = Window(text =
		"You have started the game! This is where we'd put some information about the backstory in order to introduce you to the characters and the setting, but right now we're just deving the framework, not an actual game!", clearing = True)
		self.game_start_window.display()
		self.prompt()

class Home(State):

	name = 'home'

	def __init__(self, name = None):
		super(Home, self).__init__(name)

	def prompt(self):

		self.input_ = input('What would you like to do?: ')

	def procedure(self):

		self.home_menu_window = Window(text = 
		'You are home\n\nGo Outside: outside\nExit: exit', clearing = True)
		self.home_menu_window.display()
		self.prompt()

class Outside(State):

	name = 'outside'

	def __init__(self, name = None):
		super(Outside, self).__init__(name)

	def prompt(self):
		input('Press Enter')

	def procedure(self):

		self.outside_window = Window(text = "You're outside! Yay! Okay, you've had your fun. Time to go back in.", clearing = True)
		self.outside_window.display()
		self.prompt()




