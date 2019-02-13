import tkinter
import Listener
import os


class Instructions(object):
    def __init__(self, f, t):
        self.file_ = f
        self.title_ = t
        self.tk_ = tkinter.Tk()
        self.tk_.title(t)
        self.var_ = tkinter.StringVar()
        self.label_ = tkinter.Message(self.tk_, textvariable=self.var_)
        file = open(self.file_, mode='r')
        self.instructions_ = file.read()
        self.var_.set(self.instructions_)
        file.close()
        self.label_.pack()

    def quit(self, event=None):
        # while True:  # making a loop
        os.system('python run_sarmata.py')
        f = open("result.txt", "r")
        command = f.read()
        f.close()
        if command == "zamknij instrukcje":
            self.tk_.destroy()
            # break
        elif command == "repeat":
            winsound.PlaySound("repeat_pl.wav", winsound.SND_FILENAME)
            # continue
        # elif command == "":
        #     break
        # else:
        #     continue

    def show_instructions(self):
        self.tk_.bind("<space>", self.quit)
        self.tk_.mainloop()

