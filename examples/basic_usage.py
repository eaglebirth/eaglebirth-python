"""
Basic usage examples for the EagleBirth Python SDK
"""

from eaglebirth import EagleBirth

# Initialize the client with your API key
client = EagleBirth('eb_test_your_api_key_here')


def send_email_example():
    """Example: Send an email"""
    response = client.email.send(
        email='user@example.com',
        subject='Welcome to EagleBirth!',
        message='Thank you for signing up for our service.',
        reply_to='support@myapp.com'
    )
    print('Email sent:', response)


def send_sms_example():
    """Example: Send an SMS"""
    response = client.sms.send(
        phone_number='+1234567890',
        message='Your verification code is 123456'
    )
    print('SMS sent:', response)


def send_whatsapp_example():
    """Example: Send a WhatsApp message"""
    response = client.whatsapp.send(
        phone_number='+1234567890',
        message='Hello from EagleBirth!'
    )
    print('WhatsApp message sent:', response)


def otp_flow_example():
    """Example: Complete OTP flow"""
    # Send OTP
    result = client.otp.send(
        validation_type='email',
        email='user@example.com',
        code_length=6,
        timeout=180
    )
    code_id = result['code_id']
    print(f'OTP sent with code_id: {code_id}')

    # User enters code...
    user_code = input('Enter the code you received: ')

    # Validate OTP
    validation = client.otp.validate(
        code_id=code_id,
        code=user_code
    )
    print('Validation result:', validation)

    # Check if validated
    status = client.otp.check_validated(code_id)
    print('Validation status:', status)


def generate_qr_example():
    """Example: Generate a QR code"""
    qr = client.qr.generate(
        text='https://eaglebirth.com',
        color='#000000',
        background_color='#FFFFFF'
    )
    print('QR code generated:', qr)


def vision_ai_example():
    """Example: Use Vision AI features"""
    # Extract face details
    details = client.vision.extract_face_details(
        image='/path/to/photo.jpg',
        image_type='object'
    )
    print('Face details:', details)

    # Compare two faces
    comparison = client.vision.compare_faces(
        image1='/path/to/photo1.jpg',
        image2='/path/to/photo2.jpg'
    )
    print('Face comparison:', comparison)

    # OCR - Extract text from image
    text = client.vision.extract_text(
        image='/path/to/document.jpg'
    )
    print('Extracted text:', text)


if __name__ == '__main__':
    print('EagleBirth SDK Examples')
    print('========================\n')

    # Uncomment the examples you want to run:
    # send_email_example()
    # send_sms_example()
    # send_whatsapp_example()
    # otp_flow_example()
    # generate_qr_example()
    # vision_ai_example()

    print('\nDone!')
