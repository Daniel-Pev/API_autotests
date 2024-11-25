import requests

from common.conf import Cfg
from endpoints.base_class import BaseClass


class GetAuth(BaseClass):

    def get_auth(self):
        self.response = (
            requests.get(url=f'{Cfg.URL}/auth/me',
                         headers={"x-token": Cfg.TOKEN}))
        self.response_json = self.response.json()

    def check_empty_token(self):
        self.response = requests.get(url=f'{Cfg.URL}/auth/me',
                                     headers=None)
        self.response_json = self.response.json()
        assert self.response_json['detail']['reason'] == 'Please use auth method for getting data for private method', \
            'Unexpected string in reason'
        assert self.response.status_code == 401, 'Unexpected statuscode'

    # def check_invalid_token(self):
    #     self.response = requests.get(url=f'{Cfg.URL}/auth/me',
    #                                  headers={"x-token": Cfg.INVALID_TOKEN})
    #     print(self.response_json)
    #     assert self.response_json['detail']['reason'] == 'Token is incorrect. Please login and try again', \
    #         'Unexpected string in reason'
    #     assert self.response.status_code == 403, 'Unexpected statuscode'


user = GetAuth()
user.get_auth()
user.check_empty_token()

