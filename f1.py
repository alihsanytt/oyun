import random
import time

class F1Car:
    def __init__(self, name):
        self.name = name
        self.speed = random.uniform(150, 200)  # Araç hızı (km/s)
        self.position = 0

    def move(self):
        self.position += self.speed * random.uniform(0.8, 1.2)  # Rastgele hız değişimi

    def display(self):
        print(f"{self.name} {self.position:.1f} km")

# Yarış araçlarını oluştur
car1 = F1Car("Mercedes")
car2 = F1Car("Ferrari")
car3 = F1Car("Red Bull")
cars = [car1, car2, car3]

race_distance = 300  # Yarış mesafesi (km)

print("F1 Yarışı Başlıyor!\n")

while True:
    for car in cars:
        car.move()
        car.display()
    
    print("")  # Arayüzde boşluk oluştur

    # Bir araç yarışı bitirdiyse
    if any(car.position >= race_distance for car in cars):
        winner = max(cars, key=lambda car: car.position)
        print(f"{winner.name} yarışı kazandı!")
        break
    
    time.sleep(1)  # Yarışı bir saniye beklet

print("\nYarış sona erdi.")
