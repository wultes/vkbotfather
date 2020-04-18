
class About:

    @staticmethod
    def get_about(msg):
        if '/help' in msg:
            return 'Данный бот создан при помощи фреймворка VkBotFather'
    
    @staticmethod
    def get_info(msg):
        if '/info about' in msg:
            return "Плагин - 'Об Боте'\nДанный бот был создан с помощью VkBotFather"
    
    @staticmethod
    def get_icon(msg):
        if '/get image' in msg:
            return '/example/icon.png'

    @staticmethod
    def get_document(msg):
        if '/get document' in msg:
            return 'Здесь должен быть ваш документ'