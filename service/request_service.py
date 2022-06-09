from models.request_dto import Request
from repository.login_dao import insert_user, get_user_id
from repository.user_info_dao import insert_user_info
from repository.request_dao import *
# To register
# Valid Username and Password
# Valid first name and last name

def validate_request_service(input):
    request_dto = Request(0, input.get("request_desc"), input.get("request_amount"), "pending")
    return request_dto.validate_employee_request()

def create_request(user_id, input):
    return insert_user_request(user_id, input.get("request_desc"), int(input.get("request_amount")))

def get_view_request(user_id):
    return get_request(user_id)

def update_status(request_id, status):
    return update_request(request_id, status)