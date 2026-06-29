from httpx import Response


class RiotAPIException(Exception):
    def __init__(self, message: str, error_code: int, response: Response | None = None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.response = response

    def __str__(self) -> str:
        return f"{self.message} (Error Code: {self.error_code})"

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(message={self.message!r}, "
            f"error_code={self.error_code}, response={self.response!r})"
        )


class BadRequest(RiotAPIException):
    pass


class Unauthorized(RiotAPIException):
    pass


class Forbidden(RiotAPIException):
    pass


class DataNotFound(RiotAPIException):
    pass


class MethodNotAllowed(RiotAPIException):
    pass


class UnsupportedMediaType(RiotAPIException):
    pass


class RateLimitExceeded(RiotAPIException):
    pass


class InternalServerError(RiotAPIException):
    pass


class BadGateway(RiotAPIException):
    pass


class ServiceUnavailable(RiotAPIException):
    pass


class GatewayTimeout(RiotAPIException):
    pass


class UnknownError(RiotAPIException):
    pass


class RequestTimeout(RiotAPIException):
    pass
