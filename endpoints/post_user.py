import requests

from common.conf import Cfg
from endpoints.base_class import BaseClass


class PostUser(BaseClass):
    def post_user(self, payload=Cfg.BODY):
        self.response = requests.post(url=f'{Cfg.URL}/users', json=payload)
        self.response_json = self.response.json()

    def check_name(self):
        self.post_user()
        self.response_json.pop('user_id')
        assert self.response_json == Cfg.BODY, 'Incorrect response body'
