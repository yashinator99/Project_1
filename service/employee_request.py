from models.employee_request_dto import Request
from repository.employee_request_dao import delete_employee_request, get_employee_request, insert_employee_request


def validate_employee_request_service(input):
    request_dto = Request(0, input.get("request_description"), input.get("request_amount"))
    return request_dto.validate_request()

def create_request(user_id, input):
    return insert_employee_request(user_id, input.get("request_description"), input.get("request_amount"))

def get_view_request(user_id):
    return get_employee_request(user_id)

def delete_request(user_id):
    return delete_employee_request(user_id)