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
