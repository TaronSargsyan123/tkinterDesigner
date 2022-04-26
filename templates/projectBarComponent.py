import tkinter

class projectBarComponent:
    def __init__(self, canvas, title):
        self.canvas = canvas
        self.text = title

        self.createWidgets()
        self.pack()

    def createWidgets(self):
        self.allCanvas = tkinter.Button(self.canvas, text=str(self.text), command=self.buttonCommand, bg="white", bd=0, highlightthickness=0, relief=tkinter.FLAT)

    def pack(self):
        self.allCanvas.pack(side=tkinter.LEFT, padx=(0, 10))

    def buttonCommand(self):
        print("test")