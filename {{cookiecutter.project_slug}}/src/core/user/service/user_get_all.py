from src.core import usecase_map
from src.core.shared import UseCase
from src.core.shared.application import Result
from src.core.user import User

from .user_repository import UserRepository


@usecase_map('/user')
@usecase_map('/user/get_all')
class UserGetAll(UseCase):

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, entity: User) -> Result:
        result = Result()

        if not isinstance(entity, User):
            result.msg = f'{entity.__class__.__name__} is not a User Entity.'

        if result.qty_msg() > 0:
            result.entities = entity
            return result
        
        try:
            user_list = self.repository.get_all(entity)

            user_list = [u for u in user_list if u.status != 'removed']
            
            if len(user_list) > 0:
                result.entities = user_list
            else:
                result.entities = user_list
                result.msg = 'There are no users in database.'

            return result
        except Exception as error:
            result.msg = str(error)
            result.entities = entity
            return result




