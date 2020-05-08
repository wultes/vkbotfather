class About:
	def __init__(self, command, message):
		self.command = command
		self.message = message

	def get_about(self, msg, *args):
		if self.command in msg:
			return self.message