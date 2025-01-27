from endpoints.get_auth import GetAuth
from endpoints.get_comp import GetComp
from endpoints.get_users import GetUsers
from endpoints.post_auth import PostAuth
from endpoints.post_user import PostUser


def test_get_comp():
    comp = GetComp()
    comp.get_comp()
    comp.check_status_code()
    comp.check_comp_status()


def test_get_users():
    user = GetUsers()
    user.get_users()
    user.check_status_code()
    user.check_def_params()


def test_post_user():
    user = PostUser()
    user.post_user()
    user.check_status_code(201)
    user.check_name()


def test_post_auth():
    auth = PostAuth()
    auth.post_auth()
    auth.check_status_code(200)
    auth.check_token()


def test_get_auth():
    auth = GetAuth()
    auth.get_auth()
    auth.check_status_code(200)
    auth.check_empty_token()
    auth.check_invalid_token()
