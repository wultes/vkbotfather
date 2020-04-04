from bot.bot import MakeBot
from plugins import * 

bot = MakeBot(config="/configs/config.toml")
bot.model.addPlugins([
    about.About.get_about,
    about.About.get_info,
])

bot.startBot() 
