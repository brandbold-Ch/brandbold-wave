from typing import Any, Type, Optional
from sqlmodel import select, update
from sqlmodel import Session
from sqlalchemy import ScalarResult
from src.api.v1.interfaces import AbstractCrud, T
from src.utils.wrappers import ListWrapper
from src.exceptions import NotFoundException


class BaseRepository(AbstractCrud):
    """
    Base repository class providing generic CRUD operations for SQLModel models.
    Implements methods for create, read, update, and delete, as well as conditional queries.
    """

    def __init__(self, model: Type[T]) -> None:
        """
        Initialize the repository with a specific model class.
        Args:
            model (Type[T]): The SQLModel model class to operate on.
        """
        self.model = model
        
    @property
    def model_name(self) -> str:
        """
        Get the name of the model class managed by this repository.

        Returns:
            str: The name of the SQLModel class.
        """
        return self.model.__name__

    def create(
        self,
        model: T,
        session: Session = None,
        auto_commit: bool = True
    ) -> T:
        """
        Add a new model instance to the database.
        Args:
            model (T): The model instance to add.
            session (Session, optional): The database session.
            auto_commit (bool, optional): Whether to commit after adding. Defaults to True.
        Returns:
            T: The created model instance.
        """
        session.add(model)
        if auto_commit:
            session.commit()
            session.refresh(model)
        return model
    
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
        data = list(session.exec(select(self.model)))
        return ListWrapper[self.model](data)

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
        result = session.get(self.model, _id)
        if result is None:
            raise NotFoundException(
                f"{self.model_name} not found with ID {_id}"
            )
        return result

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
        result = self.get(_id, session)
        if result:
            session.delete(result)
            if auto_commit:
                session.commit()
        return result

    def update(
        self,
        _id: Any,
        data: dict,
        session: Session = None,
        auto_commit: bool = True
    ) -> Optional[T]:
        """
        Update a model instance by its primary key.
        Args:
            _id (Any): The primary key value.
            data (dict): The data to update.
            session (Session, optional): The database session.
            auto_commit (bool, optional): Whether to commit after updating. Defaults to True.
        Returns:
            Optional[T]: The updated model instance if found, else None.
        """
        result = self.get(_id, session)
        if result:
            result.fromkeys(**data)
            session.add(result)
            if auto_commit:
                session.commit()
                session.refresh(result)
        return result
        
    def fetch_by_condition(
        self,
        condition: bool,
        session: Session
    ) -> ScalarResult:
        """
        Fetch model instances matching a given condition.
        Args:
            condition (bool): The SQLAlchemy condition to filter by.
            session (Session): The database session.
        Returns:
            ScalarResult: The result of the query.
        """
        stmt = (
            select(self.model)
            .where(condition)
        )
        return session.exec(stmt)
    
    def update_by_condition(
        self, 
        data: dict,
        condition: bool, 
        session: Session
    ) -> ScalarResult:
        """
        Update model instances matching a given condition.
        Args:
            data (dict): The data to update.
            condition (bool): The SQLAlchemy condition to filter by.
            session (Session): The database session.
        Returns:
            ScalarResult: The result of the update query.
        """
        smtp = (
            update(select.model)
            .where(condition)
            .values(**data)
        )
        return session.exec(smtp)

    def get_one(
        self,
        condition: bool,
        session: Session
    ) -> T:
        """
        Retrieve the first model instance matching a condition.
        Args:
            condition (bool): The SQLAlchemy condition to filter by.
            session (Session): The database session.
        Returns:
            T: The first matching model instance.
        """
        result = self.fetch_by_condition(condition, session).first()
        if result is None:
            raise NotFoundException(
                f"{self.model_name} not found with condition {condition}"
            )
        return result

    def get_many(
        self,
        condition: bool,
        session: Session
    ) -> ListWrapper:
        """
        Retrieve all model instances matching a condition.
        Args:
            condition (bool): The SQLAlchemy condition to filter by.
            session (Session): The database session.
        Returns:
            ListWrapper: A wrapper containing all matching model instances.
        """
        result = self.fetch_by_condition(condition, session)
        return ListWrapper[self.model](result.all())

    def delete_one(
        self,
        condition: bool,
        session: Session,
        auto_commit: bool = True
    ) -> Optional[T]:
        """
        Delete the first model instance matching a condition.
        Args:
            condition (bool): The SQLAlchemy condition to filter by.
            session (Session): The database session.
            auto_commit (bool, optional): Whether to commit after deleting. Defaults to True.
        Returns:
            Optional[T]: The deleted model instance if found, else None.
        """
        result = self.get_one(condition, session)
        if result:
            session.delete(result)
            if auto_commit:
                session.commit()
        return result

    def delete_many(
        self,
        condition: bool,
        session: Session,
        auto_commit: bool = True
    ) -> list[T]:
        """
        Delete all model instances matching a condition.
        Args:
            condition (bool): The SQLAlchemy condition to filter by.
            session (Session): The database session.
            auto_commit (bool, optional): Whether to commit after deleting. Defaults to True.
        Returns:
            list[T]: The list of deleted model instances.
        """
        result = self.get_many(condition, session)
        for r in result:
            session.delete(r)
        if auto_commit:
            session.commit()
        return result

    def update_one(
        self,
        condition: bool,
        data: dict,
        session: Session,
        auto_commit: bool = True
    ) -> Optional[T]:
        """
        Update the first model instance matching a condition.
        Args:
            condition (bool): The SQLAlchemy condition to filter by.
            data (dict): The data to update.
            session (Session): The database session.
            auto_commit (bool, optional): Whether to commit after updating. Defaults to True.
        Returns:
            Optional[T]: The updated model instance if found, else None.
        """
        result = self.get_one(condition, session)
        if result:
            result.fromkeys(**data)
            session.add(result)
            if auto_commit:
                session.commit()
                session.refresh(result)
        return result
