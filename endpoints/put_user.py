import requests

from common.conf import Cfg
from endpoints.base_class import BaseClass


class PutUser(BaseClass):
    def put_user(self, id, payload):
        self.response = requests.post(url=f'{Cfg.URL}/users/{id}', json=payload)
        self.response_json = self.response.json()



