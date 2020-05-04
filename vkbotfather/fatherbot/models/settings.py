import toml

from vkbotfather.utils.config_tool import get_config
from vkbotfather.fatherbot.models.vkapi import VKAPI

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
        
        self.vk_api = VKAPI(token=self.token, group_id=self.group_id)

        self.plugins = []

        self.image_types = []

        self.document_types = []