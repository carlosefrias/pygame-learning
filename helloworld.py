import pygame, sys

pygame.init()

window_size = (800, 600)

screen = pygame.display.set_mode(window_size)

myriadProFont = pygame.font.SysFont("Myriad Pro", 48)

hw = myriadProFont.render("Hello world!", 1, (255, 0, 255), (255, 255, 255))

hw_size = hw.get_size()
# direction_x, direction_y = 1, 1

# x, y = 0, 0
clock = pygame.time.Clock()
while True:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0,0,0))
    mouse_pos = pygame.mouse.get_pos()
    x, y = mouse_pos
    if x + hw_size[0] > window_size[0]:
        x = 800 - hw_size[0]
    if y + hw_size[1] > window_size[1]:
        y = 600 - hw_size[1]
    screen.blit(hw, (x,y))   
    pygame.display.update()