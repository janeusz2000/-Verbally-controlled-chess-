"""This in listener who so gonna react to commends"""


class Listener(object):

    # constructor
    def __init__(self):
        self.exit_game_ = False

    # temporary managiing to end program
    def exit_game(self):
        self.exit_game_ = True

    def exit_variable(self):
        return self.exit_game_
