import datetime
from src.core.shared.entity import Entity


class User(Entity):

    def __init__(self,
                 id_        : int = None,
                 created_at : datetime.date = None,
                 name       : str = None,
                 age        : int = None,
                 username   : str = None,
                 password   : str = None):
        
        self.id         = id_
        self.created_at = created_at
        self.name       = name
        self.age        = age
        self.username   = username
        self.password   = password

    def validate_data(self):
        return super().validate_data()

    def __repr__(self) -> str:
        return ('User('
            f'id_={self.id}, '
            f'created_at={self.created_at}, '
            f'name={self.name}, '
            f'age={self.age}, '
            f'username={self.username}, '
            f'password={self.password}'
            ')'
        )