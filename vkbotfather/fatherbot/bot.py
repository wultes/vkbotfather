from vkbotfather.fatherbot.models.settings import SettingsBot
from vkbotfather.fatherbot.models.model import Model

from vkbotfather.utils.config_tool import get_config

class MakeBot(SettingsBot):
    def __init__(self, token=None, group_id=None, config=None):      
        SettingsBot.__init__(self, token, group_id, config)
        self.model = Model(token, group_id, config)
    
    def startBot(self):
        self.model.startListen()
    