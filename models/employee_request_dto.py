# remove



# class Request:
#     def __init__(self, user_id, request_description, request_amount):
#         self.user_id = user_id
#         self.request_description = request_description
#         self.request_amount = request_amount


#     def __repr__(self):
#         return f"{self.user_id}, {self.request_description}, {self.request_amount}"

#     def validate_employee_request(self) -> bool:
#         if len(self.request_description)  > 100:
#             return False
#         elif len(self.request_amount) >= 1 or len(self.request) <= 1000:
#             return False
#         else:
#             return True