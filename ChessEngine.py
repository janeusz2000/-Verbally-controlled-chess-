# This is main program running chess

import chess
import Listener
import winsound


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
        self.listener_ = Listener.Listener()

    def move(self):

        print(self.board_.legal_moves)
        while True:
            self.listener_.listen()
            move = chess.Move.from_uci(self.listener_.move_)
            if move in self.board_.legal_moves:
                print("True")
                self.board_.push_san(move)
                break
            else:
                winsound.PlaySound("wrong_move_pl.wav", winsound.SND_FILENAME)
                continue

    def console_view(self):
        print(self.board_)

