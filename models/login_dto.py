class Login:
    def __init__(self, user_id, username, password, role):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self) -> str:
        return f"User Login : id - {self.user_id} username - {self.username} password - {self.password} role - {self.role}"

    def validate_login(self) -> bool:
        if len(self.username) < 5 or len(self.password) < 5:
            return False
        elif len(self.username) > 30 or len(self.password) > 30:
            return False
        else:
            return True
