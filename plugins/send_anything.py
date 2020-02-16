from utils.config_tool import get_config
import random

class AnythingBot:

    @staticmethod
    def get_anything():

        config = get_config()

        random_message = config['random_message'][random.randint(0, len(config['random_message'])-1)]

        return random_message