import pygame, sys

pygame.init()
# pygame.mixer.init()

window_size = (800, 600)

screen = pygame.display.set_mode(window_size)

hw = pygame.image.load('PS circle.png')

hw_size = hw.get_size()

# sound = pygame.mixer.Sound('Pluralsight.wav')

pygame.mouse.set_visible(False)

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
        # sound.stop()
        # sound.play()
    if y + hw_size[1] > window_size[1]:
        y = 600 - hw_size[1]
        # sound.stop()
        # sound.play()

    # if x==0 or y==0:
        # sound.stop()
        # sound.play()

    screen.blit(hw, (x,y))   
    pygame.display.update()