[Русский](https://github.com/wultes/vkbotfather/blob/master/README.md) | [English](https://github.com/wultes/vkbotfather/blob/master/README_ENG.md)

# vkbotfather

This project makes it easier to create VK bots. 🤖

![made-with-python](https://img.shields.io/badge/Made%20with%20-Python-blue)
![version](https://img.shields.io/pypi/v/vkbotfather?color=blue)
![license](https://img.shields.io/github/license/wultes/vkbotfather)
![downloads](https://img.shields.io/pypi/dw/vkbotfather)

### 💿 Install

1. Install Python version no lower than 3.6. When installing, be sure to checkmark **Add Python 3.8 to PATH**. If you have Python installed, then check its operation through the command line.

   ```bash
   python -h
   ```

   If you get an error:

   ```bash
   python -h
   
   "python" is not recognized as an internal or external command operable program or batch file.
   ```

   **Then you need to add Python to your PATH.** To do this, do the following:

   - Open the "Properties" of your PC.
   - In the window that opens, go to "Advanced system settings".
   - Click on "Environment Variables".
   - Find the "Path" (or something similar) and click, then click on "Change."
   - Click on "Add" and insert the path to the folder where Python is located.
   - Repeat the previous paragraph, but add the path to Python \ Scripts.

   **Now Python is installed and configured on your PC.**

2. [Download](https://github.com/wultes/vkbotfather/archive/master.zip) this repository and unzip it to any place convenient for you.

   Or you can clone.

   ```bash
   git clone https://github.com/wultes/vkbotfather
   ```

   Also, you can use ```pip```.

   ```bash
   pip install vkbotfather
   ```

3. Open command line and write this command:

   ```bash
   pip install -r requirements.txt --upgrade
   ```

    


### 💻 Getting Community Token

In order to get a token, you need to go to the settings of the community that you created or in which you are an admin:

- Go to "Settings" -> "API Usage".
  - Enable Long Poll in the tab "Long Poll API" and set the version **not lower than 5.80**.
  - In the tab "Event types" select what you need.
- Go to "Access tokens" and click on "Create token".



### 🚀 Usage

Before starting the bot, you need to make sure that you can even send messages to your community. To do this, go to "Manage" -> "Messages". The line "Community messages" should be "Enable".

To add a bot to the conversation, do the following:

- Go to your community.
- Go to "Manage" -> "Messages" -> "Bot settings".
- Enable the bot features and check the "Ability to add this community to chats" box.
- Go back to the community and you will see a menu where it says "Add to chat".

After that, you can write a bot in PM or mention it in a conversation.

*If after that the bot did not answer, then look at the logs on the command line.*

### 👾 Example bot and plugins

You can see an example of a bot by going to the `` example`` folder or by looking at the code below.

```python
from vkbotfather.fatherbot.bot import MakeBot

bot = MakeBot(config="/configs/config.toml") #or bot = MakeBot(token="", group_id="")
bot.model.addPlugins([])

bot.startBot() 
```

Example of plugins and creating it you can see in [Wiki](https://github.com/wultes/vkbotfather/wiki).

All pre-installed plugins are dynamic type. You can see the necessary parameters in the Wiki.

Add plugins using the function ```addPlugins```

```python
from vkbotfather.fatherbot.bot import MakeBot
from vkbotfather.plugins.groups.allmember import GetAllMember

bot = MakeBot(config="/configs/config.toml")

getallmember = GetAllMember(token='', group_id='') #Init dinamic plugin

bot.model.addPlugins([
    getallmember.get_allmember,
])

bot.model.imageTypes([ #Determine which image format the bot can process.
   'jpg',
   'png'
])

 bot.model.documentTypes([ #Determine which document format the bot can process.
   'txt',
   'pdf',
   'doc'
])
 

bot.startBot() 
```

Now your plugin is installed and ready to use. You can run the bot. 

### 📃 License

This module is licensed. [MIT](https://choosealicense.com/licenses/mit/).  
Copyright © 2020 [Wultes](https://github.com/wultes/).

### ✉️ Communication

If you have questions about the module, you can always contact me through [Telegram](https://t.me/wultes).
