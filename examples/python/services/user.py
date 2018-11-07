import requests


class UserService:

    def __init__(self):
        self.url = 'http://api/users'

    def list(self):
        r = requests.get(self.url)
        return r.json()

    def list_by_id(self, id):
        r = requests.get('%s/%d' % (self.url, id))
        return r.json()

    def create(self, **kwargs):
        r = requests.post(self.url, kwargs)
        id = r.json()['id']
        return id

    def update(self, id, **kwargs):
        r = requests.put('%s/%d' % (self.url, id), kwargs)
        return r.json()

    def delete(self, id):
        r = requests.delete('%s/%d' % (self.url, id))
        return r.json()
