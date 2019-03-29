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
        self.instruction = False

    def move(self):
        print(self.board_.legal_moves)
        self.listener_.listen()
        move = self.listener_.move_
        print(move)
        # move = self.check_with_legal_moves(move)
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

    def check_one(self, move, index):
        print("start of checking")
        while True:
            if move[index] == "a":
                move[index] = "h"
                if move in self.board_.legal_moves:
                    print("success")
                    break
                else:
                    move[index] = "e"
                    if move in self.board_.legal_moves:
                        print("success")
                        break
                    else:
                        move[index] = "a"
            elif move[index] == "b":
                move[index] = "d"
                if move in self.board_.legal_moves:
                    print("success")
                    break
                else:
                    move[index] = "d"
            elif move[index] == "d":
                move[index] = "b"
                if move in self.board_.legal_moves:
                    print("success")
                    break
                else:
                    move[index] = "b"
            elif move[index] == "e":
                move[index] = "f"
                if move in self.board_.legal_moves:
                    print("success")
                    break
                else:
                    move[index] = "e"
            elif move[index] == "f":
                move[index] = "e"
                if move in self.board_.legal_moves:
                    print("success")
                    break
                else:
                    move[index] = "f"
            elif move[index] == "h":
                move[index] = "a"
                if move in self.board_.legal_moves:
                    print("success")
                    break
                else:
                    move[index] = "h"
                    break
            elif move[index] == "c":
                print("checking not needed")
                break
        return move

    def check_with_legal_moves(self, move):
        while True:
            if move not in self.board_.legal_moves:
                if move[1] == "a":
                    move[1] = "h"
                    if move in self.board_.legal_moves:
                        print("success")
                        break
                    else:
                        move = self.check_one(move, 3)
                        if move in self.board_.legal_moves:
                            print("success")
                            break
                        else:
                            move[1] = "e"
                            if move in self.board_.legal_moves:
                                print("success")
                                break
                            else:
                                move = self.check_one(move, 3)
                                if move in self.board_.legal_moves:
                                    print("success")
                                    break
                                else:
                                    move[1] = "a"
                elif move[1] == "b":
                    move[1] = "d"
                    if move in self.board_.legal_moves:
                        print("success")
                        break
                    else:
                        move = self.check_one(move, 3)
                        if move in self.board_.legal_moves:
                            print("success")
                            break
                        else:
                            move[1] = "b"
                elif move[1] == "d":
                    move[1] = "b"
                    if move in self.board_.legal_moves:
                        print("success")
                        break
                    else:
                        move = self.check_one(move, 3)
                        if move in self.board_.legal_moves:
                            print("success")
                            break
                        else:
                            move[1] = "d"
                elif move[1] == "e":
                    move[1] = "f"
                    if move in self.board_.legal_moves:
                        print("success")
                        break
                    else:
                        move = self.check_one(move, 3)
                        if move in self.board_.legal_moves:
                            print("success")
                            break
                        else:
                            move[1] = "e"
                elif move[1] == "f":
                    move[1] = "e"
                    if move in self.board_.legal_moves:
                        print("success")
                        break
                    else:
                        move = self.check_one(move, 3)
                        if move in self.board_.legal_moves:
                            print("success")
                            break
                        else:
                            move[1] = "f"
                elif move[1] == "h":
                    move[1] = "a"
                    if move in self.board_.legal_moves:
                        print("success")
                        break
                    else:
                        move = self.check_one(move, 3)
                        if move in self.board_.legal_moves:
                            print("success")
                            break
                        else:
                            move[1] = "h"
                elif move[1] == "c":
                    print("checking not needed")
                else:
                    self.check_one(move, 3)
        return move

