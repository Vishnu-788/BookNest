from typing import Generic, TypeVar, Optional

T=TypeVar("T")

class Result(Generic[T]):
    def __init__(self, success: bool, data: Optional[T] = None, error: Optional[str] = None, status_code: Optional[int] = 200):
        self.success = success
        self.data = data
        self.error = error
        self.status_code = status_code

    @classmethod
    def ok(cls, data: T, status_code: int):
        return cls(success=True, data=data, status_code=status_code)
    
    @classmethod
    def fail(cls, error: str, status_code: int):
        return cls(success=False, error=error, status_code=status_code)
        