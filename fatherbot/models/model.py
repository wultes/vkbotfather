import datetime
import random

from fatherbot.models.settings import SettingsBot


class Model(SettingsBot):

    def startListen(self):
        """Listens to messages and sends their responses to analyzes"""
        try:
            print('| Server is running\n| {0}'.format(datetime.datetime.now()))
            for event in self.vk_api.listenServer():
                if self.vk_api.isNewMessage(event):
                    self.giveResponse(event['object']['message']['text'], event['object']['message']['peer_id'])

        except KeyboardInterrupt:
            print('| Server shutdown\n| {0}'.format(datetime.datetime.now()))

    def giveResponse(self, event_text, event_user_id):
        """Takes a response and analyzes it. 
        This function processes requests from only one user. 
        You can change the response processing parameters."""

        print('| {2} :Bot got a message "{0}" <- @{1}'.format(event_text, event_user_id, datetime.datetime.now())) 
        
        response = self.messageAnalysis(event_text)
        if '.png' in response:
            self.sendImage(response, event_user_id)
        else:
            self.sendMessage(response, event_user_id)

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
            path = image,
            random_id = random.randint(1, 10 ** 8)
        )

        print('| {2} :Bot send a image "{0}" -> @{1}'.format(image, user_id, datetime.datetime.now()))
    
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