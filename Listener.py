"""This in listener who so gonna react to commends"""
import os
import run_sarmata


class Listener(object):

    # constructor
    def __init__(self):
        self.exit_game_ = False

    # temporary managing to end program
    def listen(self):
        x = input()
        if x == " ":
            os.system('python run_sarmata.py')

    def exit_game(self):
        self.exit_game_ = True

    def exit_variable(self):
        return self.exit_game_


