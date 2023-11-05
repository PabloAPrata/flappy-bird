import pygame
from sys import exit

pygame.init()
clock = pygame.time.Clock()

# Janela
win_height = 720
win_width = 550
window = pygame.display.set_mode((win_width, win_height))


def quit_game():
    # Sair do Jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def main():
    run = True
    while run:
        quit_game()

        window.fill((0, 0, 0))
        clock.tick(60)
        pygame.display.update()


main()
