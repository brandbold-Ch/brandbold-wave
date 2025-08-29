from abc import abstractmethod, ABC
from typing import TypeVar, Any, Optional
from sqlmodel import SQLModel, Session
from src.utils.wrappers import ListWrapper

T = TypeVar("T", bound=SQLModel)


class AbstractCrud(ABC):
    """
    Abstract base class for generic CRUD operations.
    Defines the interface for create, read, update, and delete methods for SQLModel models.
    """

    @abstractmethod
    def create(
        self,
        model: T,
        session: Session,
        auto_commit: bool = True
    ) -> T:
        """
        Create a new model instance in the database.
        Args:
            model (T): The model instance to add.
            session (Session): The database session.
            auto_commit (bool, optional): Whether to commit after adding. Defaults to True.
        Returns:
            T: The created model instance.
        """

    @abstractmethod
    def update(
        self,
        _id: Any,
        data: dict,
        session: Session,
        auto_commit: bool = True
    ) -> Optional[T]:
        """
        Update a model instance by its primary key.
        Args:
            _id (Any): The primary key value.
            data (dict): The data to update.
            session (Session): The database session.
            auto_commit (bool, optional): Whether to commit after updating. Defaults to True.
        Returns:
            Optional[T]: The updated model instance if found, else None.
        """

    @abstractmethod
    def select(
        self,
        session: Session
    ) -> ListWrapper:
        """
        Retrieve all records of the model from the database.
        Args:
            session (Session): The database session.
        Returns:
            ListWrapper: A wrapper containing all model instances.
        """

    @abstractmethod
    def get(
        self,
        _id: Any,
        session: Session
    ) -> Optional[T]:
        """
        Retrieve a single model instance by its primary key.
        Args:
            _id (Any): The primary key value.
            session (Session): The database session.
        Returns:
            Optional[T]: The model instance if found, else None.
        """

    @abstractmethod
    def delete(
        self,
        _id: Any,
        session: Session,
        auto_commit: bool = True
    ) -> Optional[T]:
        """
        Delete a model instance by its primary key.
        Args:
            _id (Any): The primary key value.
            session (Session): The database session.
            auto_commit (bool, optional): Whether to commit after deleting. Defaults to True.
        Returns:
            Optional[T]: The deleted model instance if found, else None.
        """
