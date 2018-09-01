import os
import platform

class Window:

	WINDOW_LEN = 151

	def __init__(self, length = None, text = None, clearing = False):

		self.length = length
		self.text = text
		self.clearing = clearing

		if platform.system() == 'Windows':
			self.clear_str = 'cls'
		else:
			self.clear_str = 'clear'


	def display(self):

		if self.clearing == True:
			print('screen should clear')
			os.system(self.clear_str)

		if self.length == None:
			self.length = len(self.text)
			if self.length > self.WINDOW_LEN:
				self.length = self.WINDOW_LEN
		
		window_x = ""
		for x in range(self.length):
			window_x = window_x + '-'

		print(window_x)
		print(self.text)
		print(window_x)

	def max_sub_len(self, subs):

		max_len = 0
		
		for line in subs:
			if len(line) > max_len:
				max_len = len(line)
		
		return max_len




