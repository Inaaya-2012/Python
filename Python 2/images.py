import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((400,500))
pygame.display.set_caption("Image window")
screen.fill("Turqoise")

bg_surf = pygame.transform.scale(pygame.image.load("background.jpeg").convert(),(400,400))

next_surf = pygame.transform.scale(pygame.image.load("penguin.png").convert(),(400,400))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        screen.bilt(bg_surf,(0,0))
        screen.bilt(next_surf,(0,0))
        
    pygame.display.update()   
