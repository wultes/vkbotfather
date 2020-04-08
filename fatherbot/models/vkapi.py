import requests

class VKAPI:
    def __init__(self, token, group_id):
        self.token = token
        self.group_id = group_id

    def updateLongpoll(self):
        api_url = 'https://api.vk.com/method/groups.getLongPollServer?access_token={0}&group_id={1}&v=5.102'.format(self.token, self.group_id)
        response = requests.get(api_url).json()

        server_url = response['response']['server']
        key = response['response']['key']
        ts = response['response']['ts']

        return server_url, key, ts

    def checkLongpoll(self):
        server_url, key, ts = self.updateLongpoll()
        longoll_url = '{0}?act=a_check&key={1}&wait=25&mode=2&ts={2}'.format(server_url, key, ts)
        longoll_get = requests.get(longoll_url).json()
        ts = longoll_get['ts']
        updates = longoll_get['updates']

        return updates

    def listenServer(self):
        while True:
            for event in self.checkLongpoll():
                yield event

    def openFile(self, path):
        file = open(path, 'rb')
        
        return file


    def uploadImage(self, peer_id, path):
        server_url = 'https://api.vk.com/method/photos.getMessagesUploadServer?peer_id={0}&access_token={1}&v=5.103'.format(peer_id, self.token)
        upload_server = requests.get(server_url).json()

        image = self.openFile(path)

        post_url = upload_server['response']['upload_url']
        post_response = requests.post(post_url, files=dict(file=image)).json()
        server, photo, vk_hash = post_response['server'], post_response['photo'], post_response['hash']

        save_url = 'http://api.vk.com/method/photos.saveMessagesPhoto?photo={0}&server={1}&hash={2}&access_token={3}&v=5.103'.format(photo, server, vk_hash, self.token)
        save_response  = requests.get(save_url).json()
        upload_image = 'photo{0}_{1}'.format(save_response['response'][0]['owner_id'], save_response['response'][0]['id'])

        return upload_image
    
    def sendImage(self, peer_id, path, random_id):
        photo = self.uploadImage(peer_id, path)
        url_send = 'https://api.vk.com/method/messages.send?attachment={0}&peer_id={1}&access_token={2}&random_id={3}&v=5.103'.format(photo, peer_id, self.token, random_id)
        response_send = requests.get(url_send).json()
        print(response_send)

    
    def sendMessage(self, message, peer_id, random_id):
        url_send = 'https://api.vk.com/method/messages.send?message={0}&peer_id={1}&access_token={2}&random_id={3}&v=5.103'.format(message, peer_id, self.token, random_id)
        response_send = requests.get(url_send).json()

    def isNewMessage(self, event):
        if event['type'] == 'message_new':
            return True
        else:
            return False