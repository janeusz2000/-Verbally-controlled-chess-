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
        self.listener_.listen()
        move = self.listener_.move_
        if move != '':
            try:
                print(move)
                self.board_.push_san(move)
                if self.board_.is_check():
                    winsound.PlaySound("check_pl.wav", winsound.SND_FILENAME)
            except ValueError:
                winsound.PlaySound("wrong_move_pl.wav", winsound.SND_FILENAME)


    def console_view(self):
        print(self.board_)

    def console_move(self):
        print(self.board_.legal_moves)
        try:
            self.board_.push_san(input("Please make a move: "))
        except ValueError:
            print("illegal move")

    def checking_all_ends(self):

        """

        return [checkmate, insufficient_material, five_fold_repetition, stalemate]
        """

        output = []

        # checkmate
        if self.board_.is_checkmate():
            output.append(True)
        else:
            output.append(False)

        # insufficient material
        if self.board_.is_insufficient_material():
            output.append(True)
        else:
            output.append(False)

        # fivefold_repetition
        if self.board_.is_fivefold_repetition():
            output.append(True)
        else:
            output.append(False)

        # stalemate
        if self.board_.is_stalemate():
            output.append(True)
        else:
            output.append(False)

        return output


