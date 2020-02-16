from utils.config_tool import get_config
import random

class HeadsAndTailsBot:

    @staticmethod
    def get_heads_and_tails():
        random_coin = random.randint(1, 101)
        config = get_config()

        if random_coin in range(1, 50):
            return config['heads_and_tails'][0]
        elif random_coin in range(51, 101):
            return config['heads_and_tails'][1]
