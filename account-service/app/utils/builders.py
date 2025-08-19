from app.utils.settings import get_settings
from app.models.base_model import EntityBaseModel


def build_spring_url(*paths, proxy: bool = False) -> str:
    settings = get_settings()
    base_url = settings.spring_proxy_prefix \
        if proxy else settings.spring_internal_url
        
    for p in paths:
        if "/" in p or " " in p:
            raise ValueError(f"Invalid path part: '{p}'. "
                             f"Do not include slashes or spaces.")

    if len(paths) > 0:
        return "/".join([base_url.strip("/"), *paths])
    return base_url


def serialize_objects(
    data: list[EntityBaseModel], 
    deep: bool
) -> list[dict]:
    return [model.as_json(deep) for model in data]
