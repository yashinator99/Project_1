from models.login_dto import Login
from repository.login_dao import get_user_role, select_user,select_user_role, get_user_role


def check_login(login_input):
    user_dto = select_user(login_input.get("username"),login_input.get("password"))
    print(login_input)
    if user_dto is not None:
        return user_dto
    else:
        return None

def check_login_role(login_input, role):
    user_dto = select_user_role(login_input.get("username"),login_input.get("password"), role)
    print(login_input)
    if user_dto is not None:
        return user_dto
    else:
        return None

