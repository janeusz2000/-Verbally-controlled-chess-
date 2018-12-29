""" initializating program from here"""

import Commander
import ChessConverter

#c = ChessConverter.ChessConverter()
#converted = c.convert("skoczek ef pięć bije a trzy")
#con = c.convert("pionek gie sześć bije ef siedem")

GameCommander = Commander.Commander()
GameCommander.game_run(iteration_number=15) # iteration number = ile łacznie zostanie wykonanych ruchów
