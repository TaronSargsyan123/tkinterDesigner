import tkinter as tk
from button import button
import textLabel
from textLabel import textLabel
from tkinter import *
from singleton import inspectorType, widgetInfo
import inspector as inspector
from entry import entry
from tkinter import filedialog
from json import dumps, loads
from projectBarComponent import projectBarComponent
import os
from pathlib import Path
class MainWindow:
    def __init__(self, centerWindowWidth, centerWindowHeight, centerWindowTitle):
        print("[INFO]: init start...")
        self.pathToProject = ""

        self.centerWindowWidth = centerWindowWidth
        self.centerWindowHeight = centerWindowHeight
        self.title = centerWindowTitle
        self.centerWindowColor = "white"

        self.buttonCount = 1
        self.textLabelCount = 1
        self.entryCount = 1
        self.count = 1

        self.mainWindowColorOne = ""
        self.mainWindowColorTwo = ""

        self.centerWindowColorOne = ""
        self.centerWindowColorTwo = ""

        self.inspectorType = inspectorType("textLabelInspector")
        self.widgetInfo = widgetInfo(0, 0, 0, 0, "Null", "Null", "white", "black")
        self.widgetsList = []

        self.allCode = ""

        self.initWindow()

        print("[INFO]: init ending...")

    def initWindow(self):
        self.__width = 1200
        self.__height = 600

        self.startWindow()
        self.createWidgets()
        self.inspector = inspector.textLabelInspector(self.rightCanvas)
        self.pack()
        self.centerWindow(self.centerWindowWidth, self.centerWindowHeight, self.centerCanvas, self.centerWindowColor, self.title)
        #self.projectsBarComponent = projectBarComponent(self.projectsBar, self.title)





    def startWindow(self):
        self.window = tk.Tk()
        self.window.geometry(str(self.getWidth()) + "x" + str(self.getHeight()))
        self.window.title("TK designer")

        self.window["bg"] = "white"
        self.window.bind('<Escape>', lambda e: self.clearCentralWindow())#self.generateCode())  # self.printWidgetInfo()  self.window.quit()

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

        self.createLabelButton = tk.Button(self.leftCanvas, text="create label", command=self.createTextLabelCommand, relief='ridge')
        self.createButtonButton = tk.Button(self.leftCanvas, text="create button", command=self.createButtonCommand, relief='ridge')
        self.createEntryButton = tk.Button(self.leftCanvas, text="create entry", command=self.createEntryCommand, relief='ridge')
        self.centerCanvas = tk.Canvas(self.allCanvas, bg="#D4D4D4", relief=FLAT)

        self.rightCanvas = tk.Canvas(self.allCanvas, bg="white", relief=FLAT)


        self.nameCanvas = tk.Canvas(self.rightCanvas)

        self.codeGenerateButton = tk.Button(self.leftCanvas, text="Generate", command=self.generateCodeButtonCommand, relief=FLAT, bg="#00ED60", fg="White", font=("Arial", 11))

        menubar = Menu(self.window)
        self.window.config(menu=menubar)
        fileMenu = Menu(menubar, tearoff=0)
        codeMenu = Menu(menubar, tearoff=0)
        fileMenu.add_command(label='New', command=self.newFile)
        fileMenu.add_command(label='Open...', command=self.openFile)
        fileMenu.add_command(label='Save', command=self.saveFile)
        fileMenu.add_command(label='Save As...', command=self.saveAsFile)
        fileMenu.add_command(label='Settings')
        fileMenu.add_command(label='Menu')

        fileMenu.add_separator()
        fileMenu.add_command(label='Exit', command=self.window.destroy)

        codeMenu.add_command(label="Generate", command=self.generateCodeButtonCommand)
        codeMenu.add_command(label='Export python file', command=self.exportFile)
        menubar.add_cascade(label="File", menu=fileMenu, underline=0)
        menubar.add_cascade(label="Code", menu=codeMenu, underline=0)

        #self.projectsBar = tk.Canvas(self.allCanvas, bg="red", bd=0, highlightthickness=0, relief=FLAT)



    def pack(self):
        self.allCanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        #self.projectsBar.pack(side=tk.TOP, fill=tk.X)


        self.leftCanvas.pack(side=tk.LEFT, fill=tk.Y)
        self.rightCanvas.pack(side=tk.RIGHT, fill=tk.Y)
        self.centerCanvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.TRUE)
        self.createLabelButton.pack(side=tk.TOP, pady=5, fill=tk.X)
        self.createEntryButton.pack(side=tk.TOP, fill=tk.X)
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
        self.textLabel = textLabel(200, 250, self.itemsCanvas, self.textLabelCount, self.widgetsList, self.inspector, 70, 50, "label", "white", "black")
        self.textLabelCount += 1
        self.widgetsList.append(self.textLabel)


        self.inspector.setTextLabel(self.widgetInfo.getItem())
        self.setInspectorInfo()

    def createButtonCommand(self):
        self.button = button(200, 250, self.itemsCanvas, self.buttonCount, self.widgetsList, self.inspector, 70, 50, "button", "white", "black")
        self.buttonCount += 1
        self.widgetsList.append(self.button)

        self.inspector.setTextLabel(self.widgetInfo.getItem())
        self.setInspectorInfo()

    def createEntryCommand(self):
        self.entry = entry(200, 250, self.itemsCanvas, self.entryCount, self.widgetsList, self.inspector, 70, 50, "entry", "white", "black")
        self.entryCount += 1
        self.widgetsList.append(self.entry)

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

    def centerWindow(self, width, height, canvas, color, title):
        centerWindowColor = color
        self.centerWindowtitle = title
        self.dragCanvas = tk.Canvas(canvas, bg="white")
        self.centerWindowTitleCanvas = tk.Canvas(self.dragCanvas, bg="white")
        self.centerWindowTitle = tk.Label(self.centerWindowTitleCanvas, text=self.centerWindowtitle, bg="white", font=("Arial", 11))
        self.itemsCanvas = tk.Canvas(self.dragCanvas, bg=centerWindowColor)
        try:
            self.upBarImage = PhotoImage(file="sprites/upBar.png")
            upBarLabel = tk.Label(self.dragCanvas, image=self.upBarImage)
        except:
            pass
        self.dragCanvas.place(x=50, y=20, width=width, height=height + 30)
        self.centerWindowTitleCanvas.place(x=30, y=0, height=30)
        self.centerWindowTitle.pack( side=LEFT, anchor=SW)

        self.itemsCanvas.place(x=0, y=30, width=width, height=height)
        try:
            upBarLabel.place(x=width - 140, y=0, width=140, height=30)
        except:
            pass
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
                        "       self.root.title(\"" + str(self.centerWindowtitle) + "\")\n" \
                        "       self.root.config(bg=\"" + str(self.centerWindowColor) + "\")\n" \
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

    def browseFolder(self, value):
        filetypes = ""
        if value == "export":
            filetypes = (('python files', '*.py'), ('All files', '*.*'))
        elif value == "save":
            filetypes = (('text files', '*.txt'), ('All files', '*.*'))

        folderPath = StringVar()
        filename = filedialog.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
        folderPath.set(filename)
        print(filename)
        return filename

    def saveAsFile(self):
        path = str(self.browseFolder("save"))
        settingsTxtPath = "settingsTxt"
        self.pathToProject = path

        try:
            txtFile = open(path, 'a').close()
            print(txtFile)
        except OSError:
            print('Failed creating the file')
        else:
            print('File created')
            print(path)
            f = open(path, 'w')
            f.truncate(0)
            for item in self.widgetsList:
                result = dumps(item.saveLineGeneration())
                print(result + "\n")
                f.write(result + "\n")

            settingsTxt = open(settingsTxtPath, 'w')
            settingsTxt.write(str(self.centerWindowtitle) + " - " + path)

            f.close()

    def exportFile(self):
        path = str(self.browseFolder("export"))

        try:
            pyFile = open(path, 'a').close()
            print(pyFile)
        except OSError:
            print('Failed creating the file')
        else:
            print('File created')
            print(path)
            f = open(path, 'w')
            f.truncate(0)

            f.write(self.generateCode())
            f.close()

    def openFile(self):
        for i in range(len(self.widgetsList) + 10):
            self.clearCentralWindow()
        path = str(self.browseFolder("open..."))
        self.pathToProject = path
        with open(path) as f:
            lines = f.readlines()
            for i in lines:
                #print(i)
                result = loads(i)
                #print(result)
                if result['type'] == 'button':
                    self.button = button(result['x'], result['y'], self.itemsCanvas, self.buttonCount, self.widgetsList, self.inspector, result['w'], result['h'], result['txt'], result['bg'], result['fg'])
                    self.buttonCount += 1
                    #self.button.createWidgets()
                    self.button.place()
                    self.widgetsList.append(self.button)

                    self.inspector.setTextLabel(self.widgetInfo.getItem())
                    self.setInspectorInfo()
                elif result['type'] == 'label':
                    self.label = textLabel(result['x'], result['y'], self.itemsCanvas, self.buttonCount, self.widgetsList, self.inspector, result['w'], result['h'], result['txt'], result['bg'], result['fg'])
                    self.textLabelCount += 1
                    #self.label.createWidgets()
                    self.label.place()
                    self.widgetsList.append(self.label)

                    self.inspector.setTextLabel(self.widgetInfo.getItem())
                    self.setInspectorInfo()
                elif result['type'] == 'entry':
                    self.entry = entry(result['x'], result['y'], self.itemsCanvas, self.buttonCount, self.widgetsList, self.inspector, result['w'], result['h'], result['txt'], result['bg'], result['fg'])
                    self.entryCount += 1
                    #self.entry.createWidgets()
                    self.entry.place()
                    self.widgetsList.append(self.entry)

                    self.inspector.setTextLabel(self.widgetInfo.getItem())
                    self.setInspectorInfo()

    def clearCentralWindow(self):
        print(self.widgetsList)
        for item in self.widgetsList:
            item.placeForget()
        print(self.widgetsList)

    def newFile(self):
        for i in range(len(self.widgetsList) + 10):
            self.clearCentralWindow()
        pathToUser = Path.home()

        directory = Path(str(pathToUser) + "\Tk-Projects")

        try:
            os.mkdir(directory)
            print("Directory ", directory, " Created ")
        except FileExistsError:
            print("Directory ", directory, " already exists")



        f = open(directory.joinpath("project.txt"), 'w')
        print('File created')

        self.pathToProject = str(directory) + "\project.txt"

    def saveFile(self):
        path = self.pathToProject
        print(path)
        f = open(Path(path), "w")

        for item in self.widgetsList:
            result = dumps(item.saveLineGeneration())
            print(result + "\n")
            f.write(result + "\n")




