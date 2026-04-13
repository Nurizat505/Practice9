import pygame
from clock import draw_clock

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

def main():
    hand_img = pygame.image.load("images/mickey_hand.png").convert_alpha()

    sec_hand = pygame.transform.smoothscale(hand_img, (500, 80))
    min_hand = pygame.transform.smoothscale(hand_img, (420, 100))

    clock = pygame.time.Clock()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_clock(screen, sec_hand, min_hand, WIDTH, HEIGHT)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()