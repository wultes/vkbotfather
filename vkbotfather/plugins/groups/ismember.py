import requests


class GetIsMember:
    def __init__(self, token, group_id, command):
        self.group_id = group_id
        self.command = command
        self.token = token
  
    def get_json(self, user_id):
        vk_api = 'https://api.vk.com/method/groups.isMember?group_id={0}&user_id={1}&access_token={2}&v=5.103'.format(self.group_id, user_id, self.token)
        call = requests.get(vk_api).json()

        return call
  
    def get_message(self, msg):
        user_id = msg[len(self.command)+1:]

        call = self.get_json(user_id)

        if call['response'] == 1:
            return 'Данный пользователь является участником сообщества'
        return 'Данный пользователь не является участником сообщества'
  
    def get_ismember(self, msg, *args):
        if self.command in msg:
        message = self.get_message(msg)

        return message
