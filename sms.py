from twilio.rest import Client

# Twilio API bilgileri
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
twilio_number = 'YOUR_TWILIO_PHONE_NUMBER'

# Kullanıcı bilgileri
user_phone_number = '+905511918803'  # Kullanıcının telefon numarası
verification_code = '1234'  # Oluşturulan doğrulama kodu

# Twilio Client oluşturma
client = Client(account_sid, auth_token)

# SMS gönderme işlemi
message = client.messages.create(
    body=f"Your verification code is: {verification_code}",
    from_=twilio_number,
    to=user_phone_number
)

print("SMS successfully sent!")
