"""User Management resource for managing application users"""

import logging
from typing import Optional, Dict, Any
from . import BaseResource
from ..exceptions import APIError

logger = logging.getLogger(__name__)


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
        """
        Create a new app user.

        Args:
            email: User's email address
            username: Unique username
            first_name: User's first name
            middle_name: User's middle name (optional)
            last_name: User's last name
            phone: User's phone number
            birth: User's birth date
            password: User's password
            referer_id: ID of the user who referred this user
            authentication_type: Third-party authentication type (e.g., 'google', 'facebook')
            authentication_type_id: Third-party authentication ID

        Returns:
            dict: API response with user creation data
                {
                    'res': 'success',
                    'message': 'User created successfully',
                    'data': {
                        'user_id': 'user_id',
                        'email': 'user@example.com',
                        'username': 'username',
                        ...
                    }
                }

        Raises:
            APIError: If user creation fails
        """
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

        try:
            response = self.client._make_request('POST', '/app/users/', data)
            logger.info(f"Successfully created user: {username or email}")
            return response
        except Exception as e:
            logger.error(f"Failed to create user: {e}")
            raise APIError(f"Failed to create user: {e}")

    def get(
        self,
        username: Optional[str] = None,
        user_id: Optional[str] = None,
        authentication_type: Optional[str] = None,
        authentication_type_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get a single user's details.

        Args:
            username: Username to lookup
            user_id: User ID to lookup
            authentication_type: Third-party authentication type
            authentication_type_id: Third-party authentication ID

        Returns:
            dict: User details from the API

        Raises:
            APIError: If user retrieval fails
        """
        data = {}
        if username: data['username'] = username
        if user_id: data['user_id'] = user_id
        if authentication_type: data['authentication_type'] = authentication_type
        if authentication_type_id: data['authentication_type_id'] = authentication_type_id

        try:
            response = self.client._make_request('POST', '/app/users/get_app_user/', data)
            logger.info(f"Successfully retrieved user: {username or user_id}")
            return response
        except Exception as e:
            logger.error(f"Failed to retrieve user: {e}")
            raise APIError(f"Failed to retrieve user: {e}")

    def list(self, page: int = 1, limit: int = 20) -> Dict[str, Any]:
        """
        List all app users (paginated).

        Args:
            page: Page number (default: 1)
            limit: Number of users per page (default: 20)

        Returns:
            dict: Paginated list of users

        Raises:
            APIError: If listing users fails
        """
        data = {'page': page, 'limit': limit}
        try:
            response = self.client._make_request('POST', '/app/users/get_app_users/', data)
            logger.info(f"Successfully retrieved users list (page {page})")
            return response
        except Exception as e:
            logger.error(f"Failed to list users: {e}")
            raise APIError(f"Failed to list users: {e}")

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
        """
        Update user details.

        Args:
            username: Username to identify the user
            user_id: User ID to identify the user
            email: New email address
            first_name: New first name
            middle_name: New middle name
            last_name: New last name
            phone: New phone number
            birth: New birth date
            referer_id: New referer ID
            authentication_type: Third-party authentication type
            authentication_type_id: Third-party authentication ID

        Returns:
            dict: API response with updated user data

        Raises:
            APIError: If user update fails
        """
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

        try:
            response = self.client._make_request('POST', '/app/users/update_app_user/', data)
            logger.info(f"Successfully updated user: {username or user_id}")
            return response
        except Exception as e:
            logger.error(f"Failed to update user: {e}")
            raise APIError(f"Failed to update user: {e}")

    def delete(self, username: Optional[str] = None, user_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Delete a user.

        Args:
            username: Username to identify the user
            user_id: User ID to identify the user

        Returns:
            dict: API response confirming deletion

        Raises:
            APIError: If user deletion fails
        """
        data = {}
        if username: data['username'] = username
        if user_id: data['user_id'] = user_id

        try:
            response = self.client._make_request('POST', '/app/users/delete_app_user/', data)
            logger.info(f"Successfully deleted user: {username or user_id}")
            return response
        except Exception as e:
            logger.error(f"Failed to delete user: {e}")
            raise APIError(f"Failed to delete user: {e}")

    def exists(
        self,
        username: Optional[str] = None,
        user_id: Optional[str] = None,
        authentication_type: Optional[str] = None,
        authentication_type_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Check if a user exists.

        Args:
            username: Username to check
            user_id: User ID to check
            authentication_type: Third-party authentication type
            authentication_type_id: Third-party authentication ID

        Returns:
            dict: API response with existence status
                {'data': {'exists': True/False}}

        Raises:
            APIError: If existence check fails
        """
        data = {}
        if username: data['username'] = username
        if user_id: data['user_id'] = user_id
        if authentication_type: data['authentication_type'] = authentication_type
        if authentication_type_id: data['authentication_type_id'] = authentication_type_id

        try:
            response = self.client._make_request('POST', '/app/users/check_if_app_user_exists/', data)
            logger.info(f"Checked existence for user: {username or user_id}")
            return response
        except Exception as e:
            logger.error(f"Failed to check user existence: {e}")
            raise APIError(f"Failed to check user existence: {e}")

    def sign_in(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        authentication_type: Optional[str] = None,
        authentication_type_id: Optional[str] = None,
        code: Optional[str] = None,
        code_verifier: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Sign in a user (username/password or third-party auth).

        Args:
            username: Username for classic authentication
            password: Password for classic authentication
            authentication_type: Third-party authentication type (e.g., 'google', 'facebook')
            authentication_type_id: Third-party authentication ID
            code: Authorization code for OAuth PKCE flow
            code_verifier: PKCE code verifier

        Returns:
            dict: API response with access and refresh tokens
                {
                    'data': {
                        'access': 'access_token',
                        'refresh': 'refresh_token',
                        'user_id': 'user_id',
                        ...
                    }
                }

        Raises:
            APIError: If sign-in fails
        """
        data = {}
        if username: data['username'] = username
        if password: data['password'] = password
        if authentication_type: data['authentication_type'] = authentication_type
        if authentication_type_id: data['authentication_type_id'] = authentication_type_id
        if code: data['code'] = code
        if code_verifier: data['code_verifier'] = code_verifier

        try:
            response = self.client._make_request('POST', '/app/users/sign_app_user_in/', data)
            logger.info(f"Successfully signed in user: {username or authentication_type}")
            return response
        except Exception as e:
            logger.error(f"Failed to sign in user: {e}")
            raise APIError(f"Failed to sign in user: {e}")

    def sign_out(self, refresh_token: str) -> Dict[str, Any]:
        """
        Sign out a user (invalidate refresh token).

        Args:
            refresh_token: Refresh token to invalidate

        Returns:
            dict: API response confirming sign-out

        Raises:
            APIError: If sign-out fails
        """
        data = {'refresh_token': refresh_token}
        try:
            response = self.client._make_request('POST', '/app/users/sign_app_user_out/', data)
            logger.info("Successfully signed out user")
            return response
        except Exception as e:
            logger.error(f"Failed to sign out user: {e}")
            raise APIError(f"Failed to sign out user: {e}")

    def refresh_token(self, refresh: str) -> Dict[str, Any]:
        """
        Refresh user session token.

        Args:
            refresh: Refresh token

        Returns:
            dict: API response with new access token

        Raises:
            APIError: If token refresh fails
        """
        data = {'refresh': refresh}
        try:
            response = self.client._make_request('POST', '/app/users/refresh_signin_token/', data)
            logger.info("Successfully refreshed user token")
            return response
        except Exception as e:
            logger.error(f"Failed to refresh token: {e}")
            raise APIError(f"Failed to refresh token: {e}")

    def verify_token(self, token: str) -> Dict[str, Any]:
        """
        Verify if a session token is valid.

        Args:
            token: Access token to verify

        Returns:
            dict: API response with verification status

        Raises:
            APIError: If token verification fails
        """
        data = {'token': token}
        try:
            response = self.client._make_request('POST', '/app/users/verify_signin_token/', data)
            logger.info("Successfully verified token")
            return response
        except Exception as e:
            logger.error(f"Failed to verify token: {e}")
            raise APIError(f"Failed to verify token: {e}")

    def update_password(
        self,
        password: str,
        username: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Update user password (admin action).

        Args:
            password: New password
            username: Username to identify the user
            user_id: User ID to identify the user

        Returns:
            dict: API response confirming password update

        Raises:
            APIError: If password update fails
        """
        data = {'password': password}
        if username: data['username'] = username
        if user_id: data['user_id'] = user_id

        try:
            response = self.client._make_request('POST', '/app/users/update_app_user_password/', data)
            logger.info(f"Successfully updated password for user: {username or user_id}")
            return response
        except Exception as e:
            logger.error(f"Failed to update password: {e}")
            raise APIError(f"Failed to update password: {e}")

    def reset_password(self, code: str, code_id: str, password: str) -> Dict[str, Any]:
        """
        Reset password using verification code (self-service).

        Args:
            code: Verification code
            code_id: Code ID from send_verification_code
            password: New password

        Returns:
            dict: API response confirming password reset

        Raises:
            APIError: If password reset fails
        """
        data = {'code': code, 'code_id': code_id, 'password': password}
        try:
            response = self.client._make_request('POST', '/app/users/reset_password_for_app_user/', data)
            logger.info("Successfully reset password")
            return response
        except Exception as e:
            logger.error(f"Failed to reset password: {e}")
            raise APIError(f"Failed to reset password: {e}")

    def update_status(
        self,
        status: str,
        username: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Update user status.

        Args:
            status: New status ('active', 'suspended', 'pending', 'deleted')
            username: Username to identify the user
            user_id: User ID to identify the user

        Returns:
            dict: API response confirming status update

        Raises:
            APIError: If status update fails
        """
        data = {'status': status}
        if username: data['username'] = username
        if user_id: data['user_id'] = user_id

        try:
            response = self.client._make_request('POST', '/app/users/update_app_user_status/', data)
            logger.info(f"Successfully updated status to '{status}' for user: {username or user_id}")
            return response
        except Exception as e:
            logger.error(f"Failed to update status: {e}")
            raise APIError(f"Failed to update status: {e}")

    def update_type(
        self,
        user_type: str,
        username: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Update user type/role.

        Args:
            user_type: New user type/role
            username: Username to identify the user
            user_id: User ID to identify the user

        Returns:
            dict: API response confirming type update

        Raises:
            APIError: If type update fails
        """
        data = {'type': user_type}
        if username: data['username'] = username
        if user_id: data['user_id'] = user_id

        try:
            response = self.client._make_request('POST', '/app/users/update_app_user_type/', data)
            logger.info(f"Successfully updated type to '{user_type}' for user: {username or user_id}")
            return response
        except Exception as e:
            logger.error(f"Failed to update type: {e}")
            raise APIError(f"Failed to update type: {e}")

    def reactivate(self, username: Optional[str] = None, user_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Reactivate a deactivated user.

        Args:
            username: Username to identify the user
            user_id: User ID to identify the user

        Returns:
            dict: API response confirming reactivation

        Raises:
            APIError: If reactivation fails
        """
        data = {}
        if username: data['username'] = username
        if user_id: data['user_id'] = user_id

        try:
            response = self.client._make_request('POST', '/app/users/reactivate_app_user/', data)
            logger.info(f"Successfully reactivated user: {username or user_id}")
            return response
        except Exception as e:
            logger.error(f"Failed to reactivate user: {e}")
            raise APIError(f"Failed to reactivate user: {e}")

    def send_verification_code(
        self,
        username: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Send verification code to user's email.

        Args:
            username: Username to identify the user
            user_id: User ID to identify the user

        Returns:
            dict: API response with code_id
                {'data': {'code_id': 'code_id'}}

        Raises:
            APIError: If sending verification code fails
        """
        data = {}
        if username: data['username'] = username
        if user_id: data['user_id'] = user_id

        try:
            response = self.client._make_request('POST', '/app/users/send_code_via_email_to_app_user/', data)
            logger.info(f"Successfully sent verification code to user: {username or user_id}")
            return response
        except Exception as e:
            logger.error(f"Failed to send verification code: {e}")
            raise APIError(f"Failed to send verification code: {e}")

    def validate_verification_code(self, code: str, code_id: str) -> Dict[str, Any]:
        """
        Validate verification code sent to email.

        Args:
            code: Verification code received by user
            code_id: Code ID from send_verification_code

        Returns:
            dict: API response with validation status

        Raises:
            APIError: If code validation fails
        """
        data = {'code': code, 'code_id': code_id}
        try:
            response = self.client._make_request('POST', '/app/users/validate_code_via_email_for_app_user/', data)
            logger.info("Successfully validated verification code")
            return response
        except Exception as e:
            logger.error(f"Failed to validate verification code: {e}")
            raise APIError(f"Failed to validate verification code: {e}")

    def exchange_code_for_user(self, code: str, code_verifier: str) -> Dict[str, Any]:
        """
        Exchange authorization code for user session data (OAuth PKCE flow).

        This is used after a user authenticates through EagleBirth Auth UI.
        The Auth UI redirects back to your app with a 'code', and you exchange
        it for the user's information and session tokens.

        Args:
            code: Authorization code from OAuth redirect
            code_verifier: PKCE code verifier that matches the code_challenge

        Returns:
            dict: User session data with access/refresh tokens and user information
                {
                    'res': 'success',
                    'data': {
                        'email': 'user@example.com',
                        'username': 'username',
                        'first_name': 'John',
                        'middle_name': '',
                        'last_name': 'Doe',
                        'phone': '+1234567890',
                        'user_id': 'user_id',
                        'access': 'access_token',
                        'refresh': 'refresh_token'
                    }
                }

        Raises:
            APIError: If code exchange fails
        """
        payload = {
            'code': code,
            'code_verifier': code_verifier
        }

        try:
            response = self.client._make_request(
                method='POST',
                endpoint='/app/users/sign_app_user_in/',
                data=payload
            )

            # Extract user data from response
            user_info = response.get('data', {})

            logger.info(f"Successfully exchanged code for user: {user_info.get('email')}")
            return response

        except Exception as e:
            logger.error(f"Failed to exchange code for user: {e}")
            raise APIError(f"Failed to exchange authorization code: {e}")
