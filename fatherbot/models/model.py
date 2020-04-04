import random 
import asyncio
import datetime

from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll

from fatherbot.models.settings import SettingsBot


class Model(SettingsBot):

    def startListen(self):
        """Listens to messages and sends their responses to analyzes"""
        try:
            print('| Server is running\n| {0}'.format(datetime.datetime.now()))
            for event in self.long_poll.listen():
                if self.validEvent(event):
                    if event.from_user:
                        self.giveResponseUser(event.obj['message']['text'], event.obj['message']['peer_id'])
                    if event.from_chat:
                        self.giveResponseChat(event.obj['message']['text'], event.obj['message']['peer_id'])

        except KeyboardInterrupt:
            print('| Server shutdown\n| {0}'.format(datetime.datetime.now()))

    def giveResponseUser(self, event_text, event_user_id):
        """Takes a response and analyzes it. 
        This function processes requests from only one user. 
        You can change the response processing parameters."""

        print('| {2} :Bot got a message "{0}" <- @{1}'.format(event_text, event_user_id, datetime.datetime.now())) 
        
        response = self.messageAnalysis(event_text)
        if '.jpg' in response:
            photo = self.photoUpload(response)
            self.sendImageUser(photo, event_user_id)
        else:
            self.sendMessageUser(response, event_user_id)

    def sendMessageUser(self, msg, user_id):
        """Sends a text message to the user."""
        self.vk.messages.send(
            peer_id=user_id,
            message=msg,
            random_id=random.randint(1, 10 ** 8)
        )

        print('| {2} :Bot send a message "{0}" -> @{1}'.format(msg, user_id, datetime.datetime.now()))

    def sendImageUser(self, image, user_id):
        """Sends a image to the user."""
        self.vk.messages.send(
            peer_id=user_id,
            message='.', 
            attachment = image,
            random_id = random.randint(1, 10 ** 8)
        )

        print('| {2} :Bot send a image "{0}" -> @{1}'.format(image, user_id, datetime.datetime.now()))

    def giveResponseChat(self, event_text, event_chat_id):
        """Takes response and analyzes them. 
        This function processes requests from only chats. 
        You can change the response processing parameters."""

        print('| {2} :Bot got a message "{0}" from chat id{1}'.format(event_text, event_chat_id, datetime.datetime.now()))
        
        response = self.messageAnalysis(event_text)
        if '.jpg' in response:
            photo = self.photoUpload(response)
            self.sendImageChat(photo, event_chat_id)
        else:
            self.sendMessageChat(response, event_chat_id)

    def sendMessageChat(self, msg, chat_id):
        """Sends a text message to the chat."""

        self.vk.messages.send(
            peer_id=chat_id,
            message=msg,
            random_id=random.randint(1, 10 ** 8)
        )
        print('| {2} :Bot send a message "{0}" to chat id{1}'.format(msg, chat_id, datetime.datetime.now()))
    
    def sendImageChat(self, image, chat_id):
        """Sends a image to the chat"""

        self.vk.messages.send(
            peer_id=chat_id,
            message="на",
            attachment = image,
            random_id=random.randint(1, 10 ** 8)
        )

        print('| {2} :Bot send a image "{0}" to chat id{1}'.format(image, chat_id, datetime.datetime.now()))


    def validEvent(self, event):
        """Check message type."""
        return event.type == VkBotEventType.MESSAGE_NEW


    def photoUpload(self, url_photo):
        """For upload images on VK server."""

        images = []
        photo = self.vk_upload.photo_messages(url_photo)[0]
        images.append(
            'photo{0}_{1}'.format(photo['owner_id'], photo['id'])
        )

        return images
    
    def messageAnalysis(self, message):
        """Analyzes messages and return response.
        
        If your response has line breaks, then use double quotes for this."""

        response = None
        for plugin in self.plugins:
            response = plugin(message)
            if response != None:
                return response

    def addPlugin(self, plugin):
        """Add only one plugin in plugins list."""

        self.plugins.append(plugin)
    
    def addPlugins(self, plugins):
        """Add plugins in plugins list."""

        for plugin in plugins:
            self.addPlugin(plugin)