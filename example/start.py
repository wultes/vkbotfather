from bot.bot import MakeBot
from plugins import * 

bot = MakeBot(token='', group_id='') #or bot = MakeBot(config="")
bot.model.addPlugins([
    about.About.get_about,
    about.About.get_info,
    about.About.get_icon,
    about.About.get_document,
])

bot.model.imageTypes([
	'jpg',
	'png'
])

bot.model.documentTypes([
	'txt',
	'pdf',
	'doc'
])

bot.startBot() 