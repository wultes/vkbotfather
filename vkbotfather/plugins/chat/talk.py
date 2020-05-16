

class GetTalk:
	def __init__(self, words):
		self.words = words

	def get_message(self, item):

		message = self.words[item]
		return message

	def get_talk(self, msg, *args):

		zero_message = False

		for item in self.words:
			if item in msg:
				message = self.get_message(item)
				zero_message = True
				return message

		if zero_message == False:
			message = 'Я не понимаю вас'
			return message
