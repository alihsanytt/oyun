import pygame
pygame.init()

# Pencere boyutları
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basit Platform Oyunu")

# Ana oyun döngüsü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Oyun işlemleri
    # Oyuncu kontrolleri, oyun mantığı vb.

    # Pencereyi güncelle
    pygame.display.update()

pygame.quit()