from typing import Callable
from sqlalchemy.exc import (
    SQLAlchemyError,
    IntegrityError,
    DBAPIError,
    NoResultFound,
    MultipleResultsFound,
)
from functools import wraps
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
    @wraps(func)
    def wrapper(self, *args, **kwargs) -> Callable:
        try:
            return func(self, *args, **kwargs)

        except IntegrityError as e:
            raise DuplicatedRecordException(repr(e))

        except DBAPIError as e:
            raise ServerDBConnectionException(repr(e))

        except NoResultFound as e:
            raise NotFoundException(str(e))

        except MultipleResultsFound as e:
            raise ServerUnknownException(repr(e))

        except SQLAlchemyError as e:
            raise ServerUnknownException(repr(e))

        except (FileNotFoundError, ValueError, TypeError,
                KeyError, AttributeError, PermissionError) as e:
            exception_map = {
                ValueError: DataValidationException,
                TypeError: TypeException,
                KeyError: KeyException,
                AttributeError: AttributeException,
                PermissionError: PermissionException,
            }
            raise exception_map[type(e)](repr(e))
    return wrapper
