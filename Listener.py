"""This in listener who so gonna react to commends"""
import os
import run_sarmata
import keyboard
import Instructions
import ChessConverter
import sys
import winsound


class Listener(object):

    # constructor
    def __init__(self):
        self.exit_game_ = False
        self.message_ = ''
        self.move_ = ''
        self.converter_ = ChessConverter.ChessConverter()

    # temporary managing to end program
    def listen(self):
        instructions = Instructions.Instructions("instructions_pl.txt", "instrukcje gry")
        try:
            self.move_ = ''
            os.system('python run_sarmata.py')
            f = open("result.txt", "r")
            self.message_ = f.read()
            if self.message_ == "otwórz instrukcje" or self.message_ == "pokaż instrukcje":
                instructions.show_instructions()
            elif self.message_ == "poddaję się" or self.message_ == "poddaj się" \
                    or self.message_ == "zakończ grę" or self.message_ == "koniec gry" or self.message_ == "koniec":
                sys.exit(1)
            elif self.message_ == "repeat":
                winsound.PlaySound("repeat_pl.wav", winsound.SND_FILENAME)
                self.listen()
            else:
                self.move_ = self.converter_.convert(c=self.message_)
            f.close()
        except:
            pass

    def exit_game(self):
        self.exit_game_ = True

    def exit_variable(self):
        return self.exit_game_
