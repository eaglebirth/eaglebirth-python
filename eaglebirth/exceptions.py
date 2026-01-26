"""
EagleBirth SDK Exceptions
"""


class EagleBirthError(Exception):
    """Base exception for all EagleBirth errors"""
    pass


class AuthenticationError(EagleBirthError):
    """Raised when API key authentication fails"""
    pass


class APIError(EagleBirthError):
    """Raised when the API returns an error"""
    def __init__(self, message, status_code=None, response=None):
        super().__init__(message)
        self.status_code = status_code
        self.response = response


class ValidationError(EagleBirthError):
    """Raised when request validation fails"""
    pass


class RateLimitError(EagleBirthError):
    """Raised when rate limit is exceeded"""
    pass
