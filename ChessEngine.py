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
        self.ending_ = None
        self.from_where_ = ''
        self.to_where_ = []
        self.instructions_ = False

    def move(self):
        print(self.board_.legal_moves)
        self.listener_.listen()
        move = self.listener_.move_
        if self.listener_.checking_:
            try:
                print(move)
                self.from_where_ = move
                self.checking_moves(move)
                self.listener_.checking_ = False
            except ValueError:
                winsound.PlaySound("wrong_move_pl.wav", winsound.SND_FILENAME)
                return False
        else:
            if move == 39:
                self.instruction = True
            elif move == 40:
                self.instruction = False
            elif move != '':
                self.from_where_ = ''
                self.to_where_ = []
                try:
                    print(move)
                    self.board_.push_san(move)
                    self.listener_.move_ = ''
                    if self.board_.is_check():
                        winsound.PlaySound("check_pl.wav", winsound.SND_FILENAME)

                    return False
                except ValueError:
                    winsound.PlaySound("wrong_move_pl.wav", winsound.SND_FILENAME)
                    return False


    def console_view(self):
        print(self.board_)

    def console_move(self):

        move = self.listener_.move_
        if move == 39:
            self.instruction = True
        elif move == 40:
            self.instruction = False
        else:
            print(self.board_.legal_moves)
            try:
                self.board_.push_san(input("Please make a move: "))

            except ValueError:
                print("illegal move")

    def checking_all_ends(self):

        """
        return true if it is end/[checkmate, insufficient_material, five_fold_repetition, stalemate]
        """

        # checkmate
        if self.board_.is_checkmate():
            winsound.PlaySound("checkmate_pl.wav", winsound.SND_FILENAME)
            self.ending_ = 'checkmate'
            return True
        # insufficient material
        elif self.board_.is_insufficient_material():
            winsound.PlaySound("insufficient_material_pl.wav", winsound.SND_FILENAME)
            self.ending_ = 'insufficient_material'
            return True
        # fivefold_repetition
        elif self.board_.is_fivefold_repetition():
            winsound.PlaySound("fivefold_repetition_pl.wav", winsound.SND_FILENAME)
            self.ending_ = 'fivefold_repetition'
            return True
        # stalemate
        elif self.board_.is_stalemate():
            winsound.PlaySound("stalemate_pl.wav", winsound.SND_FILENAME)
            self.ending_ = 'stalemate'
            return True
        else:
            return False

    def checking_moves(self, from_where):
        moves = self.board_.legal_moves
        list_of_moves = []
        for move in moves:
            if from_where in move.uci():
                list_of_moves.append(move.uci()[2:])
        self.to_where_ = list_of_moves

