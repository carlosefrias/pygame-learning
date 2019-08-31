import pygame, sys

pygame.init()

window_size = (800, 600)

screen = pygame.display.set_mode(window_size)

myriadProFont = pygame.font.SysFont("Myriad Pro", 48)

hw = myriadProFont.render("Hello world!", 1, (255, 0, 255), (255, 255, 255))

hw_size = hw.get_size()
direction_x, direction_y = 1, 1

x, y = 0, 0
clock = pygame.time.Clock()
while True:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0,0,0))
    screen.blit(hw, (x,y))

    x += 5 * direction_x
    y += 5 * direction_y
    if x + hw_size[0] > 800 or x <= 0:
        direction_x *= -1
    if y + hw_size[1] > 600 or y <= 0:
        direction_y *= -1    
    pygame.display.update()