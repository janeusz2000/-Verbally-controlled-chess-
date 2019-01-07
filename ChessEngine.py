# This is main program running chess

import chess
import Listener
import ChessConverter
import Instructions
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
        self.listener = Listener.Listener()
        self.converter = ChessConverter.ChessConverter()

    def move(self):
        instructions = Instructions.Instructions("instructions_pl.txt", "instrukcje gry")
        print(self.board_.legal_moves)
        while True:
            message = self.listener.listen()
            if message == "włącz instrukcje" or message == "pokaż instrukcje":
                instructions.show_instructions()
            if message == "wyłącz instrukcje" or message == "zamknij instrukcje":
                instructions.close_instructions()
            move = self.converter.convert(c=message)
            move = chess.Move.from_uci(move)
            if move in self.board_.legal_moves:
                self.board_.push(move)
                break
            else:
                winsound.PlaySound("wrong_move_pl.wav", winsound.SND_FILENAME)
                continue

    def console_view(self):
        print(self.board_)

