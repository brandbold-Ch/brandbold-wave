"""
Utility functions for building URLs and serializing model objects.
Includes helpers for constructing Spring service URLs and serializing lists of models to dictionaries.
"""
from src.utils.settings import get_settings
from src.api.v1.models.base_model import EntityBaseModel


def build_spring_url(*paths, proxy: bool = False) -> str:
    """
    Build a URL for a Spring service endpoint.
    Args:
        *paths: Variable length path components to append to the base URL.
        proxy (bool, optional): If True, use the proxy prefix; otherwise, use the internal URL. Defaults to False.
    Returns:
        str: The constructed URL.
    Raises:
        ValueError: If any path part contains a slash or space.
    """
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
    """
    Serialize a list of EntityBaseModel objects to a list of dictionaries.
    Args:
        data (list[EntityBaseModel]): The list of model instances to serialize.
        deep (bool): Whether to include related objects in the serialization.
    Returns:
        list[dict]: The list of serialized model data.
    """
    return [model.as_json(deep) for model in data]
