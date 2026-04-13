import pygame
import datetime

def draw_clock(screen, sec_hand, min_hand, width, height):
    center = (width // 2, height // 2)

    now = datetime.datetime.now()

    sec_angle = -(now.second * 6)
    min_angle = -((now.minute + now.second / 60) * 6)

    screen.fill((255, 255, 255))

    min_rot = pygame.transform.rotate(min_hand, min_angle)
    min_rect = min_rot.get_rect(center=center)
    screen.blit(min_rot, min_rect)

    sec_rot = pygame.transform.rotate(sec_hand, sec_angle)
    sec_rect = sec_rot.get_rect(center=center)
    screen.blit(sec_rot, sec_rect)

    pygame.draw.circle(screen, (0, 0, 0), center, 12)