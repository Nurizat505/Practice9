import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Moving Ball")

x = 300
y = 200
speed = 20
radius = 25

running = True

while running:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x - speed - radius >= 0:
                    x -= speed

            if event.key == pygame.K_RIGHT:
                if x + speed + radius <= 600:
                    x += speed

            if event.key == pygame.K_UP:
                if y - speed - radius >= 0:
                    y -= speed

            if event.key == pygame.K_DOWN:
                if y + speed + radius <= 400:
                    y += speed

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)

    pygame.display.update()

pygame.quit()