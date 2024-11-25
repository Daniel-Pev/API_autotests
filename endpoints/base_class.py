class BaseClass:
    response = None
    response_json = None

    def check_status_code(self, statuscode=200):
        assert self.response.status_code == statuscode, "Unexpected response status code"

    def check_user_id(self, user_id):
        assert self.response_json["user_id"] == id, 'Incorrect id in response'
