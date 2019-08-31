import pygame, sys

pygame.init()
# pygame.mixer.init()

window_size = (800, 600)

screen = pygame.display.set_mode(window_size)

hw = pygame.image.load('PS circle.png')

hw_size = hw.get_size()

# sound = pygame.mixer.Sound('Pluralsight.wav')

pygame.mouse.set_visible(False)

x, y = 0, 0

clock = pygame.time.Clock()
while True:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x += 5
            if event.key == pygame.K_LEFT:
                x -=5
            if event.key == pygame.K_DOWN:
                y += 5
            if event.key == pygame.K_UP:
                y -= 5
    screen.fill((0,0,0))
    if x + hw_size[0] > window_size[0]:
        x = 800 - hw_size[0]
        # sound.stop()
        # sound.play()
    if y + hw_size[1] > window_size[1]:
        y = 600 - hw_size[1]
        # sound.stop()
        # sound.play()

    if x <= 0:
        x = 0
        # sound.stop()
        # sound.play()
    
    if y <= 0:
        y = 0
        # sound.stop()
        # sound.play()
        

    screen.blit(hw, (x,y))   
    pygame.display.update()