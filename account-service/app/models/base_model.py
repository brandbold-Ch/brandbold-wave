"""
Base model class for all SQLModel entities.
Provides serialization, field protection, and dynamic update utilities for models.
"""
from pydantic import TypeAdapter
from sqlmodel import SQLModel



class EntityBaseModel(SQLModel):
    """
    Base class for all entity models in the application.
    Extends SQLModel and provides common serialization and update methods.
    """

    def as_json(self, deep: bool = True) -> dict:
        """
        Serialize the model to a JSON-compatible dictionary.
        Args:
            deep (bool, optional): Whether to include related objects. Defaults to True.
        Returns:
            dict: The serialized model data.
        """
        return self.model_dump(mode="json", exclude=self.hide_fields())
    
    def _meta_fields(self) -> dict:
        """
        Get the model's field metadata.
        Returns:
            dict: The model's field definitions.
        """
        return self.__class__.model_fields

    def fromkeys(self, **kwargs) -> None:
        """
        Update model fields from keyword arguments, skipping protected fields.
        Args:
            **kwargs: Field names and values to update.
        """
        pf = self.protected_fields()
        fields_info = self._meta_fields() 
        for key, value in kwargs.items():
            if key in pf:
                continue
            field_meta = fields_info[key].annotation
            cheked = TypeAdapter(field_meta).validate_python(value)
            setattr(self, key, cheked)

    def protected_fields(self) -> set:
        """
        Return a set of fields that should not be updated dynamically.
        Returns:
            set: The set of protected field names.
        """
        return {"id"}

    def hide_fields(self) -> set:
        """
        Return a set of fields to hide when serializing the model.
        Returns:
            set: The set of field names to hide.
        """
        return
