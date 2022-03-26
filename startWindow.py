from tkinter import *

import mainWindow


class startWindow:
    def __init__(self):
        self.color = "white"
        self.buttonsStage = 0
        self.projectsCanvasItems = []
        self.templatesCanvasItems = []
        self.newWindow = newWindow
        self.window = Tk()
        self.window.geometry("650x500")
        self.window.title("tk designer")
        self.createWidgets()
        self.pack()


    def createWidgets(self):
        self.allCanvas = Canvas(self.window, bg="red")
        self.buttonsCanvas = Canvas(self.allCanvas, bg='lavender')
        self.newWindowButton = Button(self.buttonsCanvas, text="new", width=10, height=1, relief=FLAT, bg='white', command=self.newWindow)
        self.openWindowButton = Button(self.buttonsCanvas, text="open", width=10, height=1, relief=FLAT, bg='white')
        self.rightCanvas = Canvas(self.allCanvas, bg="lavender")
        self.upBarCanvas = Canvas(self.rightCanvas, bg='lavender')

        self.projectsButton = Button(self.upBarCanvas, text="projects", relief=FLAT, bg='lavender', command=self.projectsButtonCommand)
        self.templatesButton = Button(self.upBarCanvas, text="templates", relief=FLAT, bg='lavender', command=self.templatesButtonCommand)

        self.projectsCanvas = Canvas(self.rightCanvas, bg="white", bd=0, highlightthickness=0, relief='ridge')
        self.templatesCanvas = Canvas(self.rightCanvas, bg="white", bd=0, highlightthickness=0, relief='ridge')

    def canvasItemsPackOrPackForget(self, list, stage):
        if stage == 1:
            for item in list:
                item.pack()
        elif stage == 2:
            for item in list:
                item.pack_forget()


    def pack(self):
        self.allCanvas.pack(expand=1, fill=BOTH, side=TOP)
        self.buttonsCanvas.pack(fill=Y, side=LEFT)
        self.newWindowButton.pack(fill=X, side=TOP, padx=10, pady=(20, 5))
        self.openWindowButton.pack(fill=X, side=TOP, padx=10)
        self.rightCanvas.pack(expand=1, fill=BOTH, side=TOP)
        self.upBarCanvas.pack(fill=X, side=TOP)
        self.projectsButton.pack(side=LEFT, padx=(0, 5))
        self.templatesButton.pack(side=LEFT)


    def projectsButtonCommand(self):
        self.buttonsStage = 1
        self.projectsButton.config(bg="white")
        self.templatesButton.config(bg="lavender")
        try:
            self.templatesCanvas.pack_forget()
            self.canvasItemsPackOrPackForget(self.templatesCanvasItems, 2)
        except:
            pass
        self.projectsCanvas.pack(expand=1, fill=BOTH, side=TOP)
        self.canvasItemsPackOrPackForget(self.projectsCanvasItems, 1)
        print("projects canvas")

    def templatesButtonCommand(self):
        self.buttonsStage = 2
        self.templatesButton.config(bg="white")
        self.projectsButton.config(bg="lavender")
        try:
            self.projectsCanvas.pack_forget()
            self.canvasItemsPackOrPackForget(self.projectsCanvasItems, 2)
        except:
            pass
        self.templatesCanvas.pack(expand=1, fill=BOTH, side=TOP)
        self.canvasItemsPackOrPackForget(self.templatesCanvasItems, 1)
        print("templates canvas")

    #def choseColor(self):
    #    color_code = colorchooser.askcolor(title="Choose color")
    #    self.color = color_code[1]




class newWindow:
    from mainWindow import MainWindow
    def __init__(self):

        self.topLvlWindow = Tk()
        self.topLvlWindow.title("Generate code")
        self.topLvlWindow.geometry("250x120")
        self.topLvlWindow.config(bg="White")
        self.topLvlWindow.resizable(False, False)

        widthCanvas = Canvas(self.topLvlWindow, bg="White")
        heightCanvas = Canvas(self.topLvlWindow, bg="White")
        titleCanvas = Canvas(self.topLvlWindow, bg="White")
        colorCanvas = Canvas(self.topLvlWindow, bg="White")


        widthEntry = Entry(widthCanvas, relief='ridge', bg="White")
        heightEntry = Entry(heightCanvas, relief='ridge', bg="White")
        titleEntry = Entry(titleCanvas, relief='ridge', bg="White")

        widthLabel = Label(widthCanvas, text="Width", relief=FLAT, bg="White")
        heightLabel = Label(heightCanvas, text="Height", relief=FLAT, bg="White")
        titleLabel = Label(titleCanvas, text="Title", relief=FLAT, bg="White")

        #colorLabel = Label(colorCanvas, text="bg color", bg="White")
        #color = Button(colorCanvas, text="chose bg color")#, command=self.choseColor, relief=FLAT, bg="White")

        okButton = Button(self.topLvlWindow, relief=FLAT, bg="#00ED60", fg="White", font=("Arial", 11), text="OK", command=lambda: self.okCommand(widthEntry.get(), heightEntry.get(), titleEntry.get()))

        okButton.pack(side=BOTTOM, fill=X)


        #colorCanvas.pack(side=BOTTOM, fill=X)
        titleCanvas.pack(side=BOTTOM, fill=X)
        heightCanvas.pack(side=BOTTOM, fill=X)
        widthCanvas.pack(side=BOTTOM, fill=X)


        widthEntry.pack(side=RIGHT)
        heightEntry.pack(side=RIGHT)
        titleEntry.pack(side=RIGHT)

        widthLabel.pack(side=LEFT)
        heightLabel.pack(side=LEFT)
        titleLabel.pack(side=LEFT)
        self.topLvlWindow.mainloop()

    def okCommand(self,widthEntry, heightEntry, titleEntry):
        self.app = mainWindow.MainWindow(int(widthEntry), int(heightEntry), titleEntry)
        self.topLvlWindow.destroy()
        self.app.window.mainloop()



