class Request:
    def __init__(self, user_id, request_desc, request_amount, status):
        self.user_id = user_id
        self.request_desc = request_desc
        self.request_amount = request_amount
        self.status = status

    def __repr__(self) -> str:
        return f"User Request : id - {self.user_id} request title - {self.request_desc} request - {self.request_amount} status - {self.status}"

    def validate_employee_request(self) -> bool:
        if len(self.request_desc)  > 100:
            return False
        elif len(self.request_amount) < 1 or len(self.request_amount) > 1000:
            return False
        else:
            return True
