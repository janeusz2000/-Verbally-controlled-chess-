# This is main program running chess

import chess
import Listener
import ChessConverter
import Instructions


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

        print(self.board_.legal_moves)
        message = self.listener.listen()
        instructions = Instructions.Instructions("instructions_pl.txt", "instrukcje gry")
        if message == "Włącz instrukcje" or message == "Pokaż instrukcje":
            instructions.show_instructions()
        if message == "Wyłącz instrukcje" or message == "Zamknij instrukcje":
            instructions.close_instructions()
        command = self.converter.convert(c=message)
        self.board_.push_san(command)


    def console_view(self):
        print(self.board_)

