""" This is main commander """
import ChessEngine
import GUI
import Listener
# initialization


class Commander(object):

    # constructor
    def __init__(self):
        self.chess_engine_ = ChessEngine.ChessEngine(True)
        self.listener_ = Listener.Listener()
        self.gui_ = GUI.GUI()

    def game_run(self, iteration_number):

        local_iteration = 1

        while True:

            self.gui_.load_texture()
            self.gui_.check_events()
            self.gui_.update_screen()

            self.gui_.read_game(chess_board=self.chess_engine_) # TO DO

            # =====================================

            # # temporary console view
            # self.chess_engine_.console_view()
            # self.chess_engine_.move()
            #
            # # ENDING PROGRAM HERE
            # if local_iteration >= iteration_number:
            #     self.listener_.exit_game()
            # else:
            #     local_iteration += 1






