import tkinter
import Listener


class Instructions(object):
    def __init__(self, f, t):
        self.file_ = f
        self.title_ = t
        self.tk_ = tkinter.Tk()
        self.tk_.title(self.title_)
        self.var_ = tkinter.StringVar()
        self.label_ = tkinter.Message(self.tk_, textvariable=self.var_)
        file = open(self.file_, mode='r')
        self.instructions_ = file.read()
        self.var_.set(self.instructions_)
        file.close()
        self.label_.pack()

    def show_instructions(self):
        self.tk_.mainloop()
        while True:  # making a loop
            try:
                if keyboard.is_pressed('space'):
                    os.system('python run_sarmata.py')
                    f = open("result.txt", "r")
                    command = f.read()
                    if command == "zamknij instrukcje":
                        self.close_instructions()
                    f.close()
                    break
                else:
                    pass
            except:
                break

    def close_instructions(self):
        self.tk_.destroy()

