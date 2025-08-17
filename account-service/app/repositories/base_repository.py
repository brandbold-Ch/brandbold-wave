from typing import Any, Type, Optional
from sqlalchemy import ScalarResult
from sqlmodel import Session
from app.abstract.abstract_crud import AbstractCrud, T
from sqlmodel import select, update
from app.decorators.handlers import exception_handler
from app.utils.wrappers import ListWrapper


class BaseRepository(AbstractCrud):

    def __init__(self, model: Type[T]) -> None:
        self.model = model

    @exception_handler
    def create(
            self,
            model: T,
            session: Session = None,
            auto_commit: bool = True
    ) -> T:
        session.add(model)
        if auto_commit:
            session.commit()
            session.refresh(model)
        return model
    
    @exception_handler
    def select(
            self,
            session: Session
    ) -> ListWrapper:
        data = list(session.exec(select(self.model)))
        return ListWrapper[self.model](data)

    @exception_handler
    def get(
            self,
            _id: Any,
            session: Session
    ) -> Optional[T]:
        return session.get(self.model, _id)

    @exception_handler
    def delete(
            self,
            _id: Any,
            session: Session,
            auto_commit: bool = True
    ) -> Optional[T]:
        result = self.get(_id, session)
        if result:
            session.delete(result)
            if auto_commit:
                session.commit()
        return result

    @exception_handler
    def update(
            self,
            _id: Any,
            data: dict,
            session: Session = None,
            auto_commit: bool = True
    ) -> Optional[T]:
        result = self.get(_id, session)
        if result:
            result.fromkeys(**data)
            session.add(result)
            if auto_commit:
                session.commit()
                session.refresh(result)
        return result
        
        
    @exception_handler
    def fetch_by_condition(
            self,
            condition: bool,
            session: Session
    ) -> ScalarResult:
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
        smtp = (
            update(select.model)
            .where(condition)
            .values(**data)
        )
        return session.exec(smtp)

    @exception_handler
    def get_one(
            self,
            condition: bool,
            session: Session
    ) -> T:
        result = self.fetch_by_condition(condition, session)
        return result.first()

    @exception_handler
    def get_many(
            self,
            condition: bool,
            session: Session
    ) -> ListWrapper:
        result = self.fetch_by_condition(condition, session)
        return ListWrapper[self.model](result.all())

    @exception_handler
    def delete_one(
            self,
            condition: bool,
            session: Session,
            auto_commit: bool = True
    ) -> Optional[T]:
        result = self.get_one(condition, session)
        if result:
            session.delete(result)
            if auto_commit:
                session.commit()
        return result

    @exception_handler
    def delete_many(
            self,
            condition: bool,
            session: Session,
            auto_commit: bool = True
    ) -> list[T]:
        result = self.get_many(condition, session)
        for r in result:
            session.delete(r)
        if auto_commit:
            session.commit()
        return result

    @exception_handler
    def update_one(
            self,
            condition: bool,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> Optional[T]:
        result = self.get_one(condition, session)
        if result:
            result.fromkeys(**data)
            session.add(result)
            if auto_commit:
                session.commit()
                session.refresh(result)
        return result
