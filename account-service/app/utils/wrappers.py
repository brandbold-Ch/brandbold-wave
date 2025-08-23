"""
Utility wrappers for model collections.
Defines a generic ListWrapper class for serializing lists of model instances.
"""
from typing import Generic, TypeVar
from app.models import EntityBaseModel
from app.utils.builders import serialize_objects

T = TypeVar("T", bound=EntityBaseModel)


class ListWrapper(Generic[T]):
    """
    Generic wrapper for a list of model instances.
    Provides serialization utilities for lists of EntityBaseModel objects.
    """
    def __init__(self, items: list[T]):
        """
        Initialize the ListWrapper with a list of items.
        Args:
            items (list[T]): The list of model instances to wrap.
        """
        self.items = items

    def serialize(self, deep: bool = True) -> list[dict]:
        """
        Serialize the wrapped list of model instances to a list of dictionaries.
        Args:
            deep (bool, optional): Whether to include related objects in the serialization. Defaults to True.
        Returns:
            list[dict]: The list of serialized model data.
        """
        return serialize_objects(self.items, deep)
    