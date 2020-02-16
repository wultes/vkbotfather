import toml
import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll
from vk_api import VkUpload

from plugins import *
from utils.config_tool import get_config

class SettingsBot:
    def __init__(self):

        self.config = get_config()

        self._token = self.config['token']
        self.session = vk_api.VkApi(token=self._token)
        self.long_poll = VkLongPoll(self.session)
        self.vk = self.session.get_api()
        self.vk_upload = VkUpload(self.session)

        self.plugins = (
            about.AboutBot(), #0
            send_anything.AnythingBot(), #1
            heads_and_tails.HeadsAndTailsBot(), #2
            meme_generate.MemeGenerateBot(), #3
        )