import random

class WhatRandom:
	def __init__(self, command):
		self.command = command

	def get_message(self):

		rand = random.randint(0, 100)

		message = "Вероятность этого равна {0}%".format(rand)

		return message

	def get_random(self, msg, *args):
		if self.command in msg:
			message = self.get_message()
			return message

