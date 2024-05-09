import random

def tahmin_oyunu():
    print("=== Sayı Tahmin Oyununa Hoş Geldiniz ===")
    print("1 ile 100 arasında bir sayıyı tahmin edin.")
    print("Oyundan çıkmak için 'q' tuşuna basabilirsiniz.")

    secret_number = random.randint(1, 100)

    while True:
        try:
            guess = input("\nTahmininiz: ")

            if guess.lower() == 'q':
                print("Oyundan çıkılıyor...")
                break

            guess = int(guess)
            if guess == secret_number:
                print("Tebrikler! Doğru tahmin ettiniz.")
                break
            elif guess < secret_number:
                print("Daha yüksek bir sayı tahmin edin.")
            else:
                print("Daha düşük bir sayı tahmin edin.")

        except ValueError:
            print("Geçersiz giriş! Lütfen bir tamsayı girin.")

    print("Oyundan çıkış yaptınız. İyi günler!")

# Oyunu başlat
tahmin_oyunu()