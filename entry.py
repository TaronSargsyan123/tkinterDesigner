import tkinter

from parentItem import parentItem
from tkinter import *
from singleton import widgetInfo


class entry(parentItem):
    def __init__(self, x, y, canvas, labelCount, buttonCount, count, entryCount, list, inspector):
        super().__init__(x, y, canvas, labelCount, buttonCount,  count, entryCount, list, inspector)





    def createWidgets(self):
        print(self.entryCount)
        self.id = "Entry" + str(self.entryCount)
        self.text = "entry" + str(self.entryCount)

        self.button = tkinter.Button(self.canvas, text=self.text, bg=self.bg, fg=self.fg, command=self.command, relief='ridge')

        self.resizeButton = tkinter.Button(self.canvas, relief=FLAT, bg="red")


    def itemStageFalse(self):
        self.button.config(borderwidth=2)
        self.resizeButton.place_forget()


    def generateCode(self):
        self.code = "       self." + str(self.id) + " = tkinter.Entry(self.root, bg=\"" + str(self.bg) + "\", fg=\"" + str(self.fg) + "\", text=\"" + str(self.text) + "\")\n" \
                    "       self." + str(self.id) + ".place(x=" + str(self.getX()) + ", y=" + str(self.getY()) + ", width=" + str(self.getWidth()) + ", height=" + str(self.getHeight()) + ")\n"\
                    "\n"

        return self.code