import requests


class KickUser:
	def __init__(self, word_list, token):
		self.word_list = word_list
		self.token = token

	def get_json(self, chat_id, user_id):
		vk_api = 'https://api.vk.com/method/messages.removeChatUser?chat_id={0}&user_id={1}&access_token={2}&v=5.103'.format(chat_id, user_id, self.token)
		call = requests.get(vk_api).json()
		return call

	def get_message(self, chat_id, user_id):
		json = self.get_json(chat_id, user_id)

		message = "За использованние запрещенных слов\n"

		return message

	def get_kickuser(self, msg, *args):
		chat_id = args[0]['message']['peer_id']
		user_id = args[0]['message']['from_id']

		new_chat_id = ''

		for word in self.word_list:
			if word in msg:
				if '200000000' in str(chat_id):
					for i in str(chat_id):
						if i != '0':
							new_chat_id += i
		
        message = self.get_message(new_chat_id[1:], user_id)
        return message

				else:
					pass
