import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Move Player")
x = 300
y = 200
speed = 5
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    screen.fill((25, 25, 40))
    pygame.draw.circle(screen, (50, 160, 255), (x, y), 25)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()