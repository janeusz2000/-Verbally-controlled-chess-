<<<<<<< HEAD
# This is main program running chess
#
# Couple of examples how moves are made:
# >>> board.push_san("e4")
# Move.from_uci('e2e4')
# >>> board.push_san("e5")
# Move.from_uci('e7e5')
# >>> board.push_san("Qh5")
# Move.from_uci('d1h5')
# >>> board.push_san("Nc6")
# Move.from_uci('b8c6')
# >>> board.push_san("Bc4")
# Move.from_uci('f1c4')
# >>> board.push_san("Nf6")
# Move.from_uci('g8f6')
# >>> board.push_san("Qxf7")
# Move.from_uci('h5f7')
#
# >>> board.is_checkmate()
#

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
            move = chess.Move.from_uci(input("Please make a move"))
            self.board_.push(move=move)

    def console_view(self):
        print(self.board_)






=======
# This is main program running chess
#
# Couple of examples how moves are made:
# >>> board.push_san("e4")
# Move.from_uci('e2e4')
# >>> board.push_san("e5")
# Move.from_uci('e7e5')
# >>> board.push_san("Qh5")
# Move.from_uci('d1h5')
# >>> board.push_san("Nc6")
# Move.from_uci('b8c6')
# >>> board.push_san("Bc4")
# Move.from_uci('f1c4')
# >>> board.push_san("Nf6")
# Move.from_uci('g8f6')
# >>> board.push_san("Qxf7")
# Move.from_uci('h5f7')
#
# >>> board.is_checkmate()
#

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
            move = chess.Move.from_uci(input("Please make a move"))
            self.board_.push(move=move)

    def console_view(self):
        print(self.board_)






>>>>>>> d269694eea858310c264b6adf698d61bfd150415
