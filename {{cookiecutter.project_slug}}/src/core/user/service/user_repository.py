from abc import abstractmethod
from typing import Protocol, runtime_checkable

from src.core.shared.repository import Repository


@runtime_checkable
class UserRepository(Repository, Protocol):
    
    @abstractmethod
    def registry(self, entity: User) -> User:
        """_summary_
        """

    @abstractmethod
    def get_all(self, entity: User) -> List[User]:
        """_summary_
        """
