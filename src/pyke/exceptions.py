class RiotAPIException(Exception):
    def __init__(self, message: str, error_code: int):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self) -> str:
        return f"{self.message} (Error Code: {self.error_code})"


class BadRequest(Exception):
    pass


class Unauthorized(Exception):
    pass


class Forbidden(Exception):
    pass


class DataNotFound(Exception):
    pass


class MethodNotAllowed(Exception):
    pass


class UnsupportedMediaType(Exception):
    pass


class RateLimitExceeded(Exception):
    pass


class InternalServerError(Exception):
    pass


class BadGateway(Exception):
    pass


class ServiceUnavailable(Exception):
    pass


class GatewayTimeout(Exception):
    pass


class UnknownError(Exception):
    pass
