"""This in listener who so gonna react to commends"""
import os
import run_sarmata
import keyboard
import Instructions
import ChessConverter
import time


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
        while True:  # making a loop
            try:
                if keyboard.is_pressed('space'):
                    os.system('python run_sarmata.py')
                    f = open("result.txt", "r")
                    self.message_ = f.read()
                    self.message_ = "pionek a dwa na a cztery"
                    if self.message_ == "otwórz instrukcje" or self.message_ == "pokaż instrukcje":
                        instructions.show_instructions()
                    elif self.message_ == "zamknij instrukcje":
                        instructions.close_instructions()
                    elif self.message_ == "poddaję się" or self.message_ == "poddaj się" \
                            or self.message_ == "zakończ grę" or self.message_ == "koniec gry" or c == "koniec":
                        print("exit") # jeszcze trzeba połączyc z funkcja exit
                    else:
                        self.move_ = self.converter.convert(c=self.message_)
                    f.close()
                    break
                else:
                    pass
            except:
                break

    def exit_game(self):
        self.exit_game_ = True

    def exit_variable(self):
        return self.exit_game_


