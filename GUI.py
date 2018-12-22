"""this program is responsible for graphic representation of current chess board"""
import pygame
import sys
import ChessEngine


class GUI(object):
    def __init__(self):
        pygame.init()
        self.screen_ = pygame.display.set_mode([800, 800])

    def __del__(self):
        pygame.quit()

    def read_game(self, chess_board):

        # TO DO

        pass

    def load_texture(self):
        self.screen_.fill((0, 0, 0))
        self.screen_.blit(pygame.image.load('ChessArt/texture.png').convert(), (0, 0))

    def update_screen(self):
        pygame.display.update()

    @staticmethod
    def check_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

