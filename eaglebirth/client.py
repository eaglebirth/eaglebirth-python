"""
EagleBirth API Client
"""

import requests
from typing import Optional, Dict, Any, BinaryIO
from .exceptions import AuthenticationError, APIError, RateLimitError
from .resources import (
    EmailResource,
    SMSResource,
    WhatsAppResource,
    OTPResource,
    QRCodeResource,
    ImageProcessingResource,
    StorageResource,
)
from .resources.users import UserManagementResource


class EagleBirth:
    """
    EagleBirth API Client

    Example:
        >>> from eaglebirth import EagleBirth
        >>>
        >>> client = EagleBirth(api_key='eb_live_...')
        >>>
        >>> # Send an email
        >>> client.email.send(
        ...     email='user@example.com',
        ...     subject='Welcome',
        ...     message='Welcome to our platform!'
        ... )
    """

    PRODUCTION_URL = "https://eaglebirth.com/api"
    SANDBOX_URL = "https://sandbox.eaglebirth.com/api"

    def __init__(
        self,
        api_key: str,
        base_url: Optional[str] = None,
        timeout: int = 30
    ):
        """
        Initialize EagleBirth client

        Args:
            api_key: Your EagleBirth API key (eb_test_... or eb_live_...)
            base_url: Optional custom base URL (overrides automatic environment detection)
            timeout: Request timeout in seconds (default: 30)
        """
        if not api_key:
            raise ValueError("API key is required")

        if not api_key.startswith(('eb_test_', 'eb_live_')):
            raise ValueError("Invalid API key format. Must start with 'eb_test_' or 'eb_live_'")

        self.api_key = api_key

        # Auto-detect environment from API key if base_url not provided
        if base_url:
            self.base_url = base_url
        elif api_key.startswith('eb_test_'):
            self.base_url = self.SANDBOX_URL
        else:
            self.base_url = self.PRODUCTION_URL

        self.timeout = timeout

        # Initialize resources
        self.email = EmailResource(self)
        self.sms = SMSResource(self)
        self.whatsapp = WhatsAppResource(self)
        self.otp = OTPResource(self)
        self.qr = QRCodeResource(self)
        self.vision = ImageProcessingResource(self)
        self.storage = StorageResource(self)
        self.users = UserManagementResource(self)

    def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Make an authenticated request to the API"""
        url = f"{self.base_url}{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        try:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                data=data,
                files=files,
                params=params,
                timeout=self.timeout
            )

            # Handle rate limiting
            if response.status_code == 429:
                raise RateLimitError("Rate limit exceeded. Please slow down your requests.")

            # Handle authentication errors
            if response.status_code == 401:
                raise AuthenticationError("Invalid API key or unauthorized access")

            # Try to parse JSON response
            try:
                response_data = response.json()
            except ValueError:
                # Not JSON, return as text
                if not response.ok:
                    raise APIError(
                        f"API request failed: {response.text}",
                        status_code=response.status_code,
                        response=response.text
                    )
                return {"data": response.text}

            # Check for API errors
            if response_data.get('res') == 'failed':
                raise APIError(
                    response_data.get('message', 'Unknown error'),
                    status_code=response.status_code,
                    response=response_data
                )

            return response_data

        except requests.exceptions.Timeout:
            raise APIError("Request timed out")
        except requests.exceptions.ConnectionError:
            raise APIError("Connection error. Please check your network.")
        except requests.exceptions.RequestException as e:
            raise APIError(f"Request failed: {str(e)}")
