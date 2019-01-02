"""This in listener who so gonna react to commends"""
import os
import run_sarmata
import keyboard
import time


class Listener(object):

    # constructor
    def __init__(self):
        self.exit_game_ = False
        self.message = ''

    # temporary managing to end program
    def listen(self):
        while True:  # making a loop
            try:
                if keyboard.is_pressed('space'):
                    os.system('python run_sarmata.py')
                    time.sleep(10)
                    f = open("result.txt", "r")
                    self.message = f.read()
                    f.close()
                    break
                else:
                    pass
            except:
                break
        return self.message

    def exit_game(self):
        self.exit_game_ = True

    def exit_variable(self):
        return self.exit_game_


