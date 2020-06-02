import requests

class VKAPI:
    def __init__(self, token, group_id):
        self.token = token
        self.group_id = group_id
        self.api_link = 'https://api.vk.com/method/{method}'

    def call(self, method, **kwargs):
        """Call method from VK API"""
        params = {}
        params.update(**kwargs)
        params['v'] = '5.103'
        api_url = self.api_link.format(method=method)
        response = requests.get(api_url, params=params).json()

        return response

# Utils
    def openFile(self, path):
        file = open(path, 'rb')
        
        return file


# LongPoll 
    def updateLongpoll(self):
        api_url = 'https://api.vk.com/method/groups.getLongPollServer?access_token={0}&group_id={1}&v=5.103'.format(self.token, self.group_id)
        response = requests.get(api_url).json()

        server_url = response['response']['server']
        key = response['response']['key']
        ts = response['response']['ts']

        return server_url, key, ts

    def checkLongpoll(self):
        """Check LongPoll server on new updates"""
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

# UploadServer 
    def uploadImage(self, peer_id, path):
        """Upload and save images ONLY for message
        
        peer_id - user id to whom the image is sent
        path - path of image file

        """
        upload_server = self.call('photos.getMessagesUploadServer', peer_id=peer_id, access_token=self.token)

        image = self.openFile(path)

        post_url = upload_server['response']['upload_url']
        post_response = requests.post(post_url, files=dict(file=image)).json()
        server, photo, vk_hash = post_response['server'], post_response['photo'], post_response['hash']

        save_response = self.call('photos.saveMessagesPhoto', photo=photo, server=server, hash=vk_hash, access_token=self.token)
        upload_image = 'photo{0}_{1}'.format(save_response['response'][0]['owner_id'], save_response['response'][0]['id'])

        return upload_image

    def uploadDocument(self, peer_id, path):
        """Upload and save documents ONLY for message 
        
        peer_id - user id to whom the image is sent
        path - path of image file
        
        """
        upload_server = self.call('docs.getMessagesUploadServer', type='doc', peer_id=peer_id, access_token=self.token)

        document = self.openFile(path)

        post_url = upload_server['response']['upload_url']
        post_response = requests.post(post_url, files=dict(file=document)).json()
        document = post_response['file']

        save_response = self.call('docs.save', file=document, access_token=self.token)
        upload_document = 'doc{0}_{1}'.format(save_response['response']['doc']['owner_id'], save_response['response']['doc']['id'])
      
        return upload_document

# Messages
    def sendImage(self, peer_id, path, random_id):
        """Send Image ONLY for message
        
        peer_id - user id to whom the image is sent
        path - path of image file
        random_id - random integer number, but use a random.randint(1, 10 ** 8)

        """
        photo = self.uploadImage(peer_id, path)
        response_send = self.call('messages.send', attachment=photo, peer_id=peer_id, access_token=self.token, random_id=random_id)

        return response_send  
    
    def sendDocument(self, peer_id, path, random_id):
        """Send Document ONLY for message
        
        peer_id - user id to whom the image is sent
        path - path of image file
        random_id - random integer number, but use a random.randint(1, 10 ** 8)
        
        """

        document = self.uploadDocument(peer_id, path)
        response_send = self.call('messages.send', attachment=document, peer_id=peer_id, access_token=self.token, random_id=random_id)

        return response_send
    
    def sendMessage(self, message, peer_id, random_id):
        """Send message
        
        peer_id - user id to whom the image is sent
        random_id - random integer number, but use a random.randint(1, 10 ** 8)
        
        """
        response = self.call('messages.send', peer_id=peer_id, message=message, random_id=random_id, access_token=self.token)

        return response

# Type message
    def isNewMessage(self, event):
        """Check message type
        
        event - variable that save updates from listenServer()

        """
        if event['type'] == 'message_new':
            return True
        return False

    def isMessageFromChat(self, event):
        """Check from message

        event - variable that save updates from listenServer()

        """
        if '200000000' in str(event['object']['message']['peer_id']):
            return True
        return False

    def isMessageFromUser(self, event):
        """Check from message

        event - variable that save updates from listenServer()

        """
        if not '200000000' in str(event['object']['message']['peer_id']):
            return True
        return False
