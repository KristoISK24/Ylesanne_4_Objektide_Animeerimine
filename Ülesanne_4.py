import pygame
import sys
import random

# Initsialiseeri pygame
pygame.init()

# Ekraani suurus
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ülesanne 4 - Autode animatsioon")

# Lae pildid
bg = pygame.image.load("bg_rally.jpg")
red_car = pygame.image.load("f1_red.png")
blue_car = pygame.image.load("f1_blue.png")

# Punase auto algpositsioon
red_x = WIDTH // 2 - red_car.get_width() // 2
red_y = HEIGHT - red_car.get_height() - 30

# Siniste autode algandmed
blue_cars = [
    {"x": random.randint(100, WIDTH - 100), "y": random.randint(-300, -50)},
    {"x": random.randint(100, WIDTH - 100), "y": random.randint(-600, -100)}
]

# Skoor
score = 0
font = pygame.font.SysFont(None, 36)

# Kiirus
blue_speed = 4

# Kaadrisagedus
clock = pygame.time.Clock()

# Mängu tsükkel
running = True
while running:
    clock.tick(60)

    # Sündmused
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Taust
    screen.blit(bg, (0, 0))

    # Punane auto (ei liigu)
    screen.blit(red_car, (red_x, red_y))

    # Sinised autod liikumises
    for car in blue_cars:
        car["y"] += blue_speed
        screen.blit(blue_car, (car["x"], car["y"]))

        if car["y"] > HEIGHT:
            car["y"] = random.randint(-400, -100)
            car["x"] = random.randint(100, WIDTH - 100)
            score += 1  

    # Skoori kuvamine
    score_text = font.render("Skoor: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Uuenda ekraani
    pygame.display.flip()

# Lõpeta mäng
pygame.quit()
sys.exit()
