import pygame

pygame.init()

HEIGHT = 1000
WIDTH = 1000
CENTRE = (HEIGHT/2, WIDTH/2)
HZ = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def update(scrn):
    scrn.fill(WHITE)
    pygame.display.set_caption("The Dungeon")  # setting the title
    #image = pygame.image.load("D:\\Code\\NEA\\Images\\temp_knight_sprite.PNG")  # getting image from files
    #image = pygame.transform.scale(image, (500, 500))  # scales down image
    #scrn.blit(image, (250, 250))
    pygame.display.update()


if __name__ == "__main__":
    screen = pygame.display.set_mode((HEIGHT, WIDTH))
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(HZ)  # Capping frame rate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # When person closes program
                running = False
        update(screen)  # updates screen
    pygame.quit()
