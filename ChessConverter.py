import ChessEngine


class ChessConverter(object):

    # constructor
    def __init__(self):
        print("converter")

    def convert(self, c):
        converted = ''
        if c != '':
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
                if len(command) >= 4:
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
                if len(command) >= 5:
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
                    elif command[4] == "ha":
                        converted += 'h'
                if len(command) >= 6:
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

        else:
            converted = ''

        return converted

    def convert_pos(self, c):
        converted = ''
        if c != '':
            command = c.split()
            if len(command) == 3:
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

                if command[2] == "jeden":
                    converted += "1"
                elif command[2] == "dwa":
                    converted += "2"
                elif command[2] == "trzy":
                    converted += "3"
                elif command[2] == "cztery":
                    converted += "4"
                elif command[2] == "pięć":
                    converted += "5"
                elif command[2] == "sześć":
                    converted += "6"
                elif command[2] == "siedem":
                    converted += "7"
                elif command[2] == "osiem":
                    converted += "8"
        else:
            converted = ''
        return converted

    def convert_field_for_gui(self, c):
        X = 0
        Y = 0
        if c[1] == 8:
            X = 0
        elif c[1] == 7:
            X = 1
        elif c[1] == 6:
            X = 2
        elif c[1] == 5:
            X = 3
        elif c[1] == 4:
            X = 4
        elif c[1] == 3:
            X = 5
        elif c[1] == 2:
            X = 6
        elif c[1] == 1:
            X = 7
        if c[0]=="a":
            Y = 7
        elif c[0]=="b":
            Y = 6
        elif c[0]=="c":
            Y = 5
        elif c[0]=="d":
            Y = 4
        elif c[0]=="e":
            Y = 3
        elif c[0]=="f":
            Y = 2
        elif c[0]=="g":
            Y = 1
        elif c[0]=="h":
            Y = 0
        wsp = [(X*75+20), (Y*75+20)]
        return wsp
        # Pole A7(2 * 75 + 20, 1 * 75 + 20)
        # Pole A8 (1 * 75 + 20, 1 * 75 + 20)
