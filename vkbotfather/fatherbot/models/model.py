import datetime
import random

from vkbotfather.fatherbot.models.settings import SettingsBot


class Model(SettingsBot):

    def startListen(self):
        """Listens to messages and sends their responses to analyzes"""
        try:
            print('| Server is running\n| For shutdown server press Ctrl + C\n| {0}'.format(datetime.datetime.now()))
            for event in self.vk_api.listenServer():
                if self.vk_api.isNewMessage(event):
                    if self.vk_api.isMessageFromChat(event):
                        self.giveResponse(event['object'], 'chat')
                    elif self.vk_api.isMessageFromUser(event):
                        self.giveResponse(event['object'], 'user')


        except KeyboardInterrupt:
            print('| Server shutdown\n| {0}'.format(datetime.datetime.now()))

    def giveResponse(self, obj, type_message):
        """Takes a response and analyzes it. 
        This function processes requests from only one user. 
        You can change the response processing parameters."""

        print('| {2} :Bot got a message "{0}" <- @{1}'.format(obj['message']['text'], obj['message']['peer_id'], datetime.datetime.now()))
        response = self.messageAnalysis(obj)
        if response is None:
            pass
        else: 
            if len(response) > 3 and response[-3:] in self.image_types:
                self.sendImage(response, obj['message']['peer_id'])
            if len(response) > 3 and response[-3:] in self.document_types:
                self.sendDocument(response, obj['message']['peer_id'])
            else:
                self.sendMessage(response, obj['message']['peer_id'])

    def sendMessage(self, msg, user_id):
        """Sends a text message to the user."""
        self.vk_api.sendMessage(
            peer_id=user_id,
            message=msg,
            random_id=random.randint(1, 10 ** 8)
        )

        print('| {2} :Bot send a message "{0}" -> @{1}'.format(msg, user_id, datetime.datetime.now()))

    def sendImage(self, image, user_id): #Work only one sendImage
        """Sends a image to the user."""
        self.vk_api.sendImage(
            peer_id=user_id, 
            path=image,
            random_id=random.randint(1, 10 ** 8)
        )

        print('| {2} :Bot send a image "{0}" -> @{1}'.format(image, user_id, datetime.datetime.now()))

    def sendDocument(self, document, user_id):
        """Sends a document to the user"""
        self.vk_api.sendDocument(
            peer_id=user_id,
            path=document,
            random_id=random.randint(1, 10 ** 8)
        )

        print('| {2} :Bot send a document "{0}" -> @{1}'.format(document, user_id, datetime.datetime.now()))
    
    def messageAnalysis(self, obj):
        """Analyzes messages and return response.
        
        If your response has line breaks, then use double quotes for this."""

        response = None
        for plugin in self.plugins:
            response = plugin(obj['message']['text'], obj)
            if response != None:
                return response
        if response == None:
            print('Yours plugins not have a return message/image/document')

    def addPlugin(self, plugin):
        """Add only one plugin in plugins list."""

        self.plugins.append(plugin)
    
    def addPlugins(self, plugins):
        """Add plugins in plugins list."""

        for plugin in plugins:
            self.addPlugin(plugin)

    def imageTypes(self, types):
        """Add new format images"""

        for typ in types:
            self.image_types.append(typ)

    def documentTypes(self, types):
        """Add new format document"""

        for typ in types:
            self.document_types.append(typ)
