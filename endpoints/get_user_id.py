import requests

from common.conf import Cfg
from endpoints.base_class import BaseClass


class GetUsers(BaseClass):

    def get_users(self, id):
        self.response = requests.get(url=f'{Cfg.URL}/users/{id}')
        self.response_json = self.response.json()
