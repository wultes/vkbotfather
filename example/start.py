from bot.bot import MakeBot
from plugins import * 

bot = MakeBot(config="C:/wultes/Projects/Python/vkbotfather-dev/configs/config.toml") #or bot = MakeBot(config="")
bot.model.addPlugins([
    about.About.get_about,
    about.About.get_info,
])

bot.startBot() 