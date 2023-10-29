from typing import List

from settings.connection import DBConnectionHandler
from src.core.user.service.user_repository import UserRepository


class SlalchemyUserRepository(UserRepository):

    def __init__(self):
        self.database = DBConnectionHandler()
    
    def registry(self, entity: User) -> User:
        pass

    def get_all(self, entity: User) -> List[User]:
        pass