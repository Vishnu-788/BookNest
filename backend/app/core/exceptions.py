class AppException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

class NotFoundException(AppException):
    def __init__(self, message):
        super().__init__(message, 404)

class ConflictException(AppException):
    def __init__(self, message: str = "Conflict"):
        super().__init__(message, 409)

class ValidationException(AppException):
    def __init__(self, message: str):
        super().__init__(message, 422)

class InternalServerError(AppException):
    def __init__(self, message: str):
        super().__init__(message, 500)

class UnauthorizedException(AppException):
    def __init__(self, message: str = "Unauthorized access"):
        super().__init__(message, status_code=401)

        