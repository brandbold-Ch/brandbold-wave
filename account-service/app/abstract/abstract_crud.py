from abc import abstractmethod, ABC
from typing import TypeVar, Any, Optional
from sqlmodel import SQLModel, Session
from app.utils.wrappers import ListWrapper

T = TypeVar("T", bound=SQLModel)


class AbstractCrud(ABC):

    @abstractmethod
    def create(
            self,
            model: T,
            session: Session,
            auto_commit: bool = True
    ) -> T:
        pass

    @abstractmethod
    def update(
            self,
            _id: Any,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> Optional[T]:
        pass

    @abstractmethod
    def select(
            self,
            session: Session,
            auto_commit: bool = True
    ) -> ListWrapper:
        pass

    @abstractmethod
    def get(
            self,
            _id: Any,
            session: Session,
            auto_commit: bool = True
    ) -> Optional[T]:
        pass

    @abstractmethod
    def delete(
            self,
            _id: Any,
            session: Session,
            auto_commit: bool = True
    ) -> Optional[T]:
        pass
