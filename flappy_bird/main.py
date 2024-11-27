import pygame

pygame.init()

WIDTH = 864
HEIGHT = 936
run = True
ground_scroll = 0
scroll_speed = 4


screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("flappy bird")

bg_image = pygame.image.load("img/bg.png")

ground = pygame.image.load("img/ground.png")

while run:
    screen.blit(bg_image,(0,0))
    screen.blit(ground,(ground_scroll,768))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()