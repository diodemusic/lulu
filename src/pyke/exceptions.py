class BadRequest(Exception):
    def __init__(self, message: str, error_code: int):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"


class Unauthorized(Exception):
    def __init__(self, message: str, error_code: int):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"


class Forbidden(Exception):
    def __init__(self, message: str, error_code: int):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"


class DataNotFound(Exception):
    def __init__(self, message: str, error_code: int):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"


class MethodNotAllowed(Exception):
    def __init__(self, message: str, error_code: int):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"


class UnsupportedMediaType(Exception):
    def __init__(self, message: str, error_code: int):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"


class RateLimitExceeded(Exception):
    def __init__(self, message: str, error_code: int):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"


class InternalServerError(Exception):
    def __init__(self, message: str, error_code: int):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"


class BadGateway(Exception):
    def __init__(self, message: str, error_code: int):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"


class ServiceUnavailable(Exception):
    def __init__(self, message: str, error_code: int):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"


class GatewayTimeout(Exception):
    def __init__(self, message: str, error_code: int):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"


class UnknownError(Exception):
    def __init__(self, message: str, error_code: int):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"
