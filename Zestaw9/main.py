import sys
from random import randint
import pygame


white = (255, 255, 255)
black = (0, 0, 0)




pygame.init()

size = width, height = (600, 700)

screen = pygame.display.set_mode(size)

pygame.display.set_caption('Catch all the snowflakes')

# CLOCK
FPS = 60   # frames per second setting
clock = pygame.time.Clock()

boxes = []
tick_time = 1500 # prędkosć pojawiania się moich zniezynek

speed = [0, 1]   #predkosc opadania sniezynek
prev_time = pygame.time.get_ticks()

points = 0
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # QUIT Event
            pygame.quit()   # deaktywacja pygame
            sys.exit("You managed to get " + str(points) + " points")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                point = event.pos
                for box in boxes:
                    if box.collidepoint(point):
                        boxes.remove(box)
                        points +=1

    time = pygame.time.get_ticks() # pobranie aktualnego czasu
    if time > 10000: # przyspieszenie pojawiania się i opadania płatków sniegu
        speed = [0, 2]
        tick_time = 750
    if time - prev_time > tick_time: # sniezynka ma się pojawiać co min. 1,5 s
        boxes.append(pygame.Rect(randint(0,550), 0, 50, 60))
        prev_time = time

    screen.fill(black) #na nowo malujemy prostokąty

    for box in boxes:
        box.move_ip(speed)
        pygame.draw.rect(screen, white, box)
        if(box.top > height): # reguła przegranej
            pygame.event.post(pygame.event.Event(pygame.QUIT))


    pygame.display.flip()

    clock.tick(FPS)
