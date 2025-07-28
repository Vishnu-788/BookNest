from enum import Enum


class RoleEnum(str, Enum):
    LIBRARIAN = "librarian"
    MEMBER = "member"


class LoanStatus(str, Enum):
    LOANED = "loaned"
    RETURNED = "returned"
