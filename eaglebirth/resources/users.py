"""User Management resource for managing application users"""

from typing import Optional, Dict, Any
from .base import BaseResource


class UserManagementResource(BaseResource):
    """User Management resource for CRUD operations on application users"""

    def create(
        self,
        email: Optional[str] = None,
        username: Optional[str] = None,
        first_name: Optional[str] = None,
        middle_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[str] = None,
        birth: Optional[str] = None,
        password: Optional[str] = None,
        referer_id: Optional[str] = None,
        authentication_type: Optional[str] = None,
        authentication_type_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Create a new app user"""
        data = {}
        if email: data['email'] = email
        if username: data['username'] = username
        if first_name: data['first_name'] = first_name
        if middle_name: data['middle_name'] = middle_name
        if last_name: data['last_name'] = last_name
        if phone: data['phone'] = phone
        if birth: data['birth'] = birth
        if password: data['password'] = password
        if referer_id: data['referer_id'] = referer_id
        if authentication_type: data['authentication_type'] = authentication_type
        if authentication_type_id: data['authentication_type_id'] = authentication_type_id

        return self.client._make_request('POST', '/app/users/', data)

    def get(
        self,
        username: Optional[str] = None,
        user_id: Optional[str] = None,
        authentication_type: Optional[str] = None,
        authentication_type_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get a single user's details"""
        data = {}
        if username: data['username'] = username
        if user_id: data['user_id'] = user_id
        if authentication_type: data['authentication_type'] = authentication_type
        if authentication_type_id: data['authentication_type_id'] = authentication_type_id

        return self.client._make_request('POST', '/app/users/get_app_user/', data)

    def list(self, page: int = 1, limit: int = 20) -> Dict[str, Any]:
        """List all app users (paginated)"""
        data = {'page': page, 'limit': limit}
        return self.client._make_request('POST', '/app/users/get_app_users/', data)

    def update(
        self,
        username: Optional[str] = None,
        user_id: Optional[str] = None,
        email: Optional[str] = None,
        first_name: Optional[str] = None,
        middle_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[str] = None,
        birth: Optional[str] = None,
        referer_id: Optional[str] = None,
        authentication_type: Optional[str] = None,
        authentication_type_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Update user details"""
        data = {}
        if username: data['username'] = username
        if user_id: data['user_id'] = user_id
        if email: data['email'] = email
        if first_name: data['first_name'] = first_name
        if middle_name: data['middle_name'] = middle_name
        if last_name: data['last_name'] = last_name
        if phone: data['phone'] = phone
        if birth: data['birth'] = birth
        if referer_id: data['referer_id'] = referer_id
        if authentication_type: data['authentication_type'] = authentication_type
        if authentication_type_id: data['authentication_type_id'] = authentication_type_id

        return self.client._make_request('POST', '/app/users/update_app_user/', data)

    def delete(self, username: Optional[str] = None, user_id: Optional[str] = None) -> Dict[str, Any]:
        """Delete a user"""
        data = {}
        if username: data['username'] = username
        if user_id: data['user_id'] = user_id

        return self.client._make_request('POST', '/app/users/delete_app_user/', data)

    def exists(
        self,
        username: Optional[str] = None,
        user_id: Optional[str] = None,
        authentication_type: Optional[str] = None,
        authentication_type_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Check if a user exists"""
        data = {}
        if username: data['username'] = username
        if user_id: data['user_id'] = user_id
        if authentication_type: data['authentication_type'] = authentication_type
        if authentication_type_id: data['authentication_type_id'] = authentication_type_id

        return self.client._make_request('POST', '/app/users/check_if_app_user_exists/', data)

    def sign_in(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        authentication_type: Optional[str] = None,
        authentication_type_id: Optional[str] = None,
        code: Optional[str] = None,
        code_verifier: Optional[str] = None
    ) -> Dict[str, Any]:
        """Sign in a user (username/password or third-party auth)"""
        data = {}
        if username: data['username'] = username
        if password: data['password'] = password
        if authentication_type: data['authentication_type'] = authentication_type
        if authentication_type_id: data['authentication_type_id'] = authentication_type_id
        if code: data['code'] = code
        if code_verifier: data['code_verifier'] = code_verifier

        return self.client._make_request('POST', '/app/users/sign_app_user_in/', data)

    def sign_out(self, refresh_token: str) -> Dict[str, Any]:
        """Sign out a user (invalidate refresh token)"""
        data = {'refresh_token': refresh_token}
        return self.client._make_request('POST', '/app/users/sign_app_user_out/', data)

    def refresh_token(self, refresh: str) -> Dict[str, Any]:
        """Refresh user session token"""
        data = {'refresh': refresh}
        return self.client._make_request('POST', '/app/users/refresh_signin_token/', data)

    def verify_token(self, token: str) -> Dict[str, Any]:
        """Verify if a session token is valid"""
        data = {'token': token}
        return self.client._make_request('POST', '/app/users/verify_signin_token/', data)

    def update_password(
        self,
        password: str,
        username: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Update user password (admin action)"""
        data = {'password': password}
        if username: data['username'] = username
        if user_id: data['user_id'] = user_id

        return self.client._make_request('POST', '/app/users/update_app_user_password/', data)

    def reset_password(self, code: str, code_id: str, password: str) -> Dict[str, Any]:
        """Reset password using verification code (self-service)"""
        data = {'code': code, 'code_id': code_id, 'password': password}
        return self.client._make_request('POST', '/app/users/reset_password_for_app_user/', data)

    def update_status(
        self,
        status: str,
        username: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Update user status (active, suspended, pending, deleted)"""
        data = {'status': status}
        if username: data['username'] = username
        if user_id: data['user_id'] = user_id

        return self.client._make_request('POST', '/app/users/update_app_user_status/', data)

    def update_type(
        self,
        user_type: str,
        username: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Update user type/role"""
        data = {'type': user_type}
        if username: data['username'] = username
        if user_id: data['user_id'] = user_id

        return self.client._make_request('POST', '/app/users/update_app_user_type/', data)

    def reactivate(self, username: Optional[str] = None, user_id: Optional[str] = None) -> Dict[str, Any]:
        """Reactivate a deactivated user"""
        data = {}
        if username: data['username'] = username
        if user_id: data['user_id'] = user_id

        return self.client._make_request('POST', '/app/users/reactivate_app_user/', data)

    def send_verification_code(
        self,
        username: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Send verification code to user's email"""
        data = {}
        if username: data['username'] = username
        if user_id: data['user_id'] = user_id

        return self.client._make_request('POST', '/app/users/send_code_via_email_to_app_user/', data)

    def validate_verification_code(self, code: str, code_id: str) -> Dict[str, Any]:
        """Validate verification code sent to email"""
        data = {'code': code, 'code_id': code_id}
        return self.client._make_request('POST', '/app/users/validate_code_via_email_for_app_user/', data)
