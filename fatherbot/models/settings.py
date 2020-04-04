import toml
import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api import VkUpload

from plugins import *
from utils.config_tool import get_config

class SettingsBot:
    """It contains all the bot settings."""
    def __init__(self, token=None, group_id=None, config=None):

        if token == None and group_id == None:
            self.config = get_config(config)
            self.token = self.config['token']
            self.group_id = self.config['group_id']
        else:
            self.token = token
            self.group_id = group_id

        self.session = vk_api.VkApi(token=self.token)
        self.long_poll = VkBotLongPoll(self.session, self.group_id)
        self.vk = self.session.get_api()
        self.vk_upload = VkUpload(self.session)

        self.plugins = []