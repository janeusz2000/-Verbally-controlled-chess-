"""this program is responsible for graphic representation of current chess board"""
import pygame
import sys
import ChessEngine
import chess
import time

class GUI(object):

    # constructor
    def __init__(self):
        pygame.init()

        self.black_pawn_ = pygame.image.load("ChessArt/BP.png")
        self.black_knight_ = pygame.image.load("ChessArt/BN.png")
        self.black_bishop_ = pygame.image.load("ChessArt/BB.png")
        self.black_king_ = pygame.image.load("ChessArt/BK.png")
        self.black_queen_ = pygame.image.load("ChessArt/BQ.png")
        self.black_rook_ = pygame.image.load("ChessArt/BR.png")

        self.white_pawn_ = pygame.image.load("ChessArt/WP.png")
        self.white_knight_ = pygame.image.load("ChessArt/WN.png")
        self.white_bishop_ = pygame.image.load("ChessArt/WB.png")
        self.white_king_ = pygame.image.load("ChessArt/WK.png")
        self.white_queen_ = pygame.image.load("ChessArt/WQ.png")
        self.white_rook_ = pygame.image.load("ChessArt/WR.png")

        self.screen_ = pygame.display.set_mode([600, 600])
        pygame.display.set_icon(self.black_king_)
        pygame.display.set_caption('Verbally Controlled Chess')

        self.clock_ = pygame.time.Clock()

    # destructor
    def __del__(self):
        pygame.quit()

    def number_check(self, number_):
        try:
            int(number_)
            return True
        except ValueError:
            return False

    def read_game(self, chess_board):

        board = chess_board.board_.epd()
        temp_board = []
        temp_row = []

        for position in board:

            if position == "/":
                temp_board.append(temp_row)
                temp_row = []
            elif position == " ":
                break
            else:
                if self.number_check(position):
                    for each in range(0, int(position)):
                        temp_row.append("_")
                else:
                    temp_row.append(position)

        temp_board.append(temp_row)
        return temp_board

    def figure(self, name):
        if name == "R":
            return self.white_rook_
        elif name == "N":
            return self.white_knight_
        elif name == "B":
            return self.white_bishop_
        elif name == "Q":
            return self.white_queen_
        elif name == "K":
            return self.white_king_
        elif name == "P":
            return self.white_pawn_
        elif name == "r":
            return self.black_rook_
        elif name == "n":
            return self.black_knight_
        elif name == "b":
            return self.black_bishop_
        elif name == "q":
            return self.black_queen_
        elif name == "k":
            return self.black_king_
        elif name == "p":
            return self.black_pawn_
        else:
            return False

    def paint_figures(self, temp_board):
        for row in range(0, 8):
            for column in range(0, 8):
                a = row * 75 + 6    # Y
                b = column * 75 + 6     # X
                if self.figure(temp_board[row][column]) == False:
                    pass
                else:
                    self.screen_.blit(self.figure(temp_board[row][column]), (b, a))

    def load_texture(self):
        self.screen_.fill((0, 0, 0))
        self.screen_.blit(pygame.image.load('ChessArt/texture_mid_2.png').convert(), (0, 0))

    def update_screen(self):
        pygame.display.update()

    def instructions(self):
        print("jaaa")

    def clock(self):
        self.clock_.tick(60)

    @staticmethod
    def check_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

    @staticmethod
    def display_flip():
        pygame.display.flip()



