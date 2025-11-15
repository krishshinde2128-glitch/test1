# ...existing code...
import hashlib
from typing import Dict

class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.__password = self._hash(password)  # private attribute

    def _hash(self, pwd: str) -> str:
        return hashlib.sha256(pwd.encode('utf-8')).hexdigest()

    def verify_password(self, password: str) -> bool:
        return self.__password == self._hash(password)

    def set_password(self, old_password: str, new_password: str) -> bool:
        if self.verify_password(old_password):
            self.__password = self._hash(new_password)
            return True
        return False


class LoginManager:
    def __init__(self):
        self._users: Dict[str, User] = {}

    def register(self, username: str, password: str) -> bool:
        if username in self._users:
            return False
        self._users[username] = User(username, password)
        return True

    def login(self, username: str, password: str) -> bool:
        user = self._users.get(username)
        return bool(user and user.verify_password(password))

# simple CLI for manual testing
if __name__ == "__main__":
    lm = LoginManager()
    while True:
        cmd = input().strip().lower()
        if cmd == "exit":
            break
        if cmd == "register":
            u = input().strip()
            p = input().strip()
            print("registered" if lm.register(u, p) else "username exists")
        elif cmd == "login":
            u = input().strip()
            p = input().strip()
            print("success" if lm.login(u, p) else "failed")
#