"""
EagleBirth Python SDK
Official Python SDK for EagleBirth API

Documentation: https://eaglebirth.com/developer/documentation
"""

from .client import EagleBirth
from .exceptions import (
    EagleBirthError,
    AuthenticationError,
    APIError,
    ValidationError,
    RateLimitError,
)

__version__ = "1.1.0"
__all__ = [
    "EagleBirth",
    "EagleBirthError",
    "AuthenticationError",
    "APIError",
    "ValidationError",
    "RateLimitError",
]
