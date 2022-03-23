import tkinter
from tkinter import *
from singleton import widgetInfo
class parentItem:
    def __init__(self, x, y, canvas, count, list, inspector):
        self.__x = x
        self.__y = y

        self.type = "item"

        self.list = list
        self.count = count
        self.id = "item" + str(self.count)
        self.__width = 70
        self.__height = 40
        self.text = "item" + str(self.count)
        self.bg = "white"
        self.fg = "black"
        self.relief = tkinter.FLAT
        self.borderColor = "black"
        self.borderSize = 3
        self.img = ""
        self.canvas = canvas
        self.inspectorItem = inspector
        print(self.inspectorItem.getTextLabel)

        self.stage = False

        self.createWidgets()
        self.place()

    def getWidth(self):
        return self.__width

    def setWidth(self, value):
        self.__width = value

    def getHeight(self):
        return self.__height

    def setHeight(self, value):
        self.__height = value


    def getX(self):
        return self.__x

    def setX(self, value):
        self.__x = value

    def getY(self):
        return self.__y

    def setY(self, value):
        self.__y = value

    def createWidgets(self):
        self.button = tkinter.Button(self.canvas, text=self.text, bg=self.bg, fg=self.fg,command=self.command)

        self.resizeButton = tkinter.Button(self.canvas, relief=FLAT, bg="red")


    def place(self):
        self.button.place(x=self.getX(), y=self.getY(), width=self.getWidth(), height=self.getHeight())



        self.button.bind("<Button-1>", self.drag_start)
        self.button.bind("<B1-Motion>", self.drag_motion)

        self.resizeButton.bind("<Button-1>", self.drag_start)
        self.resizeButton.bind("<B1-Motion>", self.resizeMotion)


    def drag_start(self, event):
        widget = event.widget
        widget.startX = event.x
        widget.startY = event.y
        self.resizeButton.place(x=int(self.getX()) + int(self.getWidth()), y=int(self.getY()) + int(self.getHeight()))
        self.inspectorItem.enterValue(self.getX(), self.getY(), self.getWidth(), self.getHeight(), self.text, self.bg, self.fg)

    def drag_motion(self, event):
        widget = event.widget
        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y
        widget.place(x=x, y=y)

        self.setX(x)
        self.setY(y)
        self.resizeButton.place(x=int(self.getX())+ int(self.getWidth()), y=int(self.getY())+ int(self.getHeight()))
        self.inspectorItem.enterValue(self.getX(), self.getY(), self.getWidth(), self.getHeight(), self.text, self.bg, self.fg)



    def resizeMotion(self, event):

        x = int(self.getWidth()) + (event.x - int(self.getX()))
        y = int(self.getHeight()) + (event.y - int(self.getY()))

        self.button.place(width=x, height=y)
        self.resizeButton.place(x=x, y=y)
        self.setWidth(x)
        self.setHeight(y)
        self.widgetInspector.setWidth(self.getWidth())
        self.widgetInspector.setHeight(self.getHeight())
        self.inspectorItem.setWidth(self.getWidth())
        self.inspectorItem.setHeight(self.getHeight())



    def command(self):
        for item in self.list:
            if item.id == self.id:
                self.idItem = item



        for item in self.list:
            item.stage = False
            item.itemStageFalse()

        self.inspector()
        self.widgetInspector.setItem(self.idItem)
        self.stage = True

        self.itemStageTrue()

    def itemStageFalse(self):
        self.button.config(borderwidth=0)
        self.resizeButton.place_forget()

    def itemStageTrue(self):
        self.button.config(borderwidth=2)
        self.resizeButton.place(x=int(self.getX())+int(self.getWidth()), y=int(self.getY())+int(self.getHeight()), width=5, height=5)
        self.inspector()
        self.generateCode()
        #self.button.bind('<Return>', self.placeForget)


    def inspector(self):
        self.widgetInspector = widgetInfo(self.getX(), self.getY(), self.getWidth(), self.getHeight(), self.text, self.idItem, self.bg, self.fg)

    def setFg(self, value):
        self.fg = value
        self.button.config(fg=self.fg)

    def setBg(self, value):
        self.bg = value
        self.button.config(bg=self.bg)

    def setText(self, value):
        self.text = value
        self.button.config(text=self.text)

    def setButtonInfo(self, x, y, width, height, text, bg, fg):
        print(fg)
        print(bg)
        self.setX(x)
        self.setY(y)
        self.setWidth(width)
        self.setHeight(height)
        self.text = text
        self.bg = bg
        self.fg = fg
        self.button.config(bg=self.bg)
        self.button.config(fg=self.fg)
        self.button.config(text=self.text)
        self.button.place(x=self.getX(), y=self.getY(), width=self.getWidth(), height=self.getHeight())
        self.resizeButton.place(x=self.getX() + self.getWidth(), y=self.getY() + self.getHeight())

    def generateCode(self):
        pass

    def saveLineGeneration(self):
        self.saveFileLine = {"x": int(self.getX()), "y": int(self.getY()),
                             "w": int(self.getWidth()), "h": int(self.getHeight()),
                             "txt": self.text, "bg": self.bg, "fg": self.fg,
                             "type": self.type, "id": self.id}
        print(type(self.saveFileLine))
        return self.saveFileLine

    def placeForget(self):

        self.button.place_forget()
        self.resizeButton.place_forget()
        self.list.remove(self)
        print(self.list)
