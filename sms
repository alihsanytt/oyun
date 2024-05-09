import subprocess
import json

def read_sms():
    # termux-sms-list komutu ile gelen SMS'leri al
    sms_list = subprocess.run(['termux-sms-list', '-l', '10'], capture_output=True, text=True)

    # Çıktıyı JSON formatında parse et
    sms_data = json.loads(sms_list.stdout)

    return sms_data

def find_verification_code(sms_data):
    # Gelen SMS'ler içinde doğrulama kodunu ara
    for sms in sms_data:
        if 'Your verification code' in sms['body']:
            # Doğrulama kodunu mesaj içinden al
            words = sms['body'].split()
            verification_code = words[-1]  # Son kelimeyi doğrulama kodu olarak al
            return verification_code

    return None

try:
    # Gelen SMS'leri al
    sms_data = read_sms()

    # Doğrulama kodunu bul
    verification_code = find_verification_code(sms_data)

    if verification_code:
        print("Bulunan doğrulama kodu:", verification_code)
    else:
        print("Doğrulama kodu bulunamadı.")

except Exception as e:
    print("Hata oluştu:", e)