import random

# Kullanıcı bilgileri (örnek olarak)
kullanici_bilgileri = {
    "telefon_numarasi": "5511918803",
    "dogrulama_kodu": None,
    "ikinci_telefon_numarasi": "5557654321"  # İkinci telefon numarası örneği
}

# SMS gönderme fonksiyonu (gerçek hizmet yerine kullanılacak)
def sms_gonder(telefon_numarasi, icerik):
    print(f"Telefon numarasına ({telefon_numarasi}) şu mesaj gönderildi: {icerik}")

# Doğrulama kodu oluşturma fonksiyonu
def dogrulama_kodu_olustur():
    return str(random.randint(1000, 9999))  # Rastgele 4 basamaklı bir kod oluştur

# SMS doğrulama işlemi
def sms_dogrulama():
    # Kullanıcıya doğrulama kodu oluştur ve telefonuna gönder
    dogrulama_kodu = dogrulama_kodu_olustur()
    kullanici_bilgileri["dogrulama_kodu"] = dogrulama_kodu

    sms_icerik = f"SMS Doğrulama Kodunuz: {dogrulama_kodu}"
    sms_gonder(kullanici_bilgileri["telefon_numarasi"], sms_icerik)

    # Kullanıcıdan doğrulama kodunu girmesini iste
    girilen_kod = input("Telefonunuza gönderilen doğrulama kodunu girin: ")

    # Girilen kodu doğrula
    if girilen_kod == dogrulama_kodu:
        print("Doğrulama başarılı! Giriş yapabilirsiniz.")
        ikinci_sms_gonder()  # Başarı durumunda ikinci SMS gönderme işlemi
    else:
        print("Doğrulama başarısız! Lütfen doğru kodu girin.")

# Başarı durumunda ikinci SMS gönderme işlemi
def ikinci_sms_gonder():
    ikinci_sms_icerik = "Başarıyla giriş yapıldı. İyi günler!"
    sms_gonder(kullanici_bilgileri["ikinci_telefon_numarasi"], ikinci_sms_icerik)

# Ana program
if __name__ == "__main__":
    sms_dogrulama()
