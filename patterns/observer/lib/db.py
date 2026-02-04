from hashlib import blake2b

# user database mock
users: list[User] = []


class User:
    def __init__(self, name: str, password: str, email: str) -> None:
        self.name = name
        self.password = blake2b(password.encode()).hexdigest()
        self.email = email
        self.plan = "basic"
        self.reset_code = ""

    def __repr__(self) -> str:
        return f"NAME: {self.name}, EMAIL: {self.email}, PASSWD: {self.password}"

    def reset_password(self, code: str, new_password: str) -> None:
        if code != self.reset_code:
            msg = "Invalid password reset code."
            raise ValueError(msg)
        self.password = blake2b(new_password.encode()).hexdigest()


def create_user(name: str, password: str, email: str) -> User:
    new_user = User(name, password, email)
    users.append(new_user)
    return new_user


def find_user(email: str) -> User:
    if user := next((u for u in users if u.email == email), None):
        return user
    msg = f"User with email address {email} not found."
    raise LookupError(msg)
