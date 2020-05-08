import requests 

class GetAllMember:
	def __init__(self, group_id, token, command):
		self.group_id = group_id
		self.token = token
		self.vk_api = 'https://api.vk.com/method/groups.getMembers?group_id={0}&fields=sex&access_token={1}&v=5.103'.format(self.group_id, self.token)
		self.command = command

	def get_json(self):
		call = requests.get(self.vk_api).json()
		return call 

	def get_message(self):
		json = self.get_json()

		message = "Список всех подписчиков:\n"
		count = 0

		for item in json['response']['items']:
			count += 1 
			message = message + "{3}. [id{0}|{1} {2}]\n".format(item['id'], item['first_name'], item['last_name'], count)

		return message

	def get_allmembers(self, msg, *args):
		if self.command in msg:
			message = self.get_message()
			return message
