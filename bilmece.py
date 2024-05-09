import random

# Bilmece ve cevapları
bilmeceler = {
    "Bir öküzün favori müziği nedir?": "Haydi durma hop hop!",
    "Hangi saat asla çalışmaz?": "Kum saati",
    "Hangi piller en uzun süre dayanır?": "Dışarıda kullanılan piller",
    "Hangi yıl yeni yıldan önce gelir?": "Sonraki yıl",
    "En hızlı sayı hangisidir?": "Koşu",
    "Hangi araba sürekli sıfırda kalır?": "Polis arabası"
}

# Rastgele bir bilmece seçme
soru = random.choice(list(bilmeceler.keys()))

# Kullanıcıya bilmeceyi sor
print("Bilmece: " + soru)

# Kullanıcıdan cevabı al
cevap = input("Cevabınız nedir? ")

# Cevabı kontrol et
if cevap.lower() == bilmeceler[soru].lower():
    print("Doğru! Tebrikler.")
else:
    print("Yanlış cevap. Doğru cevap: " + bilmeceler[soru])
