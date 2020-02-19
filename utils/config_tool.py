import toml

CONFIG_COMMAND = ['token']

def get_config():

    config = {}

    with open('VkBot/config.toml', 'r', encoding='utf-8') as config_file:
        for line in CONFIG_COMMAND:
            if line not in config:
                for key, value in toml.load(config_file).items():
                    config[key] = value
    
    return config
