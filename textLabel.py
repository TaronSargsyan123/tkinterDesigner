import tkinter

from parentItem import parentItem
from tkinter import *
from singleton import widgetInfo


class textLabel(parentItem):
    def __init__(self, x, y, canvas, count, list, inspector, width, height, text, bg, fg):
        super().__init__(x, y, canvas, count, list, inspector)
        self.type = "label"
        self.setWidth(width)
        self.setHeight(height)

        self.setText(text)
        self.setBg(bg)
        self.setFg(fg)



    def createWidgets(self):
        print(self.count)
        self.id = "Label" + str(self.count)
        self.text = "text" + str(self.count)
        self.button = tkinter.Button(self.canvas, relief=SOLID, text=self.text, bg=self.bg, fg=self.fg, highlightbackground=self.borderColor, borderwidth=0, command=self.command)

        self.resizeButton = tkinter.Button(self.canvas, relief=FLAT, bg="red")


    def itemStageFalse(self):
        self.button.config(borderwidth=0)
        self.resizeButton.place_forget()



    def generateCode(self):
        self.code = "       self." + str(self.id) + " = tkinter.Label(self.root, bg=\"" + str(self.bg) + "\", fg=\"" + str(self.fg) + "\", text=\"" + str(self.text) + "\")\n" \
                    "       self." + str(self.id) + ".place(x=" + str(self.getX()) + ", y=" + str(self.getY()) + ", width=" + str(self.getWidth()) + ", height=" + str(self.getHeight()) + ")\n"\
                    "\n"

        return self.code


