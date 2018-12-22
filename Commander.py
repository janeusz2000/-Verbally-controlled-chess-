<<<<<<< HEAD
""" This is main commander """
import ChessEngine
import GUI
import Listener
# initialization


class Commander(object):

    # constructor
    def __init__(self):
        self.chess_engine_ = ChessEngine.ChessEngine(True)
        self.gui_ = GUI.GUI()
        self.listener_ = Listener.Listener()

    def game_run(self, iteration_number):

        # main game loop
        local_iteration = 1
        while True:

            self.gui_.read_game(chess_board=self.chess_engine_)

            # temporary console view
            self.chess_engine_.console_view()
            self.chess_engine_.move()

            # ENDING PROGRAM HERE
            if local_iteration >= iteration_number:
                self.listener_.exit_game()
            else:
                local_iteration += 1








=======
""" This is main commander """
import ChessEngine
import GUI
import Listener
# initialization


class Commander(object):

    # constructor
    def __init__(self):
        self.chess_engine_ = ChessEngine.ChessEngine(True)
        self.gui_ = GUI.GUI()
        self.listener_ = Listener.Listener()

    def game_run(self, iteration_number):

        # main game loop
        local_iteration = 1
        while True:

            self.gui_.read_game(chess_board=self.chess_engine_)

            # temporary console view
            self.chess_engine_.console_view()
            self.chess_engine_.move()

            # ENDING PROGRAM HERE
            if local_iteration >= iteration_number:
                self.listener_.exit_game()
            else:
                local_iteration += 1








>>>>>>> d269694eea858310c264b6adf698d61bfd150415
