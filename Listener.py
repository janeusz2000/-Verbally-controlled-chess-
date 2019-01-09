"""This in listener who so gonna react to commends"""
import os
import run_sarmata
import keyboard
import Instructions
import ChessConverter


class Listener(object):

    # constructor
    def __init__(self):
        self.exit_game_ = False
        self.message_ = ''
        self.move_ = ''
        self.converter_ = ChessConverter.ChessConverter()
        self.show_moves_ = False

    # temporary managing to end program
    def listen(self):
        instructions = Instructions.Instructions("instructions_pl.txt", "instrukcje gry")
        while True:  # making a loop
            try:
                if keyboard.is_pressed('space'):
                    self.show_moves_ = False
                    self.move_ = ''
                    os.system('python run_sarmata.py')
                    f = open("result.txt", "r")
                    self.message_ = f.read()
                    if self.message_ == "otwórz instrukcje" or self.message_ == "pokaż instrukcje":
                        instructions.show_instructions()
                        self.listen()
                    elif self.message_ == "zamknij instrukcje":
                        instructions.close_instructions()
                    elif self.message_ == "poddaję się" or self.message_ == "poddaj się" \
                            or self.message_ == "zakończ grę" or self.message_ == "koniec gry" or self.message_ == "koniec":
                        print("exit") # jeszcze trzeba połączyc z funkcja exit
                    elif self.message_ == "pokaż dostępne ruchy" or self.message_ == "pokaż możliwe ruchy":
                        self.show_moves_ = True
                    else:
                        self.move_ = self.converter_.convert(c=self.message_)
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


