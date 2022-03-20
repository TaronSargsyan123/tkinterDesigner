class singletonInspector:
    __instance = None

    def __new__(cls, inspectorType, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super(singletonInspector, cls).__new__(cls)
            cls.__instance.inspectorType = inspectorType



        return cls.__instance


class inspectorType(singletonInspector):

    def __init__(self, inspectorType):
        self.__inspectorType = inspectorType


    def getInspectorType(self):
        return self.__inspectorType

    def setInspectorType(self, value):
        self.__inspectorType = value



class singletonWidget:
    __instance = None

    def __new__(cls, x, y, width, height, text, bg, fg, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super(singletonWidget, cls).__new__(cls)
            cls.__instance.x = x
            cls.__instance.y = y
            cls.__instance.width = width
            cls.__instance.height = height
            cls.__instance.text = text
            cls.__bg = bg
            cls.__fg = fg



        return cls.__instance


class widgetInfo(singletonWidget):

    def __init__(self, x, y, width, height, text, item, bg, fg):

        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__text = text
        self.__item = item
        self.__bg = bg
        self.__fg = fg


    def getX(self):
        return self.__x

    def setX(self, value):
        self.__x = value

    def getY(self):
        return self.__y

    def setY(self, value):
        self.__y = value

    def getWidth(self):
        return self.__width

    def setWidth(self, value):
        self.__width = value

    def getHeight(self):
        return self.__height

    def setHeight(self, value):
        self.__height = value

    def getText(self):
        return self.__text

    def setText(self, value):
        self.__text = value

    def getItem(self):
        return self.__item

    def setItem(self, value):
        self.__item = value

    def getBg(self):
        return self.__bg

    def setBg(self, value):
        self.__bg = value

    def getFg(self):
        return self.__fg

    def setFg(self, value):
        self.__fg = value