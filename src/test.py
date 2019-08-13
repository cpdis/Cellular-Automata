import pygame

white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 165, 0)


pygame.init()
display = pygame.display.set_mode((1280, 1024))
pygame.display.set_caption('ReflectOS')

exit = False

while not exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        print(event)

    display.fill(white)
    pygame.display.update()

pygame.quit()
quit()
