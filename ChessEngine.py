# This is main program running chess

import chess
import Listener
import winsound


class ChessEngine:

    # constructor

    def __init__(self, manual_input):
        self.board_ = chess.Board("rnbq1bnr/pppPk1pp/8/8/8/4p3/PPP2PPP/RNBQKBNR w KQ - 1 6")
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
        else:
            if move != '':
                self.from_where_ = ''
                self.to_where_ = []
                try:
                    print(move)
                    self.board_.push_san(move)
                    self.listener_.move_ = ''
                    if self.board_.is_check():
                        winsound.PlaySound("check_pl.wav", winsound.SND_FILENAME)
                except ValueError:
                    if self.is_end_of_board() == False:
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

    def is_end_of_board(self):
        moves = self.board_.legal_moves
        move_ = self.listener_.move_
        move_.replace(move_[1], "x")
        change = False
        if len(move_) == 4:
            for move in moves:
                if move_ in move.uci():
                    winsound.PlaySound("ask_for_figure_pl.wav", winsound.SND_FILENAME)
                    self.listener_.listen()
                    move_ = move_ + "=" + self.listener_.move_
                    try:
                        print(move_)
                        self.board_.push_san(move_)
                        change = True
                        self.listener_.move_ = ''
                        if self.board_.is_check():
                            winsound.PlaySound("check_pl.wav", winsound.SND_FILENAME)
                        break
                    except ValueError:
                        winsound.PlaySound("wrong_move_pl.wav", winsound.SND_FILENAME)
        return change
