import random 
import asyncio
import datetime

from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll

from VkBot.settings import SettingsBot



class MakeBot(SettingsBot):

    def start_listen(self):
        try:
            print('| Сервер запущен\n| {0}'.format(datetime.datetime.now()))
            for event in self.long_poll.listen():
                if self.valid_event(event):
                    if event.from_user:
                        self.give_response_user(event.obj['message']['text'], event.obj['message']['peer_id'])
                    if event.from_chat:
                        self.give_response_chat(event.obj['message']['text'], event.obj['message']['peer_id'])

        except KeyboardInterrupt:
            print('| Сервер выключен\n| {0}'.format(datetime.datetime.now()))

    #Если написали боту в лс
    def give_response_user(self, event_text, event_user_id):
        print('| {2} :Бот получил сообщение "{0}" <- @{1}'.format(event_text, event_user_id, datetime.datetime.now()))
        response = self.message_analysic(event_text)
        if '.jpg' or '.png' in response:
            photo = self.photo_upload(response)
            self.send_image_user(photo, event_user_id)
        else:
            self.send_message_user(response, event_user_id)

    def send_message_user(self, msg, user_id):
        self.vk.messages.send(
            peer_id=user_id,
            message=msg,
            random_id=random.randint(1, 10 ** 8)
        )
        print('| {2} :Бот отправил сообщение "{0}" -> @{1}'.format(msg, user_id, datetime.datetime.now()))

    def send_image_user(self, image, user_id):
        
        self.vk.messages.send(
            peer_id=user_id,
            message='на',
            attachment = image,
            random_id = random.randint(1, 10 ** 8)
        )

        print('| {2} :Бот отправил изображение "{0}" -> @{1}'.format(image, user_id, datetime.datetime.now()))

    #Если боту написали в беседу
    def give_response_chat(self, event_text, event_chat_id):
        print('| {2} :Бот получил сообщение "{0}" из беседы id{1}'.format(event_text, event_chat_id, datetime.datetime.now()))
        response = self.message_analysic(event_text)
        if '.jpg' in response:
            photo = self.photo_upload(response)
            self.send_image_chat(photo, event_chat_id)
        else:
            self.send_message_chat(response, event_chat_id)

    def send_message_chat(self, msg, chat_id):
        self.vk.messages.send(
            peer_id=chat_id,
            message=msg,
            random_id=random.randint(1, 10 ** 8)
        )
        print('| {2} :Бот отправил сообщение "{0}" в беседу id{1}'.format(msg, chat_id, datetime.datetime.now()))
    
    def send_image_chat(self, image, chat_id):
        self.vk.messages.send(
            peer_id=chat_id,
            message="на",
            attachment = image,
            random_id=random.randint(1, 10 ** 8)
        )

        print('| {2} :Бот отправил изображение "{0}" в беседу id{1}'.format(image, chat_id, datetime.datetime.now()))

    #Проверка на получение сообщений
    def valid_event(self, event):
        return event.type == VkBotEventType.MESSAGE_NEW

    #Для загрузки изображений (специально для плагинов)
    def photo_upload(self, url_photo):
        images = []

        photo = self.vk_upload.photo_messages(url_photo)[0]

        images.append(
            'photo{0}_{1}'.format(photo['owner_id'], photo['id'])
        )

        return images
    
    #Здесь меняем условия запуска плагина
    def message_analysic(self, message):
        if 'help' in message:
            return self.plugins[0].get_about() #выводит информацию о возможностях бота
        if 'орел или решка' in message:
            return self.plugins[2].get_heads_and_tails() #выводит рандомно "орел" или "решка"
        else:
            return self.plugins[1].get_anything() #выводит рандомные фразы