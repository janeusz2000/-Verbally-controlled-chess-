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
        pass

    @staticmethod
    def check_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

    def load_texture(self):
        self.screen_.fill((0, 0, 0))
        self.screen_.blit(pygame.image.load('ChessArt/texture.png').convert(), (0, 0))


    def update_screen(self):
        pygame.display.update()

#     def __init__(self):
#         self.screen_ = pygame.display.set_mode([800, 800])
#
#
# while True:
#
#
#
#
#
#
#     # EVENTS
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit(0)
