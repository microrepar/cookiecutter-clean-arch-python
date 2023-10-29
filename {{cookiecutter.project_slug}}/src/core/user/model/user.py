from src.core.shared.entity import Entity


class User(Entity):

    def __init__(self, name: str, username: str, age: int):
        self.username = username
        self.name     = name
        self.age      = age
