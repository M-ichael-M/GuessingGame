import pygame
import numpy as np
import time
import Constants
import DataProperty
import Model

def realtime(img):
    layer1_3 = []
    listPX = DataProperty.property(img)

    for i in range(len(Model.elements)):
        layer1_1 = (Model.layer1_1(listPX, Model.elements[i].weights1_1))
        layer1_2 = (Model.layer1_2(listPX, layer1_1, Model.elements[i].weights1_2))
        full = (Model.layer1_1(Constants.full, Model.elements[i].weights1_1))
        layer1_3.append(Model.layer1_3(layer1_2, full))

    maxResult = max(layer1_3)
    idOfMax = layer1_3.index(maxResult)

    print(Model.elements[idOfMax].label)
    
    # Ta funkcja może wykorzystać tablicę img, która przechowuje informacje o pikselach
    # img to trójwymiarowa tablica, gdzie każdy wiersz zawiera RGB pikseli w danym rzędzie

def init_UI():
    # Inicjalizacja
    pygame.init()

    # Wymiary ekranu
    width, height = 500, 500

    # Tworzenie ekranu
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Prosty Edytor")

    # Kolor czarny
    black = (0, 0, 0)

    # Powierzchnia do rysowania
    drawing_surface = pygame.Surface((width, height))
    drawing_surface.fill((255, 255, 255))  # Wypełnienie białym kolorem

    # Dwuwymiarowa tablica na piksele
    pixel_array = np.full((height, width, 3), 255, dtype=np.uint8)  # Rozmiar 3 reprezentuje RGB

    # Główna pętla programu
    drawing = False
    running = True
    last_realtime = time.time()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Lewy przycisk myszy
                    drawing = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False

            elif event.type == pygame.MOUSEMOTION and drawing:
                try:
                    x, y = event.pos
                    pygame.draw.circle(drawing_surface, black, (x, y), 4)  # Rysowanie czarnym kolorem
                    pixel_array[y][x] = black  # Aktualizacja wartości piksela w tablicy

                    # Przesyłanie informacji o pikselach do funkcji realtime co 0,5 sekundy
                    __current_time = time.time()
                    if __current_time - last_realtime >= 0.5:
                        realtime(pixel_array)
                        last_realtime = __current_time
                except:
                    pass

        # Rysowanie powierzchni do ekranu
        screen.blit(drawing_surface, (0, 0))
        pygame.display.flip()

    # Zakończenie programu
    pygame.quit()
