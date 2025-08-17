from pydantic import TypeAdapter
from sqlmodel import SQLModel


class EntityBaseModel(SQLModel):

    def as_json(self, deep: bool = True) -> dict:
        return self.model_dump(mode="json", exclude=self.hide_fields())
    
    def _meta_fields(self) -> dict:
        return self.__class__.model_fields

    def fromkeys(self, **kwargs) -> None:
        pf = self.protected_fields()
        fields_info = self._meta_fields() 
    
        for key, value in kwargs.items():
            if key in pf:
                continue

            field_meta = fields_info[key].annotation
            cheked = TypeAdapter(field_meta).validate_python(value)
            setattr(self, key, cheked)


    def protected_fields(self) -> set:
        return {"id"}

    def hide_fields(self) -> set:
        return
