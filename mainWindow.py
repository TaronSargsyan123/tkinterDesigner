import tkinter as tk
from button import button
import textLabel
from textLabel import textLabel
from tkinter import *
from singleton import inspectorType, widgetInfo
import inspector as inspector


class MainWindow:
    def __init__(self):
        print("[INFO]: init start...")
        self.textLabelCount = 1
        self.buttonCount = 1

        self.mainWindowColorOne = ""
        self.mainWindowColorTwo = ""

        self.centerWindowColorOne = ""
        self.centerWindowColorTwo = ""

        self.inspectorType = inspectorType("textLabelInspector")
        self.widgetInfo = widgetInfo(0, 0, 0, 0, "Null", "Null", "white", "black")
        self.widgetsList = []

        self.centerWindowTitleText = "test title"
        self.allCode = ""

        self.initWindow()

        print("[INFO]: init ending...")

    def initWindow(self):
        self.__width = 1200
        self.__height = 600

        self.centerWindowWidth = 800
        self.centerWindowHeight = 450

        self.startWindow()
        self.createWidgets()
        self.inspector = inspector.textLabelInspector(self.rightCanvas)
        self.pack()
        self.centerWindow(self.centerWindowWidth, self.centerWindowHeight, self.centerCanvas)

    def startWindow(self):
        self.window = tk.Tk()
        self.window.geometry(str(self.getWidth()) + "x" + str(self.getHeight()))
        self.window.title("TK designer")

        self.window["bg"] = "white"
        self.window.bind('<Escape>', lambda e: self.generateCode())  # self.printWidgetInfo()  self.window.quit()

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        self.__width = width

    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        self.__height = height

    def createWidgets(self):



        self.allCanvas = tk.Canvas(self.window)


        self.leftCanvas = tk.Canvas(self.allCanvas, bg="white", bd=0, highlightthickness=0, relief=FLAT)

        self.createLabelButton = tk.Button(self.leftCanvas, text="     create label       ", command=self.createTextLabelCommand, relief='ridge')
        self.createButtonButton = tk.Button(self.leftCanvas, text="     create button       ", command=self.createButtonCommand, relief='ridge')
        self.centerCanvas = tk.Canvas(self.allCanvas, bg="#D4D4D4", relief=FLAT)

        self.rightCanvas = tk.Canvas(self.allCanvas, bg="white", relief=FLAT)


        self.nameCanvas = tk.Canvas(self.rightCanvas)

        self.codeGenerateButton = tk.Button(self.leftCanvas, text="Generate", command=self.generateCodeButtonCommand, relief=FLAT, bg="#00ED60", fg="White", font=("Arial", 11))

    def pack(self):
        self.allCanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)

        self.leftCanvas.pack(side=tk.LEFT, fill=tk.Y)
        self.rightCanvas.pack(side=tk.RIGHT, fill=tk.Y)
        self.centerCanvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.TRUE)
        self.createLabelButton.pack(side=tk.TOP, pady=5, fill=tk.X)
        self.createButtonButton.pack(side=tk.TOP, pady=5, fill=tk.X)
        self.codeGenerateButton.pack(side=tk.BOTTOM, fill=tk.X)


        if self.inspectorType.getInspectorType() == "textLabelInspector":
            self.inspector.drawInspector(self.widgetInfo.getItem())

            self.setInspectorInfo()




    def setInspectorInfo(self):
        self.inspector.setX(self.widgetInfo.getX())
        self.inspector.setY(self.widgetInfo.getY())
        self.inspector.setWidth(self.widgetInfo.getWidth())
        self.inspector.setHeight(self.widgetInfo.getHeight())
        self.inspector.setText(self.widgetInfo.getText())

    def printWidgetInfo(self):
        print("inspector type: " + str(self.inspectorType.getInspectorType()))
        print("x: " + str(self.widgetInfo.getX()))
        print("y: " + str(self.widgetInfo.getY()))
        print("width: " + str(self.widgetInfo.getWidth()))
        print("height: " + str(self.widgetInfo.getHeight()))
        print("text: " + str(self.widgetInfo.getText()))
        print("item: " + str(self.widgetInfo.getItem()))





    def createTextLabelCommand(self):
        self.textLabel = textLabel(200, 250, self.itemsCanvas, self.textLabelCount, self.widgetsList, self.inspector)
        self.textLabelCount += 1
        self.widgetsList.append(self.textLabel)


        self.inspector.setTextLabel(self.widgetInfo.getItem())
        self.setInspectorInfo()

    def createButtonCommand(self):
        self.button = button(200, 250, self.itemsCanvas, self.textLabelCount, self.widgetsList, self.inspector)
        self.buttonCount += 1
        self.widgetsList.append(self.button)

        self.inspector.setTextLabel(self.widgetInfo.getItem())
        self.setInspectorInfo()





    def drag_start(self, event):
        widget = event.widget
        widget.startX = event.x
        widget.startY = event.y

    def drag_motion(self, event):
        widget = event.widget
        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y
        widget.place(x=x, y=y)

    def centerWindow(self, width, height, canvas):

        self.dragCanvas = tk.Canvas(canvas, bg="white")
        self.centerWindowTitleCanvas = tk.Canvas(self.dragCanvas, bg="#FFFFFF")
        self.centerWindowTitle = tk.Label(self.centerWindowTitleCanvas, text=self.centerWindowTitleText, bg="white", font=("Arial", 11))
        self.itemsCanvas = tk.Canvas(self.dragCanvas, bg="#FFFFFF")
        self.upBarImage = PhotoImage(file="sprites/upBar.png")
        upBarLabel = tk.Label(self.dragCanvas, image=self.upBarImage)
        self.dragCanvas.place(x=50, y=20, width=width, height=height + 30)
        self.centerWindowTitleCanvas.place(x=30, y=0, height=30)
        self.centerWindowTitle.pack( side=LEFT, anchor=SW)

        self.itemsCanvas.place(x=0, y=30, width=width, height=height)
        upBarLabel.place(x=width - 140, y=0, width=140, height=30)

        self.dragCanvas.bind("<Button-1>", self.drag_start)
        self.dragCanvas.bind("<B1-Motion>", self.drag_motion)


    def generateCode(self):
        self.allCode = ""
        self.initCode = "import tkinter\n" \
                        "\n"\
                        "class mainWindow():\n" \
                        "\n" \
                        "   def __init__(self):\n" \
                        "       self.root = tkinter.Tk()\n" \
                        "       self.root.geometry(\"" + str(self.centerWindowWidth) + "x" + str(self.centerWindowHeight) + "\")\n" \
                        "       self.root.title(\"" + str(self.centerWindowTitleText) + "\")\n"\
                        "\n"

        self.finalCode = "app = mainWindow()\n" \
                         "app.root.mainloop()\n"

        self.allCode = self.allCode + self.initCode

        for item in self.widgetsList:
            self.allCode = self.allCode + item.generateCode()

        self.allCode = self.allCode+self.finalCode

        return self.allCode

    def generateCodeButtonCommand(self):

        topLvlWindow = tk.Toplevel(self.window)
        topLvlWindow.title("Generate code")
        topLvlWindow.geometry("710x500")
        topLvlWindow.config(bg="White")

        topLvlLabel = tk.Text(topLvlWindow, bg="White", font=("Arial", 9))
        topLvlCopyButton = tk.Button(topLvlWindow, text="Copy", command=self.copyToClipboard, relief=FLAT, bg="#00ED60", fg="White", font=("Arial", 11))

        topLvlLabel.pack(fill=BOTH, side=TOP, expand=True, anchor=NW, padx=10, pady=10)
        topLvlCopyButton.pack(fill=X, side=BOTTOM, pady=10, padx=10)
        topLvlLabel.insert(INSERT, self.generateCode())

    def copyToClipboard(self):
        self.window.clipboard_clear()
        self.window.clipboard_append(self.generateCode())
        #print(self.generateCode())

