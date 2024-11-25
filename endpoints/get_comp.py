import requests
from endpoints.base_class import BaseClass
from common.conf import Cfg


class GetComp(BaseClass):
    default_params = {"status": None, "limit": 3, "offset": 0}

    def get_comp(self, params=None):
        if params is None:
            params = self.default_params
        self.response = (
            requests.get(url=f'{Cfg.URL}/companies',
                         params=params))
        self.response_json = self.response.json()

    def check_comp_status(self):
        statuses = ["ACTIVE", "CLOSED", "BANKRUPT"]
        for status in statuses:
            self.get_comp(params={'status': status})
            assert all(i['company_status'] == status for i in self.response_json["data"]), 'Unexpected company status'
