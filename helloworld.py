import pygame, sys

pygame.init()

window_size = (800, 600)

screen = pygame.display.set_mode(window_size)

myriadProFont = pygame.font.SysFont("Myriad Pro", 48)

hw = myriadProFont.render("Hello world!", 1, (255, 0, 255), (255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(hw, (0,0))
    pygame.display.update()