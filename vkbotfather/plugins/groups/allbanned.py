import requests


class GetAllBanned:
	def __init__(self, token, group_id, command):
		self.token = token
		self.group_id = group_id
		self.vk_api = 'https://api.vk.com/method/groups.getBanned?group_id={0}&fields=sex&access_token={1}&v=5.103'.format(self.group_id, self.token)
		self.command = command

	def get_json(self):
		call = requests.get(self.vk_api).json()
		return call

	def get_message(self):

		message = "Список пользователей в черном списке сообщества:\n"
		count = 0 

		json = self.get_json()
		if json['response']['count'] == 0:
			message = message + "У вас нет пользователей в черном списке"
		else:
			for item in json['response']['items']:
				count += 1
				message = message + "{3}. [id{0}|{1} {2}]\n".format(item['profile']['id'], item['profile']['first_name'], item['profile']['last_name'], count)

		return message

	def get_allbanned(self, msg, *args):
		if self.command in msg:
			message = self.get_message()
			return message