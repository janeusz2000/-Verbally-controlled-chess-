import ChessEngine


class ChessConverter(object):

    # constructor
    def __init__(self):
        print("converter")

    def convert(self, c):
        converted = ''
        # splitting to words "pionek e trzy na/zbij e cztery"
        command = c.split()

        if c == "roszada w stronę króla":
            converted += 'O-O'
        elif c == "roszada w stronę królowej":
            converted += 'O-O-O'
        else:
            if command[0] == "wieża":
                converted += 'R'
            elif command[0] == "skoczek":
                converted += 'N'
            elif command[0] == "laufer" or command[0] == "goniec":
                converted += 'B'
            elif command[0] == "królowa" or command[0] == "hetman":
                converted += 'Q'
            elif command[0] == "król":
                converted += 'K'
            elif command[0] == "pionek":
                converted = converted
            if command[3] == "zbij" or command[3] == "bije" or command[3] == "bij" or command[3] == "zbija":
                if command[1] == "a":
                    converted += 'a'
                elif command[1] == "be":
                    converted += 'b'
                elif command[1] == "ce":
                    converted += 'c'
                elif command[1] == "de":
                    converted += 'd'
                elif command[1] == "e":
                    converted += 'e'
                elif command[1] == "ef":
                    converted += 'f'
                elif command[1] == "gie":
                    converted += 'g'
                elif command[1] == "ha":
                    converted += 'h'
                converted += "x"
            if command[4] == "a":
                converted += 'a'
            elif command[4] == "be":
                converted += 'b'
            elif command[4] == "ce":
                converted += 'c'
            elif command[4] == "de":
                converted += 'd'
            elif command[4] == "e":
                converted += 'e'
            elif command[4] == "ef":
                converted += 'f'
            elif command[4] == "gie":
                converted += 'g'
            elif command[4] == "h":
                converted += 'h'
            if command[5] == "jeden":
                converted += "1"
            if command[5] == "dwa":
                converted += "2"
            if command[5] == "trzy":
                converted += "3"
            if command[5] == "cztery":
                converted += "4"
            if command[5] == "pięć":
                converted += "5"
            if command[5] == "sześć":
                converted += "6"
            if command[5] == "siedem":
                converted += "7"
            if command[5] == "osiem":
                converted += "8"

        return converted