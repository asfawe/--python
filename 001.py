import pygame

FPS = 60

pygame.init()

screen = pygame.display.set_mode((500, 600))
clock = pygame.time.Clock()

running = True

while running:
    clock.tick(FPS) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((0,255,0))
    pygame.display.update()
pygame.quit()