""" This is main commander """
import ChessEngine
import GUI
import ChessConverter
import Instructions
import keyboard
import time


class Commander(object):

    # constructor
    def __init__(self):
        self.instructions_ = Instructions.Instructions("instructions_pl.txt", "instrukcje gry")
        self.instructions_.show_instructions()
        self.chess_engine_ = ChessEngine.ChessEngine(True)
        self.gui_ = GUI.GUI()

    def game_run(self):
        END = False
        local_iteration = 1

        while True:

            # texture
            if not END:
                self.gui_.load_texture()

            # events
            self.gui_.check_events()

            # game
            temp = self.gui_.read_game(self.chess_engine_)

            # painting game
            if not END:
                self.gui_.paint_figures(temp)

            # making move
            if keyboard.is_pressed('space'):
                self.chess_engine_.console_move()

            # decreasing CPU usage
            self.gui_.clock()

            # flip display
            self.gui_.display_flip()

            # checking game events
            if self.chess_engine_.checking_all_ends():
                END = True
                self.gui_.update_screen()
                time.sleep(1)
                self.gui_.ending(self.chess_engine_.ending_)
                self.gui_.update_screen()

            # refreshing screen
            self.gui_.update_screen()
