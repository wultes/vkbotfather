import random 
import asyncio
import datetime

from vk_api.longpoll import VkEventType

from VkBot.settings import SettingsBot

IMAGE_TYPE = ['.jpg', '.png']

class MakeBot(SettingsBot):

    def start_listen(self):
        try:
            print('| Сервер запущен\n| {0}'.format(datetime.datetime.now()))
            for event in self.long_poll.listen():
                if self.valid_event(event):
                    self.give_response(event.text, event.user_id)

        except KeyboardInterrupt:
            print('| Сервер выключен\n| {0}'.format(datetime.datetime.now()))

    def give_response(self, event_text, event_user_id):
        print('| {2} :Бот получил сообщение "{0}" <- @{1}'.format(event_text, event_user_id, datetime.datetime.now()))
        response = self.message_analysic(event_text)
        if '.jpg' in response: 
            photo = self.photo_upload(response)
            self.send_image(photo, event_user_id)
        else:
            self.send_message(response, event_user_id)

    def photo_upload(self, url_photo):
        images = []

        photo = self.vk_upload.photo_messages(url_photo)[0]

        images.append(
            'photo{0}_{1}'.format(photo['owner_id'], photo['id'])
        )

        return images


    def message_analysic(self, message):
        if message == '/help':
            return self.plugins[0].get_about()
        if 'орел или решка' in message:
            return self.plugins[2].get_heads_and_tails()
        else:
            return self.plugins[1].get_anything()
        

    def send_message(self, msg, user_id):
        self.vk.messages.send(
            user_id=user_id,
            message=msg,
            random_id=random.randint(1, 10 ** 8)
        )
        print('| {2} :Бот отправил сообщение "{0}" -> @{1}'.format(msg, user_id, datetime.datetime.now()))

    def send_image(self, image, user_id):
        
        self.vk.messages.send(
            user_id=user_id,
            message='вот',
            attachment = image,
            random_id = random.randint(1, 10 ** 8)
        )

        print('| {2} :Бот отправил изображение "{0}" -> @{1}'.format(image, user_id, datetime.datetime.now()))

    def valid_event(self, event):
        return event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text and event.from_user
        