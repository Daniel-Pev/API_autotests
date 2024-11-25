import requests

from common.conf import Cfg
from endpoints.base_class import BaseClass


class PostAuth(BaseClass):
    token = None

    def post_auth(self, payload=Cfg.AUTHORIZE):
        self.response = requests.post(url=f'{Cfg.URL}/auth/authorize', json=payload)
        self.response_json = self.response.json()
        self.token = self.response_json['token']

    def check_token(self):
        self.post_auth()
        assert self.token is not None, 'Unexpected response token'
