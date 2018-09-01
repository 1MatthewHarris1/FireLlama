import sys, inspect
import GameStates
from State import State

class TransitionFunctionBase:

	def __init__(self, transition_list):
		
		self.transition_list = transition_list

	def transition(self, state, input_):

		transition_to = self.determine_transition_name(state, input_)
		game_states = self.get_game_state_names()
		for state_name in game_states:
			if state_name == transition_to:
				return game_states[state_name]()

		return None

	def determine_transition_name(self, state, input_):
	
		for transition in transition_list:
			if transition[0] == state:
				if input_ == transition[1]:
					return transition[2]

		return None
		
	def options(self, state):

		option_list = []

		for transition in transition_list:
			if transition[0] == state:
				option_list.append(transition[1])

		return option_list

	def get_game_state_names(self):

		names = {}
		
		for name, obj in inspect.getmembers(sys.modules['GameStates']):
			if inspect.isclass(obj):
				if issubclass(obj, State):
					if obj.name != 'base_state':
						names[obj.name] = obj

		return names

transition_list = [
('main_menu', 'exit', 'exit'),
('main_menu', 'play', 'game_start'),
('main_menu', 'credits', 'credits'),
('credits', None, 'main_menu'),
('game_start', None, 'home'),
('home', 'exit', 'main_menu'),
('home', 'outside', 'outside'),
('outside', None, 'home')
]
TransitionFunction = TransitionFunctionBase(transition_list)








