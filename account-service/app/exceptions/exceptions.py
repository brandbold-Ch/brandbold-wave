"""
Custom exception classes for application error handling.
Defines a base exception and specific exceptions for various error scenarios.
"""
from app.exceptions.codes import *


class BaseExceptionError(Exception):
    """
    Base exception class for custom application errors.
    Stores error message, error code, HTTP code, and additional details.
    """
    def __init__(
        self,
        message: str,
        error_code: ErrorCodes,
        http_code: HTTPCodes,
        details: any
    ) -> None:
        super().__init__(message)
        self.message = repr(message)
        self.error_code = int(error_code.value)
        self.error_name = error_code.name
        self.http_code = int(http_code.value)
        self.http_name = http_code.name
        self.details = details

    def to_dict(self) -> dict:
        """
        Convert the exception to a dictionary for JSON responses.
        Returns:
            dict: The error details and codes.
        """
        error_response = {
            "details": {
                "message": self.message,
                "httpName": self.http_name,
                "errorName": self.error_name,
            },
            "codes": {
                "httpCode": self.http_code,
                "errorCode": self.error_code,
            }
        }
        if self.details:
            error_response["error"]["details"] = self.details
        return error_response


class DuplicatedWatchHistoryException(BaseExceptionError):
    """
    Exception for duplicated watch history records.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.DUPLICATED_WATCH_HISTORY, http_code=HTTPCodes.BAD_REQUEST, details=details)


class DuplicatedRecordException(BaseExceptionError):
    """
    Exception for duplicated database records.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.DB_DUPLICATED_KEY, http_code=HTTPCodes.BAD_REQUEST, details=details)


class NotFoundException(BaseExceptionError):
    """
    Exception for not found database records.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.DB_NOT_FOUND, http_code=HTTPCodes.NOT_FOUND, details=details)


class InvalidTokenException(BaseExceptionError):
    """
    Exception for invalid authentication tokens.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.INVALID_TOKEN, http_code=HTTPCodes.UNAUTHORIZED, details=details)


class PasswordMismatchException(BaseExceptionError):
    """
    Exception for password mismatch errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.PASSWORD_DO_NOT_MATCH, http_code=HTTPCodes.FORBIDDEN, details=details)


class ExpiredTokenException(BaseExceptionError):
    """
    Exception for expired authentication tokens.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.EXPIRED_TOKEN, http_code=HTTPCodes.FORBIDDEN, details=details)


class IncorrectUserException(BaseExceptionError):
    """
    Exception for incorrect user errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.INCORRECT_USER, http_code=HTTPCodes.UNAUTHORIZED, details=details)


class JsonFormatInvalidException(BaseExceptionError):
    """
    Exception for invalid JSON format errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.JSON_FORMAT_INVALID, http_code=HTTPCodes.BAD_REQUEST, details=details)


class JsonNestedFormatInvalidException(BaseExceptionError):
    """
    Exception for invalid nested JSON format errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.JSON_NESTED_FORMAT_INVALID, http_code=HTTPCodes.BAD_REQUEST, details=details)


class JsonInvalidDataTypeException(BaseExceptionError):
    """
    Exception for invalid JSON data type errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.JSON_INVALID_DATA_TYPE, http_code=HTTPCodes.BAD_REQUEST, details=details)


class JsonMissingParametersException(BaseExceptionError):
    """
    Exception for missing parameters in JSON data.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.JSON_MISSING_PARAMETERS, http_code=HTTPCodes.BAD_REQUEST, details=details)


class RouteNotFoundException(BaseExceptionError):
    """
    Exception for not found routes.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.ROUTE_NOT_FOUND, http_code=HTTPCodes.NOT_FOUND, details=details)


class RouteMethodNotAllowedException(BaseExceptionError):
    """
    Exception for HTTP method not allowed on route.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.ROUTE_METHOD_NOT_ALLOWED, http_code=HTTPCodes.METHOD_NOT_ALLOWED, details=details)


class ServerNotWorkingException(BaseExceptionError):
    """
    Exception for server not working errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.SERVER_NOT_WORKING, http_code=HTTPCodes.INTERNAL_SERVER_ERROR, details=details)


class ServerDBConnectionException(BaseExceptionError):
    """
    Exception for server database connection errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.SERVER_DB_CONNECTION_ERROR, http_code=HTTPCodes.INTERNAL_SERVER_ERROR, details=details)


class ServerUnknownException(BaseExceptionError):
    """
    Exception for unknown server errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.SERVER_UNKNOWN_ERROR, http_code=HTTPCodes.INTERNAL_SERVER_ERROR, details=details)


class DataValidationException(BaseExceptionError):
    """
    Exception for data validation errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.ERROR_DATA_VALIDATION, http_code=HTTPCodes.BAD_REQUEST, details=details)


class SQLModelException(BaseExceptionError):
    """
    Exception for SQLModel errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.SQL_MODEL_ERROR, http_code=HTTPCodes.INTERNAL_SERVER_ERROR, details=details)


class IntegrityException(BaseExceptionError):
    """
    Exception for SQL integrity errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.SQL_INTEGRITY_ERROR, http_code=HTTPCodes.BAD_REQUEST, details=details)


class DatabaseConnectionException(BaseExceptionError):
    """
    Exception for database connection errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.DATABASE_CONNECTION_ERROR, http_code=HTTPCodes.INTERNAL_SERVER_ERROR, details=details)


class ForeignKeyConstraintViolationException(BaseExceptionError):
    """
    Exception for foreign key constraint violation errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.FOREIGN_KEY_CONSTRAINT_VIOLATION, http_code=HTTPCodes.BAD_REQUEST, details=details)


class UniqueConstraintViolationException(BaseExceptionError):
    """
    Exception for unique constraint violation errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.UNIQUE_CONSTRAINT_VIOLATION, http_code=HTTPCodes.BAD_REQUEST, details=details)


class SQLSyntaxException(BaseExceptionError):
    """
    Exception for SQL syntax errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.SQL_SYNTAX_ERROR, http_code=HTTPCodes.BAD_REQUEST, details=details)


class TimeoutException(BaseExceptionError):
    """
    Exception for timeout errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.TIMEOUT_ERROR, http_code=HTTPCodes.INTERNAL_SERVER_ERROR, details=details)


class NotSupportedException(BaseExceptionError):
    """
    Exception for not supported errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.NOT_SUPPORTED_ERROR, http_code=HTTPCodes.INTERNAL_SERVER_ERROR, details=details)


class TransactionException(BaseExceptionError):
    """
    Exception for transaction errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.TRANSACTION_ERROR, http_code=HTTPCodes.INTERNAL_SERVER_ERROR, details=details)


class DataTypeMismatchException(BaseExceptionError):
    """
    Exception for data type mismatch errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.DATA_TYPE_MISMATCH, http_code=HTTPCodes.BAD_REQUEST, details=details)


class NoSuchColumnException(BaseExceptionError):
    """
    Exception for no such column errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.NO_SUCH_COLUMN, http_code=HTTPCodes.BAD_REQUEST, details=details)


class NoSuchTableException(BaseExceptionError):
    """
    Exception for no such table errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.NO_SUCH_TABLE, http_code=HTTPCodes.BAD_REQUEST, details=details)


class AuthenticationException(BaseExceptionError):
    """
    Exception for authentication errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.AUTHENTICATION_ERROR, http_code=HTTPCodes.UNAUTHORIZED, details=details)


class PermissionException(BaseExceptionError):
    """
    Exception for permission errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.PERMISSION_ERROR, http_code=HTTPCodes.FORBIDDEN, details=details)


class FilePermissionException(BaseExceptionError):
    """
    Exception for file permission errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.FILE_PERMISSION_ERROR, http_code=HTTPCodes.FORBIDDEN, details=details)


class AttributeException(BaseExceptionError):
    """
    Exception for attribute errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.ATTRIBUTE_ERROR, http_code=HTTPCodes.INTERNAL_SERVER_ERROR, details=details)


class TypeException(BaseExceptionError):
    """
    Exception for type errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.TYPE_ERROR, http_code=HTTPCodes.INTERNAL_SERVER_ERROR, details=details)


class ValueException(BaseExceptionError):
    """
    Exception for value errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.VALUE_ERROR, http_code=HTTPCodes.INTERNAL_SERVER_ERROR, details=details)


class IndexException(BaseExceptionError):
    """
    Exception for index errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.INDEX_ERROR, http_code=HTTPCodes.INTERNAL_SERVER_ERROR, details=details)


class KeyException(BaseExceptionError):
    """
    Exception for key errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.KEY_ERROR, http_code=HTTPCodes.INTERNAL_SERVER_ERROR, details=details)


class ModuleNotFoundException(BaseExceptionError):
    """
    Exception for module not found errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.MODULE_NOT_FOUND_ERROR, http_code=HTTPCodes.INTERNAL_SERVER_ERROR, details=details)


class MultipleResultsException(BaseExceptionError):
    """
    Exception for multiple results found errors.
    """
    def __init__(self, message="Se encontraron múltiples resultados inesperados", details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.MULTIPLE_RESULTS, http_code=HTTPCodes.INTERNAL_SERVER_ERROR, details=details)


class GenericException(BaseExceptionError):
    """
    Exception for generic unexpected errors.
    """
    def __init__(self, message="Ocurrió un error inesperado", details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.GENERIC_ERROR, http_code=HTTPCodes.INTERNAL_SERVER_ERROR, details=details)


class NotFoundTokenException(BaseExceptionError):
    """
    Exception for not found token errors.
    """
    def __init__(self, message, details=None) -> None:
        super().__init__(message, error_code=ErrorCodes.NOT_FOUND_TOKEN, http_code=HTTPCodes.UNAUTHORIZED, details=details)

