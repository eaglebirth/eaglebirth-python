"""
EagleBirth API Resources
"""

from typing import Optional, Dict, Any, BinaryIO, Union
from io import BytesIO


class BaseResource:
    """Base class for all API resources"""

    def __init__(self, client):
        self.client = client


class EmailResource(BaseResource):
    """Email notification resource"""

    def send(
        self,
        email: str,
        subject: str,
        message: str,
        reply_to: Optional[str] = None,
        header: Optional[str] = None,
        salutation: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Send an email

        Args:
            email: Recipient email address
            subject: Email subject
            message: Email body/message
            reply_to: Optional reply-to address
            header: Optional header text
            salutation: Optional salutation text

        Returns:
            API response dictionary
        """
        data = {
            'email': email,
            'subject': subject,
            'message': message,
        }

        if reply_to:
            data['reply_to'] = reply_to
        if header:
            data['header'] = header
        if salutation:
            data['salutation'] = salutation

        return self.client._make_request('POST', '/app/messaging/email/', data=data)


class SMSResource(BaseResource):
    """SMS notification resource"""

    def send(
        self,
        phone_number: str,
        message: str,
        sending_method: Optional[str] = None,
        provider: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Send an SMS message

        Args:
            phone_number: Recipient phone number (E.164 format: +1234567890)
            message: SMS message text
            sending_method: Optional. 'email_to_sms' or 'normal_sms'
            provider: Required if sending_method is 'email_to_sms'

        Returns:
            API response dictionary
        """
        data = {
            'phone_number': phone_number,
            'message': message,
        }

        if sending_method:
            data['sending_method'] = sending_method
        if provider:
            data['provider'] = provider

        return self.client._make_request('POST', '/app/messaging/sms/', data=data)

    def get_prices(self, phone_number: Optional[str] = None) -> Dict[str, Any]:
        """Get SMS pricing information"""
        data = {}
        if phone_number:
            data['phone_number'] = phone_number

        return self.client._make_request('POST', '/app/messaging/sms/get_prices_for_sms/', data=data)


class WhatsAppResource(BaseResource):
    """WhatsApp notification resource"""

    def send(
        self,
        phone_number: str,
        message: str,
        template: str = 'normal_message'
    ) -> Dict[str, Any]:
        """
        Send a WhatsApp message

        Args:
            phone_number: Recipient phone number (E.164 format)
            message: Message text
            template: Template to use (default: 'normal_message')

        Returns:
            API response dictionary
        """
        data = {
            'phone_number': phone_number,
            'message': message,
            'template': template,
        }

        return self.client._make_request('POST', '/app/messaging/whatsapp/', data=data)


class OTPResource(BaseResource):
    """OTP/Verification code resource"""

    def send(
        self,
        validation_type: str,
        email: Optional[str] = None,
        phone_number: Optional[str] = None,
        provider: Optional[str] = None,
        code_length: int = 6,
        timeout: int = 180,
        trials: int = 3
    ) -> Dict[str, Any]:
        """
        Send an OTP/verification code

        Args:
            validation_type: 'email', 'sms', 'whatsapp', or 'whatsapp_return'
            email: Email address (required if validation_type is 'email')
            phone_number: Phone number (required if validation_type is 'sms' or 'whatsapp')
            provider: Optional provider name
            code_length: Length of the code (default: 6)
            timeout: Code expiration in seconds (default: 180)
            trials: Maximum validation attempts (default: 3)

        Returns:
            API response with code_id
        """
        data = {
            'validation_type': validation_type,
            'code_length': code_length,
            'timeout': timeout,
            'trials': trials,
        }

        if email:
            data['email'] = email
        if phone_number:
            data['phone_number'] = phone_number
        if provider:
            data['provider'] = provider

        return self.client._make_request('POST', '/app/code_validation/', data=data)

    def validate(self, code_id: str, code: str) -> Dict[str, Any]:
        """
        Validate an OTP code

        Args:
            code_id: The code_id received from send()
            code: The OTP code to validate

        Returns:
            API response indicating if code is valid
        """
        data = {
            'code_id': code_id,
            'code': code,
        }

        return self.client._make_request('POST', '/app/code_validation/validate_code_sent/', data=data)

    def check_validated(self, code_id: str) -> Dict[str, Any]:
        """
        Check if a code was successfully validated

        Args:
            code_id: The code_id to check

        Returns:
            API response with validation status
        """
        data = {'code_id': code_id}
        return self.client._make_request('POST', '/app/code_validation/check_validated_code/', data=data)


class QRCodeResource(BaseResource):
    """QR code generation resource"""

    def generate(
        self,
        text: str,
        image: Optional[Union[str, BinaryIO]] = None,
        image_type: str = 'object',
        color: Optional[str] = None,
        background_color: Optional[str] = None,
        qr_type: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Generate a QR code

        Args:
            text: Data/URL to encode in the QR code
            image: Optional logo image (file object or URL)
            image_type: 'object' for file upload, 'link' for URL
            color: Hex color for QR code pattern (e.g., '#000000')
            background_color: Hex color for background (e.g., '#FFFFFF')
            qr_type: Optional QR code pattern type

        Returns:
            API response with QR code data
        """
        data = {'text': text}
        files = {}

        if color:
            data['color'] = color
        if background_color:
            data['background_color'] = background_color
        if qr_type:
            data['qr_type'] = qr_type
        if image_type:
            data['image_type'] = image_type

        if image:
            if isinstance(image, str) and image_type == 'link':
                data['image'] = image
            elif hasattr(image, 'read'):
                files['image'] = image

        return self.client._make_request('POST', '/app/qr_code_generator/', data=data, files=files if files else None)


class ImageProcessingResource(BaseResource):
    """Image processing/Vision AI resource"""

    def extract_face_details(
        self,
        image: Union[str, BinaryIO],
        image_type: str = 'object'
    ) -> Dict[str, Any]:
        """
        Extract face details from an image

        Args:
            image: Image file or URL
            image_type: 'object' for file upload, 'link' for URL

        Returns:
            API response with face details (age, gender, expressions, etc.)
        """
        data = {'image_type': image_type}
        files = {}

        if isinstance(image, str) and image_type == 'link':
            data['image'] = image
        elif hasattr(image, 'read'):
            files['image'] = image

        return self.client._make_request(
            'POST',
            '/app/image_processing/get_details_from_an_image/',
            data=data,
            files=files if files else None
        )

    def compare_faces(
        self,
        image1: Union[str, BinaryIO],
        image2: Union[str, BinaryIO],
        image1_type: str = 'object',
        image2_type: str = 'object'
    ) -> Dict[str, Any]:
        """
        Compare two faces

        Args:
            image1: First image file or URL
            image2: Second image file or URL
            image1_type: 'object' or 'link' for first image
            image2_type: 'object' or 'link' for second image

        Returns:
            API response with similarity score
        """
        data = {
            'image1_type': image1_type,
            'image2_type': image2_type,
        }
        files = {}

        if isinstance(image1, str) and image1_type == 'link':
            data['image1'] = image1
        elif hasattr(image1, 'read'):
            files['image1'] = image1

        if isinstance(image2, str) and image2_type == 'link':
            data['image2'] = image2
        elif hasattr(image2, 'read'):
            files['image2'] = image2

        return self.client._make_request(
            'POST',
            '/app/image_processing/compare_two_faces_in_two_images/',
            data=data,
            files=files if files else None
        )

    def extract_text(
        self,
        image: Union[str, BinaryIO],
        image_type: str = 'object'
    ) -> Dict[str, Any]:
        """
        Extract text from an image (OCR)

        Args:
            image: Image file or URL
            image_type: 'object' for file upload, 'link' for URL

        Returns:
            API response with extracted text
        """
        data = {'image_type': image_type}
        files = {}

        if isinstance(image, str) and image_type == 'link':
            data['image'] = image
        elif hasattr(image, 'read'):
            files['image'] = image

        return self.client._make_request(
            'POST',
            '/app/image_processing/get_text_from_image/',
            data=data,
            files=files if files else None
        )


class StorageResource(BaseResource):
    """Cloud Storage resource for managing files and directories"""

    def __init__(self, client):
        super().__init__(client)
        self.directory = DirectoryResource(client)
        self.file = FileResource(client)


class DirectoryResource(BaseResource):
    """Directory management operations"""

    def create(self, path: str, private: str = 'no', directory_password: Optional[str] = None) -> Dict[str, Any]:
        """Create a new directory"""
        data = {'path': path, 'private': private}
        if directory_password:
            data['directory_password'] = directory_password
        return self.client._make_request('POST', '/app/storage/directory/', data)

    def delete(self, directory_id: Optional[str] = None, path: Optional[str] = None) -> Dict[str, Any]:
        """Delete a directory and all its contents"""
        data = {}
        if directory_id:
            data['directory_id'] = directory_id
        if path:
            data['path'] = path
        return self.client._make_request('POST', '/app/storage/directory/delete_a_directory/', data)

    def list_content(
        self,
        path: Optional[str] = None,
        directory_id: Optional[str] = None,
        token: Optional[str] = None,
        directory_password: Optional[str] = None
    ) -> Dict[str, Any]:
        """List contents of a directory"""
        if path:
            data = {'path': path}
            if token:
                data['token'] = token
            if directory_password:
                data['directory_password'] = directory_password
            return self.client._make_request('POST', '/app/storage/directory/list_directory_content/', data)
        elif directory_id:
            data = {'directory_id': directory_id}
            if token:
                data['token'] = token
            if directory_password:
                data['directory_password'] = directory_password
            return self.client._make_request('POST', '/app/storage/directory/list_directory_content_from_id/', data)
        else:
            raise ValueError("Either path or directory_id must be provided")

    def update_password(
        self,
        directory_password: str,
        directory_id: Optional[str] = None,
        path: Optional[str] = None
    ) -> Dict[str, Any]:
        """Update or remove directory password"""
        data = {'directory_password': directory_password}
        if directory_id:
            data['directory_id'] = directory_id
        if path:
            data['path'] = path
        return self.client._make_request('POST', '/app/storage/directory/update_directory_password/', data)

    def update_privacy(
        self,
        is_private: str,
        directory_id: Optional[str] = None,
        path: Optional[str] = None
    ) -> Dict[str, Any]:
        """Update directory privacy setting"""
        data = {'is_private': is_private}
        if directory_id:
            data['directory_id'] = directory_id
        if path:
            data['path'] = path
        return self.client._make_request('POST', '/app/storage/directory/update_directory_privacy/', data)


class FileResource(BaseResource):
    """File management operations"""

    def upload(
        self,
        file: Union[str, BinaryIO],
        path: str,
        filename: Optional[str] = None,
        private: str = 'no',
        directory_password: Optional[str] = None,
        file_password: Optional[str] = None
    ) -> Dict[str, Any]:
        """Upload a file"""
        data = {'path': path, 'private': private}
        if filename:
            data['filename'] = filename
        if directory_password:
            data['directory_password'] = directory_password
        if file_password:
            data['file_password'] = file_password

        files = {}
        if isinstance(file, str):
            files['file'] = file
        else:
            files['file'] = file

        return self.client._make_request('POST', '/app/storage/file/', data, files)

    def retrieve(
        self,
        file_id: Optional[str] = None,
        path: Optional[str] = None,
        token: Optional[str] = None,
        password: Optional[str] = None
    ) -> Dict[str, Any]:
        """Retrieve file content"""
        if file_id:
            data = {'id': file_id}
            if token:
                data['token'] = token
            if password:
                data['password'] = password
            return self.client._make_request('POST', '/app/storage/file/content_from_id/', data)
        elif path:
            params = {'path': path}
            if token:
                params['token'] = token
            if password:
                params['password'] = password
            return self.client._make_request('GET', '/app/storage/file/content/', params=params)
        else:
            raise ValueError("Either file_id or path must be provided")

    def delete(
        self,
        file_id: Optional[str] = None,
        path: Optional[str] = None,
        token: Optional[str] = None
    ) -> Dict[str, Any]:
        """Delete a file"""
        data = {}
        if file_id:
            data['file_id'] = file_id
        if path:
            data['path'] = path
        if token:
            data['token'] = token
        return self.client._make_request('POST', '/app/storage/file/delete_a_file/', data)

    def update_password(
        self,
        password: str,
        file_id: Optional[str] = None,
        path: Optional[str] = None
    ) -> Dict[str, Any]:
        """Update or remove file password"""
        data = {'password': password}
        if file_id:
            data['file_id'] = file_id
        if path:
            data['path'] = path
        return self.client._make_request('POST', '/app/storage/file/update_file_password/', data)

    def update_privacy(
        self,
        private: str,
        file_id: Optional[str] = None,
        path: Optional[str] = None,
        refresh_token: str = 'no'
    ) -> Dict[str, Any]:
        """Update file privacy and optionally refresh access token"""
        data = {'private': private, 'refresh_token': refresh_token}
        if file_id:
            data['file_id'] = file_id
        if path:
            data['path'] = path
        return self.client._make_request('POST', '/app/storage/file/update_file_privacy/', data)


