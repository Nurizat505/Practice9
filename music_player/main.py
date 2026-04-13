import pygame
from player import MusicPlayer

pygame.init()

screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Music Player")

player = MusicPlayer("music/sample_tracks")

font = pygame.font.SysFont(None, 32)

def draw_button(text, x, y, w, h):
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, (0, 0, 0), rect, 2)

    label = font.render(text, True, (0, 0, 0))
    screen.blit(label, (x + 10, y + 10))

    return rect

running = True

while running:
    screen.fill((255, 255, 255))

    # ===== ТЕКСТ =====
    text = font.render(player.tracks[player.index], True, (0, 0, 0))
    screen.blit(text, (20, 20))

    # ===== КНОПКИ =====
    play_btn = draw_button("PLAY", 50, 120, 100, 50)
    stop_btn = draw_button("STOP", 170, 120, 100, 50)
    next_btn = draw_button("NEXT", 290, 120, 100, 50)
    prev_btn = draw_button("PREV", 410, 120, 100, 50)

    # ===== EVENTS =====
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_btn.collidepoint(event.pos):
                player.play()

            if stop_btn.collidepoint(event.pos):
                player.stop()

            if next_btn.collidepoint(event.pos):
                player.next()

            if prev_btn.collidepoint(event.pos):
                player.prev()

    pygame.display.flip()

pygame.quit()