import requests

class GetInfoUser:
    def __init__(self, command, token):
        self.command = command
        self.token =  token
    
    def get_json(self, user_id):
        vk_api = 'https://api.vk.com/method/users.get?user_ids={0}&access_token={1}&v=5.103'.format(user_id, self.token)

        call = requests.get(vk_api).json()

        return call

    def get_message(self, msg):

        user_id = msg[len(self.command)+1:]

        json =  self.get_json(user_id)

        print(json)

        message = 'Неверно введен ID или некоректная работа плагина'

        try:
            message = "Информация о пользователе:\n Имя: {0}\nФамилия: {1}\nID: {2}\nЗакрыт/Открыт профиль: {3}\nСсылка на профиль: {4}".format(
                            json['response'][0]['first_name'], 
                            json['response'][0]['last_name'],
                            json['response'][0]['id'],
                            json['response'][0]['is_closed'],
                            'vk.com/id' + str(json['response'][0]['id'])
                        )
        except:
            pass


        return message

    def get_infouser(self, msg, *args):
        if self.command in msg:
            message = self.get_message(msg)

            return message
