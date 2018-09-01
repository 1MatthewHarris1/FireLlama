class State:

	name = 'base_state'

	def __init__(self, name = None):

		if name != None:
			self.name = name

		self.input_ = None

	def prompt(self):

		# Here is where you'll define the prompt for this state
		self.input_ = input(': ')

	def procedure(self):

		# Here is the procedure for what happens when this state is entered
		pass
