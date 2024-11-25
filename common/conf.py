import requests

from endpoints.post_auth import PostAuth


class Cfg:
    URL = 'https://restapi.tech/api'
    BODY = {
        "first_name": "string",  # Enter valid name
        "last_name": "string",  # Enter valid last_name
        "company_id": 1  # Enter valid company_id
    }
    AUTHORIZE = {
        "login": "string",  # Enter valid name
        "password": "qwerty12345",  # Password mustn't be changed
        "timeout": 360  # Enter valid token timeout
    }

    response = requests.post(url=f'{URL}/auth/authorize', json=AUTHORIZE)
    response_json = response.json()
    TOKEN = response_json['token'] # Enter valid token
    INVALID_TOKEN = 'rrqwdqwdq'  # Enter invalid token
