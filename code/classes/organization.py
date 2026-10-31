from config import SALT
from hashlib import sha256


class Organization:
    def __init__(self, id: int, organization_name: str, color: tuple[int, int, int], password: str) -> None:
        self.id = id
        self.organization_name = organization_name
        self.events = []
        self.color = color
        self.password = self.hash_password(password)


    def add_event(self, event) -> None:
        self.events += [event]


    def get_attributes(self) -> dict:
        return {
            "id": self.id,
            "organization_name": self.organization_name, 
            "color": self.color,
            "password": self.password
        }


    @staticmethod
    def hash_password(password: str) -> str:
        return sha256((SALT + password).encode("utf-8")).hexdigest()


    def check_password(self, password: str) -> bool:
        return self.hash_password(password) == self.password
