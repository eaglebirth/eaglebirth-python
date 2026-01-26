# EagleBirth Python SDK

Official Python SDK for the EagleBirth API - providing email, SMS, WhatsApp, OTP, QR codes, and AI-powered image processing.

## Installation

```bash
pip install eaglebirth
```

## Quick Start

```python
from eaglebirth import EagleBirth

# Initialize the client with your API key
client = EagleBirth(api_key='eb_live_...')

# Send an email
client.email.send(
    email='user@example.com',
    subject='Welcome to Our Platform',
    message='Thank you for signing up!'
)

# Send an SMS
client.sms.send(
    phone_number='+1234567890',
    message='Your verification code is: 123456'
)

# Send a WhatsApp message
client.whatsapp.send(
    phone_number='+1234567890',
    message='Hello from EagleBirth!'
)
```

## Features

- **Email Notifications** - Send transactional emails
- **SMS Notifications** - Send SMS to any phone number worldwide
- **WhatsApp Notifications** - Send WhatsApp messages
- **OTP/Verification** - Generate and validate one-time codes
- **QR Code Generation** - Create customizable QR codes
- **Vision AI** - Face detection, comparison, and OCR
- **Cloud Storage** - File and directory management with privacy controls
- **Authentication** - App sign-in and JWT token management
- **User Management** - Complete CRUD operations for managing application users

## Authentication

Get your API key from your [EagleBirth Dashboard](https://eaglebirth.com/dashboard/app/api-keys).

```python
from eaglebirth import EagleBirth

# Test environment - automatically routes to sandbox.eaglebirth.com
client = EagleBirth(api_key='eb_test_...')

# Production environment - automatically routes to eaglebirth.com
client = EagleBirth(api_key='eb_live_...')
```

## Environments

The SDK automatically routes requests to the correct environment based on your API key prefix:

- **Sandbox/Test** (`eb_test_...`) - Routes to `sandbox.eaglebirth.com`. For development and testing. No charges, uses test data.
- **Production** (`eb_live_...`) - Routes to `eaglebirth.com`. For live applications. Real charges apply.

No additional configuration needed - just use the appropriate API key and the SDK will automatically connect to the right server. You can create separate API keys for each environment from your dashboard.

## Usage Examples

### Email Notifications

```python
# Basic email
result = client.email.send(
    email='user@example.com',
    subject='Welcome',
    message='Welcome to our platform!'
)

# Email with custom header and salutation
result = client.email.send(
    email='user@example.com',
    subject='Account Verification',
    message='Please verify your email address.',
    header='Welcome to EagleBirth!',
    salutation='Hello John,',
    reply_to='support@yourcompany.com'
)
```

### SMS Notifications

```python
# Send SMS
result = client.sms.send(
    phone_number='+1234567890',
    message='Your verification code is: 123456'
)

# Get SMS pricing
prices = client.sms.get_prices(phone_number='+1234567890')
print(f"Price: ${prices['data']['price']}")
```

### WhatsApp Notifications

```python
result = client.whatsapp.send(
    phone_number='+1234567890',
    message='Your order has been shipped!'
)
```

### OTP/Verification Codes

```python
# Send OTP via email
otp_result = client.otp.send(
    validation_type='email',
    email='user@example.com',
    code_length=6,
    timeout=300  # 5 minutes
)

code_id = otp_result['data']['code_id']

# Validate the OTP
validation = client.otp.validate(
    code_id=code_id,
    code='123456'
)

if validation['res'] == 'success':
    print('Code is valid!')

# Send OTP via SMS
otp_result = client.otp.send(
    validation_type='sms',
    phone_number='+1234567890'
)

# Send OTP via WhatsApp
otp_result = client.otp.send(
    validation_type='whatsapp',
    phone_number='+1234567890'
)
```

### QR Code Generation

```python
# Generate a simple QR code
qr_result = client.qr.generate(
    text='https://example.com'
)

# Generate a styled QR code with logo
with open('logo.png', 'rb') as logo_file:
    qr_result = client.qr.generate(
        text='https://example.com',
        image=logo_file,
        color='#000000',
        background_color='#FFFFFF'
    )

print(f"QR Code URL: {qr_result['data']['qr_code_url']}")
```

### Vision AI

```python
# Extract face details
with open('photo.jpg', 'rb') as image_file:
    result = client.vision.extract_face_details(image=image_file)

    for face in result['data']['faces']:
        print(f"Age: {face['age']}")
        print(f"Gender: {face['gender']}")
        print(f"Emotions: {face['emotions']}")

# Compare two faces
with open('photo1.jpg', 'rb') as img1, open('photo2.jpg', 'rb') as img2:
    result = client.vision.compare_faces(image1=img1, image2=img2)

    print(f"Similarity: {result['data']['similarity']}%")

# Extract text from image (OCR)
with open('document.jpg', 'rb') as image_file:
    result = client.vision.extract_text(image=image_file)

    print(f"Extracted text: {result['data']['text']}")
```

### Cloud Storage

```python
# Create a directory
client.storage.directory.create(
    path='/photos/vacation/',
    private='yes',  # 'yes' or 'no'
    directory_password='secret123'  # Optional password protection
)

# Upload a file
with open('document.pdf', 'rb') as file:
    result = client.storage.file.upload(
        file=file,
        path='/documents/report.pdf',
        private='no',
        file_password='filepass123'  # Optional file password
    )

# List directory contents
contents = client.storage.directory.list_content(
    path='/photos/vacation/',
    directory_password='secret123'  # If directory is password protected
)

for item in contents['data']['directories']:
    print(f"Directory: {item['path']}")

for item in contents['data']['files']:
    print(f"File: {item['filename']} - {item['size']} bytes")

# Retrieve a file
file_data = client.storage.file.retrieve(
    path='/documents/report.pdf',
    password='filepass123'  # If file is password protected
)

# Update file privacy
client.storage.file.update_privacy(
    path='/documents/report.pdf',
    private='yes',
    refresh_token='yes'  # Generate new access token
)

# Update directory password
client.storage.directory.update_password(
    path='/photos/vacation/',
    directory_password='newsecret456'
)

# Delete a file
client.storage.file.delete(path='/documents/old_report.pdf')

# Delete a directory
client.storage.directory.delete(path='/photos/old_vacation/')
```

### User Management & Authentication

```python
# Sign in with app credentials (client_id and secret_id)
auth_response = client.auth.sign_in(
    client_id='your_client_id_here',
    secret_id='your_secret_id_here'
)

print(f"Access Token: {auth_response['access']}")
print(f"Refresh Token: {auth_response['refresh']}")

# Get user JWT tokens (exchange username/password for tokens)
tokens = client.auth.get_token(
    username='user@example.com',
    password='userpassword123'
)

print(f"User Access Token: {tokens['access']}")
print(f"User Refresh Token: {tokens['refresh']}")

# Refresh an expired access token
new_token = client.auth.refresh_token(
    refresh='your_refresh_token_here'
)

print(f"New Access Token: {new_token['access']}")
```

### User Management

```python
# Create a new user
user = client.users.create(
    email='newuser@example.com',
    username='johndoe',
    first_name='John',
    last_name='Doe',
    password='securepassword123',
    phone='+1234567890'
)
print(f"User created with ID: {user['data']['user_id']}")

# Check if a user exists
exists = client.users.exists(username='johndoe')
if exists['data']['exists']:
    print('User exists!')

# Get user details
user_details = client.users.get(username='johndoe')
print(f"User email: {user_details['data']['email']}")

# List all users (paginated)
users = client.users.list(page=1, limit=10)
for user in users['data']['users']:
    print(f"{user['username']} - {user['email']}")

# Update user details
client.users.update(
    username='johndoe',
    email='newemail@example.com',
    first_name='Jonathan'
)

# Sign in a user (classic username/password)
signin_result = client.users.sign_in(
    username='johndoe',
    password='securepassword123'
)
access_token = signin_result['data']['access']
refresh_token = signin_result['data']['refresh']

# Sign in with third-party auth (e.g., Google, Facebook)
signin_result = client.users.sign_in(
    authentication_type='google',
    authentication_type_id='google_user_id_12345'
)

# Verify if a session token is valid
is_valid = client.users.verify_token(token=access_token)

# Refresh user session token
new_tokens = client.users.refresh_token(refresh=refresh_token)

# Update user password (admin action)
client.users.update_password(
    username='johndoe',
    password='newpassword456'
)

# Send verification code for password reset
code_response = client.users.send_verification_code(username='johndoe')
code_id = code_response['data']['code_id']

# Validate the verification code
client.users.validate_verification_code(
    code='123456',
    code_id=code_id
)

# Reset password using verification code (self-service)
client.users.reset_password(
    code='123456',
    code_id=code_id,
    password='brandnewpassword789'
)

# Update user status
client.users.update_status(
    username='johndoe',
    status='suspended'  # Options: 'active', 'suspended', 'pending', 'deleted'
)

# Update user type/role
client.users.update_type(
    username='johndoe',
    user_type='premium'
)

# Reactivate a suspended user
client.users.reactivate(username='johndoe')

# Sign out a user (invalidate refresh token)
client.users.sign_out(refresh_token=refresh_token)

# Delete a user
client.users.delete(username='johndoe')
```

## Error Handling

```python
from eaglebirth import EagleBirth, AuthenticationError, APIError, RateLimitError

client = EagleBirth(api_key='eb_live_...')

try:
    result = client.email.send(
        email='user@example.com',
        subject='Test',
        message='Test message'
    )
except AuthenticationError:
    print("Invalid API key")
except RateLimitError:
    print("Rate limit exceeded - please slow down")
except APIError as e:
    print(f"API error: {e}")
    print(f"Status code: {e.status_code}")
```

## API Scopes

API keys have different scopes that determine which endpoints they can access:

- `full` - Access to all endpoints
- `messaging` - Email, SMS, WhatsApp, OTP only
- `storage` - Cloud storage only
- `qr` - QR code generation only
- `image_processing` - Vision AI only
- `read` - Read-only access

## Support

- Documentation: https://eaglebirth.com/developer/documentation
- Email: contact@eaglebirth.com
- Dashboard: https://eaglebirth.com/dashboard

## License

MIT License - see LICENSE file for details
