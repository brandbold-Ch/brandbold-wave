from typing import Generic, TypeVar
from app.models import EntityBaseModel
from app.utils.builders import serialize_objects

T = TypeVar("T", bound=EntityBaseModel)


class ListWrapper(Generic[T]):
    
    def __init__(self, items: list[T]):
        self.items = items
        
    def serialize(self, deep: bool = True) -> list[dict]:
        return serialize_objects(self.items, deep)
    