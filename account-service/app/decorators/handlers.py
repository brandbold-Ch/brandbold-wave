"""
Decorators and exception handling utilities for the application.
Provides a generic exception handler decorator and a body validation decorator for request handling.
"""
from typing import Callable, Any
from functools import wraps
import inspect
from flask import request
from pydantic import BaseModel
from pydantic import ValidationError
from sqlalchemy.exc import (
    SQLAlchemyError,
    IntegrityError,
    DBAPIError,
    NoResultFound,
    MultipleResultsFound,
)
from app.exceptions.exceptions import (
    DuplicatedRecordException,
    ServerDBConnectionException,
    NotFoundException,
    ServerUnknownException,
    DataValidationException,
    TypeException,
    KeyException,
    AttributeException,
    PermissionException
)


def exception_handler(func: Callable) -> Callable:
    """
    Decorator to handle and map exceptions to custom application exceptions.
    Catches SQLAlchemy and common Python exceptions, raising custom exceptions for each case.
    Args:
        func (Callable): The function to decorate.
    Returns:
        Callable: The wrapped function with exception handling.
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)

        except IntegrityError as e:
            raise DuplicatedRecordException(e)

        except DBAPIError as e:
            raise ServerDBConnectionException(e)

        except NoResultFound as e:
            raise NotFoundException(e)

        except MultipleResultsFound as e:
            raise ServerUnknownException(e)

        except SQLAlchemyError as e:
            raise ServerUnknownException(e)

        except (FileNotFoundError, ValueError, TypeError,
                KeyError, AttributeError, PermissionError, 
                ValidationError
            ) as e:
            exception_map = {
                ValidationError: DataValidationException,
                TypeError: TypeException,
                KeyError: KeyException,
                AttributeError: AttributeException,
                PermissionError: PermissionException
            }
            raise exception_map[type(e)](e)
    return wrapper


def parse_body(func: Callable) -> Callable:
    """
    Decorator to automatically parse and validate the request body using a Pydantic model.
    Inspects the function signature to find a parameter that is a subclass of BaseModel,
    validates the incoming JSON request body against that model, and injects the validated
    model instance into the function call.
    Args:
        func (Callable): The function to decorate.
    Returns:
        Callable: The wrapped function with validated body as argument.
    Raises:
        TypeException: If no parameter is found that is a subclass of BaseModel.
    """
    @wraps(func)
    @exception_handler
    def wrapper(*args, **kwargs) -> Any:
        signature = inspect.signature(func).parameters.values()
        subclass = list(
            filter(lambda x: issubclass(x.annotation, BaseModel), signature)
        )
        if len(subclass) == 1:
            kwargs[subclass[0].name] = subclass[0].annotation.model_validate(request.get_json())
            return func(*args, **kwargs)
        else:
            raise TypeException("No child field found for BaseModel")
    return wrapper
