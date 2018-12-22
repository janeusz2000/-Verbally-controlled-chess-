# This is main program running chess

import chess


class ChessEngine:

    # constructor

    def __init__(self, manual_input):
        self.board_ = chess.Board()
        self.stalemate_ = False
        self.draw_ = False
        self.mate_ = False
        self.repetition_ = False
        self.check_ = False
        self.manual_input_ = manual_input

    def move(self):
        if self.manual_input_:
            print(self.board_.legal_moves)
            move = chess.Move.from_uci(input("Please make a move "))
            self.board_.push(move=move)

    def console_view(self):
        print(self.board_)

