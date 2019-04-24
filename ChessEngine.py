# This is main program running chess

import chess
import Listener
import winsound


class ChessEngine:

    # constructor

    def __init__(self, manual_input):
        # "rnbq1bnr/pppPk1pp/8/8/8/4p3/PPP2PPP/RNBQKBNR w KQ - 1 6"

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

    def move(self):
        print(self.board_.legal_moves)
        self.listener_.listen()
        move = self.listener_.move_
        if self.is_move_legal(list(move), self.board_.legal_moves):
            move = self.check_with_legal_moves(move)
        if self.listener_.checking_:
            try:
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

    def is_move_legal(self, my_move, moves):
        # my_move should be a list of letters
        iterator = 0
        if len(my_move) >= 5:
            if my_move[0] == 'N' or my_move[0] == 'K' or my_move[0] == 'R' or my_move[0] == 'Q' or my_move[0] == 'B':
                my_move = my_move[1:]
        for m in moves:
            if list(m.uci()) == my_move:
                iterator = 1
        if iterator == 1:
            return True
        else:
            return False

    def check_one(self, move, index):
        move = list(move)
        moves = self.board_.legal_moves
        if self.is_move_legal(move, moves) == False:
            if move[index] == "a":
                move[index] = "h"
                if self.is_move_legal(move, moves) == True:
                    return move
                else:
                    move[index] = "e"
                    if self.is_move_legal(move, moves) == True:
                        return move
                    else:
                        move[index] = "a"
            elif move[index] == "b":
                move[index] = "d"
                if self.is_move_legal(move, moves) == True:
                    return move
                else:
                    move[index] = "b"
            elif move[index] == "d":
                move[index] = "b"
                if self.is_move_legal(move, moves) == True:
                    return move
                else:
                    move[index] = "d"
            elif move[index] == "e":
                move[index] = "f"
                if self.is_move_legal(move, moves) == True:
                    return move
                else:
                    move[index] = "e"
            elif move[index] == "f":
                move[index] = "e"
                if self.is_move_legal(move, moves) == True:
                    return move
                else:
                    move[index] = "f"
            elif move[index] == "h":
                move[index] = "a"
                if self.is_move_legal(move, moves) == True:
                    return move
                else:
                    move[index] = "h"
            elif move[index] == "c":
                print("checking not needed")
        move = "".join(move)
        return move

    def check_with_legal_moves(self, move):
        moves = self.board_.legal_moves
        move_list = list(move)
        for i in range(0, len(move_list)):
            if self.is_move_legal(move_list, moves) == False:
                move = self.check_one(move, i)
            if self.is_move_legal(move_list, moves) == True:
                break
        return move


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
        change = False
        move_ = self.listener_.move_
        if len(move_) == 4:
            moves = self.board_.legal_moves
            move_.replace(move_[1], "x")
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
