from tkinter import Tk, Label


class CamGui (Tk):

    def __init__(self):
        super().__init__()
        self.text = Label(self, text="", wraplength=2000, justify="left", font=("Andale Mono", 4))
        self.text.pack()
        self.title("video to ascii GUI")
        # self.mainloop()

    def set_text(self, txt):
        self.text.config(text=' '.join(txt.split('\n')))
