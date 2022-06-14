import re

# working impln
def validate_login(new_login: tuple) -> bool:
    return validate_username(new_login[0]) and validate_password(new_login[1]) and validate_role(new_login[3])


def validate_username(username):
    if re.findall('[A-Za-z]{3,7}', username) and len(username) <=7 and not " " in username:
       return True
    else:
        return False


def validate_password(password):
    if re.findall('[A-Za-z]{6,15}', password) and len(password) <=15 and not " " in password:
       return True
    else:
        return False

def validate_role(role):
    if role == "manager" or role == "employee":
       return True
    else:
        return False

def validate_request_desc(request_desc) -> bool:
        if len(request_desc) <= 100:
            return True
        else:
            return False

def validate_request_amount(request_amount):
    request_amount = str(request_amount)
    if(re.findall('^[0-9]+$',request_amount)):
        if int(request_amount) < 1 or int(request_amount) > 1000:
            return False
        else:
            return True
    else:
        return False