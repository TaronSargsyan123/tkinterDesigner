import tkinter
from singleton import widgetInfo
from tkinter import colorchooser
from tkinter import *

class defaultInspector:
    def __init__(self, inspectorCanvas):
        self.inspectorCanvas = inspectorCanvas
        self.xCnavas = tkinter.Canvas(self.inspectorCanvas)
        self.yCnavas = tkinter.Canvas(self.inspectorCanvas)
        self.widthCanvas = tkinter.Canvas(self.inspectorCanvas)
        self.heightCanvas = tkinter.Canvas(self.inspectorCanvas)
        self.okButton = tkinter.Button(self.inspectorCanvas, text="OK", command=self.okCommand, relief=FLAT)

        self.xLabel = tkinter.Label(self.xCnavas, text="X ")
        self.xEntry = tkinter.Entry(self.xCnavas, relief=FLAT)

        self.yLabel = tkinter.Label(self.yCnavas, text="Y ")
        self.yEntry = tkinter.Entry(self.yCnavas, relief=FLAT)

        self.weidthLabel = tkinter.Label(self.widthCanvas, text="Width ")
        self.weidthEntry = tkinter.Entry(self.widthCanvas, relief=FLAT)

        self.heightLabel = tkinter.Label(self.heightCanvas, text="Height ")
        self.heightEntry = tkinter.Entry(self.heightCanvas, relief=FLAT)

        self.xCnavas.pack(pady=10, fill=tkinter.X, anchor=tkinter.W)
        self.yCnavas.pack(pady=10, fill=tkinter.X, anchor=tkinter.W)

        self.widthCanvas.pack(pady=10, fill=tkinter.X, anchor=tkinter.W)
        self.heightCanvas.pack(pady=10, fill=tkinter.X, anchor=tkinter.W)

        self.weidthLabel.pack(side=tkinter.LEFT, padx=5)
        self.weidthEntry.pack(side=tkinter.RIGHT)
        self.heightLabel.pack(side=tkinter.LEFT, padx=5)
        self.heightEntry.pack(side=tkinter.RIGHT)

        self.xLabel.pack(side=tkinter.LEFT, padx=5)
        self.xEntry.pack(side=tkinter.RIGHT)

        self.yLabel.pack(side=tkinter.LEFT, padx=5)
        self.yEntry.pack(side=tkinter.RIGHT)

        self.okButton.pack(side=tkinter.BOTTOM, fill=X)



    def setX(self, value):
        self.xEntry.delete(0, tkinter.END)
        self.xEntry.insert(0, value)


    def setY(self, value):
        self.yEntry.delete(0, tkinter.END)
        self.yEntry.insert(0, value)

    def setWidth(self, value):
        self.weidthEntry.delete(0, tkinter.END)
        self.weidthEntry.insert(0, value)


    def setHeight(self, value):
        self.heightEntry.delete(0, tkinter.END)
        self.heightEntry.insert(0, value)

    def getX(self):
        return self.xEntry.get()


    def getY(self):
        return self.yEntry.get()

    def getWidth(self):
        return self.weidthEntry.get()


    def getHeight(self):
        return self.heightEntry.get()



    def okCommand(self):
        print("ok")

class textLabelInspector(defaultInspector):
    def drawInspector(self, textLabel):

        self.__textLabel = textLabel
        self.widgetInfo = widgetInfo(0, 0, 0, 0, "Null", textLabel, "white", "black")
        self.bg = self.widgetInfo.getBg()
        self.fg = self.widgetInfo.getFg()


        self.textCanvas = tkinter.Canvas(self.inspectorCanvas)
        self.textLabel = tkinter.Label(self.textCanvas, text="Text ")
        self.textEntry = tkinter.Entry(self.textCanvas, relief=FLAT)

        #self.refreshButton = tkinter.Button(self.inspectorCanvas, command=self.refresh, text="refresh")

        self.colorShoserCanvas = tkinter.Canvas(self.inspectorCanvas, relief=FLAT)
        self.colorShoserButton = tkinter.Button(self.colorShoserCanvas, text="chose background color", command=self.choseBgColor, relief=FLAT)
        self.colorFrame = tkinter.Frame(self.colorShoserCanvas, width=25, height=25, bg=self.bg)

        self.fgColorShoserCanvas = tkinter.Canvas(self.inspectorCanvas, relief=FLAT)
        self.fgColorShoserButton = tkinter.Button(self.fgColorShoserCanvas, text="chose font color", command=self.choseFgColor, relief=FLAT)
        self.fgColorFrame = tkinter.Frame(self.fgColorShoserCanvas, width=25, height=25, bg=self.bg)

        self.textCanvas.pack(pady=10, fill=tkinter.X)
        self.textLabel.pack(side=tkinter.LEFT)
        self.textEntry.pack(side=tkinter.RIGHT)

        self.colorShoserCanvas.pack(pady=10, fill=tkinter.X)
        self.colorFrame.pack(side=tkinter.LEFT, padx=10)
        self.colorShoserButton.pack(side=tkinter.RIGHT, padx=10)

        self.fgColorShoserCanvas.pack(pady=10, fill=tkinter.X)
        self.fgColorFrame.pack(side=tkinter.LEFT, padx=10)
        self.fgColorShoserButton.pack(side=tkinter.RIGHT, padx=10)


        #self.refreshButton.pack(side=tkinter.TOP)


    def setTextLabel(self, value):
        self.__textLabel = value

    def getTextLabel(self):
        return self.__textLabel



    def setText(self, value):
        self.textEntry.delete(0, tkinter.END)
        self.textEntry.insert(0, value)

    def getText(self):
        return self.textEntry.get()


    def okCommand(self):
        print(self.textEntry.get())
        print("test")

        self.setTextLabel(self.widgetInfo.getItem())

        self.getTextLabel().setButtonInfo(self.getX(), self.getY(), self.getWidth(), self.getHeight(), self.getText(), self.bg,self.fg)





    #def refresh(self):
    #    self.enterValue(self.widgetInfo.getX(), self.widgetInfo.getY(), self.widgetInfo.getWidth(), self.widgetInfo.getHeight(), self.widgetInfo.getText(), self.widgetInfo.getBg())


    def choseColor(self):
        color_code = colorchooser.askcolor(title="Choose color")
        return color_code[1]


    def choseBgColor(self):
        self.setTextLabel(self.widgetInfo.getItem())
        self.bg = self.choseColor()
        self.widgetInfo.setBg(self.bg)
        self.getTextLabel().setBg(self.widgetInfo.getBg())
        self.colorFrame.config(bg=self.bg)

    def choseFgColor(self):
        self.setTextLabel(self.widgetInfo.getItem())
        self.fg = self.choseColor()
        self.widgetInfo.setFg(self.fg)
        self.getTextLabel().setFg(self.widgetInfo.getFg())
        self.fgColorFrame.config(bg=self.fg)

    def enterValue(self, x, y, width, height, text, bg, fg):
        self.xEntry.delete(0, tkinter.END)
        self.xEntry.insert(0, x)

        self.yEntry.delete(0, tkinter.END)
        self.yEntry.insert(0, y)

        self.weidthEntry.delete(0, tkinter.END)
        self.weidthEntry.insert(0, width)

        self.heightEntry.delete(0, tkinter.END)
        self.heightEntry.insert(0, height)

        self.textEntry.delete(0, tkinter.END)
        self.textEntry.insert(0, text)

        self.bg = bg
        self.colorFrame.config(bg=self.bg)

        self.fg = fg
        self.fgColorFrame.config(bg=self.fg)


