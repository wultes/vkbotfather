import random

class GetWhatChoose:
	def __init__(self, command):
		self.command = command

	def get_message(self, msg):
		
		message = msg[len(self.command)+1:]
		if len(message) > 0:
			first_choise = message[message.find('или')+4:]
			second_choise = message[:-message.find('или')-4]

			random_num = random.randint(1, 2)

			if random_num == 1 and first_choise != '' and first_choise != ' ' and first_choise != None:
				return "Я думаю, что лучше {0}".format(first_choise)
			elif random_num == 2 and second_choise != '' and second_choise != ' ' and second_choise != None:
				return "Я думаю, что лучше {0}".format(second_choise)
		else:
			return '0'


	def get_choise(self, msg, *args):

		if self.command in msg:
			message = self.get_message(msg)
			if message != '0':
				return message
			else:
				pass