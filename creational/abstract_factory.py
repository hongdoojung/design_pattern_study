# https://ko.wikipedia.org/wiki/%EC%B6%94%EC%83%81_%ED%8C%A9%ED%86%A0%EB%A6%AC_%ED%8C%A8%ED%84%B4#Python_%EC%98%88%EC%A0%9C

import enum
from abc import *

class Button:
    @abstractmethod
    def Paint(self):
        pass

class MousePointer:
    @abstractmethod
    def Paint(self):
        pass

class GUIFactory:
    @abstractmethod
    def CreateButton(self):
        return Button

    @abstractmethod
    def CreateMousePointer(self):
        return MousePointer

class WinFactory(GUIFactory):
    def CreateButton(self):
        return WinButton()
    def CreateMousePointer(self):
        return WinMousePointer()

class OSXFactory(GUIFactory):
    def CreateButton(self):
        return OSXButton()
    def CreateMousePointer(self):
        return OSXMousePointer()

class WinMousePointer(MousePointer):
    def Paint(self):
        print("Render a mousepointer in a Windows style")

class OSXMousePointer(MousePointer):
    def Paint(self):
        print ("Render a mousepointer in a OSX style")

class WinButton(Button):
    def Paint(self):
        print ("Render a button in a Windows style")

class OSXButton(Button):
    def Paint(self):
        print ("Render a button in a Mac OSX style")

class Settings:
    @staticmethod
    def Default():
        return Appearance.WIN

class Appearance(enum.Enum):
    WIN = 0
    OSX = 1

def main():
    apperance = Settings.Default()
    if apperance == Appearance.WIN:
        factory = WinFactory()
    elif apperance == Appearance.OSX:
        factory = OSXFactory()
    button = factory.CreateButton()
    mousePointer = factory.CreateMousePointer()
    button.Paint()
    mousePointer.Paint()

if __name__ == '__main__':
    main()
