import requests

class GetAllMemberChat:
	def __init__(self, token, command):
		self.token = token
		self.command = command

	def get_json(self, peer_id):
		vk_api = 'https://api.vk.com/method/messages.getConversationMembers?peer_id={0}&fields=sex&access_token={1}&v=5.103'.format(peer_id, self.token)
		call = requests.get(vk_api).json()
		return call

	def get_message(self, peer_id):
		json = self.get_json(peer_id)

		message = "Все участники беседы:\n"
		count = 0

		for item in json['response']['profiles']:
			count += 1
			message = message + "{3}. [id{0}|{1} {2}]\n".format(item['id'], item['first_name'], item['last_name'], count)

		return message

	def get_allmemberchat(self, msg, *args):
		peer_id = args[0]['message']['peer_id']

		if self.command in msg:
			if '200000000' in str(peer_id):
				message = self.get_message(peer_id)
				return message
			else:
				return 'Бот не находится в беседе'




