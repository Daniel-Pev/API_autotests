import requests

from common.conf import Cfg
from endpoints.base_class import BaseClass


class DelUser(BaseClass):
    def del_user(self, id):
        self.response = requests.delete(url=f'{Cfg.URL}/users/{id}')
        self.response_json = self.response.json()

# negative_tests

    def wrong_id(self, id):
        self.del_user(id)
        assert self.response.status_code == 404, 'Wrong respond statuscode'


