from app.exceptions.base_exception import AppError


class ValidationError(AppError):
    def __init__(self, message: str, code: str, field: str = None):
        super().__init__(message, code)
        self.field = field