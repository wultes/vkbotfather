[Русский](https://github.com/wultes/vkbotfather/blob/master/README.md) | [English](https://github.com/wultes/vkbotfather/blob/master/README_ENG.md)

# vkbotfather

Данный проект позволяет облегчить создание ботов ВК. 🤖

![made-with-python](https://img.shields.io/badge/Made%20with%20-Python-blue)
![version](https://img.shields.io/pypi/v/vkbotfather?color=blue)
![license](https://img.shields.io/github/license/wultes/vkbotfather)
![dowloands](https://img.shields.io/pypi/dw/vkbotfather)

### 💿 Установка

1. Установите Python версии не ниже 3.6. При установке убедитесь, что поставили галочку в пункте **Add Python 3.8 to PATH**. Если у вас установлен Python, то проверьте его работу через командную строку.

   ```bash
   python -h
   ```

   Если у вас выводит ошибку:

   ```bash
   python -h
   
   "python" не является внутренней или внешней командой, исполняемой программой или пакетом файлов.
   ```

   **То нужно добавить Python в PATH.** Для этого стоит сделать следующие:

   - Открыть свойства своего ПК.
   - В открывшейся окне перейти в "Дополнительные параметры системы"
   - Нажать на "Переменные среды"
   - Найти Path (или что-то подобное) и нажать, после этого нажать на "Изменить".
   - Нажать на "Добавить" и вставить путь к папке, где находится Python.
   - Повторить предыдущий пункт, но добавить путь к Python\Scripts.  

   **Теперь Python установлен и настроен на вашем ПК.**

2. [Скачайте](https://github.com/wultes/vkbotfather/archive/master.zip) данный репозиторий и распакуйте в любое удобное для вас место.

   Или вы можете его клонировать.

   ```bash
   git clone https://github.com/wultes/vkbotfather
   ```
   
   Также, вы можете использовать ```pip```
   
   ```bash
   pip install vkbotfather
   ```

3. Откройте командную строку и введите следующую команду:

   ```bash
   pip install -r requirements.txt --upgrade
   ```

    


### 💻 Получение токена сообщества

Для того, чтобы получить токен нужно перейти в настройки сообщества, которое вы создали или в котором являетесь админом:

- Перейти в "Управление" -> "Работа с API".
  - Включить Long Poll во вкладке "Long Poll API" и выставить версию **не ниже 5.80**.
  - Во вкладке "Типы событий" выбрать то, что вам нужно. *(На данный момент, бот умеет получать и отправлять сообщения)*
- Перейти в "Ключи доступа" и нажать на "Получить ключ".



### 🚀 Использование

Перед запуском бота, нужно удостовериться в том, можно ли вообще отправлять сообщения в ваше сообщество. Для этого перейдите в "Управление" -> "Сообщения". В строке "Сообщения сообщества" должно быть "Включены". 

Для добавления бота в беседу нужно сделать следующее: 

- Зайти в ваше сообщество.
- Перейти в "Управление" -> "Сообщения" -> "Настройки для бота".
- Включить возможности бота и поставить галочку на "Разрешить добавлять сообщество в беседы".
- Перейти обратно в сообщество и у вас появится меню, где будет написано "Добавить в беседу".

После этого, вы можете написать боту в лс или упомянуть его в беседе.

*Если после этого бот ничего не ответил, то посмотрите логи в командной строке.*



### 👾 Примеры бота и плагинов.

Пример бота вы можете увидеть, посмотрев на код ниже.

```python
from vkbotfather.fatherbot.bot import MakeBot

bot = MakeBot(config="/configs/config.toml") #или bot = MakeBot(token="", group_id="")
bot.model.addPlugins([])

bot.startBot() 
```

Примеры плагинов и их создания, вы можете увидеть в [Wiki](https://github.com/wultes/vkbotfather/wiki).  

Все предустановленные плагины **имеют динамический тип**. Нужные параметры для их инициализации вы можете увидеть в Wiki.

Добавление плагинов происходит с помощью функции ```addPlugins```

```python
from vkbotfather.fatherbot.bot import MakeBot
from vkbotfather.plugins.groups.allmember import GetAllMember

bot = MakeBot(config="/configs/config.toml")

getallmember = GetAllMember(token='', group_id='') #Инициализация динамического плагина

bot.model.addPlugins([
    getallmember.get_allmember,
])

bot.model.imageTypes([ #Определяем какой формат изображения бот может обрабатывать 
     'jpg',
     'png'
])

 bot.model.documentTypes([ #Определяем какой формат документов бот может обрабатывать
     'txt',
     'pdf',
     'doc'
])
 
bot.startBot() 
```

Теперь ваш плагин установлен и готов к использованию. Можете запускать бота. 

### 📃 Лицензия

Данный репозиторий использует лицензию [MIT](https://choosealicense.com/licenses/mit/)  
Copyright © 2020 [Wultes](https://github.com/wultes/). 

### ✉️ Связь

Если у вас есть вопросы, то можете связаться со мной через [Telegram](https://t.me/wultes).
