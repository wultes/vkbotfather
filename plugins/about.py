from utils.config_tool import get_config


class AboutBot:
    
    @staticmethod
    def get_about():

        config = get_config()

        return config['help_message']
