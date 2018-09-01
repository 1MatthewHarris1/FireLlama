from GameStates import MainMenu
from TransitionFunction import TransitionFunction

game_state = MainMenu()

while game_state.name != 'exit':

	game_state.procedure()
	new_game_state = TransitionFunction.transition(game_state.name, game_state.input_)
	if new_game_state != None:
		game_state = new_game_state

game_state.procedure()
