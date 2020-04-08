import toml

def get_config(path_config):

    config = {}

    with open(path_config, 'r', encoding='utf-8') as config_file:
        for line in config_file:
            if line not in config:
                for key, value in toml.load(config_file).items():
                    config[key] = value

    return config