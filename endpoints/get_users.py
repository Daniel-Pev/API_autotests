import requests

from endpoints.base_class import BaseClass
from common.conf import Cfg


class GetUsers(BaseClass):
    default_params = {"limit": 3, "offset": 0}

    def get_users(self, params=None):
        if params is None:
            params = self.default_params
        self.response = (
            requests.get(url=f'{Cfg.URL}/users',
                         params=params))
        self.response_json = self.response.json()

    def check_def_params(self):
        self.get_users()
        assert isinstance(self.response_json["meta"]["total"], int), 'Unexpected meta type'
        for user_data in self.response_json["data"]:
            assert isinstance(user_data["last_name"], str), 'Unexpected last_name type'
            assert isinstance(user_data["user_id"], int), 'Unexpected user_id type'
        assert len(self.response_json["data"]) == 3, 'Unexpected users count'

    def neg_params(self):
        self.get_users(params={})

