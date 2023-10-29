from src.core import usecase_map
from src.core.shared.application import Result
from src.core.shared.usecase import UseCase
from user_repository import UserRepository


@usecase_map('/user/registry')
class UserRegistry(UseCase):

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, entity: User) -> Result:
        result = Result()
        ###################################
        # Implementation here
        ###################################
        return result




