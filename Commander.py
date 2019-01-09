""" This is main commander """
import ChessEngine
import GUI
import ChessConverter
import Instructions
import keyboard


class Commander(object):

    # constructor
    def __init__(self):
        self.instructions_ = Instructions.Instructions("instructions_pl.txt", "instrukcje gry")
        self.instructions_.show_instructions()
        self.chess_engine_ = ChessEngine.ChessEngine(True)
        self.gui_ = GUI.GUI()

    def game_run(self):

        local_iteration = 1

        while True:

            self.gui_.load_texture()
            self.gui_.check_events()

            temp = self.gui_.read_game(self.chess_engine_)
            self.gui_.paint_figures(temp)
            if keyboard.is_pressed('space'):
                self.chess_engine_.console_move()

            self.gui_.clock()
            self.gui_.display_flip()
            if self.chess_engine_.checking_all_ends():
                self.gui_.ending(self.chess_engine_.ending_)
                self.gui_.update_screen()

            self.gui_.update_screen()
