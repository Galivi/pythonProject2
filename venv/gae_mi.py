import  pygame, random, time, sys

pygame.init()
screen = pygame.display.set_mode((1200, 600))

charater_image = pygame.image.load('pongi.png').convert()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(charater_image, (100, 100))

    pygame.display.update()
