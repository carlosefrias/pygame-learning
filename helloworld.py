import pygame, sys

pygame.init()

window_size = (800, 600)

screen = pygame.display.set_mode(window_size)

myriadProFont = pygame.font.SysFont("Myriad Pro", 48)

hw = myriadProFont.render("Hello world!", 1, (255, 0, 255), (255, 255, 255))

x, y = 0, 0
clock = pygame.time.Clock()
while True:
    clock.tick(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0,0,0))
    screen.blit(hw, (x,y))
    if(x <= 800):
        x += 1
    else:
        x = 0
        y += 50
    if(y > 600):
        x, y = 0, 0
    pygame.display.update()